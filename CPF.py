import re

class CPF:
    def __init__(self, doc_num: str):
        # Tratando a entrada de doc_num.
        if type(doc_num) != str:
            raise TypeError('\033[31mAtenção! O CPF deve ser do tipo string e deve conter 11 dígitos numéricos!\033[m')
        elif type(doc_num) == str:
            pattern =  self.have_mask(doc_num)
            if pattern:
                doc_num = self.remove_mask(doc_num)
            elif pattern == False:
                pass
            else:
                raise ValueError('Atenção! O CPF deve conter 11 dígitos e deve ser inserido em um dos dois formatos: \n 1 -> 000.000.000-00\n 2 -> 00000000000')
            
        if self.repeated_digits(doc_num):
                raise ValueError('O CPF não pode conter 11 dígitos repetidos!')

        self.doc_num = doc_num

    def __str__(self) -> str:
        """
        Ao inserir o objeto CPF em um print(),
        o número do documento será exibido com a máscara 000.000.000-00.
        """
        return self.create_mask(self.doc_num)
    
    def have_mask(self, doc_num) -> bool:
        """
        Encontra o padrão da string inserida. 
        Dois padrões são válidos:
            1 - 000.000.000-00 (com máscara)
            2 - 00000000000 (sem máscara)
        :param str: doc_num -> string que contém o número do documento (CPF).
        :return bool: True or False. Depende, se tiver no padrão de máscara, retorna True.
        """

        tam_string: int = len(doc_num)
        if tam_string == 11:
            cpf_pattern_2: str = '[0-9]{11}'
            validate_2: bool = re.findall(string=doc_num,pattern=cpf_pattern_2)
            return False
        elif tam_string == 14:
            cpf_pattern_1: str = '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
            validate_1: bool = re.findall(string=doc_num,pattern=cpf_pattern_1)
            return True
      

    def create_mask(self, doc_num: str) -> str:
        """
        Cria a máscara no formato ___.___.___-__
        :param doc_num: string com o número do documento.
        :return: exemplo: 012.345.678-90 
        """
        return f'{doc_num[:3]}.{doc_num[3:6]}.{doc_num[6:9]}-{doc_num[9:]}'


    def remove_mask(self, doc_num: str) -> str:
        """
        Remove os caracteres '.' e '-'.
        :param doc_num: string com os números do documento.
        :return:
        """
        return re.sub('[.-]', '', doc_num)


    def repeated_digits(self, doc_num: str) -> bool:
        """
        Verifica se o documento informado contém apenas dígitos repetidos.
        Exemplo: 000.000.000-00 ou 00000000000
        :param doc_num: string com o número do documento (CPF).
        :return True/False: caso contenha apenas dígitos repetidos
        """
        return len(set(list(doc_num))) == 1


    def last_digits_verify(self) -> bool:
        """
        Verifica se os dois últimos dígitos do CPF são válidos. 
        :param doc_num: string com os números do documento (CPF).
        :return True/False: se os dois últimos dígitos verificados estiverem corretos, retorna True.
        """
        # doc_num = self.remove_symbols(doc_num)
        nums_cpf: list = list(self.doc_num[::-1])[2:]
        for i in list(range(0, 2)):
            to_sum: int = sum([enum * int(num) for enum, num in enumerate(nums_cpf, start=2)])
            quociente, resto =  divmod(to_sum, 11)

            if resto < 2:
                _digit: int = 0
            else:
                _digit: int = 11 - resto
            
            nums_cpf.insert(0, str(_digit))

        return ''.join(nums_cpf[::-1]) == self.doc_num
