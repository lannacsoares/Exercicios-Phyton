# # 1.  Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário. 
num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
if num1>num2:
    print(num2, num1)
else: 
    print(num1, num2)

# 2- Elabore o programa que selecione o maior valor de três valores fornecidos pelo usuário. Resolva sem usar operador lógico (e, ou, não).
num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
num3=int(input("Digite um número: "))
if num1>num2: 
    if num1>num3: 
        print(num1)
if num2>num1: 
    if num2>num3: 
        print(num2)
if num3>num1: 
    if num3>num2: 
        print(num3)

# 3- Refaça o exercício anterior utilizando também operador lógico (e, ou, não). 
num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
num3=int(input("Digite um número: "))
if num1>num2 and num1>num3: 
    print(num1)
if num2>num1 and num2>num3: 
    print(num2)
if num3>num2 and num3>num1: 
    print(num3)

# 4- Elabore o programa que simule a calculadora com as quatro operações aritméticas básicas.
# O usuário fornecerá dois números e a operação aritmética desejada.
# Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética. Utilize o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado. 
num1= float(input("Digite um núemro: "))
num2= float(input("Digite um núemro: "))
operacao= input("Digite uma operação (+, - *, /): ")
if (operacao) == "+":
    soma= num1+num2
    print (soma)
elif (operacao) == "-": 
    subtracao= num1-num2
    print (subtracao)
elif (operacao) == "*": 
    mutiplicacao= num1*num2
    print (mutiplicacao)
elif (operacao) == "/": 
    divisao= num1/num2
    print(f"{divisao:.2f}")

# 5- Dado o comprimento das três retas a, b e c. Verifique se eles podem ser o comprimento dos lados de um triângulo. Se forem, verifique se compõem um triângulo equilátero, isósceles ou escaleno. Informe se não compuserem nenhum triângulo. Relembre as seguintes definições:
# - No plano, triângulo (também aceito como trilátero) é a figura geométrica que ocupa o espaço interno limitado por três linhas retas que concorrem, duas a duas, em três pontos diferentes formando três lados e três ângulos internos. Para ser triângulo, qualquer lado tem medida menor que a soma das medidas dos outros dois lados.
# - Triângulo equilátero: possui três lados iguais;
# - Triângulo isósceles: possui dois lados iguais;
# - Triângulo escaleno: tem todos os lados diferentes.

# Obs.: verifique primeiro se os lados formam um triângulo

# Teste 1: Entrada: 1, 2 e 3   Resposta: Não é um triângulo.
# Teste 2: Entrada: 2, 3 e 4   Resposta: É um triângulo escaleno.
# Teste 3: Entrada: 3, 3 e 3   Resposta: É um triângulo equilátero.
# Teste 4: Entrada: 2, 3 e 3   Resposta: É um triângulo isósceles.

ladoA= int(input("Digite o valor do lado A: "))
ladoB= int(input("Digite o valor do lado B: "))
ladoC= int(input("Digite o valor do lado C: "))

if ladoA<(ladoB+ladoC) and ladoB<(ladoA+ladoC) and ladoC<(ladoB+ladoA):
    print("Os valores das retas podem formar um triângulo.")
else: 
    print("Os valores não podem formar um triângulo. ")

if ladoA==ladoB==ladoC:
    print("O triângulo é equilátero. ")
elif ladoA==ladoB or ladoB==ladoC or ladoC==ladoA: 
    print("O triângulo é isósceles. ")
elif ladoA!=ladoB!=ladoC:
    print("O triângulo é escaleno. ")
