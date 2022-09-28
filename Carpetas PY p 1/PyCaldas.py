from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

tablaCaldas = tablasiembras[tablasiembras["Ciudad"]=="Caldas"]

archivoCaldas=tablaCaldas.to_html()
archivotexto1=open('archivoCaldas.html', "w",encoding="utf-8")
archivotexto1.write(archivoCaldas)
archivotexto1.close()
