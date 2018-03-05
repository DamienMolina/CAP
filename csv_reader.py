import csv
from operator import itemgetter
csv_ekiden = "EKIDEN_TOULON/Resultats_ekiden_toulon.csv"

def gen_dict_relais(row, numero_relais):
    dict_relais = {'Nom': row['Relayeur {}'.format(numero_relais)]}
    dict_relais['Temps'] = row['Relayeur {} Temps'.format(numero_relais)]
    dict_relais['Relais numero'] = numero_relais
    dict_relais['Numero dossard'] = row['N° Equipe']
    dict_relais['Equipe'] = row['Equipe']
    return dict_relais
with open(csv_ekiden, 'r') as csvfile:
    ekiden_reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    list_5_km = []
    list_10_km = []
    list_7_km = []
    for row in ekiden_reader:
        list_5_km.append(gen_dict_relais(row, 1))
        list_5_km.append(gen_dict_relais(row, 3))
        list_5_km.append(gen_dict_relais(row, 5))
        list_10_km.append(gen_dict_relais(row, 2))
        list_10_km.append(gen_dict_relais(row, 4))
        list_7_km.append(gen_dict_relais(row, 6))
    print(list_5_km)
    sorted_list_5_km = sorted(list_5_km, key=itemgetter('Temps'))
    for i in range(len(sorted_list_5_km)):
        sorted_list_5_km[i]['Classement'] = i+1
    sorted_list_10_km = sorted(list_10_km, key=itemgetter('Temps'))
    for i in range(len(sorted_list_10_km)):
        sorted_list_10_km[i]['Classement'] = i+1
    sorted_list_7_km = sorted(list_7_km, key=itemgetter('Temps'))
    for i in range(len(sorted_list_7_km)):
        sorted_list_7_km[i]['Classement'] = i+1
    list_fields = ["Classement", "Numero dossard", "Equipe", "Nom", "Temps", "Relais numero"]
with open('5km.csv', 'w') as csvfile_5km:
    writer = csv.DictWriter(csvfile_5km, list_fields)
    writer.writeheader()
    writer.writerows(sorted_list_5_km)
with open('10km.csv', 'w') as csvfile_10km:
    writer = csv.DictWriter(csvfile_10km, list_fields)
    writer.writeheader()
    writer.writerows(sorted_list_10_km)
with open('7km.csv', 'w') as csvfile_7km:
    writer = csv.DictWriter(csvfile_7km, list_fields)
    writer.writeheader()
    writer.writerows(sorted_list_7_km)
