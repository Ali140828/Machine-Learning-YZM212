import numpy as np
import scipy.optimize as opt
from scipy.stats import poisson
import matplotlib.pyplot as plt


# Mevcut trafik verisi
traffic_data = np.array([12, 15, 10, 8, 14, 11, 13, 16, 9,
                         12, 11, 14, 10, 15])

# Outlier ekleme
traffic_data_with_outlier = np.append(traffic_data, 200)

# Negatif Log-Likelihood fonksiyonu
def negative_log_likelihood(lam, data):
    """
    Poisson dağılımı için Negatif Log-Likelihood hesaplar.
    log(k!) terimi optimizasyon sırasında sabit olduğu için ihmal edilebilir.
    """
    n = len(data)
    nll = -np.sum(data * np.log(lam) - lam)  # log(k!) ihmal edildi
    return nll


# Başlangıç tahmini
initial_guess = 1.0

# Optimizasyon: NLL'yi minimize ederek MLE bulma
result = opt.minimize(negative_log_likelihood, 
                      initial_guess, 
                      args=(traffic_data_with_outlier,), 
                      bounds=[(0.001, None)])

lambda_mle_outlier = result.x[0]

print(f"Sayısal Tahmin (MLE lambda) – Outlier ile: {lambda_mle_outlier:.2f}")
print(f"Analitik Tahmin (Ortalama) – Outlier ile: {np.mean(traffic_data_with_outlier):.2f}")
