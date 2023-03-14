from datetime import date, timedelta

date01 = date.today()  
date02 = date.today() + timedelta(1)
date03 = date.today() + timedelta(2)

list_investment = [
    {"name": "Alexandre", "quantity": "20", "date": date01},
    {"name": "João", "quantity": "21", "date": date02},
    {"name": "Luana", "quantity": "22", "date": date03}
]

quantity = 45

if list_investment is not None:
    quantity_investment = 0
    for investment in list_investment:
        quantity_investment += int(investment["quantity"])

    if quantity <= quantity_investment:
        list_investment.sort(key=lambda value: value["date"])
        for investment in list_investment:
            counter = 0
            quantity_value_investment = int(investment["quantity"])
            if quantity_value_investment > 0 and quantity > 0:
                falta = quantity_value_investment - quantity
                if falta < 0:
                    new_investment_value = 0
                    quantity_value_investment = new_investment_value
                else:
                    new_investment_value = quantity_value_investment - quantity
                    quantity_value_investment = new_investment_value
                quantity = falta * -1

            investment["quantity"] = quantity_value_investment
            new_investment = investment
            list_investment.pop(counter)
            list_investment.append(new_investment)
            counter += 1
    else:
        raise AttributeError(f'Quantidade de assets é insuficiente para a operação! Sua quantidade atual é {quantity_investment} e você quer vender {quantity}. Faltam {quantity - quantity_investment}.')
else:
    print('A lista está vazia!')

print(list_investment)