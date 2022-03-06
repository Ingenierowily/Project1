from inspect import classify_class_attrs
from pydoc import cli


def run():
    ciclo = 'y'
    inventario = {
                'tornillos': 100,
                'tuercas': 200,
                'lijas': 210
                }
    
    while ciclo == 'y':
        articulo = input('Que articulo desea conocer del inventario: ')
        articulo = articulo.lower()
        numero = inventario.get(articulo, 0)
        print('En inventario tenemos {} {}'.format(numero, articulo))
        ciclo2 = 1
        while ciclo2 == 1:
            ciclo = input('Deseas revisar otro articulo, Yes(y), No(n): ')
            ciclo = ciclo.lower()
            if ciclo == 'y' or ciclo == 'n':
                ciclo2 = 0
            else:
                ciclo2 = 1
    
    print('Hasta la proxima ')
    print('fin del programa')

if __name__ == '__main__':
    run()