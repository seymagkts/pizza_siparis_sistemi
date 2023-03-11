import datetime

def isValidTCID(value):
    value = str(value)
    # 11 hanelidir.
    if not len(value) == 11:
        return False
    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    # Ilk hanesi 0 olamaz.
    if int(value[0]) == 0:
        return False
    digits = [int(d) for d in str(value)]
    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
    # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    # Butun kontrollerden gecti.
    return True

def basamak_bul(sifre):
    say = 0
    while sifre > 0:
        sifre = sifre // 10
        say += 1
    return say

def odeme_yap(isim,kredi_kart,sifre,id,tutar,aciklama):
    try:
        sifre = int(sifre)
        sifre_basamak = basamak_bul(sifre)
        if isValidTCID(id) == False:
            return False
        elif len(kredi_kart) != 16:  # kart no 16 haneli olmalı
            return False
        elif sifre_basamak != 4:  # sifre 4 haneli olmalı
            return False
        else:
            txt_kayit(isim, kredi_kart, sifre, id, tutar, aciklama)
            return True
    except:
        pass

def txt_kayit(isim,kart,sifre,id,tutar,aciklama):
    now=str(datetime.datetime.now())
    aciklama = str(tutar)+" TL "+aciklama
    dosya = open("orders_database.txt", "a", encoding="utf-8")
    dosya.write(isim+",")
    dosya.write(id+",")
    dosya.write(kart+",")
    dosya.write(str(sifre)+",")
    dosya.write(aciklama+",")
    dosya.write(now+"\n")


# Pizza Sub classı
class Pizza():
    def get_cost(self):
        pass
    def get_description(self):
        pass

# Pizza classları
class classic_pizza(Pizza):
    def get_cost(self):
        return 109
    def get_description(self):
        return "Pizza sosu, mozzarella, sucuk, yeşilbiber"

class margarita(Pizza):
    def get_cost(self):
        return 99

    def get_description(self):
        return "Pizza sosu, mozzarella, pesto sos, domates"

class turkish_pizza(Pizza):
    def get_cost(self):
        return 115

    def get_description(self):
        return "Pizza sosu, mozzarella, sucuk, salam, sosis"

class sade_pizza(Pizza):
    def get_cost(self):
        return 95

    def get_description(self):
        return "Pizza sosu, mozzarella"

# Malzeme classları
class zeytin(Pizza):
    def get_cost(self):
        return 3
    def get_description(self):
        return "Zeytin"

class misir(Pizza):
    def get_cost(self):
        return 3
    def get_description(self):
        return "Mısır"

class et(Pizza):
    def get_cost(self):
        return 19
    def get_description(self):
        return "Et"

class sogan(Pizza):
    def get_cost(self):
        return 4
    def get_description(self):
        return "Sogan"

class peynir(Pizza):
    def get_cost(self):
        return 10
    def get_description(self):
        return "Keçi Peyniri"

class mantar(Pizza):
    def get_cost(self):
        return 5
    def get_description(self):
        return "Mantar"

