# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

davlatlar = ["O'zbekiston","America","Saudiya Arabiston","London","Kataloniya"]
print("Ro'yxatdagi davlatlar soni",len(davlatlar),"ta")
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
juft_sonlar = list(range(120,1200,2))
print(juft_sonlar)
yigindisi = sum(juft_sonlar)
print("120 da 1200 gacha bo'lgan juft sonlar yig'indisi (1200 soni kirmeydi):",yigindisi)
kichik = min(juft_sonlar)
katta = max(juft_sonlar)
print(katta - kichik)
print("120 dan 1200 gacha bo'lgan sonlar (1200 soni kirmedi):",len(juft_sonlar),"ta" )
print(juft_sonlar[0:20])
juft1 = juft_sonlar[0:20]
juft2 = juft_sonlar[260:280]
juft3 = juft_sonlar[520:540]
print(juft1)
print(juft2)
print(juft3)

taomlar = ["osh","sho'rva","manti","navvot","sariyog'"]
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove("sho'rva")
nonushta.remove('manti')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')
print("Taomlar", taomlar)
print("Nonushtaga yiyiledigan:", nonushta )
