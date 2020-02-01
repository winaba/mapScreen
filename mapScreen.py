import pyautogui     

print("")
print("##################################")
print("Vamos configurar os documentos SAT")
print("##################################")
print("")
print('Coloque o mouse sobre o local que ficará os campos mencionados e precione [Enter]')
print("")
print('Coloque o mouse sobre')

doc_config = ''

input('- O campo chave de acesso: ')

doc_config = doc_config + 'CHAVE_ACESSO_X=' + str(pyautogui.position()[0]) + '\n'
doc_config = doc_config + 'CHAVE_ACESSO_Y=' + str(pyautogui.position()[1]) + '\n'

print(pyautogui.position())

input("- O botão [Salvar Nota]: ")

doc_config = doc_config + 'SALVAR_NOTA_SAT_X=' + str(pyautogui.position()[0]) + '\n'
doc_config = doc_config + 'SALVAR_NOTA_SAT_Y=' + str(pyautogui.position()[1]) + '\n'

print(pyautogui.position())

print("")
print("####################################")
print("Vamos configurar os documentos Cupom")
print("####################################")
print("")
print('Coloque o mouse sobre o local que ficará os campos mencionados e precione [Enter]')
print("")
print('Coloque o mouse sobre')

input('- O campo CNPJ do Emissor da Nota: ')

doc_config = doc_config + 'CNPJ_EMISSOR_X=' + str(pyautogui.position()[0]) + '\n'
doc_config = doc_config + 'CNPJ_EMISSOR_Y=' + str(pyautogui.position()[1]) + '\n'

print(pyautogui.position())

input("- O botão [Salvar Nota]: ")

doc_config = doc_config + 'SALVAR_NOTA_CUPOM_X=' + str(pyautogui.position()[0]) + '\n'
doc_config = doc_config + 'SALVAR_NOTA_CUPOM_Y=' + str(pyautogui.position()[1]) + '\n'

print(pyautogui.position())

print("#######################################")
print("Agora vamos configurar outros controles")
print("#######################################")
print("")

doc_config = doc_config + 'ERROS_SEGUIDOS=' + input("- Qual a quantidade de erros seguidos que podem ocorrer? ") + '\n'

doc_config = doc_config + 'SAT_TOTAL_MINUTO=' + input("- Qual a quantidade maxima de SAT, podem ser registrados por minutos? ") + '\n'

doc_config = doc_config + 'CUPOM_TOTAL_MINUTO=' + input("- Qual a quantidade maxima de Cupom, podem ser registrados por minutos? ") + '\n'

arquivo = open('config.ini','w')
arquivo.write(doc_config + '\n')
arquivo.close()

#return 'Sucesso!\n\n'