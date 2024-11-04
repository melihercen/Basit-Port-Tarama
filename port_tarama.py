import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")

print("""
1-Hizli Tarama
2-Detaylı Tarama
3-Belirtilen Port Tarma
""")

secim=int(input("Şeçiminiz: "))
if secim==1:
    adres=input("hedef adress ip veya alan adı: ")
    os.system(f"nmap {adres}")

elif secim==2:
    adres=input("hedef adress ip veya alan adı: ")

    os.system(f"nmap -A -sV -vv -p- sS -O {adres}")

elif secim==3:
    adres=input("hedef adress ip veya alan adı: ")
    port=int(input("Taramak istediğiniz port:"))
    print("""
1-Hizli
2-Detaylı
          """)
    secim2=int(input("Seçim:"))
    if secim2==1:
        os.system(f"nmap -p {port} {adres}")
    elif secim2==2:
        os.system(f"nmap -p {port} -sV -sS -A -vv {adres}")
    else:
        print("Hatalı Secim Cıkış yapılıyor....")
    

else:
    print("Hatalı Seçim Cıkıs yapılıyor...")


