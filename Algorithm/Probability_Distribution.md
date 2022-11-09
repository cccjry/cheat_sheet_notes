# Probability Distribution

Python package: **Scipy**

## Continuous Distribution

### Uniform

$$
f(x;a,b)=\frac{1}{b-a}, \ -\infin<a<b<\infin
$$

Mean: $\frac{1}{2}(a+b)$

Variance: $\frac{1}{12} (b-a)^2$

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
a = 0
b = 50
size = 100

#continuous
X_continuous = np.linspace(a, b, size)
continuous_uniform = stats.uniform(loc=a, scale=b)
continuous_uniform_pdf = continuous_uniform.pdf(X_continuous)
#discrete
X_discrete = np.arange(1, 7)
discrete_uniform = stats.randint(1, 7)
discrete_uniform_pmf = discrete_uniform.pmf(X_discrete)


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
#continuous plot
ax[0].plot(X_continuous, continuous_uniform_pdf)
ax[0].set_xlabel("X")
ax[0].set_ylabel("Probability")
ax[0].set_title("Continuous Uniform Distribution")
#discrete plot
ax[1].bar(X_discrete, discrete_uniform_pmf)
ax[1].set_xlabel("X")
ax[1].set_ylabel("Probability")
ax[1].set_title("Discrete Uniform Distribution")

plt.show()
```

### Gaussian

$$
f(x;\mu,\sigma)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}
$$



## Discrete Distribution