import numpy as np

print("Neurona que aprende sobre el riego de plantas")

X = np.array([[80,18],[70,22],[65,28],[55,25],[50,32],[40,30],[35,25],[30,32],[20,35],[10,38]], dtype=float)
y = np.array([[0],[0],[0],[0],[0],[1],[1],[1],[1],[1]], dtype=float)

#Normalización

escala = np.array([100,50])

X_normalizado = X / escala

print("\nDatos normalizados:")
print(X_normalizado)

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

rng = np.random.default_rng(42)
pesos = rng.normal(size=(2,1))
sesgo = 0.0
tasa_aprendizaje = 0.8
epocas = 10000

for epoca in range(epocas):
    z = X_normalizado @ pesos + sesgo
    predicciones = sigmoide(z)

    error = predicciones - y
    gradiente_z = 2 * error * predicciones * (1-predicciones) / len(X)
    gradiente_pesos = X_normalizado.T @ gradiente_z
    gradiente_sesgo = np.sum(gradiente_z)

    pesos -= tasa_aprendizaje * gradiente_pesos
    sesgo -= tasa_aprendizaje * gradiente_sesgo

    if epoca % 2000 == 0:
        perdida = np.mean(error**2)
        print(f"Epoca: {epoca:5d} | error: {perdida:.4f} ")

print("Pesos aprendido:", pesos.ravel())
print("Sesgo aprendido:", sesgo.ravel())

print("Probar lo que el perceptron aprendió:")
print("Si la salida es mayor o igual a 0.5, va a imprimir 1")
print("Sino, va a imprimir 0")

probabilidades = sigmoide(X_normalizado @ pesos + sesgo)
respuestas = (probabilidades >= 0.5).astype(int)

for entrada, probabilidad, respuesta in zip(X_normalizado, probabilidades.ravel(), respuestas.ravel()):
    print(f"{entrada.astype(int)} -> probabilidad: {probabilidad:3f} -> respuesta: {respuesta}")

assert np.array_equal(respuestas, y.astype(int))




