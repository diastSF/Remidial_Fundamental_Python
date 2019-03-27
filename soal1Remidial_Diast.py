main = []
genap = []
ganjil = []


def Input():
    num = input('Masukkan angka dan pisahkan dengan koma : ')
    numList = num.split(',')
    for a in numList:
        main.append(int(a))
        if int(a) % 2 == 0:
            genap.append(int(a))
        elif int(a) % 2 > 0:
            ganjil.append(int(a))

def Utama():
    if len(main) == 0:
        print('\n---ARRAY KOSONG---')
    else :
        print('Isi Array Utama : \n\n{}\n'.format(main))

def GG():
    if len(main) == 0:
        print('\n---ARRAY KOSONG---')
    else :
        x = input('- Pilih 1 untuk lihat Array Ganjil\n- Pilih 2 untuk lihat Array Genap\n MASUKKAN PILIHAN : ')
        if x == '1':
            print('Isi Array Ganjil : \n\n{}\n'.format(ganjil))
        elif x == '2':
            print('Isi Array Genap : \n\n{}\n'.format(genap))

def Sort():
    if len(main) == 0:
        print('\n---ARRAY KOSONG---')
    else :
        arr = int(input('- Pilih 1 untuk sort Array Utama\n- Pilih 2 untuk sort Array Ganjil\n- Pilih 3 untuk sort Array Genap\n MASUKKAN PILIHAN : '))
        if arr == 1:
            for a in range(len(main)-1):
                for b in range(a+1, len(main)):
                    hasil = main[a] - main[b]
                    if hasil > 0:
                        main[a],main[b] = main[b],main[a]
        elif arr == 2:
            for a in range(len(ganjil)-1):
                for b in range(a+1, len(ganjil)):
                    hasil = ganjil[a] - ganjil[b]
                    if hasil > 0:
                        ganjil[a],ganjil[b] = ganjil[b],ganjil[a]
        elif arr == 3:
            for a in range(len(genap)-1):
                for b in range(a+1, len(genap)):
                    hasil = genap[a] - genap[b]
                    if hasil > 0:
                        genap[a],genap[b] = genap[b],genap[a]

listMenu = [Input, Utama, GG, Sort]

while(True):
    print("""\n--- MAIN MENU ---\n
    1. Input Angka
    2. Lihat Array Utama
    3. Lihat Array Ganjil atau Genap
    4. Sort Array
    5. Keluar\n""")
    pilihan = int(input('PILIH MENU : '))
    if pilihan >= 1 and pilihan <= 4:
        listMenu[pilihan-1]()
    elif pilihan == 5:
        print('--- TERIMA KASIH ---')
        break