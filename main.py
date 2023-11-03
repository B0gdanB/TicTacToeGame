position_dict = {
    "a1": ' ',
    "a2": ' ',
    "a3": ' ',
    "b1": ' ',
    "b2": ' ',
    "b3": ' ',
    "c1": ' ',
    "c2": ' ',
    "c3": ' ',
}


def check_choice(choice_from_user, some_dict):
    if choice_from_user[:2] in some_dict:
        if some_dict[choice_from_user[:2]] != ' ':
            print("Place has already occupied!")
        else:
            some_dict[choice_from_user[:2]] = choice_from_user[3]


def start_new_game():
    global position_dict, go_on
    new_game = input("Would you like start new game? Then press 'Y' ")
    if new_game == "Y":
        position_dict = {
            "a1": ' ',
            "a2": ' ',
            "a3": ' ',
            "b1": ' ',
            "b2": ' ',
            "b3": ' ',
            "c1": ' ',
            "c2": ' ',
            "c3": ' ',
        }

    else:
        go_on = False


go_on = True
while go_on:
    print(f"""
         a     b     c
     1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
       -----------------
     2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
       -----------------
     3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
    """)

    choice = input('Make your choice (For example a1-X or b2-0) ')

    check_choice(choice, position_dict)

    if position_dict["a1"] == "X" and position_dict["a2"] == "X" and position_dict["a3"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["a1"] == "0" and position_dict["a2"] == "0" and position_dict["a3"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    elif position_dict["b1"] == "X" and position_dict["b2"] == "X" and position_dict["b3"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["b1"] == "0" and position_dict["b2"] == "0" and position_dict["b3"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    elif position_dict["c1"] == "X" and position_dict["c2"] == "X" and position_dict["c3"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["c1"] == "0" and position_dict["c2"] == "0" and position_dict["c3"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    elif position_dict["a1"] == "X" and position_dict["b1"] == "X" and position_dict["c1"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["a1"] == "0" and position_dict["b1"] == "0" and position_dict["c1"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    elif position_dict["a2"] == "X" and position_dict["b2"] == "X" and position_dict["c2"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["a2"] == "0" and position_dict["b2"] == "0" and position_dict["c2"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    elif position_dict["a3"] == "X" and position_dict["b3"] == "X" and position_dict["c3"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["a3"] == "0" and position_dict["b3"] == "0" and position_dict["c3"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    elif position_dict["a1"] == "X" and position_dict["b2"] == "X" and position_dict["c3"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["a1"] == "0" and position_dict["b2"] == "0" and position_dict["c3"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    elif position_dict["a3"] == "X" and position_dict["b2"] == "X" and position_dict["c1"] == "X":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player X won!")
        start_new_game()
    elif position_dict["a3"] == "0" and position_dict["b2"] == "0" and position_dict["c1"] == "0":
        print(f"""
             a     b     c
         1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
           -----------------
         2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
           -----------------
         3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
        """)
        print("Player 0 won!")
        start_new_game()
    count = 0
    for item in position_dict:

        if position_dict[item] != ' ':
            count += 1

        if count == 9:
            print(f"""
                         a     b     c
                     1   {position_dict['a1']}  |  {position_dict['b1']}  |  {position_dict['c1']}
                       -----------------
                     2   {position_dict['a2']}  |  {position_dict['b2']}  |  {position_dict['c2']}
                       -----------------
                     3   {position_dict['a3']}  |  {position_dict['b3']}  |  {position_dict['c3']}
                    """)
            print("Draw!")
            start_new_game()
            count = 0
