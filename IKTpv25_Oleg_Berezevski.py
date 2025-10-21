
#ülesanne 1

# print('Tere, maailm!')
# nimi = input('Mis on sinu nimi? ').capitalize()
#
# print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
# print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
# vanus = input()
# print(f'Oi kui tore, sa oled {vanus} aastat vana')
#
#
#
#ülesanne 2
#
# vanus = 18  #int
# nimi = 'Jaak'  #str
# pikkus = 16.5  #float
# kas_käib_koolis = False  #bool
#
# if kas_käib_koolis == True:
#    print('Näeme koolis')
# else:
#    print('Näeme tööl')
#
# print(type(vanus))
# print(type(nimi))
# print(type(pikkus))
# print(type(kas_käib_koolis))
#
#ülesanne 3
#
# from random import randint
# while True:
#    kommid = randint(5, 10)
#    print(f'Laual on {kommid} kommi')
#    poiss = int(input('Mitu kommi sa soovid võtta? '))
#    if poiss > kommid:
#        print('Laual pole nii palju komme')
#    else:
#        print(f'Laual on {kommid - poiss} kommi')
#
#ülesanne 4
#
# from math import pi
#
# ümbermõõdu = float(input('Sisestage ümbermõõdu: '))
# diameeter = ümbermõõdu / pi
# print(f'diameetri pikkus on {diameeter:.2f}')
#
#ülesanne 5
#
# a = float(input('Sisestage N: '))
# b = float(input('Sisestage M: '))
#
# c = float(a**2+b**2)
# print(f'käsureal on {c:.2f}')
#
#ülesanne 6
#
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg
#
# print("Sinu kiirus oli " + str(kiirus) + " km/h")

#ülesanne 7

# numbrid = []
# for u in range(5):
#     a = int(input('Sissestage numbrid: '))
#     numbrid.append(a)
#
# kesk = 0
# for i in range(len(numbrid)):
#     kesk = kesk + numbrid[i]
#     result = kesk/len(numbrid)
# print(result)

#ülesanne 8

# print('  @..@\n'
#       ' (----)\n'
#       '( \__/ )\n'
#       '^^ "" ^^ '
#
#
#       )

#ülesanne 9

# a = float(input('Sisestage a: '))
# b = float(input('Sisestage b: '))
# c = float(input('Sisestage c: '))
#
# ümbermõõdu = a + b + c
# print(f'valem: P = a + b + c\n'
#       f'{ümbermõõdu}')

# ülesanne 10
#
# pitsa_hind = 12.90 * 0.1
# sõbrad = int(input('Mitu sõbrad läksid Pitsa eest? '))
# pitsa_hind = pitsa_hind/sõbrad
# print(f'Iga sõber peab maksta {pitsa_hind:.2f}')

#while True:
#    paev_number=int(input('Sisesta päeva number(1-7): '))
#    if paev_number==1:
#        print('Esmaspäev')
#    elif paev_number==2:
#        print('Teisipäev')
#    elif paev_number==3:
#        print('Kolmapäev')
#    elif paev_number==4:
#        print('Neljapäev')
#    elif paev_number==5:
#        print('Reede')
#    elif paev_number==6:
#        print('Laupäev')
#    elif paev_number==7:
#        print('Pühapäev')
#    else:
#        print('Vale number!')




#nimi = input('Mis on sinu nimi? ')


#if nimi == 'JUKU':
#    print('Lähme kinno')
#    vanus = int(input('Kui vana sa oled?'))
#    if vanus.isdigit:    
#        if vanus < 6:
#            print('Pilet on tasuta')
#        elif vanus <= 14:
#            print('lastepilet')
#        elif vanus <= 65:
#            print('täispilet')
#        else:
#            print('sooduspilet')
#    else:
#        print('Sisestage number!')
#else:
#    print('Kes sa oled???')

#nimi_1 = input('Sisesta oma nimi: ').capitalize
#nimi_2 = input('Sisesta oma nimi: ').capitalize

#if nimi_1.isalpha and nimi_2.isalpha:
#    if nimi_1 == 'Vitali' and nimi_2 == 'Artjom' or nimi_1 == 'Artjom' and nimi_2 == 'Vitali':
#        print('On täna pinginaabrid')
#    else:
#        print('Pole täna pinginaabrid')
#else:
#    print('Sisestage tähed!!!')




#pikkus = int(input('Sisestage pikkus: '))
#laius = int(input('Sisestage laius: '))
#if pikkus > 0 and laius > 0:
 #   pindala = pikkus * laius
  #  print(f'pindala suurus on {pindala}')
  #  user = input('Kas soovite remondi teha? ').capitalize()
  #  if user.isalpha() and user == 'Jah':
    #    hind = float(input('Ruutmeetri hind? '))
  #      if hind > 0:
   #         remondi_hind = hind * pindala
    #        print(f'Remondi summa on {remondi_hind}€')
    #        kes = input('Kes teeb remondi(ise/töötaja)? ').capitalize()
    #        if kes.isalpha() and kes == 'Ise':
   #            print(f'Siis summa on {remondi_hind}€')
  #  #        else:
   #             print(f'Siis summa on {remondi_hind + 300}€')
  #      else:
    #        print('Hind ei saa olla negatiivne')
 #   else:
   #     print('Head aega!')

#alghind = (input('Sisestage hind: '))

#if alghind.isdigit():
 #   alghind = float(alghind)
#    if alghind >= 700:
    #    hind = alghind * 0.7
   #     print(f'Hind on {hind}')
  #  else:
 #       print(f'Hind on {alghind}')

# Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)


# try:
#     temperatuur = float(input())
#     if temp.isdigit():
#         if temperatuur > 18:
#             print('Soovitatav toasoojus talvel')
#         else:
#             print('Võib olla jahe')
# except:
#         print('Sisesta number!')


# Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)
# Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

# try:
#     pikkus = float(input('Sisesta pikkus cm: '))
#     sugu = input('Sisesta sugu (mees/naine): ').lower()
#     if sugu == 'mees':
#         if pikkus <= 170 and pikkus > 0:
#             print('Oled lühike')
#         elif pikkus <= 190 and pikkus > 0:
#             print('Oled keskmine') 
#         elif pikkus > 190 and pikkus > 0:
#             print('Oled pikk')
#     elif sugu == 'naine':
#         if pikkus <= 160 and pikkus > 0:
#             print('Oled lühike')
#         elif pikkus <= 180 and pikkus > 0:
#             print('Oled keskmine') 
#         elif pikkus > 180 and pikkus > 0:
#             print('Oled pikk')
#     else:
#         print('Sisesta mees või naine!')
# except:
#     print('andmed on valed')



#Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad.
#Teata, mis summa maksma läheb(Kuva ekraanil tšekk).

from random import randint

piim = randint(1, 2)
sai = randint(2, 3)
leib = randint(1, 4)



try:
    piim_inimene = input('Kas soovite osta piima? (jah/ei): ').lower()
    if piim_inimene == 'jah':
        piim_kogus = int(input('Mitu piima soovite osta? '))
        piim_summa = piim * piim_kogus
    else:
        piim_kogus = 0
        piim_summa = 0
    sai_inimene = input('Kas soovite osta saia? (jah/ei): ').lower()
    if sai_inimene == 'jah':
        sai_kogus = int(input('Mitu saia soovite osta? '))
        sai_summa = sai * sai_kogus
    else:
        sai_kogus = 0
        sai_summa = 0
    leib_inimene = input('Kas soovite osta leiba? (jah/ei): ').lower()
    if leib_inimene == 'jah':
        leib_kogus = int(input('Mitu leiba soovite osta? '))
        leib_summa = leib * leib_kogus
    else:
        leib_kogus = 0
        leib_summa = 0
    tsekk = [piim_summa, sai_summa, leib_summa]
    kokku = sum(tsekk)
    print(f'Tšekk:\n Piim  {piim} * {piim_kogus}€\n  {piim}€,\n sai maksab {sai} * {sai_kogus}\n Kokku {sai}€,\n leib maksab {leib} * {leib_kogus}\n Kokku {leib}€.\n'
          f'Kokku tuleb maksta {kokku}€.\n'
          f'Tänan, head aega!')
except:
    pass

# Очищай мандадихалдур + выходи с акка, другой бы тебе просто хит бы снес!