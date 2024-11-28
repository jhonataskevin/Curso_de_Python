import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

print("__________________________________")

from math import sqrt # aqui ele importa apenas a função sqrt do modulo math.


resultado = sqrt(25)
print(resultado)  # Imprime 5.0

print("__________________________________")

import random # modulo que oferece gerar um numero aleatorio.
import datetime # modulo para trabalhar com data e hora.


numero_aleatorio = random.randint(1, 10)
print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual