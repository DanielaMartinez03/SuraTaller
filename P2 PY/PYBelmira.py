from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

tablaBelmira = tablasiembras[(tablasiembras["Ciudad"]=="Belmira")]

VeredasBelmira = tablaBelmira[(tablaBelmira["Vereda"]=="Rio Arriba")|(tablaBelmira["Vereda"]=="La Salazar")]


<<<<<<< HEAD
=======
VeredasBelmira = tablaBelmira[(tablaBelmira["Vereda"]=="Rio Arriba")|(tablaBelmira=="La Salazar")]
print(VeredasBelmira)

>>>>>>> b935d3efd4012356e4a502d6b8b44b78fcd03bb4
archivoVeredaBelmira=VeredasBelmira.to_html()
archivotexto1=open('VeredasBelmira.html', "w",encoding="utf-8")
archivotexto1.write(VeredasBelmira)
archivotexto1.close()
