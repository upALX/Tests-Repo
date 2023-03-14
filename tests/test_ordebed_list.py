list_desordened = None # ["154565", "154566", "154567", "154568"]

if list_desordened is None:
    selic_number = "312999"
else:

    list_ordened = sorted(list_desordened, reverse=True)
    print(list_ordened)
    
    selic_number = list_ordened[0]
    print(type(selic_number))
    selic_operation_number = int(selic_number) + 1
    list_desordened.append(selic_operation_number)

print(f'{type(selic_operation_number)} e {selic_operation_number}')
print(list_desordened)
