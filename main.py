from tkinter import *

pencere1 = Tk()
def yenipencere():
    pencere2 = Toplevel()
    buton2 = Button(pencere2, text="Url Ekle", width=20, height=5, fg="red", bg="green")
    buton4 = Button(pencere2, text="Url Listele", fg="black", bg="green", width=20, height=5)
    buton5 = Button(pencere2, text="Örümcek Gönder", fg="red", bg="green", width=20, height=5)
    buton6 = Button(pencere2, text="Sonuçları Listele", fg="black", bg="green",width=20, height=5)
    buton2.pack()
    buton4.pack()
    buton5.pack()
    buton6.pack()


buton1 = Button(text="Menü", command=yenipencere)
buton3 = Button(text="Çıkış", fg="white", bg="red", command=pencere1.quit)
buton1.pack()
buton3.pack()

pencere1.mainloop()
pencere2.mainloop()