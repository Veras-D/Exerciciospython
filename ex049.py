import colorama
for cont in range(1, 10):
    for cont2 in range(1, 10):
        print(f'|{colorama.Fore.RED}{cont}{colorama.Style.RESET_ALL} X {colorama.Fore.YELLOW}{cont2}'
              f'{colorama.Style.RESET_ALL} = {colorama.Fore.GREEN}{cont * cont2}{colorama.Style.RESET_ALL}', end='\t')
    print('|')
