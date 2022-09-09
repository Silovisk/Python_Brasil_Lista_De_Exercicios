
opcao = int(input("Digite a opçao :"))
if(opcao == 0):
    print("Programa encerrado!")
else:
    while opcao != 0:
        if (opcao == 1):
            fat = int(input("informe o numero do fatorial: "))
            if (fat <= -1):
                print("Limitado a numeros positivos")
                opcao = 0
            elif(fat == 0):
                fat = 1
                print(f"Fatorial = {fat}")
            elif(fat >= 0 and fat < 16 ):
                fatorial = 1
                while fat != 1:
                    fatorial = fatorial * fat 
                    fat = fat - 1
                    print(f"{fatorial}")
        continua = input("Deseja continuar ? y/n: ")
        if(continua == 'y' or continua == 'Y'):
            pass
        else:
            print("Encerrando programa...")
            break