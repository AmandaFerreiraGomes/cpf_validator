# cpf_validator

Help on module CPF_validator:

NAME
    CPF_validator

CLASSES
    builtins.object
        CPF

    class CPF(builtins.object)
     |  CPF(doc_num: str)
     |
     |  Methods defined here:
     |
     |  __init__(self, doc_num: str)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __str__(self) -> str
     |      Ao inserir o objeto CPF em um print(),
     |      o número do documento será exibido com a máscara 000.000.000-00.
     |
     |  create_mask(self, doc_num: str) -> str
     |      Cria a máscara no formato ___.___.___-__
     |      :param doc_num: string com o número do documento.
     |      :return: exemplo: 012.345.678-90
     |
     |  have_mask(self, doc_num) -> bool
     |      Encontra o padrão da string inserida.
     |      Dois padrões são válidos:
     |          1 - 000.000.000-00 (com máscara)
     |          2 - 00000000000 (sem máscara)
     |      :param str: doc_num -> string que contém o número do documento (CPF).
     |      :return bool: True or False. Depende, se tiver no padrão de máscara, retorna True.
     |
     |  last_digits_verify(self) -> bool
     |      Verifica se os dois últimos dígitos do CPF são válidos.
     |      :param doc_num: string com os números do documento (CPF).
     |      :return True/False: se os dois últimos dígitos verificados estiverem corretos, retorna True.
     |
     |  remove_mask(self, doc_num: str) -> str
     |      Remove os caracteres '.' e '-'.
     |      :param doc_num: string com os números do documento.
     |      :return:
     |
     |  repeated_digits(self, doc_num: str) -> bool
     |      Verifica se o documento informado contém apenas dígitos repetidos.
     |      Exemplo: 000.000.000-00 ou 00000000000
     |      :param doc_num: string com o número do documento (CPF).
     |      :return True/False: caso contenha apenas dígitos repetidos
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
