from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

tablaAndes = tablasiembras[tablasiembras["Ciudad"]=="Andes"]

archivoAndes=tablaAndes.to_html()
archivotexto1=open('archivoAndes.html', "w",encoding="utf-8")
archivotexto1.write(archivoAndes)
archivotexto1.close()
