""" Program untuk mencari faktor prima
dari suatu bilangan"""

faktor_prima = []
bil_prima = []

def check_prima(n):
    if n <= 1:
        return n
    else:
        for i in range(2,int(n**0.5)):
            if n % i == 0:
                return False
        return True

def deret_prima(n):
    for i in range(n+1):
        if check_prima(i) == True:
            bil_prima.append(i)
    return bil_prima        

# Bilangan yang dicari
def faktorisasi_prima(n):
    n = int(input("Masukan bilangan: "))
    temp = n
    a = 0

    while a < len(result):
        if n % bil_prima[a] == 0:
            temp = n // bil_prima[a] 
            n = temp
        
            faktor_prima.append(bil_prima[a])
        
        elif n % bil_prima[a] != 0:
            a += 1
    return faktor_prima
            
print (faktorisasi_prima(12))           
            
            
