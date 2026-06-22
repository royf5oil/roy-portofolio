import random as rd

print ("—"*10,"PASSWORD GENERATOR","—"*10)
len_passwd = int(input("Panjang kata sandi: "))
print ("Level keamanan")
level_keamanan = int(input("[1]rendah\n[2]sedang\n[3]tinggi\n:"))

number = [0,1,2,3,4,5,6,7,8,9]
word = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol = ["@","#","$","_","&","-","+","(",")","/","*","'","!","?"]

def rnd_algorithm(a,b):
    num_result = []
    for i in range(1,b+1):
        num_result.append(str(a[i]))
    str_result = "".join(num_result)
    return str_result        
    

if level_keamanan == 1:
    rd.shuffle(number)
    print ("Kata sandi anda: ",rnd_algorithm(number,len_passwd))

elif level_keamanan == 2:
    # Meningkatkan kombinasi huruf
    number.extend(word)
    
    rd.shuffle(number)
    print ("Kata sandi anda: ",rnd_algorithm(number, len_passwd))

elif level_keamanan == 3:
    # Meningkatkan kombinasi huruf
    number.extend(word)
    number.extend(symbol)
    
    rd.shuffle(number)
    print ("Kata sandi anda: ",rnd_algorithm(number, len_passwd))


    
