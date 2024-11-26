import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
h = 50  # Coeficiente de transferencia de calor por convección (W/m^2·K)
k = 200  # Conductividad térmica (W/m·K)
P = 0.02  # Perímetro de la sección transversal (m)
A = 0.0001  # Área de la sección transversal (m^2)
T_b = 100  # Temperatura en la base (°C)
T_inf = 25  # Temperatura del fluido circundante (°C)
L = 0.1  # Longitud de la aleta (m)

# Cálculo de m
m = np.sqrt(h * P / (k * A))

# Función para calcular la distribución de temperatura
def temperature_distribution(x, L, T_b, T_inf, h, k, m):
    # Constantes según la solución analítica
    numerator = np.cosh(m * (L - x)) + (h / (m * k)) * np.sinh(m * (L - x))
    denominator = np.cosh(m * L) + (h / (m * k)) * np.sinh(m * L)
    return T_inf + (T_b - T_inf) * (numerator / denominator)

# Discretización del dominio
x = np.linspace(0, L, 500)

# Cálculo de temperaturas
T = temperature_distribution(x, L, T_b, T_inf, h, k, m)

# Graficar la distribución de temperatura
plt.figure(figsize=(10, 6))
plt.plot(x, T, label="Distribución de temperatura", color="blue", lw=2)
plt.axhline(T_inf, color="red", linestyle="--", label="T∞ = {:.1f}°C".format(T_inf))
plt.axvline(0, color="green", linestyle="--", label="Base de la aleta (T_b = {:.1f}°C)".format(T_b))
plt.xlabel("Posición a lo largo de la aleta (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Distribución de Temperatura en una Aleta Rectangular")
plt.legend()
plt.grid()
plt.show()

