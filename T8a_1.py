import re

pattern_email = r"^[A-Za-z0-9.'!#$%&*+-/=?^_`{|}~]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

email_regex = re.compile(pattern_email)

list = ["example@example.com",
        "test.user@example.co.uk",
        "test_user@exemple.com",
        "invalid-email@exemple",
        "user@website",
        "user.name@web-site.com",
        "user+mailbox/department=shipping@example.com"]

for i in list:
    if email_regex.match(i):
        print(f"{i} est valide")
    else:
        print(f"{i} n'est pas valide")