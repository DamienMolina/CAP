import csv
import os
import math
from operator import itemgetter
from constantes import *
csv_ekiden = "EKIDEN_TOULON/Resultats_ekiden_toulon.csv"
dossier_sortie = "resultats_individuels"
if not os.path.exists(dossier_sortie):
    os.makedirs(dossier_sortie)
list_fields = ["Classement", "Numero dossard", "Equipe", "Nom", "Temps",
               "Relais numero", "Vitesse", "Allure"]

def gen_dict_relais(row, numero_relais, distance=-1):
    #If distance is not set (==-1), it will be based on "classic ekiden"
    #Relay 1,3,5 => 5km
    #Relay 2,4 => 10km
    #Relay 6 => 7,195km
    if distance == -1:
        if numero_relais in [1, 3, 5]:
            distance = 5
        elif numero_relais in [2, 4]:
            distance = 10
        else:
            distance = 7.195
    dict_relais = {'Nom': row[list_name[numero_relais-1]]}#Numero relais [1-6];
    #Range de la liste [0-5]
    time = row[list_time[numero_relais-1]]
    dict_relais['Temps'] = time
    dict_relais['Relais numero'] = numero_relais
    dict_relais['Numero dossard'] = row['N° Equipe']
    dict_relais['Equipe'] = row['Equipe']
    speed = compute_speed_kmh(distance, time)
    if speed != 0:
        pace = 60./speed
    else:
        pace = 0
    pace_minute = math.floor(pace)
    pace_second = (pace - pace_minute)*60
    dict_relais['Vitesse'] = "{}".format(round(speed, 2))
    dict_relais['Allure'] = "{0:02d}:{0:02d}".format(pace_minute, round(pace_second), 0)
    return dict_relais
def compute_speed_kmh(distance, time):
    #time follows the format HH:mm:ss
    #distance in km
    #speed in km/h
    list_time = time.split(":")
    hour = int(list_time[0])
    minute = int(list_time[1])
    second = int(list_time[2])
    speed = distance/(hour+minute/60.+second/3600.)
    return speed

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
with open('{}/5km.csv'.format(dossier_sortie), 'w') as csvfile_5km:
    writer = csv.DictWriter(csvfile_5km, list_fields)
    writer.writeheader()
    writer.writerows(sorted_list_5_km)
with open('{}/10km.csv'.format(dossier_sortie), 'w') as csvfile_10km:
    writer = csv.DictWriter(csvfile_10km, list_fields)
    writer.writeheader()
    writer.writerows(sorted_list_10_km)
with open('{}/7km.csv'.format(dossier_sortie), 'w') as csvfile_7km:
    writer = csv.DictWriter(csvfile_7km, list_fields)
    writer.writeheader()
    writer.writerows(sorted_list_7_km)
