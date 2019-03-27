arrList = []
numSum = 0
arrindex = []

def Submit():
    num = input('\nMasukkan angka dan pisahkan dengan koma : ')
    numList = num.split(',')
    for a in numList:
        arrList.append(int(a))
    print('\nIsi Array : ' + ','.join(numList))

def Search():
    if len(arrList) == 0:
        print('\n---ARRAY KOSONG---')
    else :
        num = int(input('Masukkan angka yang ingin dicari : '))
        numSum = 0
        arrindex = []
        while(True):
            arrTemp = arrList
            if num in arrTemp:
                ind = arrTemp.index(num)
                arrindex.append(str(ind))            
                arrTemp[ind] = 'null'
                numSum += 1
            else :
                break
        print('Angka : {}'.format(num))
        print('Jumlah : {}'.format(numSum))
        print('Pada index ke : ' + ','.join(arrindex))

while(True):
    print("""\n--- MAIN MENU ---\n
    1. Submit Angka
    2. Search
    3. Keluar\n""")
    pilihan = int(input('PILIH MENU : '))
    if pilihan == 1:
        Submit()
    elif pilihan == 2:
        Search()
    elif pilihan == 3:
        print('--- TERIMA KASIH ---')
        break