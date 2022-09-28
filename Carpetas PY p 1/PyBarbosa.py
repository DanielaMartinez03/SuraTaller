from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

tablaBarbosa = tablasiembras[tablasiembras["Ciudad"]=="Barbosa"]

archivoBarbosa=tablaBarbosa.to_html()
archivotexto1=open('archivoBarbosa.html', "w",encoding="utf-8")
archivotexto1.write(archivoBarbosa)
archivotexto1.close()