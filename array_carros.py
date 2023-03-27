#Declarando array de carros°
car_array = [];
#Validate option for choise
options = ['1','2','3','4','0'];
#import Os comand system
import os 
#Insert first values
car_array.append('jetta');
car_array.append('fiesta');
car_array.append('k');
#Function for show layout about cars in array car_array
def show_layout():
    os.system('cls')
    print('===========Car\'s===========');
    print('pos:\t-\t car:')
    for index, car in enumerate(car_array):
        print(index,'\t-\t',car)
    print('===========================');
    while True:
        input(' Saindo...')
        break
# Function for show mneu with option, and return choise by user
def show_menu():
    print('========Menu=========\n',
          'Option:\n\n',
          '[1] - Show Car\'s\n',
          '[2] - Add Car\n',
          '[3] - Remove Car\n',
          '[4] - Update Car\n',
          '[0] - Exit\n',);
    print('========Menu=========\n')
    option = input(' Digite a opcao: ');
    return option
#Adcionando carro ao array:
def add_car(car):
    car_array.append(car)
#Removendo carro do array: 
def rm_car(car):
    car_array.remove(car)
#Atualizando o nome de um carro no array:
def at_car(car,new_name):
    i = car_array.index(car);
    car_array[i] = new_name;
# Infinit loop for menu
while True:
    os.system('cls')
    option = show_menu();
    if option in options:
        if option == '0':
            os.system('cls')
            print('saindo... ');
            input();
            break;
        elif option == '1':
            show_layout();
        elif option == '2':
            os.system('cls')
            print('Adcionando novo carro')
            add_car(input('Digite o nome do novo veiculo: '));
        elif option == '3':
            os.system('cls')
            print('Removendo carro')
            rm_car(input('Digite o nome do veiculo a remover: '));
        else: 
            os.system('cls')
            print('Atualizando o nome carro')
            at_car(input('Digite o nome do veiculo a atualizar: '),input('Digite o novo nome'));
    else:
        print('  Opcao invalida... ');