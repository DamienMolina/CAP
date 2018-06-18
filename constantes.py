csv_duo = "resultats_corrida_pedestre_2017.csv"
#Filename for the original file
csv_ekiden = "EKIDEN_TOULON/Resultats_ekiden_toulon.csv"
#folder where the individual results will be written
dossier_sortie = "resultats_individuels"

#Fields in the original csv file
#The fields to indicate the name of each relay-runner
team_name = "Equipe"
name_first_relay = "Relayeur 1"
name_second_relay = "Relayeur 2"
name_third_relay = "Relayeur 3"
name_fourth_relay = "Relayeur 4"
name_fifth_relay = "Relayeur 5"
name_sixth_relay = "Relayeur 6"

#The fields to indicate the times of each relay-runner
#In this case, it follows the format for the names:
# Relayeur X Temps
team_time = "TEMPS Equipe"
time_first_relay = "{} Temps".format(name_first_relay)
time_second_relay = "{} Temps".format(name_second_relay)
time_third_relay = "{} Temps".format(name_third_relay)
time_fourth_relay = "{} Temps".format(name_fourth_relay)
time_fifth_relay = "{} Temps".format(name_fifth_relay)
time_sixth_relay = "{} Temps".format(name_sixth_relay)

#To access the name of the relay numbered X,
#you call list_name[X-1]
list_name = [name_first_relay, name_second_relay, name_third_relay,
             name_fourth_relay, name_fifth_relay, name_sixth_relay]
#Same thing for the times
list_time = [time_first_relay, time_second_relay, time_third_relay,
             time_fourth_relay, time_fifth_relay, time_sixth_relay]
#Category is the category of the team
#In the case where each runner are Master 1(40-49 yo) 
#The category is "MAS".
#
#Else If three runner are male and three runner are female,
#The category is "MIX"
#
#Else If more than three runners are male (4-2, 5-1, 6-0)
#The category is "HOM"
#
#Else if more than three runners are female
#The category is "FEM"
#There is also a military category (MIL)
#and a corporate category (ENTR)
category = "Categ"
ranking_category = "Pos. Categ"#Ranking of the team for its category
ranking = "Place"
bib_number = "N° Equipe"


#################################################
#New fields for the individual stats
first_name = "Prenom"
last_name = "Nom"
time = "Temps"
relay_number = "Relais numero" #The n-th relay
speed_relay = "Vitesse"
pace_relay = "Allure"
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
