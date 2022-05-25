def commands(com_input):
    if com_input !='End':
        print(f'Processing "{com_input}" command...')
        com_input = input()
        commands(com_input)
    else:
        print('Good bye!')


com_input = input()
commands(com_input)