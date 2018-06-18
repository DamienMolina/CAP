import math
from constantes import *
#Define all the functions used in the csv reader
def gen_dict_relais(row, numero_relais, distance=-1):
    #Will generate all the stats for one runner
    #
    #If distance is not set (==-1), it will be based on "classic ekiden"
    #Relay 1,3,5 => 5km
    #Relay 2,4 => 10km
    #Relay 6 => 7,195km
    if distance == -1:
        if numero_relais in [0, 2, 4]:
            distance = 5
        elif numero_relais in [1, 3]:
            distance = 10
        else:
            distance = 7.195
    name = row[list_name[numero_relais]]
    name_split = name.split(",")
    #dict_relais = {last_name: row[list_name[numero_relais]]}#Numero relais [1-6];
    dict_relais = {last_name: name_split[0], first_name: name_split[1]}
    category_team = row[category]
    time_relay = row[list_time[numero_relais]]
    dict_relais[category] = category_team
    dict_relais[time] = time_relay
    dict_relais[relay_number] = numero_relais+1
    dict_relais[bib_number] = row[bib_number]
    dict_relais[team_name] = row[team_name]
    speed = compute_speed_kmh(distance, time_relay)
    if speed != 0:
        pace = 60./speed
    else:
        pace = 0
    pace_minute = math.floor(pace)
    pace_second = (pace - pace_minute)*60
    dict_relais[speed_relay] = "{}".format(round(speed, 2))
    dict_relais[pace_relay] = "{0:02d}:{1:02d}".format(pace_minute, round(pace_second), 0)
    return dict_relais

#Pretty print for 
def int_2_minutes(minutes):
    return "{0:02d}:{0:02d}".format(int(minutes), int((minutes-int(minutes))*60))
