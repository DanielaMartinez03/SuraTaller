from statistics import median
from numpy import std
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')


VeredaQuitasol = tablasiembras[(tablasiembras["Ciudad"]=="Bello")&(tablasiembras["Vereda"]=="Quitasol")]
VeredaQuitasol = VeredaQuitasol.sort_values(by="Arboles")
promedio = VeredaQuitasol.describe()
tablaPromedio = promedio.loc[['mean']]
arbolesPromedio = tablaPromedio['Arboles'].to_frame()

'''archivoarbolesPromedio=arbolesPromedio.to_html()
archivotexto1=open('arbolesPromedio.html', "w",encoding="utf-8")
archivotexto1.write(archivoarboles)
archivotexto1.close()'''

##como guardar el archivo para que genere el HTML con el promedio
archivoVereda=VeredaQuitasol.to_html()
archivotexto1=open('vereda.html', "w",encoding="utf-8")
archivotexto1.write(archivoVereda)
archivotexto1.close()