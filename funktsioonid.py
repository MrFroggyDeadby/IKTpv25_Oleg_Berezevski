def int_kontrol(sisend:str):
    """Kontrollib, kas sisestatud andmed on teisendatavad int aruks
    :param str sisend: kasutaja sisestatud andmed
    :return/rtype: teisendatud int arv
    """
    while True:
        try:
            arv = int(sisend)
            return arv
        except ValueError:
            sisend = input("Palun sisesta arv: ")

def float_kontrol(sisend:str):
    """Kontrollib, kas sisestatud andmed on teisendatavad float aruks
    :param str sisend: kasutaja sisestatud andmed
    :return/rtype: teisendatud float arv
    """
    while True:
        try:
            arv = float(sisend)
            return arv
        except ValueError:
            sisend = input("Palun sisesta arv: ")

def arithmetic(a:float, b:float, tehe:str)->any:
    """Lihtne kalkulaator:
    + — liitmine
    - — lahutamine
    * — korrutamine
    / — jagamine
    Muul juhul tagastab "Tundmatu tehe"
    :param float a: esimene arv
    :param float b: teine arv
    :param str tehe: Tehe, mis tuleb teha
    :return/rtype: tehte tulemus float või str
    """
    if tehe in ["+", "-", "*", "/"]:
        if tehe == "/" and b==0:
            vastus = "Nulliga jagamine pole lubatud"
        else:
            vastus = eval(f"{a}{tehe}{b}")
    else:
        vastus = "Tundmatu tehe"
    return vastus


def is_year_leap(aasta:int)->bool:
    """Kontrollib, kas aasta on liigaasta
    :param: int aasta: aasta arvuna
    :return/rtype: True kui liigaasta, False kui tavaline aasta
    """
    if (aasta % 4 == 0 and aasta % 100 != 0):
        return True
    else:
        return False

def square(külg:float)->any:
    """Arvutab ruudud ümbermõõdu, pindala ja diagonaali
    :param float külg: ruudu külje pikkus
    :return/rtype: ümbvermõõt, pindala, diagonaal"""
    ümbermõõt = 4 * külg
    pindala = külg ** 2 # või külg * külg
    diagonaal = külg ** 0.5 * 2
    return ümbermõõt, pindala, diagonaal