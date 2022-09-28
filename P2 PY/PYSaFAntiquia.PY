from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

SiembrasSantaFe = tablasiembras[(tablasiembras["Ciudad"]=="Santa Fe de Antioquia")&(tablasiembras["Arboles"]>250)]
print(SiembrasSantaFe)

# falta imprimir las dos en un solo filtro==  como se hace???
archivoSantaFe=SiembrasSantaFe.to_html()
archivotexto1=open('archivoSantaFe.html', "w",encoding="utf-8")
archivotexto1.write(archivoSantaFe)
archivotexto1.close()
