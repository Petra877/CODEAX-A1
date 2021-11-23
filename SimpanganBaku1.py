import numpy
from numpy.core.fromnumeric import mean, var
print("Standar Deviasi 1")
print(" ")

#Rata Rata
nilai = [80,30,20,15,12,6,10,3]#Masukan Nilai
rata2 = numpy.mean(nilai)#Rata Rata Nilai Dihitung

print("Nilai",nilai)
print("Rata Rata:",rata2)

#Hitung Standar Deviasi
SD = numpy.std(nilai)

print("Standar Deviasi:",SD)

#Hitung Variansi
Var = numpy.var(nilai)

print("Variansi:",Var)

print(" ")

#menentukan rata rata representasi yang buruk atau baik
if SD > rata2:
    print("Rata rata Merupakan representasi yang buruk") #Jika SD lebih Tinggi dari Rata2 maka representasinya buruk

elif SD < rata2:
    print("Rata Rata dapat merepresentasikan data dengan baik ") #Jika SD lebih rendah dari rata2 maka representasinya baik

print(" ")