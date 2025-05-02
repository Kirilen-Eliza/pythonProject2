from typing import Dict, List, Union

import pytest


@pytest.fixture
def account() -> int:
    return 73654108430135874305


@pytest.fixture(params=["Visa Gold 59994", "Счет 0122333"])
def wrong_answer(request) -> str:
    return request.param


@pytest.fixture
def date() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def incorrect_date() -> float:
    return 18.671407


@pytest.fixture(params=["11-03-2024T02:26:18.671407", "Восьмое февраля две тысячи двадцать пятого года"])
def date_invalid(request) -> str:
    return request.param


@pytest.fixture
def transactions() -> List[Dict[str, Union[str, int]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
