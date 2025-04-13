def words(num):
    return {str(d): 'nol odin dva tri chetire pyat shest sem vosem devyat'.split()[int(d)] for d in str(num)}

with open("symbols.txt", 'r') as f:
    total = {}
    for n in f.readline().split(','):
        n = n.strip()
        if n.isdigit():  
            num = int(n)
            if (num % 2 != 0 and len(n) % 2 == 0 and len(n) > 3) or (n[1] == '0' and n[-2] == '0'):
                for d in set(n):
                    total[words(num)[d]] = total.get(words(num)[d], 0) + n.count(d)
                print(n)
        else:
            print(f'oshibka {n}')

    for digit, count in total.items():
        print(f'{digit}: {count}')




     