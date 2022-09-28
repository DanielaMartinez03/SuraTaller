from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

tablaTámesis = tablasiembras[tablasiembras["Ciudad"]=="Támesis"]

archivoTámesis=tablaTámesis.to_html()
archivotexto1=open('archivoTámesis.html', "w",encoding="utf-8")
archivotexto1.write(archivoTámesis)
archivotexto1.close()

