import math


class Fraction:

    def __init__(self, num=0, denom=1):
        if denom == 0:
            raise ZeroDivisionError
        self.__num = int(num)
        self.__denom = int(denom)
        self.simplify()

    def __str__(self):
        return f"{self.__num}/{self.__denom}"

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.value() == other.value()
        elif self.value() == other:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.value() < other.value()
        elif self.value() < other:
            return True
        return False

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.value() <= other.value()
        elif self.value() <= other:
            return True
        return False

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.value() >= other.value()
        elif self.value() >= other:
            return True
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.value() > other.value()
        elif self.value() > other:
            return True
        return False

    def __add__(self, other):
        if isinstance(other, Fraction):
            return self.add(other)
        elif isinstance(other, int):
            return self.add(Fraction(other))
        elif isinstance(other, float) and other.is_integer():
            self.add(Fraction(int(other)))
        else:
            raise TypeError(
                "Unsupported operand type"
            )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return self + Fraction(-other.get_num(), other.get_denom())
        elif isinstance(other, int) or (isinstance(other, float) and other.is_integer()):
            return self.add(Fraction(int(-other)))
        else:
            raise TypeError(
                "Unsupported operand type"
            )

    def value(self):
        return float(self.__num) / float(self.__denom)

    def get_num(self):
        return self.__num

    def get_denom(self):
        return self.__denom

    def set_num(self, num):
        self.__num = num

    def set_denom(self, denom):
        self.__denom = denom

    def simplify(self):
        gcd = math.gcd(self.__num, self.__denom)
        self.__num //= gcd
        self.__denom //= gcd

        if self.__denom < 0:
            self.__num *= -1
            self.__denom *= -1
        return self.__num, self.__denom

    def add(self, other):
        new_num = self.__num * other.__denom + self.__denom * other.__num
        new_denom = self.__denom * other.__denom
        result = Fraction(new_num, new_denom)
        result.simplify()
        return result

    def plus(self, other):
        new_num = self.__num * other.__denom + self.__denom * other.__num
        new_denom = self.__denom * other.__denom
        gcd = math.gcd(new_num, new_denom)
        new_num //= gcd
        new_denom //= gcd

        if new_denom < 0:
            new_num *= -1
            new_denom *= -1
        return f"{new_num}/{new_denom}"

    def equal(self, other):
        self.simplify()
        other.simplify()

        return self.__num == other.__num and self.__denom == other.__denom


if __name__ == "__main__":
    print(Fraction(-1, 2).equal(Fraction(2, -4)))
    print(Fraction(4, 2) < 2)
