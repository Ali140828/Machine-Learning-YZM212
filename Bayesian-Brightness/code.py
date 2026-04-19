import os
import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner


os.makedirs("figures", exist_ok=True)
os.makedirs("results", exist_ok=True)


# True values
true_mu = 150.0
true_sigma = 10.0
n_obs = 50

# Generate noisy observations
np.random.seed(42)
data = true_mu + true_sigma * np.random.randn(n_obs)

print("First 10 observations:")
print(data[:10])


# Histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=12, edgecolor="black")
plt.xlabel("Observed Brightness")
plt.ylabel("Frequency")
plt.title("Histogram of Noisy Observations")
plt.savefig("figures/histogram.png", dpi=300, bbox_inches="tight")
plt.show()


# Bayesian functions
def log_likelihood(theta, data):
    mu, sigma = theta
    if sigma <= 0:
        return -np.inf
    return -0.5 * np.sum(((data - mu) / sigma) ** 2 + np.log(2 * np.pi * sigma**2))


def log_prior(theta):
    mu, sigma = theta
    if 0 < mu < 300 and 0 < sigma < 50:
        return 0.0
    return -np.inf


def log_probability(theta, data):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data)


# MCMC
initial = [140, 5]
n_walkers = 32
n_dim = 2

pos = initial + 1e-4 * np.random.randn(n_walkers, n_dim)

sampler = emcee.EnsembleSampler(n_walkers, n_dim, log_probability, args=(data,))
sampler.run_mcmc(pos, 2000, progress=False)


# Trace plot
samples = sampler.get_chain()

fig, axes = plt.subplots(2, figsize=(10, 7), sharex=True)

axes[0].plot(samples[:, :, 0], alpha=0.5)
axes[0].set_ylabel("mu")

axes[1].plot(samples[:, :, 1], alpha=0.5)
axes[1].set_ylabel("sigma")
axes[1].set_xlabel("Step")

plt.tight_layout()
plt.savefig("figures/trace_plot.png", dpi=300, bbox_inches="tight")
plt.show()


# Flatten samples
flat_samples = sampler.get_chain(discard=500, thin=15, flat=True)

print("Shape of flat samples:", flat_samples.shape)


# Summary statistics
mu_median = np.median(flat_samples[:, 0])
sigma_median = np.median(flat_samples[:, 1])

mu_p16, mu_p84 = np.percentile(flat_samples[:, 0], [16, 84])
sigma_p16, sigma_p84 = np.percentile(flat_samples[:, 1], [16, 84])

mu_abs_error = abs(mu_median - true_mu)
sigma_abs_error = abs(sigma_median - true_sigma)

print("mu median =", mu_median)
print("mu 16th percentile =", mu_p16)
print("mu 84th percentile =", mu_p84)
print("mu absolute error =", mu_abs_error)

print("sigma median =", sigma_median)
print("sigma 16th percentile =", sigma_p16)
print("sigma 84th percentile =", sigma_p84)
print("sigma absolute error =", sigma_abs_error)


# Corner plot
fig = corner.corner(
    flat_samples,
    labels=[r"$\mu$ (Brightness)", r"$\sigma$ (Noise)"],
    truths=[true_mu, true_sigma]
)
plt.savefig("figures/corner_plot.png", dpi=300, bbox_inches="tight")
plt.show()


# Save results
with open("results/summary.txt", "w", encoding="utf-8") as f:
    f.write("Parameter Comparison Table\n")
    f.write(
        f"mu     | true: {true_mu:.2f} | median: {mu_median:.2f} | "
        f"p16: {mu_p16:.2f} | p84: {mu_p84:.2f} | abs error: {mu_abs_error:.2f}\n"
    )
    f.write(
        f"sigma  | true: {true_sigma:.2f} | median: {sigma_median:.2f} | "
        f"p16: {sigma_p16:.2f} | p84: {sigma_p84:.2f} | abs error: {sigma_abs_error:.2f}\n"
    )


# Experiment 1: Narrow prior
def log_prior_narrow(theta):
    mu, sigma = theta
    if 100 < mu < 110 and 0 < sigma < 50:
        return 0.0
    return -np.inf


def log_probability_narrow(theta, data):
    lp = log_prior_narrow(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data)


initial_narrow = [105, 5]
pos_narrow = initial_narrow + 1e-4 * np.random.randn(n_walkers, n_dim)

sampler_narrow = emcee.EnsembleSampler(
    n_walkers, n_dim, log_probability_narrow, args=(data,)
)
sampler_narrow.run_mcmc(pos_narrow, 2000, progress=False)

flat_samples_narrow = sampler_narrow.get_chain(discard=500, thin=15, flat=True)

mu_median_narrow = np.median(flat_samples_narrow[:, 0])
sigma_median_narrow = np.median(flat_samples_narrow[:, 1])

print("\nNarrow prior results:")
print("mu median =", mu_median_narrow)
print("sigma median =", sigma_median_narrow)

fig = corner.corner(
    flat_samples_narrow,
    labels=[r"$\mu$ (Brightness)", r"$\sigma$ (Noise)"]
)
plt.savefig("figures/corner_plot_narrow.png", dpi=300, bbox_inches="tight")
plt.show()


# Experiment 2: Small sample size
n_obs_small = 5
np.random.seed(42)
data_small = true_mu + true_sigma * np.random.randn(n_obs_small)

print("\nSmall sample data:")
print(data_small)

initial_small = [140, 5]
pos_small = initial_small + 1e-4 * np.random.randn(n_walkers, n_dim)

sampler_small = emcee.EnsembleSampler(
    n_walkers, n_dim, log_probability, args=(data_small,)
)
sampler_small.run_mcmc(pos_small, 2000, progress=False)

flat_samples_small = sampler_small.get_chain(discard=500, thin=15, flat=True)

mu_median_small = np.median(flat_samples_small[:, 0])
sigma_median_small = np.median(flat_samples_small[:, 1])

mu_p16_small, mu_p84_small = np.percentile(flat_samples_small[:, 0], [16, 84])
sigma_p16_small, sigma_p84_small = np.percentile(flat_samples_small[:, 1], [16, 84])

print("\nSmall sample results:")
print("mu median =", mu_median_small)
print("mu 16th percentile =", mu_p16_small)
print("mu 84th percentile =", mu_p84_small)
print("sigma median =", sigma_median_small)
print("sigma 16th percentile =", sigma_p16_small)
print("sigma 84th percentile =", sigma_p84_small)

fig = corner.corner(
    flat_samples_small,
    labels=[r"$\mu$ (Brightness)", r"$\sigma$ (Noise)"],
    truths=[true_mu, true_sigma]
)
plt.savefig("figures/corner_plot_small.png", dpi=300, bbox_inches="tight")
plt.show()

