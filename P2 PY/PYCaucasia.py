from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

HectareasCaucasia = tablasiembras[(tablasiembras["Ciudad"]=="Caucasia")&(tablasiembras["Hectareas"])]
print(HectareasCaucasia)

archivoHectareasMed=HectareasCaucasia.to_html()
archivotexto1=open('HectareasMed.html', "w",encoding="utf-8")
archivotexto1.write(HectareasMed)
archivotexto1.close()
