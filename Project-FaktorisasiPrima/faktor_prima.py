""" Program untuk mencari faktor prima
dari suatu bilangan"""

print ("—"*40)
print ("cari faktorisasi prima suatu bilangan")
print ("—"*40)
print ("Ketik: x untuk berhenti")
print ("—"*40)

def check_prima(n):
    if n <= 1:
        return n
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def deret_prima(m):
    bil_prima = []
    for j in range(2,m+1):
        if check_prima(j) == True:
            bil_prima.append(j)
    return bil_prima        


# Bilangan yang dicari
def faktorisasi_prima():
    n = str(input("Masukan bilangan: "))
    temp = n
    a = 0
   
    if n == "x":
        return 0
    
    faktor_prima = []
    
    result = deret_prima(int(n))
    
    while a < len(result):
        if int(n) % result[a] == 0:
            temp = int(n) // result[a] 
            n = temp
        
            faktor_prima.append(str(result[a]))
        
        elif int(n) % result[a] != 0:
            a += 1
    new = " x ".join(faktor_prima)
    print (new)

def note():
    print ("—"*40)
    print ("Terimakasih telah mengunakan program sederha ini!")    
    
while True:
    if faktorisasi_prima() == 0:
        note()
        break
    else:
        faktorisasi_prima()
            
            
