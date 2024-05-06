import re

cantons = {"AG": "Argovie", "AI": "Appenzell Rhodes-Intérieures", "AR": "Appenzell Rhodes-Extérieure", "BE": "Bern",
           "BL": "Bâle-Campagne", "BS": "Bâle-Ville", "FR": "Fribourg", "GE": "Genève", "GL": "Glaris", "GR": "Grisons",
           "JU": "Jura", "LU": "Lucerne", "NE": "Neuchâtel", "NW": "Nidwald", "OW": "Obwald", "SG": "Saint-Gall", "SH":
           "Shaffhouse", "SO": "Soleure", "SZ": "Schwytz", "TG": "Thurgovie", "TI": "Tessin", "UR": "Uri", "VD": "Vaud",
           "VS": "Valais", "ZG": "Zoug", "ZH": "Zurich"}


def pattern(n):
    number_max = str(n)
    pattern_build = r'^([A-Z]{2}|[a-z]{2})\s?[1-9]\d{0,' + number_max + '}(?:\s([A-Z]{2}|[a-z]{2}))?$'
    return re.compile(pattern_build)


def pattern_match(compiled, s):
    match = compiled.match(s)
    if match:
        first = match.group(1)
        second = match.group(2) if match.group(2) else None

        valid_first = (first.upper() in cantons or first.lower() in cantons)

        if second:
            valid_second = second.upper() == first.upper() and (second.upper() in cantons or second.lower() in cantons)
            return valid_first and valid_second
        return valid_first
    return False


if __name__ == "__main__":

    n = 6

    list_pattern5 = ["AB123456", "VD011111", "VD 1234567", "VD123456", "vd123456", "Vd123456", "VD 123456",
                     "VD  123456", "VD t123456", "VD 1234 vd", "VD123 VD", "vd 123456vd"]

    for i in list_pattern5:
        print(f"{i}:\t {pattern_match(pattern(n), i)}")
