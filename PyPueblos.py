import pandas as pd

tablasiembras = pd.read_csv('./BD Siembra/Siembras.csv')

#print(tablasiembras)
'''
tablaAndes = tablasiembras[tablasiembras["Ciudad"]=="Andes"]

archivoAndes=tablaAndes.to_html()
archivotexto1=open('archivoAndes.html', "w",encoding="utf-8")
archivotexto1.write(archivoAndes)
archivotexto1.close()


tablaBarbosa = tablasiembras[tablasiembras["Ciudad"]=="Barbosa"]

archivoBarbosa=tablaBarbosa.to_html()
archivotexto1=open('archivoBarbosa.html', "w",encoding="utf-8")
archivotexto1.write(archivoBarbosa)
archivotexto1.close()

tablaCaldas = tablasiembras[tablasiembras["Ciudad"]=="Caldas"]

archivoCaldas=tablaCaldas.to_html()
archivotexto1=open('archivoCaldas.html', "w",encoding="utf-8")
archivotexto1.write(archivoCaldas)
archivotexto1.close()

tablaTámesis = tablasiembras[tablasiembras["Ciudad"]=="Támesis"]

archivoTámesis=tablaTámesis.to_html()
archivotexto1=open('archivoTámesis.html', "w",encoding="utf-8")
archivotexto1.write(archivoTámesis)
archivotexto1.close()


tablaYarumal = tablasiembras[tablasiembras["Ciudad"]=="Yarumal"]

archivoYarumal=tablaYarumal.to_html()
archivotexto1=open('archivoYarumal.html', "w",encoding="utf-8")
archivotexto1.write(archivoYarumal)
archivotexto1.close()



ArbolesMed = tablasiembras[(tablasiembras["Ciudad"]=="Medellín")&(tablasiembras["Arboles"])]
ArbolesMed = ArbolesMed.sort_values(by="Arboles") ##fALTA ORGANIZARLOS DE MAYOR A MENOR
print(ArbolesMed)

HectareasCaucasia = tablasiembras[(tablasiembras["Ciudad"]=="Caucasia")&(tablasiembras["Hectareas"])]
print(HectareasCaucasia)



SiembrasSantaFe = tablasiembras[(tablasiembras["Ciudad"]=="Santa Fe de Antioquia")&(tablasiembras["Arboles"]>250)]
print(SiembrasSantaFe)

# falta imprimir las dos en un solo filtro==  como se hace???
VeredasBelmira = tablasiembras[(tablasiembras["Ciudad"]=="Belmira")&(tablasiembras["Vereda"]=="Rio Arriba")]
print(VeredasBelmira)
VeredasBelmira2 = tablasiembras[(tablasiembras["Ciudad"]=="Belmira")&(tablasiembras["Vereda"]=="La Salazar")]
print(VeredasBelmira2)


VeredaQuitasol = tablasiembras[(tablasiembras["Ciudad"]=="Bello")&(tablasiembras["Vereda"]=="Quitasol")]
VeredaQuitasol = VeredaQuitasol.sort_values(by="Arboles") ##fALTA COMO HACER UN promedio
print(VeredaQuitasol)

'''

tablaCaramanta = tablasiembras[tablasiembras["Ciudad"]=="Caramanta"]
print(tablaCaramanta)
archivoCaramanta=tablaCaramanta.to_html()
archivotexto1=open('archivoCaramanta.html', "w",encoding="utf-8")
archivotexto1.write(archivoCaramanta)
archivotexto1.close()