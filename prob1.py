import re

class cuenta():

    def usuario():
        while True:
            num = input("ingrese usuario de banco")
            if re.match(r'^[0-9]{8}$', num):
                return int(num)
            print('se necesitan ocho caracteres')

    def cbanco():
        while True:
            cuenban = input("ingrese cuenta de banco")
            if re.match(r'^[0-9]{8}$', cuenban):
                return int(cuenban)
            print('se necesitan ocho caracteres')
    
    ## Me habia confundiod y para cuando me di cuenta tenia que rehacer todo, nimodo hahah


