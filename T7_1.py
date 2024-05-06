from datetime import *
import pytz


def str_date(d):
    return d.strftime("%d/%m/%Y %Hh:%M")


def str_timedelta(td):
    jours = td.days
    minutes = (td.seconds // 60)
    return f"{jours} jours, {minutes} minutes"


if __name__ == '__main__':
    dt = datetime.now()
    print(str_date(dt))
    td = timedelta(days=3, hours=11, minutes=40)
    print(str_timedelta(td))

    d1 = "27/03/2023 07h50"
    d2 = "27/03/2023 14h50"

    date1 = datetime.strptime(d1, "%d/%m/%Y %Hh%M")
    date2 = datetime.strptime(d2, "%d/%m/%Y %Hh%M")

    delta = date2 - date1

    print(str_date(date1))
    print(str_date(date2))
    print(str_timedelta(delta))

    paris_tz = pytz.timezone("Europe/Paris")
    macao_tz = pytz.timezone("Asia/Macao")

    d1_paris = paris_tz.localize(date1)
    d2_macao = macao_tz.localize(date2)

    print(d1_paris)
    print(d2_macao)

    delta_tz = d2_macao - d1_paris
    print(str_timedelta(delta_tz))



