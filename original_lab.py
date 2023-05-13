def main_menu():
    print('----MAIN MENU----')
    print('s: Shop')
    print('x: Exit')
    ans = input('Option: ').strip().lower()
    while ans != 's' and ans != 'x':
        ans = input('Invalid (s/x): ').strip().lower()
    return ans


def cart_menu():
    print('----CART MENU----')
    print('1: Cookie $1.50')
    print('2: Sandwich - $4.00')
    print('3: Water - $1.00')
    ans = input('Item: ').strip().lower()
    while ans.isalpha() or not 1 <= int(ans) <= 3:
        ans = input('Invalid (1-3): ').strip().lower()
    ans = int(ans)

    return ans


def main():
    cookie = 0
    sandwich = 0
    water = 0
    total = 0
    response = main_menu()
    while response == 's':
        item = cart_menu()
        if item == 1:
            print('Added cookie')
            cookie += 1
            total += 1.5
        if item == 2:
            print('Added sandwich')
            sandwich += 1
            total += 4
        if item == 3:
            print('Added water')
            water += 1
            total += 1
        response = main_menu()
    print('----------------------------------')
    print(f'({cookie}) - Cookie = ${(cookie * 1.5):.2f}')
    print(f'({sandwich}) - Sandwich = ${(sandwich * 4):.2f}')
    print(f'({water}) - Water = ${(water * 1):.2f}')
    print('----------------------------------')
    print(f'GRAND TOTAL = ${total:.2f}')
    print('----------------------------------')


if __name__ == '__main__':
    main()