import datetime
import time


print ("="*5,"STOPWATCH","="*5)
detik = int(input("Masukan detik: "))
detik += 1
menit = int(input("Masukan menit: "))
jam = int(input("Masukan jam: "))

if detik > 60 and menit > 60 and jam > 60:
    print ("Kelebihan (detik/menit/jam)")
elif detik > 60:
    print ("Kelebihan Detik!")
elif menit > 60:
    print ("Kelebihan Menit!")
elif jam > 60:
    print ("Kelebihan Jam!")        
else:    
    dat = datetime.time(jam,menit,detik)

    while True:
        if detik == 0 and menit == 0 and jam == 0:
            break
    
        if detik > 0:
            detik -= 1
    
        elif detik == 0:
            if menit > 0:
                detik = 59
                menit -= 1 
            elif menit == 0:
                if jam > 0:
                    menit = 59
                    jam -= 1
    
        dat = datetime.time(jam,menit,detik)
        time.sleep(1)
    
        print (dat)

print ("Timer Berakhir")   
    
