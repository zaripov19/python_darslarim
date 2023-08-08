# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:36:12 2023

@author: Zaripov
"""

#juftson = int(input("Juft son kiriting "))
#if juftson%2:
    #print("Bu son juft emas !")
#else:
    #print("Rahmat")

#yosh = int(input("Yoshingiz nechida \n>>>  "))
#if yosh <= 4 or yosh >= 60 :
    #print("Sizga kirish bepul")
#elif yosh <= 18:
    #print("Sizga kirish 10000 so'm !")
#elif yosh >= 18:
    #print("Sizga kirish 20000 so'm")
    
#son1 = int(input("Birinchi sonni kiriting: "))
#son2 = int(input("Ikkinchi sonni kiriting: "))
#if son1 < son2: 
    #print(son1, "<", son2)
#elif son1 > son2: 
    #print(son1, ">", son2)
#else: 
    #print(son1, "=", son2)

#mahsulotlar = ["kartoshka","piyoz","sabzi","olma","uzum","anor","shaftoli","banan","o'rik","gilos"]
#savat = []
#savat.append(input("Savatga 1-mahsulotni kiriting: "))
#savat.append(input("Savatga 2-mahsulotni kiriting: "))
#savat.append(input("Savatga 3-mahsulotni kiriting: ")) 
#savat.append(input("Savatga 4-mahsulotni kiriting: "))
#savat.append(input("Savatga 5-mahsulotni kiriting: "))
#print("                                                                    ")
#for aaa in savat:
    #if aaa in mahsulotlar:
        #print("Mahsulot do'konimizda bor")
    #else:
        #print("Mahsulot do'konimizda yo'q")
        
#mahsulotlar = ["kartoshka","piyoz","sabzi","olma","uzum","anor","shaftoli","banan","o'rik","gilos"]
#savat = []
#for n in range(5):
    #savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
    #print("                                                                    ")
#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
    #if mahsulot in mahsulotlar:
        #bor_mahsulotlar.append(mahsulot)
    #else:
        #mavjud_emas.append(mahsulot)
#if mavjud_emas:
  #print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  #for mahsulot in mavjud_emas:
    #print(mahsulot)
#else:
  #print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  #for n in range(5):
   #foydalanuvchilar.append(input(f"{n+1}-Yangi login kiriting: "))
  #print(foydalanuvchilar)  
#oydalanuvchilar = []
#foydalanuvchilar.append("zaripov19")
#foydalanuvchilar.append("zaripov3313")
#foydalanuvchilar.append("zaripov7008")
#foydalanuvchilar.append("ergashaliz7008")
#foydalanuvchilar.append("ergashaliz3313")

#login = input("Yangi login kiriting: ")
#if login not in foydalanuvchilar:
    #print("Xush kelibsiz",login)
#else:
    #print("Login band, yangi login kiriting !")
  
son = int(input("Istalgan sonni kiriting: "))
for n in range(2,11):
 if not (son%2):
        print(son, "bu son", n, "ga qoldiqsiz bo'linadi")
else:
        print("Bu son o'ziga va 1 ga bo'linadi ")
