# YZM212 Makine Öğrenmesi - 4. Laboratuvar Ödevi  
## Uzak Bir Galaksinin Parlaklık Analizi (Bayesyen Çıkarım)

---

## 1. Problem Tanımı

Bu projede, gürültülü gözlem verileri kullanılarak bir gök cisminin gerçek parlaklığı (μ) ve ölçüm hatası (σ) Bayesyen çıkarım yöntemleri ile tahmin edilmektedir.

Astronomide doğrudan deney yapmak mümkün olmadığından, gözlemsel veriler genellikle gürültü içerir. Bu nedenle, belirsizlikleri doğru şekilde modellemek büyük önem taşır.

Bu çalışma, Bayesyen yöntemlerin bu tür belirsizlikleri nasıl yönettiğini göstermektedir.

---

## 2. Veri

Veriler, normal dağılıma dayalı olarak sentetik şekilde üretilmiştir:

- Gerçek parlaklık (μ): 150.0  
- Gürültü seviyesi (σ): 10.0  
- Gözlem sayısı (n): 50  

Veri üretim modeli:

data = true_mu + true_sigma * np.random.randn(n_obs)

Bu yapı, teleskop ölçümlerinde oluşabilecek rastgele hataları simüle etmektedir.

---

## 3. Yöntem

Bu projede Bayesyen çıkarım ve Markov Chain Monte Carlo (MCMC) yöntemi kullanılmıştır.

### 3.1 Kullanılan Model

- Likelihood: Gaussian (Normal dağılım)
- Prior: Uniform dağılım  
  - μ ∈ (0, 300)  
  - σ ∈ (0, 50)

### 3.2 Posterior Dağılım

Bayes teoreminin logaritmik formu kullanılmıştır:

log P(θ | D) = log P(θ) + log P(D | θ) + C

### 3.3 MCMC Örnekleme

Parametrelerin posterior dağılımı emcee kütüphanesi kullanılarak elde edilmiştir:

- Walker sayısı: 32  
- Adım sayısı: 2000  
- Burn-in: 500 adım  

---

## 4. Sonuçlar

### 4.1 Parametre Tahminleri

| Parametre | Gerçek Değer |  Medyan  |   %16   |   %84   | Mutlak Hata |
|-----------|--------------|----------|---------|---------|-------------|
| μ         | 150.0        | 147.79   | 146.43  | 149.07  | 2.21        |
| σ         | 10.0         | 9.49     | 8.55    | 10.53   | 0.51        |

---

## 5. Görselleştirme

Projede aşağıdaki grafikler oluşturulmuştur:

- Histogram (veri dağılımı)
- Trace Plot (MCMC zincir davranışı)
- Corner Plot (posterior dağılım ve parametre ilişkileri)

Corner plot, parametreler arasındaki olası korelasyonu görselleştirmek için kullanılmıştır.

---

## 6. Analiz

### 6.1 Doğruluk (Accuracy)

μ parametresinin tahmini, gerçek değere oldukça yakındır. Bu durum, Bayesyen modelin gürültülü veriye rağmen doğru tahmin yapabildiğini göstermektedir.

Modelin mutlak hata değeri düşük olduğu için sonuçlar güvenilirdir.

---

### 6.2 Hassasiyet (Precision)

μ parametresi, σ parametresine göre daha hassas tahmin edilmiştir.

Bunun nedeni, ortalama değerinin doğrudan gözlemlerden etkilenmesi, σ'nın ise dağılımın yayılımına bağlı olmasıdır.

---

### 6.3 Korelasyon Analizi

Corner plot incelendiğinde, μ ve σ parametreleri arasında zayıf veya orta düzeyde bir korelasyon gözlemlenebilir.

Bu durum, gürültü seviyesindeki değişimlerin parlaklık tahminini kısmen etkileyebileceğini göstermektedir.

---

## 7. Deneyler

### 7.1 Dar Prior Etkisi

μ parametresi için dar bir prior (100–110) seçildiğinde, posterior dağılım bu aralığa çekilmiştir.

Bu, yanlış prior seçiminin sonucu ciddi şekilde etkileyebileceğini göstermektedir.

---

### 7.2 Gözlem Sayısının Azaltılması

Gözlem sayısı 50'den 5'e düşürüldüğünde, posterior dağılım genişlemiştir.

Bu durum, veri miktarının azalmasının belirsizliği artırdığını ve tahminlerin daha az güvenilir hale geldiğini göstermektedir.

---

## 8. Sonuç

Bu çalışmada, Bayesyen çıkarım yöntemleri kullanılarak gürültülü verilerden anlamlı parametre tahmini yapılmıştır.

Elde edilen sonuçlar:

- μ parametresi yüksek doğrulukla tahmin edilmiştir
- σ parametresi daha geniş belirsizlik göstermiştir
- prior seçimi sonuçları doğrudan etkiler
- veri miktarı arttıkça model daha güvenilir hale gelir

Bu proje, Bayesyen yöntemlerin belirsizlik içeren problemlerde ne kadar güçlü olduğunu ortaya koymaktadır.

---

## 9. Kullanılan Kütüphaneler

- numpy
- matplotlib
- emcee
- corner

---

<pre> ```bash Bayesian_Brightness_Analysis/ │ ├── brightness_analysis.ipynb ├── README.md ├── requirements.txt ├── report.pdf │ ├── figures/ │ ├── histogram.png │ ├── trace_plot.png │ └── corner_plot.png │ └── results/ └── summary.txt ``` </pre>

---

## 11. Not

Her simülasyon çalıştırıldığında sonuçlar küçük farklılıklar gösterebilir.
Bu nedenle tablo değerleri her kullanıcı için farklı olabilir.
