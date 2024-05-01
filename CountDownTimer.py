import time

def geri_sayaç(saniye):
    while saniye > 0:
        print(saniye)
        time.sleep(1)  # 1 saniye beklet
        saniye -= 1
    print("Geri sayım tamamlandı!")

if __name__ == "__main__":
    saniye = int(input("Kaç saniye geri saymak istersiniz? "))
    geri_sayaç(saniye)
