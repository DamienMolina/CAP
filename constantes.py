name_first_relay = "Relayeur 1"
name_second_relay = "Relayeur 2"
name_third_relay = "Relayeur 3"
name_fourth_relay = "Relayeur 4"
name_fifth_relay = "Relayeur 5"
name_sixth_relay = "Relayeur 6"

time_first_relay = "{} Temps".format(name_first_relay)
time_second_relay = "{} Temps".format(name_second_relay)
time_third_relay = "{} Temps".format(name_third_relay)
time_fourth_relay = "{} Temps".format(name_fourth_relay)
time_fifth_relay = "{} Temps".format(name_fifth_relay)
time_sixth_relay = "{} Temps".format(name_sixth_relay)

list_name = [name_first_relay, name_second_relay, name_third_relay,
             name_fourth_relay, name_fifth_relay, name_sixth_relay]
list_time = [time_first_relay, time_second_relay, time_third_relay,
             time_fourth_relay, time_fifth_relay, time_sixth_relay]
def compute_speed_kmh(distance, time):
    #time follows the format HH:mm:ss
    #distance in km
    #speed in km/h
    time_split = time.split(":")
    hour = int(time_split[0])
    minute = int(time_split[1])
    second = int(time_split[2])
    speed = distance/(hour+minute/60.+second/3600.)
    return speed
