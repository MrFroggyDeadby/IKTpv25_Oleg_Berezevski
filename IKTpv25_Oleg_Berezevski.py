#print('Tere, maailm!')
#nimi = input('Mis on sinu nimi? ').capitalize()

#print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
#print(f'Tere, maailm! Tervitan sind {nimi}! Kui vana sa oled?')
#vanus = input()
#print(f'Oi kui tore, sa oled {vanus} aastat vana')





#vanus = 18  #int
#nimi = 'Jaak'  #str
#pikkus = 16.5  #float
#kas_käib_koolis = False  #bool

#if kas_käib_koolis == True:
#    print('Näeme koolis')
#else:
#    print('Näeme tööl')

#print(type(vanus))
#print(type(nimi))
#print(type(pikkus))
#print(type(kas_käib_koolis))


from random import randint
while True:
    kommid = randint(5, 10)
    print(f'Laual on {kommid} kommi')
    poiss = int(input('Mitu kommi sa soovid võtta? '))
    if poiss > kommid:
        print('Laual pole nii palju komme')
    else:
        print(f'Laual on {kommid - poiss} kommi')
