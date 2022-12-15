from tkinter import *

pencere = Tk()

pencere.title("MİNİ ÖRÜMCEK")
baslik = Label(pencere, text="Mini Örümceğe Hoş Geldiniz!")
baslik.grid(row=0, columnspan=2, padx=50, pady=25)

buton1 = Button(pencere, text="Menüye Gitmek İçin Tıklayınız...", fg="red", bg="green")
buton3 = Button(pencere, text="<<< Çıkış >>>", fg="black", bg="red", command=pencere.quit)

buton1.grid(row=3, column=0, padx=50, pady=10)
buton3.grid(row=3, column=1, padx=50, pady=10)


pencere.mainloop()


class menusecim:
    while True:
        print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
        menuSecim = (input("Tercihiniz: "))
        if menuSecim.isdigit():
            menuSecim = int(menuSecim)
            if menuSecim == 0:
                print("Mini Örümcek kapatılıyor...")
                time.sleep(1)
                break
            elif menuSecim == 1:
                useDataURL.dataRead()
            elif menuSecim == 2:
                useDataURL.dataWrite()
            elif menuSecim == 3:
                useGetURL.getWeb()
            elif menuSecim == 4:
                useGetURL.getList()
            elif menuSecim >= 4:
                print("0 ile 4 arasında bir seçim yapınız.")
        else:
            print("Lütfen geçerli bir menü numarası giriniz.")


pencere.mainloop()



from tkinter import *
def pencere_ac():
pencere = Toplevel()
baslik = Label(pencere,text=“Ana pencereden Açılan pencere”)
baslik.pack()
ana_pencere.destroy() #Ya da ana_pencere.destroy()

if name == ‘main’:
ana_pencere = Tk()
buton1 = Button(ana_pencere, text=“Pencere Aç”,command=pencere_ac)
buton1.pack()
mainloop()