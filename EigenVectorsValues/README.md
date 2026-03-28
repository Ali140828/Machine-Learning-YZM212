
## 1. Matris Manipülasyonu, Özdeğerler ve Özvektörlerin Makine Öğrenmesi ile İlişkisi

Makine öğrenmesinde veriler genellikle matrisler şeklinde temsil edilir. Matris manipülasyonu, bu veriler üzerinde matematiksel işlemler yaparak anlamlı özellikler elde etmeyi sağlar.

Özdeğerler (eigenvalues) ve özvektörler (eigenvectors), bir matrisin lineer dönüşüm özelliklerini analiz etmek için kullanılır. Özvektörler, bir dönüşüm uygulandığında yönü değişmeyen vektörlerdir. Özdeğerler ise bu vektörlerin ne kadar ölçeklendiğini ifade eder.

Makine öğrenmesinde bu kavramlar özellikle aşağıdaki alanlarda kullanılır:

- Principal Component Analysis (PCA)
- Boyut indirgeme (dimensionality reduction)
- Veri sıkıştırma
- Özellik çıkarımı (feature extraction)
- Veri içindeki en önemli varyans yönlerinin bulunması

Özellikle PCA algoritması, veri setindeki en büyük varyansı yakalayan özvektörleri kullanarak veriyi daha düşük boyutlu bir uzaya projekte eder. Bu sayede veri daha basit ve anlamlı hale gelir.

Sonuç olarak, matris manipülasyonu veriyi temsil etmek için kullanılırken, özdeğerler ve özvektörler bu verinin yapısını analiz etmek ve önemli özellikleri استخراج etmek için kullanılır.

Kaynaklar:
- MachineLearningMastery
- Gentle Introduction to Eigenvalues and Eigenvectors

---

## 2. NumPy eig Fonksiyonu

NumPy kütüphanesinin `linalg` modülü içerisinde bulunan `eig` fonksiyonu, kare matrislerin özdeğer ve özvektörlerini hesaplamak için kullanılır.

Fonksiyon bir matrisi giriş olarak alır ve:

- Eigenvalues (özdeğerler)
- Eigenvectors (özvektörler)

çıktı olarak döndürür.

Eigenvalues bir dizi olarak, eigenvectors ise sütunlar halinde bir matris olarak döner.

Kaynak:
https://numpy.org/doc/2.1/reference/generated/numpy.linalg.eig.html

---

## 3. Özdeğerlerin Eig Fonksiyonu Kullanmadan Hesaplanması

Bu çalışmada özdeğerler, karakteristik denklem kullanılarak manuel olarak hesaplanmıştır.

Bir matris için:

det(A - λI) = 0

denkleminden özdeğerler bulunur.

Bu çalışmada elde edilen sonuçlar NumPy `eig` fonksiyonu ile karşılaştırılmış ve aynı olduğu görülmüştür.

Kaynak:
https://github.com/LucasBN/Eigenvalues-and-Eigenvectors