import pyautogui 
from arquivoDeConfiguracao import ArquivoDeConfiguracao

class RotinasDeConfiguracao:
    def __init__(self):
        self.config = ArquivoDeConfiguracao()

    def configuraArquivoSAT(self):
        print("")
        print("##################################")
        print("Vamos configurar os documentos SAT")
        print("##################################")
        print("")
        print('Coloque o mouse sobre o local que ficará os campos mencionados e precione [Enter]')
        print("")
        print('Coloque o mouse sobre')

        input('- O campo chave de acesso: ')

        self.config.addLine('CHAVE_ACESSO_X', str(pyautogui.position()[0]) )
        self.config.addLine('CHAVE_ACESSO_Y', str(pyautogui.position()[1]) )

        print('Leitura realizada')

        input("- O botão [Salvar Nota]: ")

        self.config.addLine('SALVAR_NOTA_SAT_X', str(pyautogui.position()[0]) )
        self.config.addLine('SALVAR_NOTA_SAT_Y', str(pyautogui.position()[1]) )

        print('Leitura realizada')

    def configuraArquivoCupom(self):    
        print("")
        print("####################################")
        print("Vamos configurar os documentos Cupom")
        print("####################################")
        print("")
        print('Coloque o mouse sobre o local que ficará os campos mencionados e precione [Enter]')
        print("")
        print('Coloque o mouse sobre')

        input('- O campo CNPJ do Emissor da Nota: ')

        self.config.addLine('CNPJ_EMISSOR_X', str(pyautogui.position()[0]) )
        self.config.addLine('CNPJ_EMISSOR_Y', str(pyautogui.position()[1]) )

        print('Leitura realizada')

        input("- O botão [Salvar Nota]: ")

        self.config.addLine('SALVAR_NOTA_CUPOM_X', str(pyautogui.position()[0]) )
        self.config.addLine('SALVAR_NOTA_CUPOM_Y', str(pyautogui.position()[1]) )

        print('Leitura realizada')

    def configuraControles(self):
        print("")
        print("#######################################")
        print("Agora vamos configurar outros controles")
        print("#######################################")
        print("")

        self.config.addLine('ERROS_SEGUIDOS', input("- Qual a quantidade de erros seguidos que podem ocorrer? "))

        self.config.addLine('SAT_TOTAL_MINUTO', input("- Qual a quantidade de erros seguidos que podem ocorrer? "))

        self.config.addLine('CUPOM_TOTAL_MINUTO', input("- Qual a quantidade de erros seguidos que podem ocorrer? "))

    def visualizaArquivoDeConfiguracao(self):
        print("")
        print("##############################")
        print("Visualização do arquivo gerado")
        print("##############################")
        print("")
        self.config.content()

    def gravaArquivo(self):
        import os

        print('Local do arquivo gerado: ')
        print(os.getcwd() + '\config.ini')
        self.config.post()
    