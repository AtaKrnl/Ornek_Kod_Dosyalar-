print("--- Basit Hesap Makinesi ---")

while True:
    sayi1 = float(input("1. sayıyı girin: "))
    islem = input("İşlem (+, -, *, /): ")
    sayi2 = float(input("2. sayıyı girin: "))

    if islem == '+':
        sonuc = sayi1 + sayi2
        print(f"Sonuç: {sonuc}\n")
    elif islem == '-':
        sonuc = sayi1 - sayi2
        print(f"Sonuç: {sonuc}\n")
    elif islem == '*':
        sonuc = sayi1 * sayi2
        print(f"Sonuç: {sonuc}\n")
    elif islem == '/':
        if sayi2 == 0:
            print("Bir sayı sıfıra bölünemez\n")
        else:
            sonuc = sayi1 / sayi2
            print(f"Sonuç: {sonuc}\n")
    else:
        print("Geçersiz işlem!\n")
