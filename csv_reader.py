import csv
import os
import math
from operator import itemgetter
from constantes import *
from fonctions import * 
if not os.path.exists(dossier_sortie):
    os.makedirs(dossier_sortie)
#The fields we want to display in the output file
list_fields = [ranking, bib_number, category, team_name, last_name, first_name, time,
               relay_number, speed_relay, pace_relay]


with open(csv_ekiden, 'r') as csvfile:
    ekiden_reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    list_5_km = []
    list_10_km = []
    list_7_km = []
    for row in ekiden_reader:
        #For each row in the csv file
        #it will join all the 5k runner,
        #all the 10k runner
        #and all the 7k runner
        #gen_dict_relais take in input:
        #the whole row
        #the nth relay we want to add in the list
        list_5_km.append(gen_dict_relais(row, 0))
        list_5_km.append(gen_dict_relais(row, 2))
        list_5_km.append(gen_dict_relais(row, 4))
        list_10_km.append(gen_dict_relais(row, 1))
        list_10_km.append(gen_dict_relais(row, 3))
        list_7_km.append(gen_dict_relais(row, 5))
    #To sort all the lists, first we need to have all the datas
    #Then, we can order by (key) the time spent to run the segment.
    sorted_list_5_km = sorted(list_5_km, key=itemgetter(time))
    for i in range(len(sorted_list_5_km)):
        sorted_list_5_km[i][ranking] = i+1
        #Fastest runner is the number 1, not number 0
    sorted_list_10_km = sorted(list_10_km, key=itemgetter(time))
    for i in range(len(sorted_list_10_km)):
        sorted_list_10_km[i][ranking] = i+1
    sorted_list_7_km = sorted(list_7_km, key=itemgetter(time))
    for i in range(len(sorted_list_7_km)):
        sorted_list_7_km[i][ranking] = i+1
    #Write all the datas in a different file
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
