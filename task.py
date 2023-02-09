class Sekil:
    def Ucgen(): # üçgen yapıcı metod
        for i in range(1,Program.uzunluk+1):
            print(" "*(Program.uzunluk-i) + "* "*i)
        print("\n")

    def Kare(): # kare yapıcı metod
        for i in range(1,Program.uzunluk+1):
            print("* "*Program.uzunluk)
        print("\n")

    def Dikdortgen(): # dikdörtgen yapıcı metod
        for i in range(1,(Program.uzunluk//2)+1):
            print("* "*Program.uzunluk)
        print("\n")

class Islem:
    def Arti(): # artı işareti yapıcı metod
        if Program.uzunluk % 2 == 0:
            i = 1
            while i <= Program.uzunluk+1:
                if i == (Program.uzunluk//2)+1:
                    print((Program.uzunluk)*"* "+"*")
                else:
                    print((Program.uzunluk//2)*"  " + "*" + (Program.uzunluk//2)*"  ")
                i += 1
        else:
            i = 1
            while i <= Program.uzunluk:
                if i == (Program.uzunluk//2)+1:
                    print((Program.uzunluk)*"* ")
                else:
                    print((Program.uzunluk//2)*"  " + "*" + (Program.uzunluk//2)*"  ")
                i += 1
        print("\n")

    def Carpi(): # çarpı yapıcı metod
        if Program.uzunluk % 2 == 0:
            i = -1
            n = 0
            for a in range(1,(int(Program.uzunluk/2))+1):
                i += 1
                n += 2
                print(" "*i + "*" + (Program.uzunluk-n)*" " + "*")
            for a in range(int((Program.uzunluk/2)),Program.uzunluk):
                print(" "*i + "*" + (Program.uzunluk-n)*" " + "*")
                i -= 1
                n -= 2
        else:
            i = -1
            n = 0
            for a in range(1,(Program.uzunluk//2)+1):
                i += 1
                n += 2
                print(" "*i + "*" + (Program.uzunluk-n)*" " + "*")
            print(" "*(Program.uzunluk//2) + "*")
            for a in range((Program.uzunluk//2)+1,Program.uzunluk):
                print(" "*i + "*" + (Program.uzunluk-n)*" " + "*")
                i -= 1
                n -= 2
        print("\n")

class Program:
    def __init__(self,uzunluk):
        self.uzunluk = uzunluk

    def SekilCiz():
        print("ŞEKİL ÇİZDİRME PROGRAMINA HOŞGELDİNİZ")
        print("-"*40)
        sekiller = [None,None,None,None,None]
        while True:
            Program.uzunluk = int(input("Uzunluk: "))
            sekilSayisi = int(input("Kaç tane şekil çizilsin: "))
            if sekilSayisi > 5:
                print("En fazla 5 şekil isteyebilirsiniz.")
            elif sekilSayisi <= 0 or Program.uzunluk <= 0:
                print("Hatalı değer girdiniz.")
            else:
                print("1-Üçgen 2-Kare 3-Dikdörtgen 4-Artı 5-Çarpı")
                for i in range(0,sekilSayisi):
                    sekiller[i] = complex(input(f"Şekil {(i+1)}: "))

                # i = 0
                # while i < sekilSayisi:
                #     sekiller[i] = complex(input(f"Şekil {(i+1)}: "))
                #     if sekiller[i] < 0 or sekiller[i] > 5:
                #         print("1 den 5 e kadar bir rakam girmelisiniz.")
                #     i += 1
                sayac = 0
                while sayac < sekilSayisi:
                    if sekiller[sayac] == 1 or sekiller[sayac] == "Üçgen" or sekiller[sayac] == "üçgen":
                        Sekil.Ucgen()
                        sayac += 1
                        
                    if sekiller[sayac] == 3 or sekiller[sayac] == "Dikdörgen" or sekiller[sayac] == "dikdörgen":
                        Sekil.Dikdortgen()
                        sayac += 1
                        
                    if sekiller[sayac] == 2 or sekiller[sayac] == "Kare" or sekiller[sayac] == "kare":
                        Sekil.Kare()
                        sayac += 1
                        
                    if sekiller[sayac] == 4 or sekiller[sayac] == "Artı" or sekiller[sayac] == "artı":
                        Islem.Arti()
                        sayac += 1
                        
                    if sekiller[sayac] == 5 or sekiller[sayac] == "Çarpı" or sekiller[sayac] == "çarpı":
                        Islem.Carpi()
                        sayac += 1
                break
            
Program.SekilCiz()
 