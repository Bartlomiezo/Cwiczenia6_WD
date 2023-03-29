import math
# a=input("Podaj liczbe a: ")
# b=input("Podaj liczbe b: ")
# try:
#     a=int(a)
#     b=int(b)
#     plik=open("zadanie1.txt","w")
#     plik.write(str(a**2+a*b+b**2))
#     plik.close()
# except ValueError:
#     print("Nie podałeś liczby")

# def zadanie2(tab1,tab2):
#     tab3=[]
#     if(len(tab1)==len(tab2)):
#         for i in range(len(tab1)):
#             c=tab1[i]+tab2[i]
#             tab3.append(c)
#         print(tab3)
#         return 0
#     else:
#         print("dlugosc list nie jest taka sama")
#
# tab1=[12,3,4]
# tab2=[4,6,3]
# zadanie2(tab1,tab2)

wynik=(math.e**3+math.cos(39)**2)**(1/5)+(2/7)**3+math.pi
print(round(wynik,2))
plik2=open("zadanie3.txt","w")
plik2.write("UponUUyoBYlcjzNxvxblwLscalazEiqlwwSuxSZnpuDIwunYOwSDYWRAWurHcNwruCVPPVqQUByDZWjZjTfUFlKnldDfAILJfwgHAqUKhwqjojRuljOBQZHecvPnjfQtHoicbPCJisfLNQChdxgsHKqxNkAcRhDJQLsfkphInutetUYKNrSPnKEFYpyalkuXhVwPxOgQ")
plik2.close()

plik2=open("zadanie3.txt","r")
plik2.seek(100)
zmienna=plik2.read(35)
zmienna_duze=""
for i in zmienna:
    if i.isupper():
        zmienna_duze+=i
if(zmienna_duze!=0):
    print(zmienna_duze+" "+str(len(zmienna_duze)))
else:
    print("Nie ma wielkich liter we wczytanym fragmencie")