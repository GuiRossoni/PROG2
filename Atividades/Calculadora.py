def menu_principal():
    print("\t----> PROJETO BIMESTRAL - PROGRAMACAO II <----\n")
    NomeUsuario = input("\t POR FAVOR INFORME SEU NOME: \n")
    print("\t BEM VINDO", NomeUsuario)
    print("\t PARA CONTINUAR, ESCOLHA UMA DAS OPCOES A SEGUIR: \n")

    while True:  # MENU PRINCIPAL
        start = input("\tPARA ACESSAR A CALCULADORA CIENTIFICA ----> 1\n"
                      "\tPARA ACESSAR A CALCULADORA FINANCEIRA ----> 2\n"
                      "\tPARA ACESSAR A CALCULADORA HEXADECIMAL ----> 3\n"
                      "\tPARA ACESSAR A CALCULADORA BINARIA ----> 4\n"
                      "\tPARA SAIR DA CALCULADORA ----> SAIR\n")

        if start.upper() == 'SAIR':  # ENCERRA O PROGRAMA
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        elif start == '1':  # MENU CALCULADORA CIENTIFICA
            calculadora_cientifica()

        elif start == '2':  # MENU CALCULADORA FINANCEIRA
            calculadora_financeira()
            
        elif start == '3':  # MENU CALCULADORA HEXADECIMAL
            calculadora_hexadecimal()
        
        elif start == '4':  # MENU CALCULADORA BINARIA
            calculadora_binaria()
        
        else:  # CASO O USUARIO DIGITE UMA OPCAO INVALIDA NO MENU PRINCIPAL
            print("\t OPCAO INVALIDA!!!\n")
            continue

import math

def calculadora_cientifica():
    while True:
        print("\t CALCULADORA CIENTIFICA, ESCOLHA UMA DAS OPCOES A SEGUIR:\n")
        calc_choice = input("\tPARA VOLTAR AO MENU PRINCIPAL ----> 0\n"
                            "\tPARA CALCULOS BASICOS ----> 1\n"
                            "\tPARA CIRCULOS ----> 2\n"
                            "\tPARA EQUACOES DO SEGUNDO GRAU ----> 3\n"
                            "\tPARA POTENCIAIS E RAIZES ----> 4\n"
                            "\tPARA CONVERSOR DE UNIDADE ----> 5\n"
                            "\tPARA GEOMETRIA ----> 6\n"
                            "\tPARA SISTEMAS LINEARES ----> 7\n"
                            "\tPARA DETERMINANTES ----> 8\n"
                            "\tPARA SAIR DA CALCULADORA ----> SAIR\n")

        if calc_choice.upper() == 'SAIR':
            print("\t OBRIGADO POR USAR A CALCULADORA CIENTIFICA!!!\n")
            break

        elif calc_choice == '1':
            operacoes_basicas()

        elif calc_choice == '2':
            calculos_de_circulos()
        
        elif calc_choice == '3':
            equacao_segundo_grau()
        
        elif calc_choice == '4':
            potenciais_e_raizes()
        
        elif calc_choice == '5':
            conversor_de_unidade()
        
        elif calc_choice == '6':
            geometria()
        
        elif calc_choice == '7':
            sistema_linear()
        
        elif calc_choice == '8':
            determinantes()

def calculadora_financeira():
    while True:
        print("\t CALCULADORA FINANCEIRA, ESCOLHA UMA DAS OPCOES A SEGUIR:\n")
        calc_choice = input("\tPARA VOLTAR AO MENU PRINCIPAL ----> 0\n"
                            "\tPARA JUROS SIMPLES ----> 1\n"
                            "\tPARA JUROS COMPOSTOS ----> 2\n"
                            "\tPARA SAIR DA CALCULADORA ----> SAIR\n")

        if calc_choice.upper() == 'SAIR':
            print("\t OBRIGADO POR USAR A CALCULADORA FINANCEIRA!!!\n")
            break

        elif calc_choice == '1':
            juros_simples()

        elif calc_choice == '2':
            juros_compostos()

def calculadora_hexadecimal():
    while True:
        print("\t CALCULADORA HEXADECIMAL, ESCOLHA UMA DAS OPCOES A SEGUIR:\n")
        calc_choice = input("\tPARA CONVERTER HEXADECIMAL PARA BINARIO ----> 1\n"
                            "\tPARA CONVERTER HEXADECIMAL PARA DECIMAL ----> 2\n"
                            "\tPARA CONVERTER DECIMAL PARA HEXADECIMAL ----> 3\n"
                            "\tPARA CALCULAR OPERACOES HEXADECIMAIS ----> 4\n"
                            "\tPARA SAIR DA CALCULADORA ----> SAIR\n")

        if calc_choice.upper() == 'SAIR':
            print("\t OBRIGADO POR USAR A CALCULADORA HEXADECIMAL!!!\n")
            break

        elif calc_choice == '1':
            hexadecimal_para_binario()

        elif calc_choice == '2':
            hexadecimal_para_decimal()
            
        elif calc_choice == '3':
            decimal_para_hexadecimal()
        
        elif calc_choice == '4':
            calcular_operacao_hexadecimal()

def calculadora_binaria():
    while True:
        print("\t CALCULADORA BINARIA, ESCOLHA UMA DAS OPCOES A SEGUIR:\n")
        calc_choice = input("\tPARA CONVERTER DE BINARIO PARA HEXADECIMAL ----> 1\n"
                            "\tPARA CONVERTER DE BINARIO PARA DECIMAL ----> 2\n"
                            "\tPARA CONVERTER DE DECIMAL PARA BINARIO ----> 3\n"
                            "\tPARA CALCULAR OPERACOES BINARIAS ----> 4\n"
                            "\tPARA SAIR DA CALCULADORA ----> SAIR\n")

        if calc_choice.upper() == 'SAIR':
            print("\t OBRIGADO POR USAR A CALCULADORA BINARIA!!!\n")
            break

        elif calc_choice == '1':
            binario_para_hexadecimal()

        elif calc_choice == '2':
            binario_para_decimal()
        
        elif calc_choice == '3':
            decimal_para_binario()
        
        elif calc_choice == '4':
            calcular_operacao_binaria()


def operacoes_basicas():
    print("\t CONTAS BASICAS: \n")
    while True:
        primeiro = input("\t Digite o primeiro numero:\n ")
        segundo = input("\t Digite o segundo numero:\n ")
        operacao = input("\t Digite a operacao (+, -, *, /):\n ")

        if primeiro.replace('.', '', 1).isdigit() and segundo.replace('.', '', 1).isdigit():
            resultado = None

            if operacao in ['+', '-', '*', '/']:
                if operacao == '/' and float(segundo) == 0:
                    print("\t IMPOSSIVEL DIVIDIR POR ZERO!!!")
                else:
                    resultado = eval(primeiro + operacao + segundo)

            else:
                print("\t OPERACAO INVALIDA!!!")

            if resultado is not None:
                print("\t ----> RESULTADO: {0}\n".format(resultado))
                break

        else:
            print("\t ENTRADA INVALIDA! INFORME APENAS NUMEROS INTEIROS E NUMEROS FRACIONADOS COM A UTILIZACAO DE PONTO.")
            continue


def calculos_de_circulos():
    print("\t CIRCULOS: \n")
    while True:
        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPCOES: \n")
        a = input("AREA DO CIRCULO ----> '1'\n"
                  "COMPRIMENTO DO CIRCULO ----> '2'\n"
                  "SAIR ----> 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        elif a == '1':
            calcular_area_circulo()

        elif a == '2':
            calcular_comprimento_circulo()

        else:
            print("\t OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.\n")
            continue
        
def conversor_de_unidade():
    print("\t CONVERSOR DE UNIDADE: \n")
    while True:
        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPCOES: \n")
        a = input("COMPRIMENTO ----> '1'\n"
                  "ÁREA ----> '2'\n"
                  "TEMPERATURA ----> '3'\n"
                  "VOLUME ----> '4'\n"
                  "MASSA ----> '5'\n"
                  "DADOS ----> '6'\n"
                  "SAIR ----> 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        elif a == '1':
            comprimento()

        elif a == '2':
            area()

        elif a == '3':
            temperatura()

        elif a == '4':
            volume()

        elif a == '5':
            massa()

        elif a == '6':
            dados()

        else:
            print("\t OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.\n")
            continue
        
def geometria():
    print("\t GEOMETRIA: \n")
    while True:
        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPCOES: \n")
        a = input("ÁREA DO QUADRADO ----> '1'\n"
                  "ÁREA DO RETÂNGULO ----> '2'\n"
                  "ÁREA DO TRIÂNGULO ----> '3'\n"
                  "ÁREA DO TRAPÉZIO ----> '4'\n"
                  "ÁREA DO CUBO ----> '5'\n"
                  "SAIR ----> 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        elif a == '1':
            area_quadrado()

        elif a == '2':
            area_retangulo()

        elif a == '3':
            area_triangulo()

        elif a == '4':
            area_trapezio()

        elif a == '5':
            area_cubo()

        else:
            print("\t OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.\n")
            continue

def sistema_linear():
    print("\t SISTEMA LINEAR: \n")
    while True:
        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPCOES: \n")
        a = input("SISTEMA LINEAR COM 2 INCOGNITAS ----> '2'\n"
                  "SISTEMA LINEAR COM 3 INCOGNITAS ----> '3'\n"
                  "SISTEMA LINEAR COM 4 INCOGNITAS ----> '4'\n"
                  "SAIR ----> 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        elif a in ['2', '3', '4']:
            calcular_sistema(a)

        else:
            print("\t OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.\n")
            continue

def determinantes():
    print("\t DETERMINANTES: \n")
    while True:
        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPCOES: \n")
        a = input("DETERMINANTE DE UMA MATRIZ DE ORDEM 2 ----> '2'\n"
                  "DETERMINANTE DE UMA MATRIZ DE ORDEM 3 ----> '3'\n"
                  "DETERMINANTE DE UMA MATRIZ DE ORDEM 4 ----> '4'\n"
                  "SAIR ----> 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        elif a in ['2', '3', '4']:
            calcular_determinante(a)

        else:
            print("\t OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.\n")
            continue


def calcular_area_circulo():
    print("\t ÁREA DO CIRCULO: \n")
    pi = 3.14
    r = input("DIGITE O VALOR DO RAIO: ")

    if r.replace('.', '', 1).isdigit():
        resp = (float(r) ** 2) * pi
        print("\t A ÁREA DO CIRCULO é:", resp, "\n")
    else:
        print("\t ENTRADA INVÁLIDA! Digite um número para o raio.")


def calcular_comprimento_circulo():
    print("\t COMPRIMENTO DO CIRCULO: \n")
    pi = 3.14
    r = input("DIGITE O VALOR DO RAIO: ")

    if r.replace('.', '', 1).isdigit():
        resp = 2 * float(r) * pi
        print("\t O COMPRIMENTO DO CIRCULO é:", resp, "\n")
    else:
        print("\t ENTRADA INVÁLIDA! Digite um número para o raio.")


def equacao_segundo_grau():
    print("\t EQUAÇÃO DE SEGUNDO GRAU: \n")

    while True:
        try:
            a = float(input("Digite um valor para a: "))
            b = float(input("Digite um valor para b: "))
            c = float(input("Digite um valor para c: "))

            delta = b * b - 4 * a * c

            if delta < 0:
                print("\t ESTA OPERAÇÃO NÃO POSSUI RAÍZES REAIS\n")
            elif delta == 0:
                raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
                print("\t A EQUAÇÃO POSSUI APENAS UMA RAIZ REAL", raiz)
            elif delta > 0:
                raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
                raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
                print("\t  AS RAÍZES DA EQUAÇÃO SÃO:", raiz1, "E", raiz2)
            break

        except ValueError:
            print("\t VALORES INVÁLIDOS! Por favor, insira apenas números.")
            continue

def potenciacao():
    print("\t POTENCIAÇÃO: \n")
    while True:
        try:
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            
            resultado = base ** expoente
            print(f"\t O resultado da potenciação é: {resultado}\n")
            break
        except ValueError:
            print("\t VALORES INVÁLIDOS! Insira apenas números para a base e o expoente.")
            continue

def radiciacao():
    print("\t RADICIAÇÃO: \n")
    while True:
        try:
            radicando = float(input("Digite o valor para a radiciação: "))
            
            if radicando < 0:
                print("\t Não é possível calcular a raiz de um número negativo.")
            else:
                resultado = math.sqrt(radicando)
                print(f"\t A raiz quadrada de {radicando} é: {resultado}\n")
            break
        except ValueError:
            print("\t VALOR INVÁLIDO! Insira apenas números para o radicando.")
            continue

def potenciais_e_raizes():
    print("\t POTENCIAIS E RAIZES: \n")
    while True:
        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPCOES: \n")
        a = input("POTENCIAÇÃO ----> '1'\n"
                  "RADICIAÇÃO ----> '2'\n"
                  "SAIR ----> 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        elif a == '1':
            potenciacao()

        elif a == '2':
            radiciacao()

        else:
            print("\t OPÇÃO INVÁLIDA! Por favor, escolha uma opção válida.\n")
            continue

def comprimento():
    print("\t COMPRIMENTO: \n")
    while True:
        a = input("M ----> Cm: '1'\n"
                  "M ----> Mm: '2'\n"
                  "Cm ----> M: '3'\n"
                  "Cm ----> mm: '4'\n"
                  "Mm ----> M: '5'\n"
                  "Mm ----> Cm: '6'\n"
                  "SAIR: 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        if a in ['1', '2', '3', '4', '5', '6']:
            
            try:
                
                numero = float(input("Digite o comprimento inicial: "))
                 
                if a == '1':
                    print("\t M ----> CM\n")
                    resp = numero * 100
                    print("O COMPRIMENTO e:", resp)

                elif a == '2':
                    print("\t M ----> MM\n")
                    resp = numero * 1000
                    print("O COMPRIMENTO e:", resp)
                    
                elif a == '3':
                    print("\t CM ----> M\n")
                    resp = numero / 100
                    print("O COMPRIMENTO e:", resp)
                
                elif a == '4':
                    print("\t CM ----> MM\n")
                    resp = numero * 10
                    print("O COMPRIMENTO e:", resp)
                
                elif a == '5':
                    print("\t MM ----> M\n")
                    resp = numero / 1000
                    print("O COMPRIMENTO e:", resp)
                
                elif a == '6':
                    print("\t MM ----> CM\n")
                    resp = numero / 10
                    print("O COMPRIMENTO e:", resp)
                
            except ValueError:
                print("Entrada inválida! Insira um número para o comprimento.")

                
            else:
                print("Opção inválida! Escolha um número de 1 a 6 ou 'n' para sair.")

def area():
    print("\t ÁREA: \n")
    while True:
        b = input("Área do quadrado: 'q'\n"
                  "Área do retângulo: 'r'\n"
                  "Área do triângulo: 't'\n"
                  "Área do trapézio: 'tp'\n"
                  "SAIR: 'n'\n")

        if b == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        if b in ['q', 'r', 't', 'tp']:
            try:
                if b == 'q':
                    print("\t ÁREA DO QUADRADO: \n")
                    lado = float(input("Digite um dos lados do quadrado: "))
                    resp = lado * lado
                    print("A ÁREA DO QUADRADO é:", resp)

                elif b == 'r':
                    print("\t ÁREA DO RETÂNGULO: \n")
                    lado_a = float(input("Digite o lado a do retângulo: "))
                    lado_b = float(input("Digite o lado b do retângulo: "))
                    resp = lado_a * lado_b
                    print("A ÁREA DO RETÂNGULO é:", resp)

                elif b == 't':
                    print("\t ÁREA DO TRIÂNGULO: \n")
                    base = float(input("Digite o valor da base do triângulo: "))
                    altura = float(input("Digite o valor da altura do triângulo: "))
                    resp = (base * altura) / 2
                    print("A ÁREA DO TRIÂNGULO é:", resp)

                elif b == 'tp':
                    print("\t ÁREA DO TRAPÉZIO: \n")
                    base_maior = float(input("Digite o valor da base do trapézio: "))
                    base_menor = float(input("Digite o valor da parte superior do trapézio: "))
                    altura = float(input("Digite o valor da altura do trapézio: "))
                    resp = ((base_maior + base_menor) * altura) / 2
                    print("A ÁREA DO TRAPÉZIO é:", resp)
            except ValueError:
                print("Entrada inválida! Insira um número para os cálculos de área.")
        else:
            print("Opção inválida! Escolha 'q', 'r', 't', 'tp' ou 'n' para sair.")

def temperatura():
    print("\t CONVERSOR DE TEMPERATURA: \n")

    while True:
        t = input("º Celsius ----> ºFahrenheit: '1'\n"
                  "º Celsius ----> Kelvin: '2'\n"
                  "º Fahrenheit ----> ºCelsius: '3'\n"
                  "º Fahrenheit ----> Kelvin: '4'\n"
                  "Kelvin ----> ºCelsius: '5'\n"
                  "Kelvin ----> ºFahrenheit: '6'\n"
                  "SAIR: 'n'\n")

        if t == 'n':
            print(" \t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        if t in ['1', '2', '3', '4', '5', '6']:
            try:
                if t == '1':
                    print("\t ºCelsius ----> ºFahrenheit: \n")
                    celsius = float(input("Digite a temperatura em graus Celsius: "))
                    resp = (celsius * 9 / 5) + 32
                    print("A TEMPERATURA EM ºF é:", resp)

                elif t == '2':
                    print("\t Celsius ----> Kelvin: \n")
                    celsius = float(input("Digite a temperatura em graus Celsius: "))
                    resp = celsius + 273
                    print("A TEMPERATURA EM K é:", resp)

                elif t == '3':
                    print("\t ºFahrenheit ----> ºCelsius: \n")
                    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
                    resp = (fahrenheit - 32) * 5 / 9
                    print("A TEMPERATURA EM ºC é:", resp)

                elif t == '4':
                    print("\t ºFahrenheit ----> Kelvin: \n")
                    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
                    resp = (fahrenheit + 459.67) / 1.8
                    print("A TEMPERATURA EM K é:", resp)

                elif t == '5':
                    print("\t Kelvin ----> ºCelsius: \n")
                    kelvin = float(input("Digite a temperatura em Kelvin: "))
                    resp = kelvin - 273
                    print("A TEMPERATURA EM ºC é:", resp)

                elif t == '6':
                    print("\t Kelvin ----> ºFahrenheit: \n")
                    kelvin = float(input("Digite a temperatura em Kelvin: "))
                    resp = (kelvin * 9 / 5) - 459.67
                    print("A TEMPERATURA EM ºF é:", resp)
            except ValueError:
                print("Entrada inválida! Insira um número para os cálculos de temperatura.")
        else:
            print("Opção inválida! Escolha um número de 1 a 6 ou 'n' para sair.")

def volume():
    print("\t CONVERSOR DE VOLUME: \n")

    while True:
        v = input("Litro ----> mililitro: '1'\n"
                  "Litro ----> Metro cubico: '2'\n"
                  "Litro ----> Centimetro cubico: '3'\n"
                  "Mililitro ----> Litro: '4'\n"
                  "SAIR: 'n'\n")

        if v == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        if v in ['1', '2', '3', '4']:
            try:
                if v == '1':
                    print("\t LITRO ----> MILILITRO: \n")
                    liters = float(input("Digite o volume em litros: "))
                    resp = liters * 1000
                    print("O VOLUME EM ML é:", resp)

                elif v == '2':
                    print("\t LITRO ----> METRO CÚBICO:\n")
                    liters = float(input("Digite o volume em litros: "))
                    resp = liters / 1000
                    print("O VOLUME EM M³ é:", resp)

                elif v == '3':
                    print("\t LITRO ----> CENTÍMETRO CÚBICO: \n")
                    liters = float(input("Digite o volume em litros: "))
                    resp = liters * 1000
                    print("O VOLUME EM CM³ é:", resp)

                elif v == '4':
                    print("\t MILILITRO ----> LITRO: \n")
                    milliliters = float(input("Digite o volume em mililitros: "))
                    resp = milliliters / 1000
                    print("O VOLUME EM L é:", resp)
            except ValueError:
                print("Entrada inválida! Insira um número para os cálculos de volume.")
        else:
            print("Opção inválida! Escolha um número de 1 a 4 ou 'n' para sair.")

def massa():
    print("\t MASSA: \n")

    while True:
        a = input("TONELADAS ----> KG: '1'\n"
                  "TONELADAS ----> G: '2'\n"
                  "TONELADAS ----> MG: '3'\n"
                  "QUILOGRAMAS ----> T: '4'\n"
                  "QUILOGRAMAS ----> G: '5'\n"
                  "QUILOGRAMAS ----> MG: '6'\n"
                  "GRAMAS ----> T: '7'\n"
                  "GRAMAS ----> KG: '8'\n"
                  "GRAMAS ----> MG: '9'\n"
                  "SAIR: 'n'\n")

        if a == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        if a in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            try:
                c = float(input("Digite o valor a ser convertido: "))

                if a == '1':
                    print("\t TONELADA ----> KG:\n")
                    resp = c * 1000
                    print("A MASSA EM KG é:", resp)

                elif a == '2':
                    print("\t TONELADA ----> G: \n")
                    resp = c * 1000000
                    print("A MASSA EM G é:", resp)

                elif a == '3':
                    print("\t TONELADA ----> MG: \n")
                    resp = c * 1000000000
                    print("A MASSA EM MG é:", resp)

                elif a == '4':
                    print("\t QUILOGRAMAS ----> T: \n")
                    resp = c / 1000
                    print("A MASSA EM T é:", resp)

                elif a == '5':
                    print("\t QUILOGRAMAS ----> G: \n")
                    resp = c * 1000
                    print("A MASSA EM G é:", resp)

                elif a == '6':
                    print("\t QUILOGRAMAS ----> MG: \n")
                    resp = c * 1000000
                    print("A MASSA EM MG é:", resp)

                elif a == '7':
                    print("\t GRAMAS ----> T: \n")
                    resp = c / 1000000
                    print("A MASSA EM T é:", resp)

                elif a == '8':
                    print("\t GRAMAS ----> KG: \n")
                    resp = c / 1000
                    print("A MASSA EM KG é:", resp)

                elif a == '9':
                    print("\t GRAMAS ----> MG: \n")
                    resp = c * 1000
                    print("A MASSA EM MG é:", resp)
            except ValueError:
                print("Entrada inválida! Insira um número para os cálculos de massa.")
        else:
            print("Opção inválida! Escolha um número de 1 a 9 ou 'n' para sair.")

def dados():
    print("\t DADOS: \n")

    while True:
        d = input("BIT ----> BYTE: '1'\n"
                  "BYTE ----> MEGABYTE: '2'\n"
                  "BYTE ----> GIGABYTE: '3'\n"
                  "MEGABYTE ----> BYTE: '4'\n"
                  "MEGABYTE ----> GIGABYTE: '5'\n"
                  "MEGABYTE ----> TERABYTE: '6'\n"
                  "GIGABYTE ----> BYTE: '7'\n"
                  "GIGABYTE ----> MEGABYTE: '8'\n"
                  "GIGABYTE ----> TERABYTE: '9'\n"
                  "TERABYTE ----> MEGABYTE: '10'\n"
                  "TERABYTE ----> GIGABYTE: '11'\n"
                  "SAIR: 'n'\n")

        if d == 'n':
            print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
            break

        if d in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            try:
                a = float(input("DIGITE O VALOR A SER CONVERTIDO: "))
                
                if d == '1':
                    print("\t BIT ----> BYTE: \n")
                    resp = a * 0.125
                    print("OS DADOS EM BYTES SÃO:", resp)
                elif d == '2':
                    print("\t BYTE ----> MEGABYTE: \n")
                    resp = a / 1000000
                    print("OS DADOS EM MEGABYTES SÃO:", resp)
                elif d == '3':
                    print("\t BYTE ----> GIGABYTE: \n")
                    resp = a / 1000000000
                    print("OS DADOS EM GIGABYTES SÃO:", resp)
                elif d == '4':
                    print('\t MEGABYTE ----> BYTE: \n')
                    resp = a * 1000000
                    print("OS DADOS EM BYTES SÃO: ", resp)
                elif d == '5':
                    print("\t MEGABYTE ----> GIGABYTE: \n")
                    resp = a / 1000
                    print("OS DADOS EM GIGABYTES SÃO:", resp)
                elif d == '6':
                    print("\t MEGABYTE ----> TERABYTE: \n")
                    resp = a / 1000000
                    print("OS DADOS EM TERABYTES SÃO:", resp)
                elif d == '7':
                    print("\t GIGABYTE ----> BYTE: \n")
                    resp = a * 1000000000
                    print("OS DADOS EM BYTES SÃO:", resp)
                elif d == '8':
                    print("\t GIGABYTE ----> MEGABYTE: \n")
                    resp = a * 1000
                    print("OS DADOS EM MEGABYTES SÃO:", resp)
                elif d == '9':
                    print("\t GIGABYTE ----> TERABYTE: \n")
                    resp = a / 1000
                    print("OS DADOS EM TERABYTES SÃO:", resp)
                elif d == '10':
                    print("\t TERABYTE ----> MEGABYTE: \n")
                    resp = a * 1000000
                    print("OS DADOS EM MEGABYTES SÃO:", resp)
                elif d == '11':
                    print('\t TERABYTE ----> GIGABYTE: \n')
                    resp = a * 1000
                    print("OS DADOS EM GIGABYTES SÃO:", resp)
            except ValueError:
                print("Entrada inválida! Insira um número para os cálculos de dados.")
        else:
            print("Opção inválida! Escolha um número de 1 a 11 ou 'n' para sair.")

def area_quadrado():
    lado = input("Digite o valor de um dos lados do quadrado: ")
    if not lado.isdigit():
        print("Por favor, insira um número válido.")
        return

    resp = float(lado) ** 2
    print("A área do quadrado é:", resp)

def area_retangulo():
    base = input("Digite o valor da base do retângulo: ")
    altura = input("Digite o valor da altura do retângulo: ")

    if not (base.isdigit() and altura.isdigit()):
        print("Por favor, insira números válidos.")
        return

    resp = float(base) * float(altura)
    print("A área do retângulo é:", resp)

def area_triangulo():
    base = input("Digite o valor da base do triângulo: ")
    altura = input("Digite o valor da altura do triângulo: ")

    if not (base.isdigit() and altura.isdigit()):
        print("Por favor, insira números válidos.")
        return

    resp = (float(base) * float(altura)) / 2
    print("A área do triângulo é:", resp)

def area_trapezio():
    base_maior = input("Digite o valor da base maior do trapézio: ")
    base_menor = input("Digite o valor da base menor do trapézio: ")
    altura = input("Digite o valor da altura do trapézio: ")

    if not (base_maior.isdigit() and base_menor.isdigit() and altura.isdigit()):
        print("Por favor, insira números válidos.")
        return

    resp = ((float(base_maior) + float(base_menor)) * float(altura)) / 2
    print("A área do trapézio é:", resp)

def area_cubo():
    lado = input("Digite o valor do lado do cubo: ")

    if not lado.isdigit():
        print("Por favor, insira um número válido.")
        return

    resp = float(lado) ** 2
    print("A área do cubo é:", resp * 6)
    
def resolver_sistema_linear(incognitas):
    print(f"\nResolvendo sistema linear com {incognitas} incógnitas.")

    coeficientes = []
    for i in range(incognitas):
        print(f"Equação {i+1}")
        coefs = []
        for j in range(incognitas + 1):
            coef = input(f"Insira o valor do coeficiente {j + 1} para a equação {i + 1}: ")
            coefs.append(coef)
        coeficientes.append(coefs)

    # Verificando se todas as entradas são números
    try:
        coeficientes = [[float(coef) for coef in eq] for eq in coeficientes]
    except ValueError:
        print("Por favor, insira apenas valores numéricos.")
        return

    # Realizando os cálculos do sistema linear
    # ... Cálculos para 2, 3 e 4 incógnitas

    # Exemplo de resolução de sistemas de 2, 3 e 4 incógnitas
    if incognitas == 2:
        # Realizar cálculos para 2 incógnitas
        pass
    elif incognitas == 3:
        # Realizar cálculos para 3 incógnitas
        pass
    elif incognitas == 4:
        # Realizar cálculos para 4 incógnitas
        pass

    print("Sistema linear resolvido com sucesso.")

# Função para calcular o sistema linear
def calcular_sistema(opcao):
    if opcao in ['2', '3', '4']:
        resolver_sistema_linear(int(opcao))
    elif opcao == 'n':
        print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
    else:
        print("Opção inválida! Escolha 2, 3 ou 4 para resolver um sistema linear ou 'n' para sair.")

def calcular_determinante(ordem):
    print(f"\nCalculando o determinante de uma matriz de ordem {ordem}.")

    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            elem = input(f"Insira o elemento [{i+1}][{j+1}]: ")
            linha.append(elem)
        matriz.append(linha)

    # Verificando se todas as entradas são números
    try:
        matriz = [[float(elem) for elem in linha] for linha in matriz]
    except ValueError:
        print("Por favor, insira apenas valores numéricos.")
        return

    # Cálculo do determinante para matrizes de 2, 3 e 4 ordens
    if ordem == 2:
        det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif ordem == 3:
        a, b, c = matriz
        det = a[0] * b[1] * c[2] + a[1] * b[2] * c[0] + a[2] * b[0] * c[1]
        det -= a[2] * b[1] * c[0] + a[0] * b[1] * c[2] + a[1] * b[0] * c[2]
    elif ordem == 4:
        a, b, c, d = matriz
        det = (
            a[0] * b[1] * c[2] * d[3] + a[1] * b[2] * c[3] * d[0] + a[2] * b[3] * c[0] * d[1] +
            a[3] * b[0] * c[1] * d[2] - a[3] * b[2] * c[1] * d[0] - a[0] * b[1] * c[2] * d[3] -
            a[1] * b[3] * c[0] * d[2] - a[2] * b[0] * c[3] * d[1]
        )
    else:
        det = "Determinante disponível para matrizes de 2, 3 ou 4 ordens."

    print(f"O determinante é: {det}")

def calcular_determinante_matriz(opcao):
    if opcao in ['2', '3', '4']:
        calcular_determinante(int(opcao))
    elif opcao == 'n':
        print("\t OBRIGADO POR USAR NOSSA CALCULADORA!!!\n")
    else:
        print("Opção inválida! Escolha 2, 3 ou 4 para calcular o determinante ou 'n' para sair.")

def soma_binaria(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

def subtracao_binaria(a, b):
    return bin(int(a, 2) - int(b, 2))[2:]

def multiplicacao_binaria(a, b):
    return bin(int(a, 2) * int(b, 2))[2:]

def divisao_binaria(a, b):
    try:
        result = int(a, 2) // int(b, 2)
        return bin(result)[2:]
    except ZeroDivisionError:
        return "Não é possível dividir por zero."

def operacao_binaria(operador, a, b):
    if operador == '+':
        return soma_binaria(a, b)
    elif operador == '-':
        return subtracao_binaria(a, b)
    elif operador == '*':
        return multiplicacao_binaria(a, b)
    elif operador == '/':
        return divisao_binaria(a, b)
    else:
        return "Operação inválida."

def calcular_operacao_binaria():

    num1 = input("Insira o primeiro número binário: ")
    num2 = input("Insira o segundo número binário: ")
    operacao = input("Escolha a operação (+, -, *, /): ")

    # Verificando se as entradas são válidas (apenas 0s e 1s)
    if not all(char in '01' for char in num1) or not all(char in '01' for char in num2):
        print("Por favor, insira apenas números binários (0s e 1s).")
        return

    resultado = operacao_binaria(operacao, num1, num2)
    print(f"Resultado: {resultado}")
    
def binario_para_hexadecimal(numero_binario):
    if not all(char in '01' for char in numero_binario):
        return "Entrada inválida. Insira apenas números binários (0s e 1s)."

    decimal = int(numero_binario, 2)
    hexadecimal = hex(decimal).upper()[2:]  # [2:] remove o prefixo '0x'

    return hexadecimal

def binario_para_decimal(numero_binario):
    if not set(numero_binario).issubset({'0', '1'}):
        return "Entrada inválida. Insira apenas números binários (0 ou 1)."

    decimal = int(numero_binario, 2)
    return decimal

def decimal_para_binario(numero_decimal):
    try:
        numero_decimal = int(numero_decimal)
        if numero_decimal < 0:
            return "Número inválido. Insira um número positivo."

        binario = bin(numero_decimal)[2:]
        return binario
    except ValueError:
        return "Entrada inválida. Insira um número inteiro."

def hexadecimal_para_binario(numero_hex):
    try:
        numero_binario = bin(int(numero_hex, 16))[2:]
        return numero_binario
    except ValueError:
        return "Entrada inválida. Insira um número hexadecimal válido."
    
def hexadecimal_para_decimal(numero_hex):
    try:
        numero_decimal = int(numero_hex, 16)
        return numero_decimal
    except ValueError:
        return "Entrada inválida. Insira um número hexadecimal válido."

def decimal_para_hexadecimal(numero_decimal):
    try:
        numero_hex = hex(numero_decimal)
        return numero_hex
    except ValueError:
        return "Entrada inválida. Insira um número decimal válido."

def soma_hexadecimal(a, b):
    return hex(int(a, 16) + int(b, 16))[2:]

def subtracao_hexadecimal(a, b):
    return hex(int(a, 16) - int(b, 16))[2:]

def multiplicacao_hexadecimal(a, b):
    return hex(int(a, 16) * int(b, 16))[2:]

def divisao_hexadecimal(a, b):
    try:
        result = int(a, 16) // int(b, 16)
        return hex(result)[2:]
    except ZeroDivisionError:
        return "Não é possível dividir por zero."

def operacao_hexadecimal(operador, a, b):
    if operador == '+':
        return soma_hexadecimal(a, b)
    elif operador == '-':
        return subtracao_hexadecimal(a, b)
    elif operador == '*':
        return multiplicacao_hexadecimal(a, b)
    elif operador == '/':
        return divisao_hexadecimal(a, b)
    else:
        return "Operação inválida."

def calcular_operacao_hexadecimal():
    operacao = input("Escolha a operação (+, -, *, /): ")
    num1 = input("Insira o primeiro número hexadecimal: ")
    num2 = input("Insira o segundo número hexadecimal: ")

    # Verificando se as entradas são válidas (apenas dígitos hexadecimais)
    if not all(char in '0123456789abcdefABCDEF' for char in num1) or not all(char in '0123456789abcdefABCDEF' for char in num2):
        print("Por favor, insira apenas números hexadecimais (0-9, a-f ou A-F).")
        return

    resultado = operacao_hexadecimal(operacao, num1, num2)
    print(f"Resultado: {resultado}")


# Chamada principal para o menu
menu_principal()
