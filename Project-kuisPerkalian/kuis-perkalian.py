import random as rd
print ("—"*9,"Game Kuis Perkalian","—"*9)
target = int(input("Perkalian Berapa?: "))

print ("—"*11,"Level kesulitan","—"*11)
print ("[1]Mudah")
print ("[2]Sulit")


# Status pemain
result = 0
correct = 0
wrong = 0

level = int(input("Level:"))
if level == 1:
    print ("ketik x, untuk berhenti")
    print ("—"*23)
    while True:
        number = rd.randint(1,10)
        result = number * target
        user = str(input(f"{number} x {target} = "))
        
        if user.isnumeric():
            if int(user) == result:
                print ("Anda Benar!")
                correct += 1
            elif int(user) != result:
                print ("Anda Salah!")  
                wrong += 1  
            else:
                count += 1       
        elif user == "x":
            break   
        
elif level == 2:
    print ("ketik x, untuk berhenti")
    while True:
        number = rd.randint(10,99)    
        result = number * target
        user = str(input(f"{number} x {target} = "))
        
        if user.isnumeric():
            if int(user) == result:
                print ("Anda Benar!")
                correct += 1
            elif int(user) != result:
                print ("Anda Salah!")  
                wrong += 1  
            else:
                count += 1     
        elif user == "x":
            break

        
print ("Total Benar:",correct)
print ("Total Salah:",wrong)        
print ("Programmer Quote: \"we are programmers, we create the digital world\"")   
