print("=====Silahkan Pilih menu dibawah ini=====")
print("1.Keuntungan")
print("2.Total biaya produksi")
print("3.Keuntungan perbiji")
print("4.Biaya Perbiji")
print("5.Penerimaan Kotor")
print("=========================================")

print(" ")

print("Masukan Angka Saja")
pilih = (int(input("Masukan Pilihan: ")))

print(" ")

#menhitung keuntungan
def keuntungan():
    print("Menghitung Keuntungan")
    a = int(input("Penerimaan kotor: "))
    b = int(input("Biaya Produksi: "))

    c = a - b
    print("Keuntungan =",c)
    print(" ")

#mentotal biaya produksi
def totalbiayaproduksi():
    print("mencari total biaya produksi")
    jumdata = []

    n = int(input("Jumlah data: "))

    for i in range(0, n):
        ele = int(input("Masukan biaya:"))

        jumdata.append(ele)

    x = sum(jumdata)
    print("Total biaya produksi",x)
    print(" ")

#mencari keuntungan perbiji
def keuntunganperbiji():
    print("Mencari Keuntungan Perbiji")
    e = int(input("Biaya Produksi Perbiji: "))
    f = int(input("harga barang perbiji"))

    g = f-e
    print("Keuntungan perbiji",g)
    print(" ")


#menccari biaya perbiji
def biayaperbiji():
    print("Mencari Biaya Perbiji")
    h = int(input("Masukan Jumlah Barang: "))
    i = int(input("Masukan Total Biaya produksi: "))

    j = i/h
    print("Biaya Produksi perbiji:",j)
    print(" ")

#menghitung penerimaan kotor
def peneriamaankotor():
    print("Mencari penerimaan kotor")
    x = int(input("jumlah barang: "))
    y = int(input("Harga barang: "))

    z = x*y
    print("Penerimaan kotor:",z)
    print(" ")


if pilih == 1:
    keuntungan()

elif pilih == 2:
    totalbiayaproduksi()

elif pilih == 3:
    keuntunganperbiji()

elif pilih == 4:
    biayaperbiji()

elif pilih == 5:
    peneriamaankotor()

else:
    print(pilih,"Tidak ada dalam pilihan")

while True:
    print("=====Silahkan Pilih menu dibawah ini=====")
    print("1.Keuntungan")
    print("2.Total biaya produksi")
    print("3.Keuntungan perbiji")
    print("4.Biaya Perbiji")
    print("5.Penerimaan Kotor")
    print("Masukan Angka 98 Untuk Keluar")
    print("=========================================")
    print(" ")
    print("Masukan Angka Saja")
    pilih = (int(input("Masukan Pilihan: ")))


    if pilih == 1:
        keuntungan()

    elif pilih == 2:
            totalbiayaproduksi()

    elif pilih == 3:
        keuntunganperbiji()

    elif pilih == 4:
        biayaperbiji()

    elif pilih == 5:
        peneriamaankotor()

    elif pilih == 98:
        print(" ")
        print("Anda telah selesai")
        print("...Keluar")
        print("Terimakasih")
        print(" ")
        print("Script by petra877")
        break

    else:
        print(pilih,"Tidak ada dalam pilihan")