# lms_image_downloader
Gazi Üniversitesi Uzaktan eğitim platformu için resimlerin indirilmesini kolaylaştıran bir program


Program python ile çalışmaktadır. Bunun python'ı yüklemeniz gerekmektedir. Aynı zamanda Windows kullanıcılarının python'ı path variable'larının
içine eklemeleri önerilir.

Firefox için geckodriver'ı indirmeniz gerekmektedir. Program selenium ile çalışmakta ve çalışabilmesi için geckodriver'a ihtiyaç duymaktadır.

https://github.com/mozilla/geckodriver/releases

adresinden indirebilirsiniz.

Daha sonra app.py, image_cutter.py ve del_images.py dosyalarının olduğu klasöre "New_images" ve "Images" isimli 2 tane klasör oluşturun.

Programın çalışması için gerekli olan dependency'leri

Windows için veya python virtualenv için:
$ pip install -r requirements.txt

Linux için:
$ pip3 install -r requirements.txt

ile yükleyiniz.

Sonra app.py'ı çalıştırınız.
Karşınıza full ekran'da bir browser gelecek. EKRANIN BOYUTUNU DEĞİŞTİRMEYİNİZ. Ekranı unmaximize edebilirsiniz.

Ve bir GUI gelecektir. 
Devam edip lms sistemine giriş yapınız.
Görüntülerini almak istediğiniz derse tıklayınız.
Ders başladığında GUI'yi açınız. 

İlk olarak Change to Tab2'ya tıklayınız. Çünkü izlemek istediğiniz ders yeni sekmede açılacağından ve bu da 2.sekme olacağından o sekmeden işlemler yapılacaktır.
Daha sonra increment değerini değiştirip Enter'a basabilirsiniz.
  Increment değeri Video slider'ının 700'e bölünmüş olarak kabul edilmiştir. Kodda -350'den +350 ye kadar increment artarak gider. Increment 10 kalırsa yaklaşık 70 görüntü elde edersiniz.
 Waiting time değerini değiştirip enter'a basınız. Slider kaydırıldığında ekranın yüklenmesi belirli bir vakit alacaktır. Waiting time ise slider kaydırılınca ekranın yüklenmesi için beklenilen zamandır. Default olarak 10 saniyedir. Slider kaydırılır 10 saniye beklenir ve ekran görüntüsü alınır.
 

Video bitince programı kapatınız. Resimler "Images" adlı klasörde bulunmaktadır.

Bu resimlerden istenilen kısımları kesmek için ise image_cutter.py'ı çalıştırınız.
Ekran resolution'ınıza göre resim lokasyonu değişebilir.
image_cutter.py'ı açınız ve oradaki x1 y1 x2 y2 değerlerini resimlerinizdeki pixel yerine göre belirleyiniz

Dikdörtgenin sol üst köşesinin koordinatları x1,y1 sağ alt köşesinin koordinatları ise x2,y2 olsun.

Burada asıl resimden x1,y1  ve x2,y2 değerlerine göre dikdörtgen kırpılmaktadır.

Bu x1,y1,x2,y2 değerleri ekran resolution'ınıza göre değişebilir.
Bu örnek için ekran resolution'ı 1600x900 dur.

image_cutter.py'ı çalıştırdıktan sonra "New_images" Klasörüne gidiniz.
Kesilen resimler orada bulunacaktır.

Aynı olan resimleri silmek için ise del_images.py'ı kullanabilirsiniz.
del_images.py'ı çalıştırdığınızda Birebir aynı olan resimlerden sadece 1 tanesi kalacak diğerleri silinecektir.
