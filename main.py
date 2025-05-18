import sys
import os
import json
from classes import *
from colorama import init, Fore, Style

init(autoreset=True)

def show_menu():
    print('╔══════════════════════════════════════════╗')
    print('║         ' + Style.BRIGHT + 'GREEK SCRABBLE CLI GAME' + Style.NORMAL + '          ║')
    print('╠══════════════════════════════════════════╣')
    print('║ 1. Παίξε                                 ║')
    print('║ 2. Σκορ / Στατιστικά                     ║')
    print('║ q. Έξοδος                                ║')
    print('╚══════════════════════════════════════════╝')

def show_stats():
    print(Fore.YELLOW + '\n=============== ΣΤΑΤΙΣΤΙΚΑ ===============')
    if not os.path.exists('results_data.json') or os.path.getsize('results_data.json') == 0:
        print('Δεν υπάρχουν στατιστικά.')
        return

    with open('results_data.json') as stats_file:
        data = json.load(stats_file)

    games_played = len(data["games"])
    avg_p1 = sum(g["player_score"] for g in data["games"]) // games_played
    avg_cpu = sum(g["cpu_score"] for g in data["games"]) // games_played

    print(f'Παίχτηκαν {games_played} παρτίδες.')
    print(f'Μ.Ο. Παίκτη: {avg_p1} πόντοι')
    print(f'Μ.Ο. Υπολογιστή: {avg_cpu} πόντοι')
    print('Αναλυτικά σκορ:')
    for g in data["games"]:
        print(f'  Παίκτης {g["player_score"]} - {g["cpu_score"]} Υπολογιστής')

# Main loop
while True:
    show_menu()
    user_input = input(Fore.GREEN + '\nΔιάλεξε ενέργεια (1, 2, q): ').strip()

    while user_input not in ('1', '2', 'q'):
        print(Fore.RED + '⛔ Μη αποδεκτή εντολή.')
        user_input = input('👉 Δοκίμασε ξανά (1, 2, q): ').strip()

    if user_input == 'q':
        print(Fore.MAGENTA + "\n👋 Έξοδος από το παιχνίδι. Αντίο!")
        sys.exit()

    elif user_input == '1':
        g = Game()
        g.setup()
        g.run()
        g.end()
        print(Fore.MAGENTA + '\n***************** GAME OVER *****************')

    elif user_input == '2':
        show_stats()
