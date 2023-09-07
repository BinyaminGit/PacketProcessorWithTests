
import pytest
from packet_processor import (checksum, encrypt, decrypt, validate,
                              drop_invalid_packets, add_headers, remove_headers)

def test_checksum():
    assert checksum([1, 2, 3]) == 6

def test_encrypt():
    assert encrypt([1, 2, 3], 2) == [3, 0, 1]

def test_decrypt():
    assert decrypt([3, 0, 1], 2) == [1, 2, 3]

def test_validate():
    assert validate([1, 2, 3]) == True
    assert validate([-1, 2, 3]) == False

def test_drop_invalid_packets():
    assert drop_invalid_packets([[1, 2, 3], [-1, 2, 3], [4, 5, 6]]) == [[1, 2, 3], [4, 5, 6]]

def test_add_headers():
    assert add_headers([1, 2, 3], [0, 0]) == [0, 0, 1, 2, 3]

def test_remove_headers():
    assert remove_headers([0, 0, 1, 2, 3], 2) == [1, 2, 3]

@pytest.mark.benchmark(group="checksum")
def test_checksum_performance(benchmark):
    benchmark(checksum, list(range(1, 100000)))

@pytest.mark.benchmark(group="encrypt")
def test_encrypt_performance(benchmark):
    benchmark(encrypt, list(range(1, 100000)), 2)

@pytest.mark.benchmark(group="decrypt")
def test_decrypt_performance(benchmark):
    benchmark(decrypt, list(range(1, 100000)), 2)
