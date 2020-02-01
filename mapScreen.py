import pyautogui     
from arquivoDeConfiguracao import ArquivoDeConfiguracao

print("")
print("##################################")
print("Vamos configurar os documentos SAT")
print("##################################")
print("")
print('Coloque o mouse sobre o local que ficará os campos mencionados e precione [Enter]')
print("")
print('Coloque o mouse sobre')

config = ArquivoDeConfiguracao()

input('- O campo chave de acesso: ')

config.addLine('CHAVE_ACESSO_X', str(pyautogui.position()[0]) )
config.addLine('CHAVE_ACESSO_Y', str(pyautogui.position()[1]) )

print('Leitura realizada')

input("- O botão [Salvar Nota]: ")

config.addLine('SALVAR_NOTA_SAT_X', str(pyautogui.position()[0]) )
config.addLine('SALVAR_NOTA_SAT_Y', str(pyautogui.position()[1]) )

print('Leitura realizada')

print("")
print("####################################")
print("Vamos configurar os documentos Cupom")
print("####################################")
print("")
print('Coloque o mouse sobre o local que ficará os campos mencionados e precione [Enter]')
print("")
print('Coloque o mouse sobre')

input('- O campo CNPJ do Emissor da Nota: ')

config.addLine('CNPJ_EMISSOR_X', str(pyautogui.position()[0]) )
config.addLine('CNPJ_EMISSOR_Y', str(pyautogui.position()[1]) )

print('Leitura realizada')

input("- O botão [Salvar Nota]: ")

config.addLine('SALVAR_NOTA_CUPOM_X', str(pyautogui.position()[0]) )
config.addLine('SALVAR_NOTA_CUPOM_Y', str(pyautogui.position()[1]) )

print('Leitura realizada')

print("")
print("#######################################")
print("Agora vamos configurar outros controles")
print("#######################################")
print("")

config.addLine('ERROS_SEGUIDOS', input("- Qual a quantidade de erros seguidos que podem ocorrer? "))

config.addLine('SAT_TOTAL_MINUTO', input("- Qual a quantidade de erros seguidos que podem ocorrer? "))

config.addLine('CUPOM_TOTAL_MINUTO', input("- Qual a quantidade de erros seguidos que podem ocorrer? "))


print("")
print("##############################")
print("Visualização do arquivo gerado")
print("##############################")
print("")

config.content()

config.post()