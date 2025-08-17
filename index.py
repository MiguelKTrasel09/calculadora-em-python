def calculate():
    operation = input('''
por favor, coloque a operação matematica que voce quer:
+ para adição
- para subtração
* paramultiplicação
/ para divisão
''')
    number_1 = int(input( 'coloque um numero:'))
    number_2 = int(input('coloque o segundo numero:'))
        #adição
    if operation == '+' :
        print(' {} + {} =' .format(number_1, number_2))
        print(number_1+number_2)

    #subtração
    elif operation == '-':
        print('{} - {}=' .format(number_1,number_2))
        print(number_1-number_2)

    #multiplicação
    elif operation == '*':
        print('{}*{}=' .format(number_1,number_2))
        print(number_1*number_2)

    #divisão
    elif operation == '/':
        print('{} / {}=' .format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('voce nao colocou um operador valido, rode o programa novamente')

    again ()

def again ():
    calc_again = input('''
                       quer calcular denovo?
                     aperte S para SIM e N para NÃO
                           '''   )
    if calc_again.upper() == 'S':
         calculate()

    elif calc_again.upper() == 'N':
        print(' te vejo outra hora')

    else:
        again ()

calculate()