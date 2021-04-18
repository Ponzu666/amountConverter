#untuk error handling
while True:
    try:
        n = int(input('Masukkan Bilangan Bulat : '))            #variabel n sebagai total total item 
    except ValueError:
        print('Invalid Input!')
        continue

    if n <= 0:
        print('Invalid Input!')
        continue
    elif n >= 359999:
        print('Invalid Input!')
    elif n == float:
        print('Invalid Input!')
    else:
        break

#untuk konversi 'n' yang di input
# 1 lusin = 12 buah
# 1 kodi = 20 buah
# 1 gross = 144 buah
# 1 rim = 500 lembar
def amountConverter(item):                          #rumus perhitungan RIM,KODI, dan LUSIN
    item = item
    rim = item // 500
    item %= 500
    kodi = item // 20
    item %= 20
    lusin = item // 12
    item %= 12
      
    return '%d:%02d:%02d' % (rim, kodi, lusin)

print(amountConverter(n))                           #memanggil fungsi amountConverter terhadap n