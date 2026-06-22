import random

kata_tema_kehidupan = [
    ["Hidup bukan tentang menunggu badai berlalu, tapi tentang belajar menari di tengah hujan."],
    ["Luka adalah cara hidup mengajarimu, bekasnya adalah bukti bahwa kau selamat."],
    ["Jangan terlalu keras pada masa lalu, ia datang hanya untuk membentuk, bukan menghancurkan."],
    ["Kehidupan yang berarti tidak selalu terlihat indah, tapi selalu terasa jujur."],
    ["Setiap pagi adalah halaman kosong, terserah kau ingin menulis apa hari ini."]
]  

kata_tema_motivasiDanSukses = [
    ["Kesuksesan bukan milik yang cepat, tapi milik yang terus melangkah meski lelah."],
    ["Jatuh itu wajar, tapi memilih untuk tetap berbaring adalah kekalahan sejati."],
    ["Raih mimpi setinggi langit, karena meski tak sampai, kau akan hidup di antara bintang-bintang."],
    ["Orang sukses bukan yang tak pernah gagal, tapi yang bangkit satu kali lebih banyak dari jatuhnya."],
    ["Keraguan adalah ujian pertama, keberanian adalah jawabannya."]
]    

kata_tema_cinta = [
    ["Cinta sejati bukan mencari kesempurnaan, tapi melihat kekurangan dan tetap memilih tinggal."],
    ["Hubungan yang kuat dibangun oleh dua orang yang saling mendengar, bukan saling menang sendiri."],
    ["Cinta bukan tentang siapa yang lebih dulu datang, tapi siapa yang bertahan ketika badai datang."]
]    
 
kata_tema_ketengangan = [
    ["Ketenangan adalah keberanian untuk diam"],
    ["Berhenti membandingkan hidupmu dengan orang lain, damai adalah ketika cukup dengan milikmu sendiri."],
    ["Lepaskan apa yang tak bisa kau kendalikan, dan kau akan menemukan ruang untuk bernapas."],
    ["Hati yang tenang bukan tanpa masalah, tapi mampu duduk berdampingan dengan gelisah tanpa terhanyut."]
] 

print ("- Kata kata hari ini")
print ("[1]Kehidupan")
print ("[2]Motivasi & kesuksesan")
print ("[3]Cinta & hubungan")
print ("[4]Ketenangan batin")

user_input = int(input("Pilih: "))
if user_input == 1:
    result = random.choices(kata_tema_kehidupan)
    temp = [x for y in result for x in y]
    str_temp = "".join(temp)
    print ("\"",str_temp,"\"")
elif user_input == 2:
    result = random.choices(kata_tema_motivasiDanSukses)
    temp = [x for y in result for x in y]
    str_temp = "".join(temp)
    print ("\"",str_temp,"\"")
elif user_input == 3:
    result = random.choices(kata_tema_cinta)
    temp = [x for y in result for x in y]
    str_temp = "".join(temp)
    print ("\"",str_temp,"\"")
elif user_input == 4:
    result = random.choices(kata_tema_ketengangan)   
    temp = [x for y in result for x in y]
    str_temp = "".join(temp)
    print ("\"",str_temp,"\"")
else:
    print ("Masukan pilihan yang ada")         