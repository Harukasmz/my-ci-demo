import pytest

from prime import is_prime, primes_up_to


@pytest.mark.parametrize("n", [2, 3, 13, 97])
def test_is_prime_true(n):
    assert is_prime(n) is True


@pytest.mark.parametrize("n", [100])
def test_is_prime_false_composite(n):
    assert is_prime(n) is False


@pytest.mark.parametrize("n", [0, 1, -7])
def test_is_prime_false_boundary(n):
    assert is_prime(n) is False


def test_primes_up_to_10():
    assert primes_up_to(10) == [2, 3]


def test_primes_up_to_1():
    assert primes_up_to(1) == []
