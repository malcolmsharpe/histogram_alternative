import numpy as np
import matplotlib.pyplot as plt
import histogram_alternative

# Generate samples
N = 200
samples = np.random.randn(N)

# Default histogram
plt.hist(samples, density=True, label='histogram')

# Rectangular kernel
xs, ys = histogram_alternative.rectangular_density(samples, 0.5)

plt.plot(xs, ys, label='rectangular')

# Triangular kernel
xs, ys = histogram_alternative.triangular_density(samples, 0.5)

plt.plot(xs, ys, label='triangular')

plt.title('Density visualization')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()

plt.savefig('example.png')
