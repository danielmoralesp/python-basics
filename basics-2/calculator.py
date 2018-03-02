# -*- coding: utf8 -*-

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount


def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte PMX a COP')
    print('')

    ammount = float(raw_input('Ingresa la cantidad de PMX que quieres convertir'))

    result = foreign_exchange_calculator(ammount)

    print('${} PMX son ${} COP'.format(ammount, result))
    print('')


if __name__ == '__main__':
    run()
