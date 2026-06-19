import random as rd

print ("—"*10,"PASSWORD GENERATOR","—"*10)
len_passwd = int(input("Panjang kata sandi:"))
level_keamanan = int(input("[1]rendah,[2]sedang,[3]tinggi\n:"))

number = [0,1,2,3,4,5,6,7,8,9]
word = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol = ["@","#","$","_","&","-","+","(",")","/","*","'",":",";","!","?"]

# Hasil kata sandi yang di acak oleh algoritma
your_passwd = []

a = 0
while a <= len_passwd:
    if level_keamanan == 1:
        your_passwd.append(str(rd.choice(number)))
    elif level_keamanan == 2:
        your_passwd.append(str(rd.choice(number)))
        your_passwd.append(rd.choice(word))
    elif level_keamanan == 3:
        your_passwd.append(str(rd.choice(number)))
        your_passwd.append(rd.choice(word))
        your_passwd.append(rd.choice(symbol))   
    a += 1

# Konversi array menjadi string    
hasil = "".join(your_passwd)
    
print ("Kata sandi anda: ",hasil)  
simpan = str(input("Apakah anda ingin menyimpan kata sandi tersebut kedalam file?(Ya/tidak): "))  
if simpan == "Ya":
    with open("/sdcard/kata_sandi_anda.txt","w") as file:
        file.write(hasil)
    print ("Kata sandi anda telah berhasil disimpan!!")    
        
elif simpan == "tidak":
    print ("Baiklah")        
