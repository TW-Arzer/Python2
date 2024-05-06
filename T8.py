import re

pattern = r'^[A-Z]{2}$'
pattern2 = r'^[A-Z]{2}|[a-z]{2}$'  # | = oder
pattern3 = r'^\d{1,6}$'  # \d = Zahlen 0-9
pattern4 = r'^[1-9]\d{0,5}$'
pattern5 = r'^([A-Z]{2}|[a-z]{2})\s?[1-9]\d{0,5}$'  #\s? = 0 oder 1 whitespace, \s* = 0 oder mehrere whitespaces'

list_pattern5 = ["AB123456", "VD011111", "VD 1234567", "VD123456", "vd123456", "Vd123456", "VD 123456", "VD  123456", "VD t123456"]

def pattern_match(pattern, s):
	return re.match(pattern, s) is not None

	

print("\nPattern 1")
print(pattern_match(pattern, "AB"))
print(pattern_match(pattern, "ABC"))
print(pattern_match(pattern, "A"))
print(pattern_match(pattern, "ab"))

print("\nPattern 2")
print(pattern_match(pattern2, "aa"))
print(pattern_match(pattern2, "Ab"))
print(pattern_match(pattern2, "ab"))
print(pattern_match(pattern2, "AA"))

print("\nPattern 3")
print(pattern_match(pattern3, ""))
print(pattern_match(pattern3, "7"))
print(pattern_match(pattern3, "123456"))
print(pattern_match(pattern3, "1234567"))

print("\nPattern 4")
print(pattern_match(pattern4, ""))
print(pattern_match(pattern4, "01234"))
print(pattern_match(pattern4, "123456"))
print(pattern_match(pattern4, "1234567"))

print("\nPattern 5")
for i in list_pattern5:
	print(pattern_match(pattern5, i))
