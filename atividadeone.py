# Calculando Bhaskara

print("y = a * x² + b * x + c")

a = int(input("Digite um número: ")) # Termo que acompanha o x^2
b = int(input("Digite um número: ")) # Termo que acompanha o x
c = int(input("Digite um número: ")) # Termo linear c

# Escreve no terminal as constantes da equação
print("y =", a, "* x² +", b,"* +", c)

# Cálculo do delta
delta = b**2 - 4 * a * c

# Escrevendo o valor de delta para o usuário (boa prática)
print("delta = " + str(delta))

# Condicional que checa se o valor de delta calculado é menor que zero 
# Equivale a um se
if (delta < 0):
    print("A equação não tem raiz real...")

# Equivale a um se não
else:
    x1 = (-b + (delta**(1/2)))/2*a # checar se precisa dos últimos parênteses
    x2 = (-b - (delta**(1/2)))/2*a

    # Escreve na tela as raízes x1 e x2
    print("As raízes são:", x1, "e", x2)

# se for igual a zero, calcular apenas uma raiz
'''
comentário de bloco
'''

# Código extra de verificação de primos 
# Pergunta ao usuário se ele quer saber se os números são primos
print("Você gostaria de saber se os números são primos? Digite com S para sim ou N para não.")
resposta = input()

# Escreve na tela a definição de números primos
print ("Um número é classificado como primo se ele é maior do que um e é divisível apenas por um e por ele mesmo")

# Função que verifica se um número é primo
def primos(n):

    # 0 e 1 não são primos por definição
    if n <= 1:
        return False

    # Verifica se n é divisível por algum número entre 2 e (n-1). 
    # Se testássemos até n, o número n sempre seria divisível por ele mesmo. Todo número é divisível por si mesmo.
    for i in range(2, n-1):
        if n % i == 0:
            return False

    # Se não for divisível por nenhum número, é primo
    return True

# Verifica se o usuário quer saber se os números são primos
if resposta == "S":
    print("Os números:", a, b, c, "que você inseriu são respectivamente:")
    
    for numero in [a, b, c]:
        if primos(numero):
            print(numero, "é primo")
        else:
            print(numero, "não é primo")
else:
    print("Você é realmente muito chato...")





 
