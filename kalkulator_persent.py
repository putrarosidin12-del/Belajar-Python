print("="*40)
print("Kalkulator PERSENTASE")
print("="*40)
nilai_awal=float(input("masukkan nilai awal anda : "))
nilai_akhir=float(input("masukkan nilai akhir anda : "))
#Menghitung perubahan
perubahan= nilai_akhir - nilai_awal
persentase=(perubahan/nilai_awal)*100
if persentase >0:
    print("Nilai anda berubah naik")
    status="NAIK"
elif persentase <0:
    status="TURUN"
    print("Nilai anda berubah turun")
else:
    status="TETAP"
    print("nilai anda tetap")

#Hasil
print("="*40)
print(f"Perubahan anda sebanyak {perubahan:.2f} ")
print(f"dengan nilai persentase {persentase:.2f}%")
print(f"status perubahan nilai anda adalah {status}")
print("="*40)
