import logger
import pytest


@pytest.fixture()
def log_strings():
    return ["", "1 2", "Text 123 more text 321"]


def test_answer(log_strings):
    assert not logger.parse_line(log_strings[0])
    assert [1, 2] == logger.parse_line(log_strings[1])
    assert [123, 321] == logger.parse_line(log_strings[2])

