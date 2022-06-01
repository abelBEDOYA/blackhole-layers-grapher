# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 00:45:41 2021

@author: USUARIO
"""
import numpy as np
import matplotlib.pyplot as plt

#Pueden ser definidos a voluntad cumpliendo mu>=a_
#----------
mu = float(input('mu (proporcional a la masa): '))#1    #proporcional masa
a_ = float(input('Momento angular especifico del aguejero negro: '))#0.1  #momento angular especifico
#----------

c = 1
Rs=2*mu
pi = np.pi

#Para que el formato sea LaTex:
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

def pintadorXZ(arr, nombre, pintar, col):
    '''
    Representa una capa en el plano XZ
    arr = array con el radio de la capa segun coord. theta
    '''
    #Tener en cuenta Boyer-Lindquist
    XX =np.sqrt(arr**2 +a_**2)*np.sin(np.linspace(0,2*pi))
    ZZ =arr*np.cos(np.linspace(0,2*pi))
    
    if pintar ==1: #Rellenar capa con color
        plt.fill(XX,ZZ,'black')
    
    plt.plot(XX, ZZ, '-', color=col, label = nombre)
    plt.xlabel(r'$x$', size=25)
    plt.ylabel(r'$z$', size=25)
    plt.vlines(0, -1.1*2*mu, 1.1*2*mu) #Eje z
    return XX, ZZ

#Arrays con las distancias al centro de las superficies segun theta
e_mas = mu + np.sqrt(mu**2-a_**2*(np.cos(np.linspace(0,2*pi)))**2)
e_menos = mu - np.sqrt(mu**2-a_**2*(np.cos(np.linspace(0,2*pi)))**2) 
h_mas= mu + np.sqrt(mu**2-a_**2)
h_menos= mu - np.sqrt(mu**2-a_**2)

plt.clf()

#Pintar capas una por una
pintadorXZ(Rs, 'radio Sch.', 0, 'blue')
pintadorXZ(e_mas, r'erg.esfera Out', 0, 'green')
pintadorXZ(e_menos, 'erg.esfera Inn', 0, 'lime')
pintadorXZ(h_mas, 'horizonte Out', 1, 'black')
pintadorXZ(h_menos, 'horizonte Inn', 0, 'darkviolet')
plt.title(r'$R_s$ = '+str(Rs)+', $\mu$ = '+str(mu)+', a = '+str(a_), fontsize=20)
plt.plot([-a_, a_], [0,0], '-', color = 'orange', label=r'Singul. anillo')

plt.gca().set_aspect('equal', adjustable='box') #Misma ganancia en cada eje
plt.legend()

plt.savefig('nombre')





