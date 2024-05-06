import unicodedata


with open("sample.txt", "r", encoding="ISO8859-1") as f:
    r = f.read()

with open("sample_unicode.txt", "w", encoding="utf-8") as f:
    f.write(r)

with open("sample_ascii.txt", "wb") as f:
    f.write(unicodedata.normalize("NFKD", r).encode("ASCII", "ignore"))

