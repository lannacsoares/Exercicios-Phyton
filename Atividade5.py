#1. A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo. Calcule a conversão e construa o relatório de saída tabular (em forma de tabela de duas colunas) de graus Celsius em função de graus Fahrenheit que que variam de 45 a 80 de 1 em 1.            
# Fórmula: c = 5 ( f - 32 )
#                       9
# Fahreinheit | Celsius           (Layout de saída)
#     45.0 ºF | 7.222 ºC
#     46.0 ºF | 7.778 ºC
#     47.0 ºF | 8.333 ºC
#     48.0 ºF | 8.889 ºC
#     49.0 ºF | 9.444 ºC
#     50.0 ºF | 10.000 ºC
#     51.0 ºF | 10.556 ºC
#     ...
#     80.0 ºF | 26.667 ºC                 
print("Fahrenheit", "|" , "Celsius")               

for fahrenheit in range (45,81,1):
    celsius= 5/9 * (fahrenheit - 32)
    print (fahrenheit, "        |" , f"{celsius:.2f}")
  
# 2. Melhore o programa anterior para torná-lo mais abrangente. Agora, o usuário fornecerá os valores inicial e final de graus Fahrenheit. Calcule a conversão e gere o relatório de saída tabular (em forma de tabela) considerando o intervalo digitado. 
# Gere o relatório na ordem crescente, se o valor inicial for menor ou igual ao valor final. E na ordem decrescente, se valor inicial for maior que o valor final.
a= int(input("Digite o valor inicial da temperatura em fahrenheit: "))
b= int(input("Digite o valor final da temperatura em fahrenheit: "))
if a<=b:
    for fahrenheit in range (a,b,1):
        celsius= 5/9 * (fahrenheit - 32)
        print (fahrenheit, "        |" , f"{celsius:.2f}")
elif a==b:
    print("Os valores são iguais!")
else:
    for fahrenheit in range (a,b-1,-1):
        celsius= 5/9 * (fahrenheit - 32)
        print (fahrenheit, "        |" , f"{celsius:.2f}") 
      
# 3. Elabore o programa para somar todos os números inteiros que se encontram no intervalo de um a quinhentos.

# 4. Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.

# 5. Elabore o programa que imprima a tabuada de multiplicação do número cinco de um até dez. Gere o seguinte layout:                           
# 1  x  5  =    5
# 10	x  5  =  50

# 6. Vamos tornar o programa anterior mais interessante. Agora, o programa deve gerar a tabuada de multiplicação de um número inteiro qualquer fornecido pelo usuário.
