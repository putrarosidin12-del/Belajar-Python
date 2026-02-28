#Konversi suhu 
print("="*50)
print("Program Konversi Suhu")
print("="*50)
print("\n Pilih jenis konversi suhu : ")
print("1. Celcius ke Fahrenheit")
print("2. Celcius ke Kelvin")
print("3. Fahrenheit ke Celcius")
print("4. Fahrenheit ke Kelvin")
print("5. Kelvin ke Celcius")
print("6. Kelvin ke Fahrenheit")
pilihan = int(input("\n Masukkan pilihan (1-6) : "))
suhu=float(input("masukkan suhu yang akan di konversi : "))
if pilihan == 1:
    hasil = (suhu*9/5 ) +32
    print(f"{suhu} celcius = {hasil} fahrenheit")
elif pilihan ==2:
    hasil = suhu +273.15
    print(f"{suhu} celcius = {hasil} kelvin")
elif pilihan == 3:
    hasil=(suhu-32)*5/9
    print(f"{suhu} fahrenheit = {hasil} celcius")
elif pilihan == 4:
    hasil=(suhu-32)/5/9+273.15
    print(f"{suhu} fahrenheit = {hasil} kelvin")
elif pilihan == 5:
    hasil=suhu-273.15
    print(f"{suhu} kelvin = {hasil} celcius")
elif pilihan == 6:
    hasil=(suhu-273.15)*9/5+32
    print(f"{suhu} kelvin = {hasil} fahrenheit")
else:
    print("Masukkan angka yang valid")

print("="*50)
print(f"hasil konversi dari suhu {suhu} adalah {hasil}")
print("="*50)