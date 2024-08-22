#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora (opcao, num1, num2):
    if ((opcao <1) or (opcao>4)):
        return "Opcão invalida"
    
    match opcao:
        case 1:
            resultado = num1+num2
        case 2:
            resultado = num1-num2
        case 3:
            resultado = num1*num2
        case 4:
            resultado = num1/num2
    return resultado


opcao = int(input("Escolha uma da opções:1.Soma | 2.Subtração | 3.Multiplicação | 4.Divisão: "))        
num1 = int(input("Entre com o valor do primeiro numero: "))
num2 = int(input("Entre com o valor do segundo numero: "))

resultado= calculadora(opcao, num1, num2)

print(f"O resultado da sua operação é:{resultado}")