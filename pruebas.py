import datetime

string = "{'0': {'0': 14, '1': 'recomendaciones de ricos restaurantes', '2': 'Comida', '3': 'Sun, 10 Jan 2021 00:00:00 GMT', '4': 'danbehar'}, '1': {'0': 15, '1': 'recomendaciones de lindos lugares en reu', '2': 'Turismo', '3': 'Tue, 07 Sep 2021 00:00:00 GMT', '4': 'danbehar'}}"

dicccio = eval(string)

print(dicccio)

for i in dicccio: 
    print(int(dicccio[i]['0']))