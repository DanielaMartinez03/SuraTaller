from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

VeredasBelmira = tablasiembras[(tablasiembras["Ciudad"]=="Belmira")&(tablasiembras["Vereda"]=="Rio Arriba"|tablasiembras["Vereda"]=="La Salazar")]
print(VeredasBelmira)