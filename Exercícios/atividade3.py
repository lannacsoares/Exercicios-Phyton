# 1. Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
# A quantidade de valores digitados;
# A soma dos valores digitados;
# A média aritmética dos valores digitados;
# E a quantidade de valores digitados maior que 20.

ct2= 0 
ct = 0 
soma = 0 
print("Digite [-1] para sair")
while True: 
    val= float(input("Digite um valor: "))
    if val == -1: 
        break 
    ct = ct +1
    if val>20: 
        ct2 = ct2 + 1
    soma= soma + val 
    media= soma/ct 

print(f"A quantidade de números digitados é: {ct}")
print(f"A soma de valores digitados é: {soma:.2f}")
print(f"A média aritmética dos valores digitados é: {media:.2f}")
print(f"A quantidade dde valores digitados maior que 20: {ct2} ")
    
# 2. Implemente o programa que leia a nota de vários alunos de uma turma e gere uma tela de saída com as seguintes informações: a quantidade de alunos aprovados,
# a quantidade de alunos reprovados e a quantidade de alunos que fizeram a prova. Considere que o aluno será aprovado com nota for maior ou igual a cinco.

ct_alunos_aprovados= 0
ct_alunos_reprovados = 0
ct_geral= 0 
print("Digite [-1] para sair")
materia = input("Digite o nome da matéria: ")
while True:
    nota= float(input(f"Digite a sua nota em {materia}:  "))
    if nota == -1: 
        break 
    ct_geral = ct_geral + 1 
    if nota>=5: 
        ct_alunos_aprovados = ct_alunos_aprovados + 1
    elif nota<5:
        ct_alunos_reprovados= ct_alunos_reprovados + 1
    else:
        print("A nota digitada não é válida")

print(f"A qntd de alunos aprovados: {ct_alunos_aprovados} ")
print(f"A qntd de alunos reprovados: {ct_alunos_reprovados}")
print(f"A qntd de alunos que fizeram a prova: {ct_geral}")

# 3. Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos números ímpares. O usuário fornecerá os valores de entrada que 
# pode ser um número qualquer par ou ímpar. A condição de saída será o número 0 (zero).

ct_impar =0
ct_par = 0 
ct_geral = 0 
soma_par = 0
soma_impar=0
print("Digite [0] para sair")
while True: 
    ct_geral = ct_geral + 1 
    num= int(input("Digite um número: "))
    if num == 0:
        break 
    if num % 2 == 0:
        ct_par = ct_par + 1
        soma_par = soma_par + num
    if num % 2 != 0: 
        ct_impar = ct_impar + 1
        soma_impar = soma_impar + num
media_par = soma_par / ct_par
media_impar = soma_impar / ct_impar
print(f"A media aritmética é: {media_par}")
print(f"A media aritmética é: {media_impar}")
print(f"A qntd de números contados pares é: {ct_par}")
print(f"A qntd de números contados ímpares é: {ct_impar}")
print(f"A quantidade total de números digitados é: {ct_geral}")

