import pytest
from utils import generate_combinations
from exceptions import LowLimitOfLengthsMessage

from split_msg import split_message


def max_len_fixture():
    files = (
        "./msg/test-1.html",
        "./msg/test-2.html",
        "./msg/test-3.html",
    )
    max_lens = (
        120,
        200,
        500,
    )

    return generate_combinations(files, max_lens)


def raise_exceptions_fixture():
    files = (
        "./msg/test-1.html",
        "./msg/test-2.html",
        "./msg/test-3.html",
    )
    max_lens = (
        20,
        10,
        15,
    )

    return generate_combinations(files, max_lens)


# Тестирование на привышение длинны
@pytest.mark.parametrize(
    "file, max_len",
    max_len_fixture(),
)
def test_max_len(file, max_len):
    messages = split_message(file, max_len)
    for msg in messages:
        assert len(msg) < max_len


# Тестирование на выбрасывание ошибки
@pytest.mark.parametrize(
    "file, max_len",
    raise_exceptions_fixture(),
)
def test_split_message_exception(file, max_len):
    with pytest.raises(LowLimitOfLengthsMessage):
        messages = split_message(file, max_len)
        for msg in messages:
            assert len(msg) < max_len
