### Imports
######################
# import sys

### Variables Global
######################
uf    = ['GO', 1]
count = int('00000000')

### Functions
######################
def cpf_digit_x(numberText):
  i   = 10
  sum = 0
  for x in list(numberText):
    sum = sum + (int(x) * i);
    i = i - 1
  return get_rest(sum)

def cpf_digit_y(numberText):
  i   = 11
  sum = 0
  for x in list(numberText):
    sum = sum + (int(x) * i);
    i = i - 1
  return get_rest(sum)

def get_rest(num):
  resto = num % 11
  if resto == 0 or resto == 1:
    return 0
  else:
    return 11 - resto

def validate_cpf(cpf):
  sum = 0
  for x in list(cpf):
    sum = sum + int(x);  
  if sum in [10, 11, 12, 21, 22, 23, 32, 33, 34, 43, 44, 45, 54, 55, 56, 65, 66, 67, 76, 77, 78, 87, 88]:
    return True
  else:
    return False

### Execution 
######################
while int(count) <= int('99999999'):
  x = cpf_digit_x((str(count) + str(uf[1])).zfill(9))
  y = cpf_digit_y((str(count) + str(uf[1]) + str(x)).zfill(10))
  cpf = (str(count) + str(uf[1]) + str(x) + str(y)).zfill(11)

  if (validate_cpf(cpf)):
    print(cpf)

  count = str(int(count) + 1)


### Info sobre UF
######################
# O antepenúltimo dígito (o que está representado pelo “X” em 000.000.00X-00) indica o estado de origem. 
#
# 0. Rio Grande do Sul
# 1. Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins
# 2. Amazonas, Pará, Roraima, Amapá, Acre e Rondônia
# 3. Ceará, Maranhão e Piauí
# 4. Paraíba, Pernambuco, Alagoas e Rio Grande do Norte
# 5. Bahia e Sergipe
# 6. Minas Gerais
# 7. Rio de Janeiro e Espírito Santo
# 8. São Paulo
# 9. Paraná e Santa Catarina
#
# Obs.: http://www.profcardy.com/cardicas/cpf-curiosidades.php
