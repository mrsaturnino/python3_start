"""
- IF ELSE CHALLENGE -

Criar um programa que dependendo da temperatura (em celsius) do steak, ele retorna o ponto de cozimento. O usuário deverá fornecer a temperatura.
(faça uma versão em fahreinheit se puder)

TEMPERATURAS - COZIMENTO

120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done! (Bem passada)

"""
#função para capturar dados do usuário:
def getPoint():
    global setMeasure
    global temperature
    
    setMeasure = input("Digite a unidade de medida que deseja calcular o ponto do steak, sendo 'F' para Fahrenheit ou 'C' para Celcius: ")

    temperature = int(input("Digite número da temperatura: "))
    print(str(f"Temperatura: {temperature}°{setMeasure}"))
    print()

#função para definir a informação e mostrar os resultados de acordo com os dados capturados:

def setPoint(setMeasure, temperature):
    
    if setMeasure == 'F':
        if temperature >= 120 and temperature < 130:
          print(f"SteakPoint: {temperature}°F: Rare")
        elif temperature >= 130 and temperature < 140:
          print(f"SteakPoint: {temperature}°F: Medium Rare")
        elif temperature >= 140 and temperature < 150:
          print(f"SteakPoint: {temperature}°F: Medium")
        elif temperature >= 150 and temperature < 160:
          print(f"SteakPoint: {temperature}°F: Medium Well")
        elif temperature == 160:
          print(f"SteakPoint: {temperature}°F: Well done")
        else:
            print("Erro, a temperatura em °F deve estar entre 120°F e 160°F.")
        
    if setMeasure == 'C':
      if temperature in range(48, 53):
        print(f"SteakPoint: {temperature}°C: Rare")
      elif temperature in range(54, 59):
        print(f"SteakPoint: {temperature}°C: Medium Rare")
      elif temperature in range(60, 64):
        print(f"SteakPoint: {temperature}°C: Medium")
      elif temperature in range(65, 70):
        print(f"SteakPoint: {temperature}°C: Medium Well")
      elif temperature >= 71:
        print(f"SteakPoint: {temperature}°C: Well done")
    else:
      print(f"'{setMeasure}' não é uma unidade valida.")

getPoint()
setPoint(setMeasure, temperature)