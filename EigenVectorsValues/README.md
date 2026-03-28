## 1. Makine Öğrenmesi ile Matris Manipülasyonu, Özdeğerler ve Özvektörler

Makine öğrenmesinde veri genellikle matrisler şeklinde temsil edilir. Özdeğerler ve özvektörler, bu matrislerin yapısını analiz etmek için kullanılır.

Özvektörler, bir lineer dönüşüm altında yönü değişmeyen vektörlerdir. Özdeğerler ise bu vektörlerin ne kadar ölçeklendiğini gösterir.

Makine öğrenmesinde bu kavramlar özellikle aşağıdaki alanlarda kullanılır:

- PCA (Principal Component Analysis)
- Boyut indirgeme
- Veri sıkıştırma
- Özellik çıkarımı (feature extraction)

Bu yöntemler, yüksek boyutlu veriyi daha anlamlı ve düşük boyutlu hale getirmek için kullanılır.

Kaynaklar:
- MachineLearningMastery
- Gentle Introduction to Eigenvalues and Eigenvectors


## 2. NumPy eig Fonksiyonu

NumPy kütüphanesinin linalg modülünde bulunan eig fonksiyonu, kare matrislerin özdeğer ve özvektörlerini hesaplamak için kullanılır.

Fonksiyon şu şekilde çalışır:

- Girdi olarak bir kare matris alır.
- Çıktı olarak:
  - Özdeğerler (eigenvalues)
  - Özvektörler (eigenvectors) döndürür.

Özdeğerler bir vektör olarak, özvektörler ise sütunlar halinde bir matris olarak döndürülür.

Kaynak:
https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eig.html


## 3. Özdeğerlerin Eig Fonksiyonu Kullanmadan Hesaplanması

Bu çalışmada verilen repository referans alınarak özdeğerler ve özvektörler manuel yöntemlerle hesaplanmıştır.

Aynı matris için NumPy eig fonksiyonu ile elde edilen sonuçlar ile karşılaştırıldığında sonuçların aynı olduğu görülmüştür.

Bu durum, NumPy eig fonksiyonunun doğruluğunu doğrulamaktadır.

Kaynak:
https://github.com/LucasBN/Eigenvalues-and-Eigenvectors