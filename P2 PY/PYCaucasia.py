from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

HectareasCaucasia = tablasiembras[(tablasiembras["Ciudad"]=="Caucasia")&(tablasiembras["Hectareas"])]
SoloHectarea = HectareasCaucasia["Hectareas"].to_frame()


SoloHectarea=SoloHectarea.to_html()
archivotexto1=open('SoloHectarea.html', "w",encoding="utf-8")
archivotexto1.write(SoloHectarea)
archivotexto1.close()

<<<<<<< HEAD
=======
#Falta mostrar las hectareas
>>>>>>> b935d3efd4012356e4a502d6b8b44b78fcd03bb4
