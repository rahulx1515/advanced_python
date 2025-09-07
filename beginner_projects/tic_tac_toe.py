def print_board(lst):
    st = '''
{}|{}|{}
------
{}|{}|{}
------
{}|{}|{}
'''.format(*lst)
    print(st)

choices = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print('Welcome to the Tic Tac Toe')
print_board(choices)
turns = 'X'
name1 = input('enter ur name ')
name2 = input('enter ur name ')
name = name1
for i in range(9):
    mv = int(input(f'Its your turn {name}, Your Move [0-8]'))
    if choices[mv] == ' ':
        choices[mv] = turns

    turns = 'X' if turns == '0' else '0'
    if choices[0] == choices[1] == choices[2] !=' ':
        print(f'You won {name}')
        break
    elif choices[3] == choices[4] == choices[5] !=' ':
        print(f'You won {name}')
        break
    elif choices[6] == choices[7] == choices[8] !=' ':
        print(f'You won {name}')
        break
    elif choices[0] == choices[3] == choices[6] !=' ':
        print(f'You won {name}')
        break
    elif choices[1] == choices[4] == choices[7] !=' ':
        print(f'You won {name}')
        break
    elif choices[2] == choices[5] == choices[8] !=' ':
        print(f'You won {name}')
        break
    elif choices[0] == choices[4] == choices[8] !=' ':
        print(f'You won {name}')
        break
    elif choices[0] == choices[4] == choices[8] !=' ':
        print(f'You won {name}')
        break
    name = name1 if name == name2 else name2
    print_board(choices)
print('its draw')
    
    
