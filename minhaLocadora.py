import os
import time
import sys

cars_list = [
    ("Chevrolet Opala", 100),
    ("Dodge Dart", 120),
    ("Volkswagen Fusca", 45),
    ("Ford Escort", 70),
]

rental_cars = []

def print_cars(list_cars):
    print("")
    for i, car in enumerate(list_cars):
        print(f"{i} | {car[0]} - R${car[1]}")

def get_out():
    os.system("cls")
    print("Obrigado por utilizar a locadora!")
    time.sleep(2)
    sys.exit()
    
welcome = 0

while True:
    os.system("cls")

    if welcome == 0:
        print("Bem-vindo à Locadora de Carros")
        print("")
    
    print("1 - Mostrar portifólio | 2 - Alugar um carro | 3 - Devolver um carro | 4 - Sair")
    print("")
    op = int(input("Escolha: "))

    if op == 1:
        os.system("cls")
        print("Carros de nosso portifólio:")
        print_cars(cars_list + rental_cars)
    
    elif op == 2:
        os.system("cls")

        if len(cars_list) != 0:
            print("Carros disponíveis:")
            print_cars(cars_list)

            print("")
            code = int(input("Digite o código do carro escolhido: "))
            days = int(input("Digite a quantidades de dias que ficará com o carro: "))

            os.system("cls")
            print(f"Você escolheu o {cars_list[code][0]} por {days} dias, totalizando R${(cars_list[code][1])*days}. Deseja alugar?")
            print("")
            print("1 - Sim | 2 - Não")
            print("")
            op = int(input("Escolha: "))

            if op == 1:
                rental_cars.append(cars_list.pop(code))
                os.system("cls")
                print("Carro alugado!")
                
            else:
                os.system("cls")
        else:
            print("Nenhum carro disponível!")

    elif op == 3:
        os.system("cls")

        if len(rental_cars) != 0:
            print("Carros para devolução:")
            print_cars(rental_cars)

            print("")
            code = int(input("Digite o código do carro que deseja devolver: "))

            os.system("cls")
            print(f"Devolver {rental_cars[code][0]}?")
            print("")
            print("1 - Sim | 2 - Não")
            print("")
            op = int(input("Escolha: "))

            if op == 1:
                cars_list.append(rental_cars.pop(code))
                os.system("cls")
                print("Carro devolvido!")

        else:
            print("Nenhum carro foi alugado!")

    if op == 4:
        get_out()
    
    print("")
    print("1 - Continuar para o Menu | 2 - Sair")
    print("")
    op = int(input("Escolha: "))

    if op == 2:
        get_out()