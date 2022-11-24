# soal 1
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
bilper=int(input("Masukan Angka Pertama :"))
Bilked=int(input("Masukan Angka Kedua    :"))
menu=input("Bilangan Anda   :")
if menu=="1":
    tambah=bilper+Bilked
    print("Hasil    :",tambah)
elif menu=="2":
    kurang=bilper-Bilked
    print("Hasil    :",kurang)
elif menu=="3":
    kali=bilper*Bilked
    print("hasil    :",kali)
else :
    bagi=bilper/Bilked
    print("hasil    :",bagi)

# Soal 2
bulan=int(input("Masukan Bulan (1-12) :"))
if bulan==1 or bulan==3 or bulan==5 or bulan==7 or bulan==8 or bulan==10 or bulan==12:
    print("Jumlah Hari : 31")
elif bulan==4 or bulan==6 or bulan==9 or bulan==11:
    print("Jumlah Hari : 30")
elif bulan==2 :
    print("Jumlah Hari : 28")

# Soal 3
p=input("Masukan Daftar Pesan :")
q= p.title()
print("Daftar Pesanan :",q.split(","))
r=input("Masukan Pesanan yang ingin ditammbahkan :")
s=r.title
if r in p:
    print(s,"Sudah berada dalam daftar pesanan.")
else:
    print("Hasil penambahan pada daftar pesanan :",s())


# soal 1 2
print("~~~~~~~~~~/('v')\~~~~~~~~~~")
print("PROGRAM PENGHITUNG VOLUM BANGUN RUANG")
print("~~~~~~~~~~/('v')\~~~~~~~~~~")
print("1. Limas")
print("2. Bola")
print("3. Prisma")
print("4. Kerucut")
menu=input("Masukan Pilihan Anda :")
if menu=="1":
    luas=int(input("Panjang Sisi Alas :"))
    Tinggi=int(input("Masukan Tinggi :"))
    x=luas*Tinggi/3
    print("Volume limas tersebut adalah",x)
elif menu=="2":
    jari=int(input("Jari-Jari Bola :"))
    y=4/3*3.14*jari**3
    print("Volume bola adalah :",y)
elif menu=="3":
    print("Masukan pilihan Anda :"):
    menu=

