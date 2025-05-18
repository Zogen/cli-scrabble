import sys
from classes import *

condition = True
while condition:

    print('*****************SCRABBLE******************\n'
          '-------------------------------------------\n'
          '1: ΠΑΙΞΕ\n'
          '2: ΣΚΟΡ/ΣΤΑΤΙΣΤΙΚΑ\n'
          'q: ΕΞΟΔΟΣ\n'
          '-------------------------------------------')
    user_input = input('Διάλεξε ενέργεια: ')

    while user_input != '1' and user_input != '2' and user_input != 'q':
        user_input = input('Σφάλμα! Διάλεξε κάποια αποδεκτή ενέργεια (1, 2, q): ')

    if user_input == 'q':
        sys.exit("Έξοδος")
    elif user_input == '1':
        g = Game()
        g.setup()
        g.run()
        g.end()
        del g
        print('\n*****************GAME OVER*****************\n')
    elif user_input == '2':
        if not os.path.exists('results_data.json'):
            print('===============ΣΤΑΤΙΣΤΙΚΑ==================\n'
                  'Δεν υπάρχουν στατιστικά')
        elif os.path.getsize('results_data.json') != 0:
            with open('results_data.json') as stats_file:
                x = json.load(stats_file)
            games_played = len(x["games"])
            avg_p1 = 0
            avg_cpu = 0
            for game in x["games"]:
                avg_p1 += game["player_score"]
                avg_cpu += game["cpu_score"]
            avg_p1 = round(avg_p1/games_played)
            avg_cpu = round(avg_cpu/games_played)
            print('===============ΣΤΑΤΙΣΤΙΚΑ==================\n'
                  'Παίχτηκαν', games_played, 'παρτίδες\n'
                  'Ο παίκτης συγκέντρωσε κατά μέσο όρο', avg_p1, 'πόντους\n'
                  'Ο υπολογιστής συγκέντρωσε κατά μέσο όρο', avg_cpu, 'πόντους\n'
                  'Αναλυτικά:')
            for partida in x["games"]:
                print('\tΠαίκτης', partida["player_score"], '-', partida["cpu_score"], 'Υπολογιστής')
        else:
            print('===============ΣΤΑΤΙΣΤΙΚΑ==================\n'
                  'Δεν υπάρχουν στατιστικά')

