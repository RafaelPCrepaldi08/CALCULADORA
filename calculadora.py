numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha uma operação: ")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

operacao = input("Digite o número da operação desejada: ")

if operacao == "1":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "2":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "3":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "4":
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado}")