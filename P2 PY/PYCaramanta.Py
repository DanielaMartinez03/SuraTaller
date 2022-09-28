from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

tablaCaramanta = tablasiembras[tablasiembras["Ciudad"]=="Caramanta"]
print(tablaCaramanta)
archivoCaramanta=tablaCaramanta.to_html()
archivotexto1=open('archivoCaramanta.html', "w",encoding="utf-8")
archivotexto1.write(archivoCaramanta)
archivotexto1.close()