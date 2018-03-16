import csv
from constantes import *
#To analyze the strategy of an ekiden, for now,
#I only analyze the 5km runner.
#I'll look who runs the fastest between the 1st, 3rd, and 5th relay.

csv_ekiden = "EKIDEN_TOULON/Resultats_ekiden_toulon.csv"
list_orders = []
with open(csv_ekiden) as csvfile:
    ekiden_reader = csv.DictReader(csvfile, delimiter=';')
    for row in ekiden_reader:
        time_5k = [row[list_time[i]] for i in  range(0, 5, 2)]
        time_10k = [row[list_time[i]] for i in range(1, 5, 2)]
        time_7k = row[list_time[5]]
        speed_5k = [round(compute_speed_kmh(5, i), 2) for i in time_5k]
        speed_10k = [round(compute_speed_kmh(10, i), 2) for i in time_10k]
        speed_7k = round(compute_speed_kmh(7.195, time_7k), 2)
        #In this case, the *order* list is composed of N items:
        # * the first item is the first runner
        # * the second item is the second runner
        # * ...
        # * the last item is the last runner
        #To each of these items we attribute a value 
        #between 0 and the number of relay-runner:
        #The fastest will receive 0
        #The second fastest will receive 1
        #etc...
        #The slowest runner will receive N-1
        order = [0,1,2]#0 is the fastest relay, 1 the 2nd fastest and 2 the last
        if speed_5k[0] > speed_5k[1]:
            if speed_5k[0] > speed_5k[2]:
                order[0] = 0
                if speed_5k[1] > speed_5k[2]:
                    order[1] = 1
                    order[2] = 2
                else:
                    order[1] = 2
                    order[2] = 1
            else:
                order[2] = 0
                order[0] = 1
                order[1] = 2
        else:
            if speed_5k[1] > speed_5k[2]:
                order[1] = 0
                if speed_5k[0] > speed_5k[2]:
                    order[0] = 1
                    order[2] = 2
                else:
                    order[0] = 2
                    order[2] = 1
            else:
                order[2] = 0
                order[1] = 1
                order[0] = 2
        print(order)
        list_orders.append(order)
    print(list_orders)
    first_relay = 0
    second_relay = 0
    third_relay = 0
    list_relay = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in list_orders:
        first_relay += i[0]
        second_relay += i[1]
        third_relay += i[2]
        for j in range(3):
            list_relay[j][i[j]] += 1
    print("Le premier relais est le plus rapide {} fois".format(list_relay[0][0]))
    print("Le deuxième relais est le plus rapide {} fois".format(list_relay[1][0]))
    print("Le troisième relais est le plus rapide {} fois\n".format(list_relay[2][0]))

    print("Le premier relais est le deuxième plus rapide {} fois".format(list_relay[0][1]))
    print("Le deuxième relais est le deuxième plus rapide {} fois".format(list_relay[1][1]))
    print("Le troisième relais est le deuxième plus rapide {} fois\n".format(list_relay[2][1]))
    print("Le premier relais est le plus lent {} fois".format(list_relay[0][2]))
    print("Le deuxième relais est le plus lent {} fois".format(list_relay[1][2]))
    print("Le troisième relais est le plus lent {} fois".format(list_relay[2][2]))
