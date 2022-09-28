from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')
tablaBelmira = tablasiembras[(tablasiembras["Ciudad"]=="Belmira")]


VeredasBelmira = tablaBelmira[(tablaBelmira["Vereda"]=="Rio Arriba")|(tablaBelmira=="La Salazar")]
print(VeredasBelmira)
'''
archivoVeredaBelmira=VeredasBelmira.to_html()
archivotexto1=open('VeredasBelmira.html', "w",encoding="utf-8")
archivotexto1.write(VeredasBelmira)
archivotexto1.close()
'''