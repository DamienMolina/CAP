# -*- coding: utf-8 -*- 
#!/usr/bin/python3.4
import csv
import statistics as s
from fonctions import *
from constantes import *

first = 0
second = 0
egal = 0
list_of_times = []
list_first_passage = []
list_second_relay = []
list_third_relay = []
with open(csv_duo, 'r') as csvfile:
    datas = csv.reader(csvfile)
    i = 1
    for row in datas:
        if datas.line_num >= 5:
            tps_1 = row[5]
            tps_2 = row[12]
            tps_3 = row[13]
            tps = [tps_1, tps_2, tps_3]
            if all(tps):
                tps_num_first = int(tps_1.split(':')[0])+int(tps_1.split(':')[1])/60.
                tps_num_second = int(tps_2.split(':')[0])+int(tps_2.split(':')[1])/60.
                tps_num_third= int(tps_3.split(':')[0])+int(tps_3.split(':')[1])/60.
                tps_num = [tps_num_first, tps_num_second, tps_num_third]
                list_first_passage.append(tps_num_first)
                list_second_relay.append(tps_num_second)
                list_third_relay.append(tps_num_third)
                if tps_num[0]>tps_num[1]:
                    second +=1
                elif tps_num[0]<tps_num[1]:
                    first +=1
                else:
                    egal +=1
                list_of_times.append(tps)
    avg_first = s.mean(list_first_passage)
    avg_second = s.mean(list_second_relay)
    avg_third = s.mean(list_third_relay)
    print("Nombre de fois ou le premier est plus rapide:\t{}".format(first))
    print("Nombre de fois ou le second est plus rapide:\t{}".format(second))
    print(u"Nombre de fois ou les deux font le meme temps:\t{}".format(egal))
    print(u"Moyenne de tous les premiers coureurs:\t{}".format(int_2_minutes(avg_first)))
    print(u"Moyenne de tous les seconds coureurs:\t{}".format(int_2_minutes(avg_second)))
    print(u"Moyenne de tous les troisièmes passages:\t{}".format(int_2_minutes(avg_third)))



