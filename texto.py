#Declaração

print("\n")
print("Texto simples:")
nome_completo = "Lucas Carvalho"
print(nome_completo)

print("\n")

print("Texto saltando linha:")
nome_completo_aspas = """Lucas 
Carvalho
"""
print(nome_completo_aspas)

print("Texto pulando linha somente no código:")
nome_completo_quebra = "Lucas \
Carvalho"
print(nome_completo_quebra)

print("\n")


""" Formatação
Utilizando o símbolo "+", podemos verificar que, não existe espaço para separar nome e sobrenome
 Exemplo: 
        print("Concatenando Nome + Sobreno: ", nome + sobrenome)

Utilizando o símbolo ",", podemos verificar que existe espaço para separar nome e sobrenome
        print("Concatenando Nome , Sobreno: ", nome, sobrenome)


"""
print("Concatenando duas variáveis: ")
nome = "Lucas"
sobrenome = "Carvalho"

print("1 - Concatenando Nome '+' Sobreno:", nome + sobrenome)
print("2 - Concatenando Nome ',' Sobreno:", nome, sobrenome)
print("3 - Concatenando Nome '+/,' Sobreno:"+ nome, sobrenome)
print("4 - Concatenando Nome e sobrenome: %s" % nome_completo)
print("5 - Concatenando Nome e sobrenome: %s %s" % (nome, sobrenome))
print(f"6 - Concatenando Nome e sobrenome 'f no início + chave': {nome} {sobrenome}")
print("6 - Concatenando Nome e sobrenome 'format': {} {}".format(nome, sobrenome))

