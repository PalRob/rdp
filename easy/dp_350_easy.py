# TODO:
# Move input to separate file;

def parse_input(input_str):
    input_list = input_str.strip().split('\n')
    shelves = input_list[0]
    shelves = [int(n) for n in shelves.strip().split()]

    books_input = input_list[1:]
    books = []
    for book in books_input:
        num_of_pages = int(book[:book.index(' ')])
        book_title = book[book.index(' '):].strip()
        books.append((num_of_pages, book_title))

    shelves = sorted(shelves, reverse=True)
    books = sorted(books, key=lambda book: book[0], reverse=True)

    return (shelves, books)

def get_bookshelves(input_str):
    shelves, books = parse_input(input_str)
    books_sizes = [book[0] for book in books]
    num_of_shelves = len(shelves)
    num_used = 0

    used_shelves = []
    for s in shelves:
        empty_shelve = []
        empty_shelve.append(s)
        used_shelves.append(empty_shelve)


    cant_fit_biggest = max(books_sizes) > max(shelves)
    cant_fit_all = sum(books_sizes) > sum(shelves)
    if cant_fit_biggest or cant_fit_all:
        return None

    for book in books:
        for i in range(num_of_shelves):
            if used_shelves[i][0] > book[0]:
                used_shelves[i][0] -= book[0]
                used_shelves[i].append(book)

                if i+1 > num_used:
                    num_used = i+1
                used_shelves = (sorted(used_shelves[:num_used], key=lambda shelf: shelf[0] )
                        + used_shelves[num_used:])
                break
        else:
            return None

    return used_shelves

def print_used_shelves(input_str):
    used_shelves = [s for s in get_bookshelves(input_str) if len(s)>1]
    for i, shelf in enumerate(used_shelves):
        print("shelve num {0}, space left {1}:".format(i+1, shelf[0]))
        for book in shelf[1:]:
            print("\t{}, {} pages".format(book[1], book[0]))

input_1 = """150 150 300 150 150
70 A Game of Thrones
76 A Clash of Kings
99 A Storm of Swords
75 A Feasts for Crows
105 A Dance With Dragons"""

input_2 = """270 142 501 865 384 957 947 603 987 428 907 10 691 707 397 917 492 750 935 672 935 712 234 683 702 508 822 379 36 59 382 280 867 155 829 756 360 995 526 52 559 250 450 843 523 446 972 555 55 985 81 831 43 802 473 379 461 639 910 529 128 878 914 426 569 59 139 913 69 649 501 889 470 112 92 6 80 571 220 22 676 91 889 799 115 194 555 477 277 718 378 838 822 358 178 562 674
96 b400786
69 b390773
174 b410413
189 b337528
80 b308576
194 b151872
190 b174310
157 b272731
45 b326576
112 b379689
177 b18459
122 b915759
138 b967342
96 b786519
184 b718074
75 b696975
192 b46366
168 b533904
45 b885475
186 b872991
63 b231207
162 b912709
123 b786720
7 b743805
120 b862301
54 b929784
89 b61876
168 b775890
87 b850242
60 b695331
0 b56157
139 b875241
78 b281324
122 b236962
1 b79403
68 b213353
103 b650997
97 b955752
177 b815100
139 b958679
43 b829736
163 b445471
94 b472821
167 b5429
57 b946679
13 b748794
146 b920913
17 b547056
33 b437091
12 b247401
120 b228908
178 b509018
98 b482352
152 b915322
14 b874214
71 b164605
11 b457140
35 b502201
5 b15232
49 b641136
166 b385360
183 b78285
199 b274935
195 b424221
79 b422570
150 b502699
41 b662132
63 b430898
111 b813368
100 b700970
157 b803925
140 b611243
25 b877197
136 b577201
94 b50211
56 b762270
120 b578094
21 b672002
9 b107630
156 b547721
186 b911854
71 b594375
32 b330202
3 b464002
36 b718293
44 b282975
130 b826246
77 b529800
117 b66381
89 b949447
133 b348326
178 b517646
184 b809038
105 b70260
182 b894577
123 b203409
79 b174217
159 b552286
40 b854638
78 b159990
139 b743008
1 b714402
153 b923819
107 b201001
48 b567066
138 b570537
100 b64396
139 b412215
132 b805036
121 b772401
120 b370907
51 b388905
77 b442295
152 b195720
46 b453542"""

input_3 = """150 150 300 150 150
70 A
76 B
99 C
75 D
105 E"""

print_used_shelves(input_2)