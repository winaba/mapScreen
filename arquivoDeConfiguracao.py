
class ArquivoDeConfiguracao:
    def __init__(self):
        self.doc_config = ''

    def addLine(self, key='', value=''):
        self.doc_config = self.doc_config + key + '=' +value + '\n'

    def addDoc(self, document=''):
        print(self.doc_config)
        self.doc_config = document

    def content(self):
        print(self.doc_config)

    def post(self):
        arquivo = open('config.ini','w')
        arquivo.write(self.doc_config)
        arquivo.close() 