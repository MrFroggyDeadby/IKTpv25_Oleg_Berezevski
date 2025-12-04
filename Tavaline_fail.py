from funktsioonid import *
#is_year_kontroll funktsiooni kasutmaine
# for i in range(3):
#     aasta = int_kontrol(input("Sisesta aasta: "))
#     if is_year_leap(aasta):
#         print(f"{aasta} on liigaasta")
#     else:
#         print(f"{aasta} on tavaline aasta")




#Arithmetic finktsiooni kasutamine
# print("Lahendame/testime 5 arvutehet!")
# for i in range(5):
#     arv1 = float_kontrol(input("Sisesta esimene arv: "))
#     arv2 = float_kontrol(input("Sisesta teine arv: "))

#     t = input("Sisesta tehe (+, -, *, /): ")
#     tulemus = arithmetic(arv1, arv2, t)
#     print(f"{arv1} {t} {arv2} = {tulemus}")

#square funktsiooni kasutamine

for i in range(5):
    arv1 = float_kontrol(input("Sisesta külje pikkus: "))
    ümbermõõt, pindala, diagonaal = square(arv1)
    print(f"Külje pikkus on {arv1}.\nümbermõõt on {ümbermõõt}.\npindala on {pindala}.\ndiagonaal on {diagonaal}")