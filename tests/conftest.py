import pytest


@pytest.fixture
def account():
    return 73654108430135874305


@pytest.fixture(params = ['Visa Gold 59994', 'Счет 0122333'])
def wrong_answer(request):
    return request.param


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def incorrect_date():
    return 18.671407


@pytest.fixture(params = ["11-03-2024T02:26:18.671407",
                                "Восьмое февраля две тысячи двадцать пятого года"])
def date_invalid(request):
    return request.param


