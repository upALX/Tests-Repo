from datetime import datetime

horario = 'STR' + datetime.now().strftime('%Y%m%d%H%M%S%F').replace("-","")


print(f'{horario} + {str(len(horario))}')

print(len('20221027123025'))
print(len('20221026033951243'))
