# HMM ile Konuşma Tanıma – YZM212 Makine Öğrenmesi

## Problem Tanımı
Bu projede Hidden Markov Model (HMM) kullanarak basit bir konuşma tanıma sistemi tasarlanmıştır.  
Amaç, gözlem dizilerine bakarak **"EV"** ve **"OKUL"** kelimelerini sınıflandırabilen bir model oluşturmaktır.

## Yöntem
- Fonemler **gizli durumlar (hidden states)** olarak modellenmiştir.  
- Ses özellikleri **gözlemler (observations)** olarak kabul edilmiştir.  
- En olası fonem dizisini bulmak için **Viterbi algoritması** kullanılmıştır.  
- Python tarafında `hmmlearn` kütüphanesi tercih edilmiştir.

## Veri
- Sentetik gözlem verileri kullanılmıştır.  
- Kodlama:  
  - **High frekans → 0**  
  - **Low frekans → 1**  
- Örnek gözlem dizisi: `[0,1]` (High → Low)

## Sonuçlar
- Viterbi algoritması uygulanarak gözlem dizisi `[0,1]` için en olası fonem dizisi:  
  **e → v**  
- Sistem **EV kelimesini tanımıştır**.

## Tartışma

### Gürültünün etkisi
- Gürültü veriye beklenmeyen sinyaller ekler.  
- HMM’de emisyon olasılıklarını azaltabilir ve Log-Likelihood değerlerini düşürür.  
- Örnek: “E” harfi `[1,0]` üretirken, `[0,1]` gözlemi gelirse yanlış sınıflandırma olabilir.

### Binlerce kelime olduğunda neden Deep Learning?
- **HMM + Viterbi**, sınırlı kelime ve durum için uygundur.  
- Binlerce kelime olduğunda HMM **çok karmaşık ve verimsiz** olur.  
- **Deep Learning (RNN, LSTM, Transformers)**:  
  - Uzun ve karmaşık dizileri öğrenebilir.  
  - Gürültüye dayanıklıdır.  
  - Daha yüksek doğruluk sağlar.

**Sonuç:** Küçük sistemlerde HMM uygundur, büyük ve karmaşık sistemlerde **Deep Learning tercih edilir**.
