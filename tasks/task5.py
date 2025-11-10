# tasks/task5.py

def solve():
    symbols = input().split()
    first, second, third = symbols[0], symbols[1], symbols[2]
    print(f'РљРѕРґ СЃРёРјРІРѕР»Р° {first} СЂР°РІРµРЅ {ord(first)}')
    print(f'РљРѕРґ СЃРёРјРІРѕР»Р° {second} СЂР°РІРµРЅ {ord(second)}')
    print(f'РљРѕРґ СЃРёРјРІРѕР»Р° {third} СЂР°РІРµРЅ {ord(third)}')

# Leave the code below unchanged; it is used for tests
if __name__ == '__main__':
    solve()
