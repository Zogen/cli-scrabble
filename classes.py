import random
import io
import os
import itertools
import json
from colorama import Fore, Style, init
init(autoreset=True)


values = {'Α': 1, 'Β': 8, 'Γ': 4, 'Δ': 4, 'Ε': 1,
          'Ζ': 10, 'Η': 1, 'Θ': 10, 'Ι': 1, 'Κ': 2,
          'Λ': 3, 'Μ': 3, 'Ν': 1, 'Ξ': 10, 'Ο': 1,
          'Π': 2, 'Ρ': 2, 'Σ': 1, 'Τ': 1, 'Υ': 2,
          'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3
          }

f = io.open("greek7.txt", mode="r", encoding="utf-8")
lines = [line.rstrip() for line in f]

counter = 0
words = dict()
for j in lines:
    words.update({j: counter})
    counter += 1

f.close()


class SakClass:

    def __init__(self):
        self.letters = {'Α': 12, 'Β': 1, 'Γ': 2, 'Δ': 2, 'Ε': 8,
                        'Ζ': 1, 'Η': 7, 'Θ': 1, 'Ι': 8, 'Κ': 4,
                        'Λ': 3, 'Μ': 3, 'Ν': 6, 'Ξ': 1, 'Ο': 9,
                        'Π': 4, 'Ρ': 5, 'Σ': 7, 'Τ': 8, 'Υ': 4,
                        'Φ': 1, 'Χ': 1, 'Ψ': 1, 'Ω': 3
                        }

    def __repr__(self):
        n = 0
        for i in self.letters:
            n = n + self.letters[i]
        return 'Στο σακουλάκι απομένουν %d γράμματα' % n

    def getLetters(self, player):
        hand = player.hand
        for i in range(7-len(hand)):
            if all(v == 0 for v in self.letters.values()):
                break
            x = random.choice(list(self.letters))
            while self.letters.get(x) < 1:
                x = random.choice(list(self.letters))
            hand.append(x)
            self.letters[x] = self.letters.get(x) - 1
        return hand

    def putBackLetters(self, hand):
        for i in hand:
            self.letters[i] = self.letters.get(i) + 1
            hand.remove(i)


class Player:

    def __init__(self):
        self.score = 0
        self.hand = list()

    def __repr__(self):
        return 'Score = %d' % self.score

    def gatherLetters(self, sakouli):
        self.hand = sakouli.getLetters(self)


class Human(Player):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Παίκτης, σκορ = %d' % self.score

    def play(self):

        for i in self.hand:
            print(i, values.get(i), end=',  ')
        print('\n')

        perms = list()
        for x in range(2, 8):
            p = itertools.permutations(self.hand, x)
            for y in p:
                perms.append(''.join(y))
        acceptableWords = list()
        for k in list(perms):
            if k in words:
                acceptableWords.append(k)

        action = input('Παίξε μια λέξη:')

        while action not in perms:
            if action == 'q':
                return 'q'
            elif action == 'p':
                return 'p'
            action = input('Δεν έχεις τα γράμματα γι αυτή τη λέξη. Προσπάθησε ξανά:')

        if action not in acceptableWords:
            print('Η λέξη αυτή δεν είναι αποδεκτή.')
        else:
            score = 0
            for i in action:
                score += values[i]
                self.hand.remove(i)
            print('Παίρνεις', score, 'πόντους')
            self.score += score


class Computer(Player):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Υπολογιστής, σκορ = %d' % self.score

    def play(self, hand):
        perms = list()
        for x in range(2, 8):
            p = itertools.permutations(hand, x)
            for y in p:
                perms.append(''.join(y))
        acceptableWords = list()
        for k in list(perms):
            if k in words:
                acceptableWords.append(k)

        score = 0
        bestWord = ''
        for i in acceptableWords:
            temp = 0
            for l in i:
                temp += values[l]
            if temp > score:
                bestWord = i
                score = temp

        if self.hand == hand: #εκτελουνται οταν παιζει το cpu
            for i in hand:
                print(i, end=' ')
            print('\n')
            for i in bestWord:
                self.hand.remove(i)
            self.score += score
            print(score, bestWord)
            return bestWord
        else: #εκτελειται για την υλοποιηση TEACH
            return bestWord


class Game:

    def __init__(self):
        self.rounds = 0
        self.winner = Player()
        self.sak = SakClass()
        self.p1 = Human()
        self.cpu = Computer()
        data = {}

    def __repr__(self):
        pass

    def setup(self):
        print('*************ΈΝΑΡΞΗ ΠΑΙΧΝΙΔΙΟΥ*************')
        self.p1.gatherLetters(self.sak)
        self.cpu.gatherLetters(self.sak)

    def run(self):
        p1_tempHand = self.p1.hand
        cpu_tempHand = self.cpu.hand

        while len(self.cpu.hand) >= 2 and len(self.p1.hand) >= 2:
            print('\n╔══════════════════════════════════════════╗')
            print(f'║           ΓΥΡΟΣ {self.rounds + 1}                        ║')
            print('╠══════════════════════════════════════════╣')
            print(f'║ {Fore.GREEN}Παίκτης: {self.p1.score} πόντοι{Style.RESET_ALL}' + ' ' * (25 - len(str(self.p1.score))) + '║')
            print(f'║ {Fore.RED}CPU: {self.cpu.score} πόντοι{Style.RESET_ALL}' + ' ' * (29 - len(str(self.cpu.score))) + '║')
            print('╚══════════════════════════════════════════╝')

            optWord = self.cpu.play(p1_tempHand)
            playerAction = self.p1.play()

            if playerAction == 'p':
                self.sak.putBackLetters(self.p1.hand)
            elif playerAction == 'q':
                break

            print(Fore.YELLOW + f'📣 Βέλτιστη λέξη CPU για το χέρι σου: {optWord}')

            self.cpu.hand = cpu_tempHand
            cpuAction = self.cpu.play(self.cpu.hand)

            if cpuAction == '':
                self.sak.putBackLetters(self.cpu.hand)

            print(Fore.GREEN + f'{self.p1}')
            print(Fore.RED + f'{self.cpu}')

            if len(self.p1.hand) < 7:
                self.p1.gatherLetters(self.sak)
            self.cpu.gatherLetters(self.sak)

            print(Fore.CYAN + f'{self.sak}')
            print(Fore.GREEN + 'Χέρι Παίκτη:', self.p1.hand)
            print(Fore.RED + 'Χέρι Υπολογιστή:', self.cpu.hand)

            self.rounds += 1

        print(Fore.MAGENTA + '\n============ ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ ============')
        print(f'Παίχτηκαν {self.rounds} γύροι.')
        if self.cpu.score > self.p1.score or playerAction == 'q':
            self.winner = self.cpu
        else:
            self.winner = self.p1
        print(f'🎉 Νικητής: {self.winner}')


    def end(self):
        result = {"games": []}

        data = result

        data["games"].append({"rounds": self.rounds,
                              "player_score": self.p1.score,
                              "cpu_score": self.cpu.score
                              })


        if not os.path.exists('results_data.json'):
            open('results_data.json', 'x')

        if os.path.getsize('results_data.json') == 0:
            with open('results_data.json', 'w') as f3:
                json.dump(result, f3, indent=2)
                return 0

        with open('results_data.json') as f2:
            x = json.load(f2)

        x["games"].append(data["games"][0])

        with open('results_data.json', 'w') as f2:
            json.dump(x, f2, indent=2)

        del x
        data.clear()


