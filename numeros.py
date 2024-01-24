""" Número -> Inteiro
        Exemplo: numero_inteiro = 3

    Número -> Real com ponto flutuante
                 numero_real = 3.14
"""
print("\n")
print("Trabalhando com números ⮕")
numero_inteiro = 3

print("Número Inteiro = ", numero_inteiro)
numero_real = 3.14
print("Número real com ponto flutuante", numero_real)

print("\n")

"""
Função Type()
. print ("Tipo da variável de nome 'numero_inteiro': ", type(numero_inteiro)) -> <class 'int'>

. print ("Tipo da variável de nome 'numero_real': ", type(numero_real)) -> Real com ponto flutuante <class 'float'>
"""
print ("Type/Tipo das variáveis ⮕")
print ("Tipo da variável de nome 'numero_inteiro': ", type(numero_inteiro))
print ("Tipo da variável de nome 'numero_real': ", type(numero_real))


print("\n")

"""
Operações Aritméticas 
"""
print("Operações aritméticas ⮕")

soma = 1+1
print("O resutlado da soma eh:", soma)

subtracao = 2-1
print("O resutlado da subtração eh:", subtracao)

multiplicacao = 1*12
print("O resultado da multiplicação eh:", multiplicacao)

"""Na divisão sempre é retornado um valor do tipo float, por insso deve utilizar a conversão "int"
        Para já retornar resultado inteiro, deve-se utilizar // na divisão.

    Exemplo:
"""

divisao = 12/2
print("O resultado da divisão eh:", divisao)
print("Valor em inteiro", int(divisao))

# Modulo ⮕ Utilizado para mostrar o restante da divisão

modulo = 5 % 2

print("Resultado da divisão ou (Modulo), eh:", modulo)