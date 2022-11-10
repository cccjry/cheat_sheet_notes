# Probability Distribution

Python package: **Scipy**

```python
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt #for vizualize
```



## Continuous Distribution

### Uniform

$$
f(x;a,b)=\frac{1}{b-a}, \ x\in[a,b]
$$

Mean: $\frac{1}{2}(a+b), \ -\infty < a < b < \infty$

Variance: $\frac{1}{12} (b-a)^2$

```python
a = 0
b = 50
size = 100

#continuous: scipy.stats.uniform
X_continuous = np.linspace(a, b, size)
continuous_uniform = stats.uniform(loc=a, scale=b)
continuous_uniform_pdf = continuous_uniform.pdf(X_continuous)

fig, ax = plt.subplots(figsize=(15,5))
#continuous plot
ax.plot(X_continuous, continuous_uniform_pdf)
ax.set_xlabel("X")
ax.set_ylabel("Probability")
ax.set_title("Uniform Distribution")
plt.show()

#同場加映：離散型均勻分布
X_discrete = np.arange(1, 7)
discrete_uniform = stats.randint(1, 7)
discrete_uniform_pmf = discrete_uniform.pmf(X_discrete)
#discrete plot
fig, ax = plt.subplots(figsize=(15,5))
ax.bar(X_discrete, discrete_uniform_pmf)
ax.set_xlabel("X")
ax.set_ylabel("Probability")
ax.set_title("Discrete Uniform Distribution")
plt.show()
```

### Gamma

$$
f(x;\alpha, \beta)=\frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1}e^{-\beta x}, \ x>0
$$

Mean: $\alpha / \beta$, $\alpha,\ \beta >0$

Variance: $\alpha / \beta^2$

```python
#scipy.stats.gamma
a = 1.99
x = np.linspace(gamma.ppf(0.01, a), gamma.ppf(0.99, a), 100)
 = stats.gamma.pdf(x, a)

plt.subplots(figsize=(10, 8))
ax.plot(x, gamma_distribution)
plt.title("Gamma Distribution")
plt.show()
```

### Exponential

As $\alpha=1$, $\beta=\lambda$ in **Gamma Distribution**

$$
f(x;\lambda) = \lambda e^{-\lambda x}, \ x \ge 0
$$

Mean: $\frac{1}{\lambda}, \ \lambda>0$

Variance: $\frac{1}{\lambda^2}$

```python
#scipy.stats.expon
X = np.linspace(0, 5, 100)
exponetial_distribtuion = stats.expon.pdf(X, loc=0, scale=1)

plt.subplots(figsize=(10, 8))
plt.plot(X, exponetial_distribtuion)
plt.title("Exponential Distribution")
plt.show()
```

### Chi-Squared

As $\alpha=k/2$, $\beta=1/2$ in **Gamma Distribution**

$$
\chi^2_k=f(x;k)=\frac{x^{\frac{k}{2}-1}e^{-\frac{x}{2}}}{2^{\frac{k}{2}} \Gamma(\frac{k}{2})}, \ x>0
$$

Mean: $k$

Variance: $2k$

```python
#scipy.stats.chi2
df = 30
x = np.linspace(chi2.ppf(0.01, df),
                chi2.ppf(0.99, df), 100)
chi2_distribution = chi2.pdf(x, df)

plt.subplots(figsize=(10, 8))
plt.plot(x, chi2_distribution)
plt.title("Chi-squared Distribution")
plt.show()
```

### Gaussian

$$
f(x;\mu,\sigma)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}, \ x\in R
$$

Mean: $\mu, \ \mu \in R$

Variance: $\sigma^2, \ \sigma \in R_{>0}$

```python
#scipy.stats.norm
mu = 0
variance = 1
sigma = np.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
gaussian_distribution = stats.norm.pdf(x, mu, sigma)

plt.subplots(figsize=(10, 8))
plt.plot(x, gaussian_distribution)
plt.title("Normal Distribution")
plt.show()
```

### Student's t

$$
f(x;\nu)=\frac{\Gamma(\frac{(\nu+1)}{2})}{\sqrt{\nu\pi}\ \Gamma(\frac{\nu}{2})}(1+\frac{x^2}{\nu})^{-\frac{\nu+1}{2}}, \ x\in R, \ \nu:\text{degrees of freedom}
$$

Mean: 

$$\left \lbrace
\begin{array}{rr}
0, & \nu > 1 \\
\text{undefined}, & \text{otherwise}
\end{array}
\right.$$

Variance: 

$$\left \lbrace
\begin{array}{rr}
\frac{\nu}{\nu-2}, & \nu > 2 \\
\infty, & 1<\nu < 2 \\
\text{undefined}, & \text{otherwise}
\end{array}
\right.$$

```python
#scipy.stats.t
df = 2.74
x = np.linspace(stats.t.ppf(0.01, df), stats.t.ppf(0.99, df), 100)
studentT_distribution = stats.t.pdf(x, df)

plt.subplots(figsize=(10, 8))
plt.plot(x, studentT_distribution)
plt.title("Student's t Distribution")
plt.show()
```



## Discrete Distribution

### Poisson

> Rare events.
>

$$
f(x;\lambda)=\frac{\lambda^x e^{-\lambda}}{x!}, \ x=0,1,2,3,...
$$

Mean: $\lambda, \ \lambda>0$

Variance: $\lambda$

```python
#scipy.stats.poison
X = stats.poisson.rvs(mu=3, size=500)

plt.subplots(figsize=(8, 5))
plt.hist(X, density=True, edgecolor="black")
plt.title("Poisson Distribution")
plt.show()
```

### Bernoulli 

> Draw 1 ball and put back, with 2 kinds of ball inside the bag is called a ***Bernoulli trial***.
>

$$
f(x;p)= p^x (1-p)^{1-x}, \ x=0,1
$$

Mean: $p, \ p \in [0,1]$

Variance: $p (1-p)$

```python
#scipy.stats.bernoulli
p = 0.3
x = np.arange(bernoulli.ppf(0.01, p), bernoulli.ppf(0.99, p))
bernoulli_distribution = bernoulli.pmf(x, p)

fig, ax = plt.subplots(1, 1)
ax.plot(x, bernoulli_distribution, 'bo', ms=8, label='bernoulli pmf')
ax.vlines(x, 0, bernoulli.pmf(x, p), colors='b', lw=5, alpha=0.5)
plt.show()
```

### Binomial

Consider $n$ Bernoulli trials (independently) together

$$
f(x;n,p)=\left(
\begin{array}{c}
n \\
x
\end{array} 
\right) p^x (1-p)^{n-x}, \ x=0,1,2,...,n
$$

Mean: $n p, \ n \in \{0,1,2,3,... \}, \ p \in [0,1]$

Variance: $n p (1-p)$

```python
#scipy.stats.binom
n, p = 5, 0.4
x = np.arange(stats.binom.ppf(0.01, n, p), stats.binom.ppf(0.99, n, p))
binomial_distribution = stats.binom.pmf(x, n, p)

fig, ax = plt.subplots(1, 1)
ax.plot(x, binomial_distribution, 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, stats.binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
plt.show()
```



## Reference

- Wikipedia
- [Scipy Documents](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Exponential Family](https://en.wikipedia.org/wiki/Exponential_family)
