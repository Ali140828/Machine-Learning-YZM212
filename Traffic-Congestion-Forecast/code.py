import numpy as np
import scipy.optimize as opt
from scipy.stats import poisson
import matplotlib.pyplot as plt


# Gözlemlenen trafik verisi (1 dakikada geçen araç sayısı)
traffic_data = np.array([12, 15, 10, 8, 14, 11, 13, 16, 9,
                         12, 11, 14, 10, 15])

print("Trafik verisi:", traffic_data)
print("Ortalama:", np.mean(traffic_data))


def negative_log_likelihood(lam, data):
    """
    Poisson dağılımı için Negatif Log-Olabilirlik (NLL) hesaplar.

    log(k!) terimi λ'ya bağlı olmadığı için optimizasyon sırasında
    ihmal edilebilir.
    """

    n = len(data)

    # Log-likelihood hesaplama
    log_likelihood = np.sum(data * np.log(lam) - lam)

    # Negatif log-likelihood
    nll = -log_likelihood

    return nll


# Başlangıç tahmini
initial_guess = 1.0

# Optimizasyon: NLL'yi minimize etmek Likelihood'u maximize etmek anlamına gelir
result = opt.minimize(
    negative_log_likelihood,
    initial_guess,
    args=(traffic_data,),
    bounds=[(0.001, None)]
)

print(f"Sayısal Tahmin (MLE lambda): {result.x[0]}")
print(f"Analitik Tahmin (Ortalama): {np.mean(traffic_data)}")


lambda_mle = result.x[0]  # sayısal MLE

# PMF values for possible car counts
x = np.arange(0, max(traffic_data)+5)  # slightly more than max for visualization
pmf_values = poisson.pmf(x, lambda_mle)


plt.figure(figsize=(12,5))
# Histogram of observed traffic
plt.hist(traffic_data, 
         bins=np.arange(min(traffic_data)-0.5, max(traffic_data)+1.5), 
         density=True, 
         alpha=0.6, 
         color='blue', 
         label='Gözlemlenen Veri')

# PMF line
plt.plot(x, 
         pmf_values, 
         'o-', 
         color='red', 
         label=fr'Poisson PMF ($\lambda={lambda_mle:.2f}$)')

plt.xlabel('Dakikada Geçen Araç Sayısı')
plt.ylabel('Olasılık')
plt.title('Poisson Modeli vs Gözlemlenen Trafik Verisi')
plt.legend()
plt.show()





