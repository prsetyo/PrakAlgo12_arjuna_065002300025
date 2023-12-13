# -*- coding: utf-8 -*-
"""prakalgo12

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ZlA32HfsTHRRUnqqOOBDhD5R4zhfzbT
"""

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @\n')
print('========== ELKOM 1 PRAKALGO 12 ==========\n')
print('Tanggal : rabu, 13 desember 2023\n')
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

def main():
    jumlah_angka = int(input("Masukkan jumlah angka dalam list: "))
    angka_list = []
    for i in range(jumlah_angka):
        angka = int(input(f"Masukkan angka ke-{i+1}: "))
        angka_list.append(angka)

    print(f"List angka yang dimasukkan: {angka_list}")

    angka_cari = int(input("Masukkan angka yang ingin dicari: "))

    if linear_search(angka_list, angka_cari):
        print("Angka ditemukan dalam list.")
    else:
        print("Angka tidak ditemukan dalam list.")

if __name__ == "__main__":
    main()

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @\n')
print('========== ELKOM 2 PRAKALGO 12 ==========\n')
print('Tanggal : rabu, 13 desember 2023\n')
def Binary_search(num,nilai_dicari,kiri,kanan):
    while kiri <= kanan:
        mid = (kiri + kanan)//2
        if nilai_dicari == num[mid]:
            return mid
        elif nilai_dicari > num[mid]:
            kiri = mid + 1
        else:
            kanan = mid - 1
    return -1
num =[]
minta=int(input('berapa rangenya? '))
for i in range(minta):
    i+=1
    num.append(int(input(f'masukan angka ke {i}:')))
print(num)
nilai_dicari = int(input('angka berapa?'))
hasil = Binary_search(num,nilai_dicari,0,len(num)-1)
if hasil != -1:
    print("Angka ditemukan pada index ke " + str(hasil))
else:
    print("Angka tidak ditemukan")

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @\n')
print('========== ELKOM 3 PRAKALGO 12 ==========\n')
print('Tanggal : rabu, 13 desember 2023\n')
def bubble_sorted():
    list=[]
    minta=int(input('berapa rangenya? '))
    for i in range(minta):
        i+=1
        list.append(int(input(f'masukan angka ke {i}:')))
    print('list normalnya:',list)
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(f'Hasil Bubble Sort = {list}')
bubble_sorted()

print ('@@@@@  @      @  @@     @       @')
print ('    @  @      @  @ @    @      @ @')
print ('    @  @      @  @  @   @     @   @')
print ('    @  @      @  @   @  @    @@@@@@@')
print ('   @   @      @  @    @ @   @       @')
print ('  @      @@@@    @     @@  @         @\n')
print('========== ELKOM 4 PRAKALGO 12 ==========\n')
def selection():
    list=[]
    minta=int(input('Berapa kali maunya? '))
    for i in range(minta):
        i+=1
        list.append(int(input(f'Masukan angka ke {i}: ')))
    print (f'list: {list}')
    for i in range(0,len(list)-1):
        p=0
        mini=list[-1]
        for j in range(i,len(list)):
            if list[j]<=mini:
                mini=list[j]
                p=j
        list[i],list[p]=list[p],list[i]
    print(f'list dengan selection: {list}')
selection()