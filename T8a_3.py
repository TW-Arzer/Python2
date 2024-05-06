import re

pattern = re.compile(r"^(?:\d{4}\s+\d{4}\s+\d{4}\s+\d{4}|\d{16})$")


def code(s):
    match = pattern.match(s)
    digits = [int(d) for d in s.replace(" ", "")]
    sum_total = sum(digits)
    total = sum_total % 10 == 0

    if match and total:
        return f"Le numéro de carte {s} est valide"

    else:
        return f"Le numéro de carte {s} n'est pas valide"


if __name__ == '__main__':

    list = ['0123456789012345', '01234567890123456', '0123 4567 89012345', '0123 4567 8901 2345', '0123 4567 8901 2340',
            '0123 4567 8901 2345', '0123 4567 8901234']

    for i in list:
        print(f"{code(i)}\n")