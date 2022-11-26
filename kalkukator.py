# soal 1 2
print("~~~~~~~~~~/('v')\~~~~~~~~~~")
print("PROGRAM PENGHITUNG VOLUM BANGUN RUANG")
print("~~~~~~~~~~/('v')\~~~~~~~~~~")
print("Pilihlah Salah Satu bangun ruang yang ingin dihitung volumenya :")
print("1. Limas")
print("2. Bola")
print("3. Kerucut")
print("4. Balok")
print("5. Kubus")
menu=input("Masukan Pilihan Anda :")
if menu=="1":
    luas=int(input("Panjang Sisi Alas :"))
    Tinggi=int(input("Masukan Tinggi :"))
    x=luas*Tinggi/3
    print("Volume limas tersebut adalah",x)
elif menu=="2":
    jari=int(input("Jari-Jari Bola :"))
    y=round(4/3*3.14*jari**3)
    print("Volume bola adalah :",y)
elif menu=="3":
    r=int(input("Jari-jari kerucut adalah : "))
    t=int(input("Tinggi Kerucut adalah : "))
    y=round(22/7*r**2*t)/3
    print("Volume Kerucut adalah : ",y)
elif menu=="4":
    p=int(input("Masukan Panjang : "))
    l=int(input("Masukan Lebar : "))
    t=int(input("Masukan Tinggi : "))
    v=p*l*t
    print("Volume Balok adalah : ",v)
elif menu=="5":
    s=int(input("Masukan panjang sisinya : "))
    vb=s**3
    print("Volumenya adalah : ",vb)
