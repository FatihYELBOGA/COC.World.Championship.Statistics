import pandas as pd

df = pd.read_excel("players_report.xlsx")

def show_player_info(player_name):

    total_percentages_of_attack = 0
    total_stars_of_attack = 0
    total_percentages_of_defence = 0
    total_stars_of_defence = 0
    line_number_attack = 0
    line_number_defence = 0
    total_3_attack = 0
    total_2_attack = 0
    total_1_attack = 0
    total_0_attack = 0
    total_3_defence = 0
    total_2_defence = 0
    total_1_defence = 0
    total_0_defence = 0

    for player in df[player_name].tolist():

        attack = player.split(", ")[0]
        defence =player.split(", ")[1]

        if not(attack == "NONE"):
            total_percentages_of_attack += int(attack.split(" - ")[0].split("%")[0])

            total_stars_of_attack += int(attack.split(" - ")[1].split("*")[0])
            if(int(attack.split(" - ")[1].split("*")[0]) == 3):
                total_3_attack += 1
            if(int(attack.split(" - ")[1].split("*")[0]) == 2):
                total_2_attack += 1
            if(int(attack.split(" - ")[1].split("*")[0]) == 1):
                total_1_attack += 1
            if(int(attack.split(" - ")[1].split("*")[0]) == 0):
                total_0_attack += 1

            line_number_attack += 1

        if not(defence == "NONE"):
            total_percentages_of_defence += int(defence.split(" - ")[0].split("%")[0])

            total_stars_of_defence += int(defence.split(" - ")[1].split("*")[0])
            if(int(defence.split(" - ")[1].split("*")[0]) == 3):
                total_3_defence += 1
            if(int(defence.split(" - ")[1].split("*")[0]) == 2):
                total_2_defence += 1
            if(int(defence.split(" - ")[1].split("*")[0]) == 1):
                total_1_defence += 1
            if(int(defence.split(" - ")[1].split("*")[0]) == 0):
                total_0_defence += 1

            line_number_defence += 1

    print("------------------------------------------------------------")
    print(player_name,"PERFORMANCE DETAILS")
    print()
    print("total attack number:", line_number_attack)
    print("total 3* number of attacks:", total_3_attack)
    print("total 2* number of attacks:", total_2_attack)
    print("total 1* number of attacks:", total_1_attack)
    print("total 0* number of attacks:", total_0_attack)
    print("average percentage of attacks:", round(total_percentages_of_attack / line_number_attack, 2))
    print("average star of attacks:", round(total_stars_of_attack / line_number_attack, 2))
    print()
    print("total defence number:", line_number_defence)
    print("total 3* number of defences:", total_3_defence)
    print("total 2* number of defences:", total_2_defence)
    print("total 1* number of defences:", total_1_defence)
    print("total 0* number of defences:", total_0_defence)
    print("average percentage of defences:", round(total_percentages_of_defence / line_number_defence, 2))
    print("average star of defences:", round(total_stars_of_defence / line_number_defence, 2))
    
print("------------------------------------------------------------")
print("------------------------------------------------------------")
print("ALL STATISTICS BY FATIH YELBOGA")
print("------------------------------------------------------------")
show_player_info("FATIH")
show_player_info("RAKIBUL")
show_player_info("ADEM")
show_player_info("ANURID")
show_player_info("AKASH")
print("------------------------------------------------------------")
print()
print()

def show_team_info():

    total_percentages_of_attack = 0
    total_stars_of_attack = 0
    total_percentages_of_defence = 0
    total_stars_of_defence = 0
    total_win = 0
    total_loss = 0
    total_draw = 0
    match_number = 0

    for match_result in df["MATCH RESULT"].tolist():

        score = match_result.split(", ")[0]
        percentage = match_result.split(", ")[1]
        result = match_result.split(", ")[2]

        match_number += 1
        total_stars_of_attack += float(score.split(" - ")[0])
        total_stars_of_defence += float(score.split(" - ")[1])
        total_percentages_of_attack += float(percentage.split(" - ")[0].split("%")[0])
        total_percentages_of_defence += float(percentage.split(" - ")[1].split("%")[0])

        if (result == "WIN"):
            total_win += 1
        if (result == "LOSE"):
            total_loss += 1
        if(result == "DRAW"):
            total_draw += 1

    print("average percentage of attacks:", round(total_percentages_of_attack / match_number, 2))
    print("average star of attacks:", round(total_stars_of_attack / match_number, 2))
    print("average percentage of defences:", round(total_percentages_of_defence / match_number, 2))
    print("average star of defences:", round(total_stars_of_defence / match_number, 2))
    print("total win:", total_win)
    print("total loss:", total_loss)
    print("total draw:", total_draw)
    print("------------------------------------------------------------")

print("------------------------------------------------------------")
print("GENERAL TEAM PERFORMANCE")
show_team_info()