import pymysql
import matplotlib.pyplot as plt

connexion = pymysql.connect(host='localhost',
				     user='root',
				     password='bigbrother',
				     db='gym')

def plot():

    # Initialisation et déclaration du curseur
    cursor = connexion.cursor()

    cursor.execute("SELECT name, id FROM exercises")
    result = cursor.fetchone()
    while result:
        print(result[0] +  " = " + "[" + str(result[1]) + "]")
        result = cursor.fetchone()


    # Demande d'informations à l'utilisateur
    print("")
    exo_char = input("Vous désirez afficher les données liées à quel exercice ?\n")
    exo = int(exo_char)

    cursor.execute("SELECT name_table FROM exercises WHERE id =  %s", exo)
    result = cursor.fetchone()
    exo_table = result[0]

    # Création de tableaux
    tab_day_x = []
    tab_weight_y = []
    tab_sets = []
    tab_reps = []

    cursor.execute("SELECT day, weight, sets, reps FROM " + str(exo_table))
    result = cursor.fetchone()
    while result:
        day = str(result[0])
        weight = result[1]
        sets = result[2]
        reps = result[3]

        tab_day_x.append(day)
        tab_weight_y.append(weight)
        tab_sets.append(sets)
        tab_reps.append(reps)

        result = cursor.fetchone()

    plt.title("Évolution des charges")
    plt.plot(tab_day_x, tab_weight_y, 'bo-')
    plt.xlabel("Temps")
    plt.ylabel("Poids")
    plt.ylim([0, 50])
    
    for i in range(len(tab_day_x)):
        plt.text(tab_day_x[i], tab_weight_y[i] + 1, str(tab_sets[i]) + " s & " + str(tab_reps[i]) + " r")
        
    plt.show()

plot()