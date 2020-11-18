import sys,time
def tex(teks):
    for i in teks + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
    
tex("||||||||||||||||||")        
 
print("----------Silahkan Login----------")    
user = input("Username:")
passw = input("Password:")   


if user == 'user' and passw == '123':
    print("Anda Telah Login, Silahkan Masuk")
    
else:
    print("Username Atau Password Salah")
    
import sys,time
def tex(teks):
    for i in teks + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
        
tex("||||||||||||||||||")
   
def menu():
    print("---------Menu Utama--------")
    print("1.OperasiHitungSederhana")
    print("2.BangunDatar")
    print("3.BangunRuang")
    print("---------------------------")

def OperasiHitungSederhana():
    import sys,time
    def tex(teks):
        for i in teks + "\n":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
            
    tex("/////////////////")        
    
    def menu():
        print("1.Perkalian")
        print("2.Pembagian")
        print("3.Penjumlahan")
        print("4.Pengurangan")
        print("5.AkarKuadrat")
        print("6.Pangkat2")
        
        
    def Perkalian():
        print("Anda Telah Memilih Operasi Hitung Perkalian")
        x = (int(input("Masukan Bilangan Pertama:")))
        y = (int(input("Masukan Bilangan kedua:")))
        z = x*y
        print("Hasilnya Adalah:",z)
            
    def Pembagian():
        print("Anda Telah Memilih Pembagian")
        print(" Bilangan Pertama : Bilangan Kedua")
        a = (int(input("Masukan bilangan Pertama:")))
        b = (int(input("Masukan Bilangan Kedua:")))
        c = a/b
        print("Hasilnya Adalah:",c)
        
    def Penjumlahan():
        print("Anda Telah Memilih Penjumlahan")
        x = (int(input("Masukan Bilangan Pertama:")))
        y = (int(input("Masukan Bilangan Kedua:")))
        z = x+y
        print("Hasilnya Adalah:",z)    
        
    def Pengurangan():
        print("Anda Telah Memilih Operasi Hitung Pengurangan")
        x = (int(input("Masukan Bilangan Yang dikurangkan:")))
        y = (int(input("Masukan Bilangan Pengurang:")))
        z = x-y
        print("Hasilanya Adalah:",z)
    
    def Akarkuadrat():
        import math
        print("Anda Telah Memilih Akar Kuadrat")
        x = (int(input("Masukan Bilangan:")))
        y =  math.sqrt(x)
        print("Hasilnya Adalah:",y)
     
    def Pangkat2():
        print("Anda Telah Memilih Pangkat 2")
        x = (int(input("Masukan Bilangan Yang Akan Dihitung:")))
        y = x*x
        print("Hasilnya Adalah:",y)
       
               
    print("======Operasi Hitung Sederhana======")
    print("1.Perkalian")
    print("2.Pembagian")
    print("3.Penjumlahan")
    print("4.Pengurangan")
    print("5.Akar Kuadrat")
    print("6.Pangkat 2")
    print("====================================")
    print("Masukan Nomornya Saja")
    pil = (int(input("Masukan Pilihan:")))
    
    
    if pil == 1:
        Perkalian()
        
    elif pil == 2:
        Pembagian()
            
    elif pil == 3:
        Penjumlahan()
        
    elif pil == 4:
        Pengurangan()
    
    elif pil == 5:
        Akarkuadrat()
    
    elif pil == 6:
        Pangkat2()
        
    else:
        print(pil,"Tidak Ada dalam Pilihan")
 
 
def Bangundatar():
    def menu():
        print("1.Pythagoras")
        print("2.Persegi")
        print("3.Persegipanjang")
        print("4.Segitiga")
        print("5.Lingkaran")   
        print("6.segienam")
        print("7.jajargenjang")
        print("8.trapesium")
            
    def Pythagoras():
        import math
        print("Anda Telah Memilih Pythagoras")
        a = (int(input("Masukan Sisi Pertama:")))
        b = (int(input("Masukan Sisi Kedua:",)))
        c = a*a+b*b
        d = math.sqrt(c)
        print("Hasilnya Adalah:",d)
        
        
    def Persegi():
        def menu():
            print("1.Luas")
            print("2.Keliling")
            
        def Luas():
            print("Anda Telah Memilih Luas Persegi")
            x = (int(input("Masukan Panjang Sisi:")))
            z = x*x
            print("Hasilnya Adalah:",z,"CM")
            
        def Keliling():
            print("Anda Telah Memilih Luas Persegi")
            x = (int(input("Masukan Panjang Sisi:",)))
            y = x*4
            print("Hasilnya Adalah:",y,"CM")
     
        print("====Pilihan====")
        print("1.Luas")
        print("2.Keliling")
        print("===============")
        print("Masukan Nomornya Saja")
        pil = (int(input("Masukan Pilihan")))
    
    
        if pil == 1:
            Luas()
        elif pil == 2:
            Keliling()
        else:
            print(pil,"Tidak Ada Dalam Pilihan")          
          
    def Persegipanjang():
        def menu():
            print("1.Luas")
            print("2.Keliling")
            
        def Luas():
            print("Anda Telah Memilih Luas Persegi")
            x = (int(input("Masukan Sisi Pendek:")))
            y = (int(input("Masukan Sisi Panjang:")))
            z = x*y
            print("Hasilnya Adalah",z,"CM")
        
        def keliling():
            print("Anda Telah Memilih Keliling Persegi Panjang")
            x = (int(input("Masukan Sisi Pendek:")))
            y = (int(input("Masukan Sisi Panjang")))
            z = x*2
            v = y*2
            a = z+v
            print("Hasilnya Adalah:",a,"CM")
            
            
        print("====Pilihan====")
        print("1.Luas")
        print("2.Keliling")
        print("===============")
        print("Masukan Nomornya Saja")
        pi = (int(input("Masukan Pilihan")))      
        
        if pi == 1:
            Luas()
            
        elif pi == 2:
            keliling()
            
        else:
            print(pi,"Tidak Ada Dalam Piihan")
            
    def Segitiga():
        def menu():
            print("1.Luas")
            print("2.Keliling")
            
        def Luas():
            print("Anda Telah Memilih Luas Segitiga")
            x = (int(input("Alas:")))
            y = (int(input("Tinggi:")))
            z = x*y
            c = z/2
            print("Hasilnya Adalah:",c,"CM")
            
            
        def Keliling():
            print("Anda Telah Memilih Keliling Segitiga")
            x = (int(input("Masukan Sisi A:")))
            y = (int(input("Masukan Sisi B:")))
            v = (int(input("Masukan Sisi C")))
            z = x+y+v
            print("Hasilnya Adalah:",z,"CM")
        
        
        print("====Pilihan====")
        print("1.Luas")
        print("2.Keliling")
        print("===============")
        print("Masukan Nomornya Saja")
        pi = (int(input("Masukan Pilihan")))
        
        
        if pi == 1:
            Luas()
            
        elif pi == 2:
            Keliling()
                
        else:
            print(pi,"Tidak Ada Dalam Pilihan")
     
     
    def Lingkaran():
        def menu():
            print("1.Luas")
            print("2.Keliling")

        def Luas():
            def menu():
                print("1.Diameter")
                print("2.Radius")    
                
            def Diameter():
                import math
                print("Anda Telah Memilih Luas Lingkaran Dengan Memasukan Diameter")
                x = (int(input("Masukan Diameter Lingkaran:")))
                v = x/2
                y = v*v
                z = 3.14*y
                print("Hasilnya Adalah:",z,"CM")
                
            def Radius():
                import math
                print("Anda Telah Memilih Luas Lingkaran Dengan Memasukan Radius")
                v = (int(input("Masukan Radius Lingkaran:")))
                y = v*v
                z = 3.14*y
                print("Hasilnya Adalah:",z,"CM")
                
                
            print("==Pilih Opsi==")
            print("1.Diameter")
            print("2.Radius")
            print("==============") 
            pil = int(input("Masukan Opsi:"))
            
            if pil == 1:
                Diameter()
                
            elif pil == 2:
                Radius()    
                  
            else:
                print(pil,"Tidak Ada Dalam Pilihan")
                
        def Keliling():
            def menu():
                print("1.diameter")
                print("2.radius")
                
            def diameter():
                print("Anda Telah Memilih Keliling Lingkaran Denngan Opsi Diameter")
                x = (int(input("Masukan Diameter")))
                y =  3.14 * x 
                print("Hasilnya Adalah:",y,"CM")
                
            def radius():
                print("Anda Telah Memilih Keliling Lingkaran Dengan Opsi Radius")
                x = (int(input("Masukan Radius")))
                y = 2*x*3.14
                print("Hasilnya Adalah",y,"CM")
                
            print("==Pilih Opsi==")
            print("1.Diameter")
            print("2.Radius")
            print("==============")
            pil = (int(input("Masukan Opsi:")))
            
            if pil == 1:
                diameter()        
            
            elif pil == 2:
                radius()
            
            else:
                (pil,"Tidak Ada Dalam Pilihan")
                
        print("===Pilihan===")
        print("1.Luas")
        print("2.Keliling")
        print("=============")
        pil = (int(input("Masukan Pilihan:")))
        
        if pil == 1:
            Luas()
                     
        elif pil == 2:
            Keliling()
            
        else:
            print(pil,"Tidak Ada Dalam Pilihan")
    
    
    def segienam():
        def menu():
            print("1.Luas")
            print("2.Keliling")
            
        def luas():
            print("Anda Telah Memilih Luas Segi Enam")
            x = (int(input("Masukan Panjang Sisi:")))
            z = 2.598*x*x
            print("Hasilnya Adalah:",z,"CM")
            
        def keliling():
            print("Anda Telah Memilih Keliling Segi enam")
            x = (int(input("Masukan Panjang Sisi:")))
            y = x*6
            print("Hasilnya Adalah:",y,"CM")
            
        print("===Pilihan===")
        print("1.Luas")
        print("2.Keliling")
        print("=============")
        pil = (int(input("Masukan Pilihan")))
        
        if pil == 1:
            luas()
        
        elif pil == 2:
            keliling()    
             
        else:
            print(pil,"Tidak Ada Dalam Pilihan")
            
            
    def jajargenjang():
        def menu():
            print("1.Luas")
            print("2.Keliling")
        
        def luas():
            print("Anda Telah Memilih Luas Jajar Genjang")
            x = (int(input("Masukan Alas:")))
            y = (int(input("Masukan Tinggi")))
            z = x*y
            print("Hasilnya Adalah",z,"CM")

        
        def keliling():
            print("Anda Telah Memilih Keliling Jajar Genjang")
            x = (int(input("Masukan Panjang:")))
            y = (int(input("Masukan Panjang:")))    
            z = x+y
            v = 2*z
               
        print("===Pilihan===")
        print("1.Luas")
        print("2.Keliling")
        print("=============")
        pil = (int(input("Masukan Pilihan")))
        
        if pil == 1:
            luas()
            
        elif pil == 2:
            keliling()
            
        else:
            print(pil,"Tidak Ada Dalam Pilihan")
    
    
    def trapesium():
        def menu():
            print("luas")
            print("keliling")
            
        def luas():
            print("Anda Telah Memilih Luas Trapesium")
            x = (int(input("Masukan Tinggi:")))
            y = (int(input("Masukan Sisi Sejajar Pertama:")))
            z = (int(input("Masukan Sisi Sejajar Kedua:")))
            v = y+z
            s = x*v
            c = s/2 
            print("Hasilnya Adalah:",c,"CM")
            
        def keliling():
            print("Anda Telah Memilih Keliling Trapesium")
            x = (int(input("Masukan Sisi Pertama:")))
            y = (int(input("Masukan Sisi Kedua:")))
            z = (int(input("Masukan Sisi Kedua")))
            a = (int(input("Masukan Sisi Ketiga:")))
            c = x+y+z+a
            print("Hasilnya Adalah:",c,"CM")
            
            
        print("===Pilihan===")
        print("1.Luas")
        print("2.Keliling")
        print("=============")
        pil = (int(input("Masukan Pilihan")))
        
        if pil == 1:
            luas()
                   
        elif pil == 2:
            keliling()
                
        else:
            print(pil,"Tidak Ada Dalam Pilihan")
    
    print("=======Bangun datar========")
    print("1.Pythagoras")
    print("2.Persegi")
    print("3.Persegi Panjang")
    print("4.Segitiga")
    print("5.Lingkaran")
    print("6.Segi Enam")
    print("7.Jajar genjang")
    print("8.Trapesium")
    print("===========================")
    print("Masukan Nomornya Saja")
    pil = (int(input("Masukan Pilihan:")))
    
    if pil == 1:
        Pythagoras()
        
    elif pil == 2:
        Persegi()
    
    elif pil == 3:
        Persegipanjang()     
    
    elif pil == 4:
        Segitiga()   
    
    elif pil == 5:
        Lingkaran()
    
    elif pil == 6:
        segienam()
    
    elif pil == 7:
        jajargenjang()
        
    elif pil == 8:
        trapesium()    
    
    else:
        print(pil,"Tidak Ada Dalam Pilihan")    
                  
 
def Bangunruang():
    def menu():
        print("1.Kubus")
 
    
    print("======Bangun Ruang======")
    print("1.Kubus")
    print("========================")
    
    
print("---------Menu Utama--------")
print("1.Operasi Hitung Sederhana")
print("2.Bangun Datar")
print("3.Bangun Ruang")
print("---------------------------")
print("Masukan Nomornya Saja")
pilih = (int(input("Masukan Pilihan:")))


if pilih == 1:
    OperasiHitungSederhana()
    
elif pilih == 2:
    Bangundatar()
    
elif pilih == 3:
    BangunRuang()    

else:
    print(pilih,"Tidak Ada Dalam Menu")