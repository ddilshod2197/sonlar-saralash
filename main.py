def palindrom(matn):
    matn = matn.lower()  # harfni kichik harfga o'zgartiradi
    matn = ''.join(e for e in matn if e.isalnum())  # raqamlar va harflar qoladi, boshqa belgilarni olib tashlaydi
    return matn == matn[::-1]  # matnni orqaga qaytarib ko'radi va tengligini tekshiradi

print(palindrom("A man, a plan, a canal: Panama"))  # True
print(palindrom("Not a palindrome"))  # False
