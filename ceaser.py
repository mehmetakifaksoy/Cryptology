def sifrele(metin, kaydirma):
    sifreli_metin = ""

    for harf in metin:
        if harf.isupper():
            sifreli_metin += chr((ord(harf) - 65 + kaydirma) % 26 + 65)
        elif harf.islower():
            sifreli_metin += chr((ord(harf) - 97 + kaydirma) % 26 + 97)
        else:
            sifreli_metin += harf
    return sifreli_metin

def coz(sifreli_metin, kaydirma):
    return sifrele(sifreli_metin, -kaydirma)

# Kullanım Örneği
metin = "Merhaba Dunya"
kaydirma = 3

sifreli = sifrele(metin, kaydirma)
cozulmus = coz(sifreli, kaydirma)

print("Orijinal Metin:", metin)
print("Şifrelenmiş Metin:", sifreli)
print("Çözülmüş Metin:", cozulmus)
