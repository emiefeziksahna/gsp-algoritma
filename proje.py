from math import *
import PySimpleGUI as gab
from itertools import permutations

def hesapla_mesafe(tur, mesafeler):
    toplam_mesafe = 0
    for i in range(len(tur) - 1):
        baslangic_sehri = tur[i]
        varis_sehri = tur[i + 1]
        toplam_mesafe += mesafeler[baslangic_sehri][varis_sehri]
    return toplam_mesafe

def en_kisa_turu_bul(sehirler, mesafeler):
    en_kisa_tur = None
    en_kisa_mesafe = float('inf')

    for perm in permutations(sehirler):
        mesafe = hesapla_mesafe(perm, mesafeler)
        if mesafe < en_kisa_mesafe:
            en_kisa_mesafe = mesafe
            en_kisa_tur = perm

    return en_kisa_tur

arayuz = [[],
          [gab.Text('Başlangıç Noktası:',s=(15,1)), gab.Input(key='baslangic', s=(10,1))],
          [gab.Text('Çizge Noktaları:', s=(15,1)), gab.Multiline(key='mline', s=(10,10))],
          [gab.Button('Hesapla', key='onay')]]
program = gab.Window('Gezgin Satıcı Hesaplama', arayuz)

while True:
    events, values = program.read()
    if events == gab.WIN_CLOSED:
        exit()
    noktalar = []
    for a in values['mline'].split('\n'):
        xytemp = a.split(',')
        noktalar.append([int(xytemp[0]), int(xytemp[1])])
    baslangic = [values['baslangic'].split(',')[0], values['baslangic'].split(',')[1]]
    if events == 'onay':
        uzaklikliste = []
        for i in noktalar:
            uzaklikliste0temp = []
            for j in noktalar:
                
                uzaklikliste0temp.append(ikinoktaarasiuzaklik)
                ikinoktaarasiuzaklik = sqrt((i[0] - j[0])*2 + (i[1] - j[1])*2)
            uzaklikliste.append(uzaklikliste0temp)
        sehirler = list(range(len(noktalar)))
        en_kisa_tur = en_kisa_turu_bul(sehirler, uzaklikliste)
        if en_kisa_tur is not None:
            gab.popup(f"En kısa tur: {en_kisa_tur}\nEn kısa mesafe: {hesapla_mesafe(en_kisa_tur, uzaklikliste)}")
        else:
            gab.popup("Çözüm bulunamadı.")
