import random
import matplotlib.pyplot as plt
import statistics
import math

tiradas=5000
long=0
lista1=[]
frecuencia=[]
lista2=[]
media_media=[]
varianza=[]
media_varianza=[]
desvio=[]

#calculo de media, media de la media, varianza y desvio

for i in range(tiradas):
    long=long+1
    lista1.append(random.randint(0,36))
    frecuencia.append(lista1.count(5)/len(lista1))
    suma=sum(lista1)
    media=suma/long
    lista2.append(media)
    media_media.append(statistics.mean(lista2))
    if i >= 2:
        varianza.append(statistics.variance(lista1))
        media_varianza.append(statistics.mean(varianza))
        desvio.append(math.sqrt(statistics.variance(lista1)))

#grafica de frecuencia
plt.plot(frecuencia,label='Frecuencia relativa')
plt.axhline(y=0.027027, color='m', linestyle='-',label='Frecuencia relativa esperada')
plt.title("Frecuencia Relativa del número 5 en 5000 lanzamientos")
plt.ylabel("frecuencia relativa")
plt.xlabel("lanzamientos")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

#grafica de media
plt.plot(lista2,label='Media')
plt.axhline(y=18, color='r', linestyle='-',label='Media esperada')
plt.title("Media de 5000 lanzamientos")
plt.ylabel("media")
plt.xlabel("lanzamientos")
plt.grid(True)
plt.legend(loc='upper right')
plt.show()

#grafico media y media de la medias
plt.plot(lista2,label='Media')
plt.plot(media_media,label='Media de la media')
plt.axhline(y=18, color='r', linestyle='-',label='Media esperada')
plt.title("Media y Media de las medias de 5000 lanzamientos")
plt.ylabel("media de las medias")
plt.xlabel("lanzamientos")
plt.legend(loc='lower right')
plt.grid(True)
plt.show()

#grafica de varianza
plt.axhline(y=114, color='g', linestyle='-', label='Varianza esperada')
plt.plot(varianza,label='Varianza')
plt.title("Varianza de 5000 lanzamientos")
plt.ylabel("varianza")
plt.xlabel("lanzamientos")
plt.grid(True)
plt.legend(loc='upper right')
plt.show()

#Grafica varianza y media varianza
plt.axhline(y=114, color='g', linestyle='-',label='Varianza esperada')
plt.plot(varianza,label='varianza')
plt.plot(media_varianza,label='media de la varianza')
plt.title("Varianza y media de la varianza de 5000 lanzamientos")
plt.ylabel("media de la varianza")
plt.xlabel("lanzamientos")
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

#grafica desvio estandar
plt.axhline(y=10.67711, color='y', linestyle='-',label='Desvio esperado')
plt.plot(desvio,label='Desvio')
plt.title("Desvio de 5000 lanzamientos")
plt.ylabel("desvio")
plt.xlabel("lanzamientos")
plt.grid(True)
plt.legend(loc='upper right')
plt.show()

#Grafica - Histograma
plt.hist(lista1, bins=37, alpha=1, edgecolor ='black',  linewidth=1)
plt.title('HISTOGRAMA')
plt.xlabel('valores ruleta')
plt.ylabel('frecuencia absoluta')
plt.show()
plt.clf()
