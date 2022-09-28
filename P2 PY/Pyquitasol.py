from statistics import median
from numpy import std
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')


VeredaQuitasol = tablasiembras[(tablasiembras["Ciudad"]=="Bello")&(tablasiembras["Vereda"]=="Quitasol")]
VeredaQuitasol = VeredaQuitasol.sort_values(by="Arboles")
print(VeredaQuitasol.describe())


archivoQuitasol=VeredaQuitasol.to_html()
archivotexto1=open('VeredaQuitasol.html', "w",encoding="utf-8")
archivotexto1.write(VeredaQuitasol)
archivotexto1.close()


##como guardar el archivo para que genere el HTML con el promedio

