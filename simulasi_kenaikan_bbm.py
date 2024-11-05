import numpy as np
import matplotlib.pyplot as plt

# Parameter model
H0 = 10000  # harga awal BBM
r = 0.05    # laju kenaikan 5% per tahun
t = np.linspace(0, 10, 100)  # waktu dalam tahun (10 tahun)

# Fungsi model harga BBM
H = H0 * np.exp(r * t)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, H, label="Harga BBM", color="blue")
plt.xlabel("Tahun")
plt.ylabel("Harga BBM")
plt.title("Pemodelan Kenaikan Harga BBM")
plt.legend()
plt.grid(True)
plt.show()
