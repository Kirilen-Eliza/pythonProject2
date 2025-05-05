import os

from src.decorators import log


def test_log_output_to_the_console(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(10, 5)
    result = capsys.readouterr()
    assert result.out == 'my_function ok\n'
    my_function(10, 0)
    result_not_positive = capsys.readouterr()
    assert (result_not_positive.out ==
            "my_function error: division by zero. Inputs: ((10, 0), {})\n")

def test_log_file():
    @log("mylog.txt")
    def my_function(x, y):
        return x / y

    my_function(10, 5)
    with open('mylog.txt', 'r', encoding='utf-8') as file:
        result_positive = file.read()
        assert result_positive == 'my_function ok'
    my_function(10, 0)
    with open('mylog.txt', 'r', encoding='utf-8') as file:
        result_not_positive = file.read()
        assert result_not_positive == 'my_function error: division by zero. Inputs: ((10, 0), {})'
    my_function('10',5) # type: ignore[arg-type]
    with open('mylog.txt', 'r', encoding='utf-8') as file:
        result_unsupported_type = file.read()
        assert result_unsupported_type == ("my_function error: unsupported operand"
                                           " type(s) for /: 'str' and 'int'. Inputs: (('10', 5), {})")
    os.remove('mylog.txt')
