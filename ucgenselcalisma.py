#3x3'luk matrisin türünü belirten basit bir program. Hazırlayan: Mustafa Yakın


deger3x3 = print("3x3'luk matris olusturdunuz.")
a11 = int(input("1x1 degeri:"))
a12 = int(input("1x2 degeri:"))
a13 = int(input("1x3 degeri:"))
a21 = int(input("2x1 degeri:"))
a22 = int(input("2x2 degeri:"))
a23 = int(input("2x3 degeri:"))
a31 = int(input("3x1 degeri:"))
a32 = int(input("3x2 degeri:"))
a33 = int(input("3x3 degeri:"))
# aSifir degerini verme sebebim eger matrise vereceginiz degerler benim tanimladigim degerlerden farkliysa
# tanimlanmamis matrise yönlendirsin diye. Daha akillica bir yontem aklima gelmedi.

    if a12 == 0 and a13 == 0 and a23 == 0:
        if a22 == 0 and a11 == 0 and a33 == 0:
            if a21 != 0 or a31 !=0 or a32 != 0:
                print("Tam Ucgensel matris.")

        if a22 != 0 or a11 != 0 or a33 !=0:
            print("Alt ucgensel matris")


        if a11 == 0 and a12 == 0 and a13 == 0 and a21 == 0 and a22 == 0 and a23 == 0 and a31 == 0 and a32 == 0 and a33 == 0:
            print("sifir matrisi.")


    #Ustteki yazdıgım algoritmanın ayna goruntusunu alip asagiya bir kac düzenleme ile birlikte ust ucgensel matrisin kodlarını yazdım.
    if a21 == 0 and a31 == 0 and a32 == 0:
        if a22 == 0 and a11 == 0 and a33 == 0:
            if a12 != 0 or a13 !=0 or a23 != 0:
                print("Tam Ucgensel matris")

        if a22 != 0 or a11 != 0 or a33 !=0:
            print("Ust ucgensel matris")

else:
    print("tanimlanmamis matris")