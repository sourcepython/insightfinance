

import matplotlib.pyplot as plt
import seaborn as sns

# Establecer el estilo Seaborn
sns.set(style="whitegrid")

def calcular_NPV(cf, r):
    f = 1 + r
    NPV = 0
    for i in range(len(cf)):
        NPV += cf[i] / f**(i)
    return NPV

def graficar_NPV(cf):
    l = list(range(0, 151))
    rs = [i/1000 for i in l]
    npvs = []
    for i in rs:
        npv = 0
        for j in range(len(cf)):
            npv += cf[j] / (1 + i)**(j)
        npvs.append(npv)

    plt.figure(figsize=(12, 8))
    plt.scatter(x=r, y=calcular_NPV(cf, r), s=100, c="skyblue", marker="o", label="NPV @ r")
    plt.plot(rs, npvs, color="salmon", linewidth=2, linestyle="-", label="NPV(r)")
    plt.grid()
    plt.hlines(y=0, xmin=rs[0], xmax=rs[-1], linestyles="dashed", color="gray", label="NPV = 0", alpha=0.5)
    plt.title("Valor Actual Neto (NPV) en función de la tasa de descuento", fontsize=15)
    plt.xlabel("Tasa de descuento (r)", fontsize=12)
    plt.ylabel("Valor", fontsize=12)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.legend(loc="best", fontsize=12)
    plt.show()

def calcular_ROI(cf, r):
    NPV = calcular_NPV(cf, r)
    costo_inicial = abs(cf[0])  # Tomar el valor absoluto del primer flujo de efectivo como costo inicial
    ganancia_neta = NPV + cf[0]  # Ganancia neta es el NPV más el costo inicial original
    ROI = (ganancia_neta / costo_inicial) * 100  # Fórmula para el ROI usando el valor absoluto del costo inicial
    return ROI

def graficar_NPV_ROI(cf):
    l = list(range(0, 151))
    rs = [i/1000 for i in l]
    npvs = []
    rois = []
    
    for i in rs:
        npv = calcular_NPV(cf, i)
        npvs.append(npv)
        roi = calcular_ROI(cf, i)
        rois.append(roi)

    plt.figure(figsize=(12, 8))
    plt.plot(rs, npvs, color="cornflowerblue", linewidth=2, linestyle="-", label="NPV(r)")
    plt.plot(rs, rois, color="mediumseagreen", linewidth=2, linestyle="-", label="ROI(r)")
    plt.grid()
    plt.title("Valor Actual Neto (NPV) y Retorno de la Inversión (ROI)", fontsize=15)
    plt.xlabel("Tasa de descuento (r)", fontsize=12)
    plt.ylabel("Valor", fontsize=12)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.legend(loc="best", fontsize=12)
    plt.show()

# Utiliza tus datos de flujo de efectivo (cf)
# Luego, llama a las funciones para graficar los valores de NPV y ROI


# Datos de ejemplo
cf = [-200, 20, 50, 70, 100, 50]
r = 0.06

# Calcular NPV y graficar
print("NPV:", calcular_NPV(cf, r))
graficar_NPV(cf)
#out 38.71


# Calcular NPV y graficar
print("ROI:", calcular_ROI(cf, r))
graficar_NPV_ROI(cf)
#out -80.64
