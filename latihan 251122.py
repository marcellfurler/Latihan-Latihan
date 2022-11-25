# soal 1 latihan
a=int(input("Harga Makanan sebesar :Rp."))
b=int(input("Harga Snak sebesar :Rp"))
c=int(input("Harga Minuman sebesar :Rp"))
d=a+b+c
e=int(input("Uang anda sebesar : Rp."))
f=e-d
print(f"anda membayar sebesar Rp.{d}")
if e<d:
    print("Uang anda Kurang")
    print(f"ANda harus menambah sebesar Rp.{d-e}")
elif e==d:
    print("Uang anda pas, dan tidak ada kembalian. Terima Kasih")
elif e>d:
    print(f"kembalian anda sebesar Rp.{f}")   

# soal 2 latihan
print("f(x)=ax**2+bx+c")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=D=b**2-4*a*c
e=x=-b+-sqrt(D)/2*a
print(d)
if D<0:
    print("fungsi tersebut tidak memiliki akar")
elif D>0:
    print(e)