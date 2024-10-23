class Film:
    def __init__(self,baslik,yonetmen,yil):
        self.baslik=baslik
        self.yonetmen=yonetmen
        self.yil=yil
    def bilgi(self):
        print(f"Film:{self.baslik},Yönetmen:{self.yonetmen}, Yıl:{self.yil}")
class FilmKutuphane:
    def __init__(self):
        self.filmler=[]
    def filmEkle(self,film):
        self.filmler.append(film)
    def filmCikar(self,baslik):
        self.filmler=[film for film in self.filmler if film.baslik!=baslik]
    def filmleriGoster(self):
        if self.filmler:
            print("Film kütüphanesindeki filmler:")
            for film in self.filmler:
                film.bilgi()
        else:
            print("Kütüphanede film yok")
class Kullanici:
    def __init__(self,isim):
        self.isim=isim
        self.izlenenFilmler=[]
    def filmIzle(self,film):
        self.izlenenFilmler.append(film)
        print(f"{self.isim},{film.baslik} filmini izledi")
    def izlenenFilmleriGoster(self):
        if self.izlenenFilmler:
            print(f"{self.isim}'nin İzlediği Filmler:")
            for film in self.izlenenFilmler:
                film.bilgi()
        else:
            print(f"{self.isim} henüz film izlemedi.")
film1 = Film("Inception", "Christopher Nolan", 2010)
film2 = Film("The Matrix", "Wachowskis", 1999)
kutuphane=FilmKutuphane()
kullanici1=Kullanici("Ahmet")
kutuphane.filmEkle(film1)
kutuphane.filmEkle(film2)
kutuphane.filmleriGoster()
kullanici1.filmIzle(film1)
kullanici1.izlenenFilmleriGoster()
