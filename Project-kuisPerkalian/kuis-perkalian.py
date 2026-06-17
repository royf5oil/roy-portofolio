print ("—"*10,"Kuis Perkalian","—"*10)
target = int(input("Perkalian Berapa?: "))
count = int(input("Dari 1 sampai Berapa?: "))

# Status
result = 0
correct = 0
wrong = 0


for i in range(1,count+1):
    result = i * target
    user = int(input(f"{i} x {target} = "))
    
    if user == result:
        print ("Anda Benar!")
        correct += 1
    elif user != result:
        print ("Anda Salah!")  
        wrong += 1  
    
    else:
        count += 1     
        
print ("Total Benar:",correct)
print ("Total Salah:",wrong)        
    
    