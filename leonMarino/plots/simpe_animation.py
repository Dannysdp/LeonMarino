"""
==================
Animated bar plot
==================

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd

path = "D:/Drive/Leon Marino/data/CIANOBACTERIA/Scopus-51-Analyze-Year (1).csv"
papersYear= pd.read_csv(path, encoding="latin",index_col=0)

# Preparando datos
Xvalues = np.flip(papersYear.index.values)
Yvalues = np.flip(papersYear["PAPERS"].values)

# listas vacias que se llenan cada vez que corre animate
Xani = []
Yani = []

# Creando el grafico y dandole detalle
fig, ax = plt.subplots()
ax.set_xlim(1990,2022) #lim para que la viste empieze "grande"
ax.set_ylim(0,Yvalues.max())
ax.grid()
ax.set_title("Papers publicados con la keywords 'Cyanobacteria, Uruguay'")
ax.set_xlabel("Año")
ax.set_ylabel("Cantidad de papers")

def animate(frameNumber):
    """Recorro las lista con los datos y los voy a gregando y graficando uno a uno"""   
    Xani.append(Xvalues[frameNumber])
    Yani.append(Yvalues[frameNumber])
    ax.bar(x=Xani, height=Yani, color="#CD0D0C") 
# Funcion que dibuja el grafico animado
paperPerYearAni = ani.FuncAnimation(fig, animate, frames=len(Xvalues), interval=250, repeat=False)

path = r"C:/Users/pedro/Downloads/paperPerYearAni.gif" 
writergif = ani.PillowWriter(fps=5) 
paperPerYearAni.save(path, writer=writergif)

plt.show()