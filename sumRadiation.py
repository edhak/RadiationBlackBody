import matplotlib.pyplot as plt
import numpy as np

# Autor: Edwin Paucar
# funciones a graficar
# densidad por unidad de frecuencia u=dE/df = (8.pi.h/c^3)(f^3/exp(hf/kt)-1)  -----------k=1.3805·10^-23 J/K.
# densidad de energia por unidad de longitud de onda(lo) u(x,T) = dE/d(lo) = (8.pi.h.c/lo^5)(1/exp(hc/lo.k.T)-1)
# desplazamiento de Wien

# contantes importantes
k = 1.3805*10**-23
h = 6.62*10**-34
c = 3*10**8
pi = 3.141592


#funcion de grafica parametro temperatura
def radiationBlackBody(lo,t=6000):
    const = 8*pi*h*c
    return (const/lo**5)*(1/(np.exp(h*c/(lo*k*t)-1)))

#desplazamiento de Wien punto maximos de la intensidad
def wienDisplacement(xt):
    return h*c/(4.965*k*xt)


# graficando
x = np.linspace(0, 3, 100)*10**-6
#temperaturas de prueba
xt = np.linspace(1000,6300,1000)

#maximo desplazamiento de wien
#hallando el vector de longitudes de onda donde la intencidad es maxima. dato:Las temperaturas xt
maxDesplazamiento = wienDisplacement(xt)

# graficando
plt.plot(x, radiationBlackBody(x,6000), label='Para T = 6000k')
plt.plot(x, radiationBlackBody(x,5000), label='Para T = 5000k')
plt.plot(x, radiationBlackBody(x,3000), label='Para T = 3000k')

#grafica del desplazamiento de wien
plt.plot(maxDesplazamiento, radiationBlackBody(maxDesplazamiento,xt), label='Desplazamiento de Wien')

#imprimiendo los valores maximos para nuestros datos particulares T=6000, 5000, 3000
print(6000, radiationBlackBody(wienDisplacement(6000), 6000))
print(5000, radiationBlackBody(wienDisplacement(5000), 5000))
print(3000, radiationBlackBody(wienDisplacement(3000), 3000))

plt.ylabel('Intencidad')
plt.xlabel('longitud de onda en m')

plt.title("Radiación del Cuerpo Negro")

plt.legend()

plt.show()
