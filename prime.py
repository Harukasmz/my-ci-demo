"""素数判定モジュール

仕様:
  - 素数: 2以上の整数で、1とその数自身以外に約数を持たないもの
  - 0, 1, 負の数は素数ではない (False を返す)
"""


def is_prime(n: int) -> bool:
    """n が素数なら True を返す。"""
    if n < 2:
        return False
    # n の平方根までの約数を調べれば十分
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


def primes_up_to(n: int) -> list[int]:
    """n 以下の素数をリストで返す。"""
    return [k for k in range(2, n + 1) if is_prime(k)]

