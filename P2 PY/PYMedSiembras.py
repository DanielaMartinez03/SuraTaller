from statistics import median
import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

ArbolesMed = tablasiembras[(tablasiembras["Ciudad"]=="Medellín")&(tablasiembras["Arboles"])]
ArbolesMed = ArbolesMed.sort_values(by="Arboles") ##fALTA ORGANIZARLOS DE MAYOR A MENOR
print(ArbolesMed)

archivoArbolesMed=ArbolesMed.to_html()
archivotexto1=open('archivoArbolesMed.html', "w",encoding="utf-8")
archivotexto1.write(archivoArbolesMed)
archivotexto1.close()
