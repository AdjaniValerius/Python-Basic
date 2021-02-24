
from datetime import datetime, timedelta
from time import sleep
# dit zijn de modules die ik nodig heb.


uur = input("Enter uur:")
minuut = input("Enter minuut:")
seconde = input("Enter seconde:")
# hier zet ik de gegevens in.


date_string = "20200101" + uur + minuut + seconde

date_object = datetime.strptime(date_string, "%Y%m%d%H%M%S")


while True:
    print(date_object.strftime("%H:%M:%S"))
    sleep(1)
    date_object += timedelta(seconds=1)
