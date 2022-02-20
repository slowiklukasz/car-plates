

"""
Tablice indywidualne – zasady Tak jak w przypadku zwykłych białych tablic, 
tak i tu obowiązuje rejonizacja. Indywidualny numer rejestracyjny składa się 
z: 

1.wyróżnika województwa (pierwsza znak to litera oznaczająca województwo, 
w którym auto zostało zarejestrowane, drugi znak to liczba kontrolna, którą 
jest cyfra od 0 do 9),

2. wyróżnika indywidualnego (od 3 do 5 znaków, może zawierać 
litery: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V, W, X, Y, Z, 

3. przy czym nie więcej niż dwa ostatnie znaki mogą być cyframi)

Czytaj więcej: https://www.wyborkierowcow.pl/tablice-rejestracyjne/
indywidualne-tablice-rejestracyjne/
"""

# DISTRICTS
ww = {
    "DOLNOŚLĄSKIE": "D",
    "KUJAWSKO-POMORSKIE": "C",
    "LUBELSKIE": "L",
    "LUBUSKIE": "F",
    "ŁÓDZKIE": "E",
    "MAŁOPOLSKIE": "K",
    "MAZOWIECKIE": "W",
    "OPOLSKIE": "O",
    "PODKARPACKIE": "R",
    "PODLASKIE": "B",
    "POMORSKIE": "G",
    "ŚLĄSKIE": "S",
    "ŚWIĘTORZYSKIE": "T",
    "WARMIJSKI-MAZURSKIE": "N",
    "WIELKOPOLSKIE": "P",
    "ZACHODNIO-POMORSKIE": "Z"
    }


# L33T SPEAK
l33t = {
    "a": [4],
    "b": [8, 13],
    "g": [6],
    "i": [1],
    "l": [1],
    "m": ["em", "AA"],
    "o": [0, "p"],
    "p": [9],
    "r": [2],
    "s": [5, "z", "es", "ehs"],
    "t": [7],
    "u": ["v"],
    "w": ["vv", "uu"],
    "x": ["ecks"],
    "y": ["j", 7],
    "z": [2, "s"]
    }

# REVERSE L33T SPEAK
r_l33t = {
    0: ["O", "D"],
    1: ["I", "L"],
    2: ["Z"],
    3: ["E", "e", "m", "w"],
    4: ["h", "A", "y"],
    5: ["S"],
    6: ["b", "G"],
    7: ["T", "j", "L"],
    8: ["B", "x"],
    9: ["g", "J"]
    }


path = r"C:\Users\lukas\Desktop\l33t\dict.txt"

### ALL DISTRICTS SHORTCUT + ID
districts = [val for val in ww.values()]
nbs = [nb for nb in range(10)]

d_ids = []
for dist in districts:
    for nb in range(10):
        d_ids.append("{}{}".format(dist, nb))
d_ids = sorted(d_ids)

districts = [val.lower() for val in ww.values()]
keys = [key for key in l33t.keys()]
r_keys = [str(key) for key in r_l33t.keys()]


reg_lst = []

with open(path, "r") as f:
    for line in f:
        # word = line[:-1]
        word = line

        # INCLUDING 2 FIRST SYMBOLS - 1st FROM DISTRICT AND 2nd FROM NUMBERS 0-9
        if len(word) <= 7 and word[0] in districts:
            if word[1] in keys:
                for val in l33t[word[1]]:
                    new_word = word.replace(word[1], str(val))
                    new_word = "{} {}".format(new_word[:2], new_word[2:])
                    if new_word.upper() not in reg_lst and len(new_word) in range(6, 9):
                        reg_lst.append(new_word.upper())
                        
                    if len(new_word) == 7: # registry has 6 chars
                        for i in range(10):
                            new_word2 = "{}{}".format(new_word, i)
                            if new_word2.upper() not in reg_lst and len(new_word) in range(6, 9):
                                reg_lst.append(new_word2.upper())
                    
                    if len(new_word) == 6: # registry has 5 chars
                        for i in range(10):
                            new_word2 = "{}{}".format(new_word, i)
                            if new_word2.upper() not in reg_lst and len(new_word2) in range(6, 9):
                                reg_lst.append(new_word2.upper())
                            
                            for j in range(10):
                                new_word3 = "{}{}{}".format(new_word, i, j)
                                if new_word3.upper() not in reg_lst and len(new_word3) in range(6, 9):
                                    reg_lst.append(new_word3.upper())
                    
                    if len(new_word) == 5: # registry has 4 chars (have to add 1 or 2 numbers at the end)
                        for i in range(10):
                            new_word2 = "{}{}".format(new_word, i)
                            if new_word2.upper() not in reg_lst and len(new_word2) in range(6, 9):
                                reg_lst.append(new_word2.upper())
                                    
                            for j in range(10):
                                new_word3 = "{}{}{}".format(new_word, i, j)
                                if new_word3.upper() not in reg_lst and len(new_word3) in range(6, 9):
                                    reg_lst.append(new_word3.upper())
                                        
                                for k in range(10):
                                    new_word4 = "{}{}{}{}".format(new_word, i, j, k)
                                    if new_word4.upper() not in reg_lst and len(new_word4) in range(6, 9):
                                        reg_lst.append(new_word4.upper())
                                        
                    if len(new_word) == 4: # registry has 3 chars (have to add 2 or 3 numbers at the end)
                        for i in range(10):
                            for j in range(10):
                                new_word2 = "{}{}{}".format(new_word, i, j)
                                if new_word2.upper() not in reg_lst and len(new_word2) in range(6, 9):
                                    reg_lst.append(new_word2.upper())
                                
                                for k in range(10):
                                    new_word3 = "{}{}{}{}".format(new_word, i, j, k)
                                    if new_word3.upper() not in reg_lst and len(new_word3) in range(6, 9):
                                        reg_lst.append(new_word3.upper())

                                    for l in range(10):
                                        new_word4 = "{}{}{}{}{}".format(new_word, i, j, k, l)
                                        if new_word4.upper() not in reg_lst and len(new_word4) in range(6, 9):
                                            reg_lst.append(new_word4.upper())
                    

        # WITHOUT 2 FIRST SYMBOLS - 1st FROM DISTRICT AND 2nd FROM NUMBERS 0-9

        ## takes too long
        # if len(word) == 2:
        #     for d_id in d_ids:
        #         word2 = "{} {}".format(d_id, word.upper())
        #
        #         for i in range(10):
        #             word3 = "{}{}".format(word2, i)
        #             if word3 not in reg_lst and len(word3) in range(6, 9):
        #                 reg_lst.append(word3)
        #
        #             for j in range(10):
        #                 word4 = "{}{}{}".format(word2, i, j)
        #                 if word4 not in reg_lst and len(word4) in range(6, 9):
        #                     reg_lst.append(word4)
        #
        #                 for k in range(10):
        #                     word5 = "{}{}{}{}".format(word2, i, j, k)
        #                     if word5 not in reg_lst and len(word5) in range(6, 9):
        #                         reg_lst.append(word5)


        if len(word) in (3, 4, 5):
            for d_id in d_ids:
                word2 = "{} {}".format(d_id, word.upper())
                
                if word2 not in reg_lst and len(word2) in range(6, 9):
                    reg_lst.append(word2)

                    if len(word2) == 7: # len word 2 without space == 6
                        for i in range(10):
                            word3 = "{}{}".format(word2, i)
                            if word3 not in reg_lst and len(word3) in range(6, 9):
                                reg_lst.append(word3)

                    elif len(word2) == 6: # len word 2 without space == 5
                        for i in range(10):
                            for j in range(10):
                                word3 = "{}{}{}".format(word2, i, j)
                                if word3 not in reg_lst and len(word3) in range(6, 9):
                                    reg_lst.append(word3)

                
                if word2[-1] in keys and word2[-2] not in keys:
                    for val in l33t[word2[-1]]:
                        new_word = word2.replace(word2[-1], str(val))
                        if new_word not in reg_lst and len(new_word) in range(6, 9):
                            reg_lst.append(new_word)
                            
                elif word2[-1] not in keys and word2[-2] in keys:
                    for val in l33t[word2[-2]]:
                        new_word = word2.replace(word2[-2], str(val))
                        if new_word not in reg_lst and len(new_word) in range(6, 9):
                            reg_lst.append(new_word)
            
                elif word2[-1] in keys and word2[-1] in keys:
                    for val_1 in l33t[word2[-1]]:
                        for val_2 in l33t[word2[-2]]:
                            new_word = word.replace(word2[-1], str(val_1))
                            new_word2 = new_word.replace(word2[-2], str(val_2))
                            if new_word2 not in reg_lst and len(new_word2) in range(6, 9):
                                reg_lst.append(new_word2)


# def reg_variation(word):
#     if len(word) == 3:
#         for i in range(10):
#             word2 = "{}{}".format(word, i)
#
#             for j in range(10):
#                 word3 = "{}{}{}".format(word, i, j)
#
#     elif len(word) == 4:
#         for i in range(10):
#             word2 = "{}{}".format(word, i)

    



for i in reg_lst:
    print(i)

print(len(reg_lst))


