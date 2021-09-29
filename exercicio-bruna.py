# Questão 1
# nota1, nota2 = float(input("Insira a nota1: ")), float(input("Insira a nota2: "))
# print(f"A nota1 é {nota1}, a nota dois é {nota2} e a média é {(nota1 + nota2)/2}.")

# Questão 2
# numero = int(input("Insira um número: "))
# if numero < 0:
#     print(numero, "é negativo.")
# elif numero == 0:
#     print(numero, "é neutro.")
# elif numero > 0:
#     print(numero, "é positivo.")

# #Questão 3
# senha = input("Insira uma senha: ")
# confirmacao = input("Confirme a senha: ")

# while senha != confirmacao: 
#     senha = input("Insira uma senha: ")
#     confirmacao = input("Confirme a senha: ")
# else: 
#     print("Cadastro realizado!")

# numero = int(input("Insira um número: "))
# n = 1
# while n <= 10:
#     print(f"{numero} x {n} = {numero * n}")
#     n += 1

# numero = int(input("Insira um número: "))
# if numero >=1:
#     for n in range(numero, numero + 10):
#         print(2 * n - 3)


# numero = int(input("Insira um número: "))
# lista = [1,2,3,4,5]
# for n in range(1,numero + 1):
#     lista.append(n)
# print(lista)
# print(sum(lista))

salario = float(input("Insira o valor do seu salário: "))
if salario < 700:
    salario = salario * 1.12
elif salario < 1200:
    salario = salario * 1.1
else: 
    salario = salario * 1.05

print("Seu salário com reajuste é ",salario)