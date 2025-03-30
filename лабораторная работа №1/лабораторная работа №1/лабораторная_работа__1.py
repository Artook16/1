def words(num):
    words_dict = {str(d): 'nol odin dva tri chetire pyat shest sem vosem devyat'.split()[int(d)] for d in str(num) if d.isdigit()}
    return words_dict

with open("symbols.txt", 'r') as f:
    stroki = f.readline()
mass = stroki.split(',')
total = {}

for n in mass:
    n = n.strip()  
    if n.isdigit():  
        num = int(n)
        if num % 2 != 0 and len(n) % 2 == 0 and len(n) > 3: 
            result = {words(num)[d]: str(str(num).count(d)) for d in set(str(num))}
            for digit, count in result.items():
                if digit in total:
                    total[digit] += int(count)
                else:
                    total[digit] = int(count)
            print(n)
        if n[1] == '0' and n[-2] == '0':        
            result = {words(num)[d]: str(str(num).count(d)) for d in set(str(num))}
            for digit, count in result.items():
                if digit in total:
                    total[digit] += int(count)
                else:
                    total[digit] = int(count)
            print(n)
    else:
        print(f'oshibka {n}')

for digit, count in total.items():
    print(f'{digit}: {count}')




     