import csv
from constantes import *
#To analyze an ekiden, I think of two ways:
#Compare relay 1, 3 and 5 (all the 5km) and Relay 2 and 4 (all the 10km)
#If I want to analyze the relay 6 (7km), maybe we should compare the speed
#of all the  races and maybe interpolate between 5k and 10k
csv_ekiden = "EKIDEN_TOULON/Resultats_ekiden_toulon.csv"
with open(csv_ekiden) as csvfile:
    ekiden_reader = csv.DictReader(csvfile, delimiter=';')
    for row in ekiden_reader:
        runner_5k = [row[list_time[i]] for i in  range(0, 5, 2)]
        runner_10k = [row[list_time[i]] for i in range(1, 5, 2)]
        runner_7k = row[list_time[5]]

