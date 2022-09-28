from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

tablaYarumal = tablasiembras[tablasiembras["Ciudad"]=="Yarumal"]

archivoYarumal=tablaYarumal.to_html()
archivotexto1=open('archivoYarumal.html', "w",encoding="utf-8")
archivotexto1.write(archivoYarumal)
archivotexto1.close()

