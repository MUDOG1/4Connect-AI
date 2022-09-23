#!/usr/bin/env python3
'''Vier Gewinnt!'''

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

class Spieler:
    '''Spieler Klasse'''
    def __init__(self, name: str, farbe: str) -> None:
        self.name = name
        self.farbe = farbe 
    
class Spielfeld:
    '''Spielfeld Klasse'''
    def __init__(self) -> None:
        self.breite = 7
        self.hoehe = 6
        self.spalten_stand = [0 for _ in range(self.breite)]
        self.felder = [["_" for _ in range(self.breite)] for _ in range(self.hoehe)]
        self.spielverlauf = []

    def spielfeld_anzeigen(self) -> None:
        for reihe in reversed(range(self.hoehe)):
            for spalte in range(self.breite):
                print("| " + str(self.felder[reihe][spalte]) + " ", end='')
            print("|")
        print("  0   1   2   3   4   5   6")

    def spielstein_einwerfen(self, spieler) -> bool:
        while(True):
            stelle = int(input("0 - 6: "))
            cls()
            if (self.spalten_stand[stelle] < self.hoehe):
                self.felder[self.spalten_stand[stelle]][stelle] = spieler.farbe
                self.spielverlauf.append([self.spalten_stand[stelle],[stelle]])
                gewonnen = self.__check(spieler, self.spalten_stand[stelle], stelle)

                self.spalten_stand[stelle] += 1
                self.spielfeld_anzeigen()
                if(gewonnen):
                    return True
                break
            else:
                print("Spalte voll du Hong, such ne andere aus")
                self.spielfeld_anzeigen()
    def manipulate_field(self, spieler, reihe, spalte):
        self.felder[reihe][spalte] = spieler.farbe

    def spielstein_einwerfen_test(self, spieler, stelle) -> bool:
        while(True):
            cls()
            if (self.spalten_stand[stelle] < self.hoehe):
                self.felder[self.spalten_stand[stelle]][stelle] = spieler.farbe
                self.spielverlauf.append([self.spalten_stand[stelle],[stelle]])
                gewonnen = self.__check(spieler, self.spalten_stand[stelle], stelle)

                self.spalten_stand[stelle] += 1
                self.spielfeld_anzeigen()
                if(gewonnen):
                    return True
                break
            else:
                print("Spalte voll du Hong, such ne andere aus")
                self.spielfeld_anzeigen()

    def __check(self, spieler, reihe, spalte):
        ergebnisse = []
        ergebnisse.append(self.__check_horizontal(spieler, reihe, spalte))
        ergebnisse.append(self.__check_vertical(spieler, reihe, spalte))
        ergebnisse.append(self.__check_diagonal_mirrored(spieler, reihe, spalte))
        ergebnisse.append(self.__check_diagonal_up(spieler, reihe, spalte))
        print("erg", ergebnisse)
        return 4 in ergebnisse
    
    def best_move(self, spieler, gegner):
        ergebnisse = []
        fut_ergebnisse = []
        empty = Spieler("", "_")

        for spalte in range(self.breite):
            reihe = self.spalten_stand[spalte]
            if (reihe > 5):
                continue
            tmp = []
            tmp.append(self.__check_horizontal(spieler, reihe , spalte))
            tmp.append(self.__check_vertical(spieler, reihe, spalte))
            tmp.append(self.__check_diagonal_mirrored(spieler, reihe, spalte))
            tmp.append(self.__check_diagonal_up(spieler, reihe, spalte))
            ergebnisse.append(tmp)
        
        for spalte in range(self.breite):
            reihe = self.spalten_stand[spalte]
            if (reihe > 5):
                continue
            feld.manipulate_field(spieler, reihe, spalte)
            tmp = []
            tmp.append(self.__check_horizontal(spieler, reihe , spalte))
            tmp.append(self.__check_vertical(spieler, reihe, spalte))
            tmp.append(self.__check_diagonal_mirrored(spieler, reihe, spalte))
            tmp.append(self.__check_diagonal_up(spieler, reihe, spalte))
            fut_ergebnisse.append(tmp)
            feld.manipulate_field(empty, reihe, spalte)
        
        print("all moves\t", ergebnisse)
        print("fut_erg\t\t", fut_ergebnisse)
        
        best_fut_max = 0
        best_sum = 0
        best_fut_move = 0
        for fut_move in fut_ergebnisse:
            if(max(fut_move) == 4):
                best_fut_move = fut_ergebnisse.index(fut_move)
                best_fut_max = 4
                break
            elif (max(fut_move) > best_fut_max):
                best_fut_move = fut_ergebnisse.index(fut_move)
                best_fut_max = max(fut_move)
                best_sum = sum(fut_move)
            elif (max(fut_move) == best_fut_max):
                if (sum(fut_move) >= best_sum):
                    best_fut_move = fut_ergebnisse.index(fut_move)
                    best_fut_max = max(fut_move)
                    best_sum = sum(fut_move)
        if(best_fut_move == 0 and best_fut_max == 0):
            best_fut_move = 3
        print("best future move:", best_fut_move, best_fut_max)

        best_moves_indices = []
        for move in ergebnisse:
            if (sum(move)==0):
                continue
            else:
                best_moves_indices.append(ergebnisse.index(move))

        best_fut = []
        for i in best_moves_indices:
            best_fut.append(fut_ergebnisse[i])
        print("best future moves", best_fut)

        best_max = 0
        best_sum = 0
        best_move = 0
        for i in best_moves_indices:
            if(max(ergebnisse[i]) == 4):
                best_move = i
                best_max = 4
                break
            elif (max(ergebnisse[i]) > best_max):
                best_move = i
                best_max = max(ergebnisse[i])
                best_sum = sum(ergebnisse[i])
            elif (max(ergebnisse[i]) == best_max):
                if (sum(ergebnisse[i]) >= best_sum):
                    best_move = i
                    best_max = max(ergebnisse[i])
                    best_sum = sum(ergebnisse[i])
        print("best move:", best_move)

        best_max = 0
        best_sum = 0
        best_move = 0
        for i in best_moves_indices:
            if(max(fut_ergebnisse[i]) == 4):
                best_move = i
                best_max = 4
                break
            elif (max(fut_ergebnisse[i]) > best_max):
                best_move = i
                best_max = max(fut_ergebnisse[i])
                best_sum = sum(fut_ergebnisse[i])
            elif (max(fut_ergebnisse[i]) == best_max):
                if (sum(fut_ergebnisse[i]) >= best_sum):
                    best_move = i
                    best_max = max(fut_ergebnisse[i])
                    best_sum = sum(fut_ergebnisse[i])

        if(best_move == 0 and best_max == 0):
            best_move = 3
        
        print(spieler.name, "best move:", best_move)
        return (best_fut_move, best_fut_max)
    
    def block_opponent(self, spieler, gegner):
        return self.best_move(gegner, spieler)

    def choose_move(self, spieler, gegner):
        block = self.block_opponent(spieler, gegner)
        print("opponents best move", block)
        if block[1] >= 3: 
            return block[0]
        elif block[1] == 1:
            return 3
        else:
            return self.best_move(spieler, gegner)[0]

    def __check_horizontal(self, spieler, reihe, spalte):
        start = spalte - 3
        end = spalte + 3
        if start < 0: start = 0 
        if end <= 3: end = 4
        if end > 6: end = 6
        if end == 6 and start == 3: start = 2
       # print(spalte, "s", start, "e", end, len(range(start, end + 1)))
        reihen_string = ""
        for i in range(start, end + 1):
            reihen_string += self.felder[reihe][i]

        sub_win = spieler.farbe * 4
        sub_three = spieler.farbe * 3
        sub_two = spieler.farbe * 2
        if sub_win in reihen_string:
            return 4
        elif sub_three in reihen_string:
            return 3
        elif sub_two in reihen_string:
            return 2
        else:
            return 1   

    def __check_vertical(self, spieler, reihe, spalte):
        vier_in_reihe = 0
        maximal = 0

        start = reihe - 3
        end = reihe + 3
        if start < 0: start = 0
        if end > 5: end = 5
        #if end == 5 and start == 2: start = 1

        reihen_string = ""
        for i in range(start, end + 1):
            reihen_string += self.felder[i][spalte]
        
        sub_win = spieler.farbe * 4
        sub_three = spieler.farbe * 3
        sub_two = spieler.farbe * 2
        if sub_win in reihen_string:
            return 4
        elif sub_three in reihen_string:
            return 3
        elif sub_two in reihen_string:
            return 2

        else:
            return 1  

    def __check_diagonal_mirrored(self, spieler, reihe, spalte):
        upper_list_mirrored = feld.return_upper_coordinates_mirrored(reihe, spalte)
        lower_list_mirrored = feld.return_lower_coordinates_mirrored(reihe, spalte)
        coordinates_mirrored = upper_list_mirrored + lower_list_mirrored

        maximal = 0
        vier_in_reihe = 0
        
        for field in coordinates_mirrored:
            if self.felder[field[0]][field[1]] == spieler.farbe:
                vier_in_reihe += 1
            else:
                maximal = max(vier_in_reihe, maximal)
                vier_in_reihe = 0
            if vier_in_reihe >= 4:
                return 4
        
        #falls keine 4 erreicht wurden, wird die höchste Anzahl ausgegeben
        return maximal

    def return_lower_coordinates_mirrored(self, reihe, spalte):
        lower_mirrored = []

        for _ in range(3):
            if(reihe >= 1 and spalte != self.breite-1):
                reihe -= 1
                spalte += 1
                lower_mirrored.append([reihe, spalte])

        return lower_mirrored

    def return_upper_coordinates_mirrored(self, reihe, spalte):
        upper = []
        upper.append([reihe, spalte])
        for _ in range(3):
            if(reihe <= 4 and spalte != 0):
                reihe += 1
                spalte -= 1
                upper.append([reihe, spalte])

        return list(reversed(upper))

    def __check_diagonal_up(self, spieler, reihe, spalte):
        upper_list = feld.return_upper_coordinates(reihe, spalte)
        lower_list = feld.return_lower_coordinates(reihe, spalte)
        coordinates = upper_list + lower_list

        maximal = 0
        vier_in_reihe = 0

        for field in coordinates:
            if vier_in_reihe == 4:
                return 4
            if self.felder[field[0]][field[1]] == spieler.farbe:
                vier_in_reihe += 1
            else:
                maximal = max(vier_in_reihe, maximal)
                vier_in_reihe = 0
        
        #falls keine 4 erreicht wurden, wird die höchste Anzahl ausgegeben
        return maximal

    def return_upper_coordinates(self, reihe, spalte):
        upper = []
        upper.append([reihe, spalte])

        for _ in range(3):
            if(reihe != 0 and spalte != 0):
                reihe -= 1
                spalte -= 1
                upper.append([reihe, spalte])

        return list(reversed(upper))

    def return_lower_coordinates(self, reihe, spalte):
        lower = []
        for _ in range(3):
            if(reihe != self.hoehe-1 and spalte != self.breite-1):
                reihe += 1
                spalte += 1
                lower.append([reihe, spalte])

        return lower

    
if __name__ == "__main__":
    debug = False
    automatic = True
    spieler1 = Spieler("Levent", "R")
    spieler2 = Spieler("Spiro", "Y")
    roboter = Spieler("K.I.", "Y")
    roboter2 = Spieler("K.I.2", "R")
    spielzuege = [[6, 5], [5, 4], [3, 4], [4, 3], [2, 3], [3,1]]
    spielzuege2 = [[0,1], [1,2], [3, 2], [2,3], [4,3], [3,1]]
    feld = Spielfeld()
    feld.spielfeld_anzeigen()
    if(debug):
        if(automatic):
            for zug in spielzuege + spielzuege2:
                best_move = feld.choose_move(roboter, roboter)
                input()
                win = feld.spielstein_einwerfen_test(roboter, best_move)
                if win:
                    print(roboter.name, "hat gewonnen")
                    break
                best_move = feld.choose_move(roboter2, roboter)
                input()
                win = feld.spielstein_einwerfen_test(roboter2, best_move)
                if win:
                    print(roboter2.name, "hat gewonnen")
                    break
        else:
            for zug in spielzuege2:
                feld.choose_move(spieler1, spieler2)
                input()
                win = feld.spielstein_einwerfen_test(spieler1, zug[0])
                if win:
                    print(spieler1.name, "hat gewonnen")
                    break
                feld.choose_move(spieler2, spieler1)
                input()
                win = feld.spielstein_einwerfen_test(spieler2, zug[1])
                
                if win:
                    print(spieler2.name, "hat gewonnen")
                    break
    else:
        if(automatic):
            for _ in range(21):
                win = feld.spielstein_einwerfen(spieler1)
                if win:
                    print(spieler1.name, "hat gewonnen")
                    break
                best_move = feld.choose_move(roboter, spieler1)
                input()
                win = feld.spielstein_einwerfen_test(roboter, best_move)
                if win:
                    print(roboter.name, "hat gewonnen")
                    break
        else:
            for _ in range(21):
                win = feld.spielstein_einwerfen(spieler1)
                if win:
                    print(spieler1.name, "hat gewonnen")
                    break
                win = feld.spielstein_einwerfen(spieler2)
                if win:
                    print(spieler2.name, "hat gewonnen")
                    break
     