from numpy import *
import pandas as pd


class Almacen:
    global df

    def afegirBeguda(self, bebida):
        to_append = bebida
        df = pd.DataFrame(to_append, columns=['ID','Columna', 'Marca', 'Preu', 'Litros', 'Origen', 'Promo', 'Azúcar'])
        #print(df)
        df.to_pickle("./dummy.pkl")

    def calcularPrecioTotal(self):
        dataf = pd.read_pickle("./dummy.pkl")
        Total = dataf['Preu'].sum()
        return str(Total)

    def calcularPrecioMarca(self, marca):
        dataf = pd.read_pickle("./dummy.pkl")
        total = dataf.loc[dataf['Marca'] == marca, 'Preu'].sum()
        return str(total)

    def calcularPrecioColumna(self, columna):
        dataf = pd.read_pickle("./dummy.pkl")
        total = dataf.loc[dataf['Columna'] == columna, 'Preu'].sum()
        return str(total)

    def eliminarBebida(self, id):
        dataf = pd.read_pickle("./dummy.pkl")
        indexID = dataf[dataf['ID'] == id ].index
        dataf.drop(indexID, inplace=True)
        dataf.to_pickle("./dummy.pkl")


    def mostrarEstanteria(self):
        unpickled_df = pd.read_pickle("./dummy.pkl")
        print(unpickled_df)
