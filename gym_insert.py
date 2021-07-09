import pymysql
from datetime import datetime, date


connexion = pymysql.connect(host='localhost',
				     user='root',
				     password='bigbrother',
				     db='gym')

def insert_data():

    # Initialisation et déclaration du curseur
    cursor = connexion.cursor()

    # Demande d'informations à l'utilsateur
    print("")
    date_char = input("À quelle date avez-vous effectué cet entraînement ? (Au format YYYY-MM_DD)\n")
    live_date = datetime.strptime(date_char, "%Y-%m-%d")

    # Demande d'informations à l'utilsateur
    print("")
    nb_exos_char = input("Combien d'exercices avez-vous effectué ce jour là ?\n")
    nb_exos = int(nb_exos_char)

    for i in range(nb_exos):

        # Affichage des zone du corps ainsi que leur numéro correspondant
        cursor.execute("SELECT NAME, ZONE FROM TYPE_SEANCE")
        result = cursor.fetchone()
        while result:
            print(result[0] +  " = " + "[" + str(result[1]) + "]")
            result = cursor.fetchone()

        # Demande d'informations à l'utilsateur
        print("")
        zone_char = ""
        if i == 0 :
            zone_char = input("Quelle partie du corps avez-vous travaillé durant votre premier exercice ?\n")
        elif i == nb_exos - 1:
            zone_char = input("Quelle partie du corps avez-vous travaillé durant votre " + str(i + 1) + "ème et dernier exercice ?\n")
        else :
            zone_char = input("Quelle partie du corps avez-vous travaillé durant votre " + str(i + 1) + "ème exercice ?\n")
        
        zone = int(zone_char)

        # Affichage de tous les exercices travaillant la zone du corps selectionnée
        print("")
        print("Voici, ci-dessous, les exercices que vous auriez pu faire :")
        print("")
        cursor.execute("SELECT NAME, ID FROM EXERCISES WHERE ZONE = %s", zone)
        result = cursor.fetchone()
        while result:
            print(result[0] +  " = " + "[" + str(result[1]) + "]")
            result = cursor.fetchone()

        # Demande d'informations à l'utilsateur
        print("")
        exo_char = input("Tapez le numéro qui est associé à l'exercice que vous voulez sélectionner\n")
        exo = int(exo_char)

        # Affichage de l'exercice + Confirmation
        cursor.execute("SELECT NAME, ID, NAME_TABLE FROM EXERCISES WHERE ID = %s", exo)
        result = cursor.fetchone()
        print("")
        print("Vous avez choisi l'exercice " + result[0])

        nom_table = result[2]

        # Demande d'informations complémentaires
        print("")
        weight_char = input("Indiquez le poids maximal soulevé pendant cet exercice (Si c'est un décimal, mettez un point et non une virgule)\n")
        weight = float(weight_char)

        print("")
        set_char = input("Indiquez le nombre de séries effectuées avec le poids max\n")
        set_var = int(set_char)

        print("")
        rep_char = input("Indiquez le nombre maximal de répetitions effectuées avec le poids max\n")
        rep_var = int(rep_char)

        print("")
        time_char = input("Indiquez le temps max, en secondes, durant lequel vous avez effectué l'exercice (Si l'exercice ne s'y prête pas, tapez 0)\n")
        time = int(time_char)

        print("")
        superset_char = input("Indiquez si cet exercice fait partie d'un superset\n")
        superset = bool(superset_char)

        # Date du jour
        now = date.today()

        # Insertion dans la table concernée = Enregistrement des données

        # Enregistrement du premier exercice de la séance
        sql = "INSERT INTO " + str(nom_table) + " (day, weight, sets, reps, time, superset) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (live_date, weight, set_var, rep_var, time, superset)
        cursor.execute(sql, val)

        connexion.commit()

    print("")
    print("Les données liées à la séance effectuée le " + date_char + " ont été enregistrées !\n")


insert_data()