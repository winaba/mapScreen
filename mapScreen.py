from rotinasDeConfiguracao import RotinasDeConfiguracao

if __name__ == "__main__":
    
    a = RotinasDeConfiguracao()

    a.configuraArquivoSAT()
    a.configuraArquivoCupom()
    a.configuraControles()
    a.visualizaArquivoDeConfiguracao()
    a.gravaArquivo()