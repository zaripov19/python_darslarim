# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:11:46 2023

@author: Zaripov
"""

#bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
#mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
#print("Men " + mahsulot + " sotib oldim")
#print("Olinmagan mahsulotlar: ", bozorlik)
#ismlar = ["Aziz" ,"Sohib ","Otabek"]
#print("Salom" + " " + ismlar[0],"," "bugun choyxona bormi ?")
#print(ismlar[1] + "," + "choyxonaga boramizmi ?"  )
#sonlar = [2,-1,10,6.5]
#del sonlar[1]
#print(sonlar)
#sonlar.insert(3, 4)
#print(sonlar)
#kun = []
#kun.append('dushanba')
#kun.append("seshanba".capitalize())
#print(kun)
#print(sonlar[0] + sonlar[2])
#print(sonlar[1] - sonlar[3])
#print(sonlar[2] * sonlar[0])
#print(sonlar[3] / sonlar[0])
#print(sonlar[0] % sonlar[3])
#t_shaxslar = ["Muhammad S.A.V","Amir Temur","Alisher Navoiy","Islom Karimov"]
#z_shaxslar = ["Abdulloh domla","Leonel Messi","Shavkat Mirziyoyev","Dadam"]
#tarix = t_shaxslar.pop(0)
#print(tarix)
#zamon = z_shaxslar.pop(0)
#print(zamon)
#print("Men tarixiy shaxslardan" + " " + tarix +" " + "bilan" + ",", "\n\
#zamonaviy shaxslardan esa" + " " + zamon + "lar bilan suxbat qurishni istardim.")

friends = []
friends.append("Azizbek")
friends.append("Sohibjon")
friends.append("Husanboy")
friends.append("Ahliddin")
friends.append("Samandar")
friends.append("Oyatillo")
friends.append("Umidjon")
friends.append("Jaxongir")
#print(friends)
friends.remove("Azizbek")
friends.remove("Husanboy")
#print(friends)  #kela oladiganlar
friends.append("Ubaydullo")
friends.insert(0,"Otabek")
friends.insert(5, "Qurbonali")
#print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)
