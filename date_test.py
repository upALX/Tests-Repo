from datetime import date, timedelta

date01 = date.today()  
date02 = date.today() + timedelta(1)
date03 = date.today() + timedelta(2)

list_investment = [
    {"name": "Alexandre", "quantity": "20", "date": date01},
    {"name": "João", "quantity": "20", "date": date02},
    {"name": "Luana", "quantity": "20", "date": date03}
]
list_investment.sort(key=lambda value: value["date"])

print(list_investment)

for investment in list_investment:
    print(investment["date"])

