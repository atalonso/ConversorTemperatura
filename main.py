from helpers import celsius_para_kelvin, celsius_para_fahrenheit
if __name__ == '__main__':
 while True:
    mensagem = "\nPor favor, insira a temperatura em Celsius:"
    mensagem += "\nPara sair do programa basta digitar 'q':"
    try:
          celsius = input(mensagem)
          if celsius.lower() != 'q':
             print(f"\n A temperatura em Kelvin(K) = {celsius_para_kelvin(float(celsius))}")
             print(f"\n A temperatura em Fahrenheit(F) = {celsius_para_fahrenheit(float(celsius))}")
          else:
             print("Até a Próxima ")
             break
    except ValueError:
             print("\n Você digitou um caracter inválido, por favor, digite um número válido, ou 'q' para sair.")