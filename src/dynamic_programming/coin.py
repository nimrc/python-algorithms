"""
Coin problem
"""
import sys


class Kind(int):
    Small = 1
    Mid = 5
    Big = 11


class Coin:
    @staticmethod
    def need(count: int) -> int:
        if count < Kind.Small:
            return sys.maxsize

        if count is Kind.Small or count is Kind.Mid or count is Kind.Big:
            return 1

        return min(Coin.need(count - Kind.Small), Coin.need(count - Kind.Mid), Coin.need(count - Kind.Big)) + 1
