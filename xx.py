# soal 1
x=str(input("Masukan Nama Anda  :"))
if(x=="Bond"):
    print("Selamat DAtang AGne 007")
else:
    print("Good Morning",x)

# soal 2
angka=int(input("Masukan angka  :"))
if(angka%2==0):
    print("genap")
else:
    print("Ganjil")


# soal 3
a=input("Masukan Angka Pecahan  :")
if("." or ",") not in a:
    print("Bilangan Bulat")
else:
    print(a.split(".",1)[1])