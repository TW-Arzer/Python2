from datetime import *

s1 = "05/01/20 10h45, 500 jours"
s2 = "2020-08-10 1:05pm; 2020-08-18 4:10pm"

s1_split = s1.split(", ")
s2_split = s2.split("; ")

date1 = datetime.strptime(s1_split[0], "%d/%m/%y %Hh%M")
days = int(s1_split[1].split(" ")[0])
delta1 = timedelta(days=days)

date2 = datetime.strptime(s2_split[0], "%Y-%m-%d %I:%M%p")
date2_2 = datetime.strptime(s2_split[1], "%Y-%m-%d %I:%M%p")

print(datetime.weekday(date1), date1.strftime("%A"), date1.strftime("%W"))

delta2 = date2_2 - date2

new_expiration = date1 + delta1 + delta2
print(new_expiration)


date_changement = "01/01/2022"
date_new = datetime.strptime(date_changement, "%d/%m/%Y")

print(date_new < new_expiration)

now = datetime.now()

print(now < new_expiration)