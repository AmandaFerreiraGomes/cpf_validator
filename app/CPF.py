import re

def validate_input_doc_num(doc_num: str) -> str:
    """
    Valida a entrada do documento.

    Args:
        doc_num (str): string que contém o número do documento.
    Returns:
        doc_num (str): string caso o número do documento seja válido.
    """
    if not isinstance(doc_num, str):
        raise TypeError('O CPF deve ser do tipo string, contendo 11 dígitos numéricos!')
    else:
        pattern: bool = have_mask(doc_num)
        if pattern:
            doc_num: str = remove_mask(doc_num)
        elif pattern == False:
            pass
        else:
            raise ValueError('O CPF deve conter 11 dígitos e deve ser inserido em um dos dois formatos a seguir:\n 1 -> 000.000.000-00\n 2-> 00000000000')
    if repeated_digits(doc_num):
        raise ValueError('O CPF não pode conter 11 dígitos repetidos!')

    return doc_num


def have_mask(doc_num: str) -> bool:
    """
    Encontra o padrão da string inserida. 
    Dois padrões são válidos:
        1 - 000.000.000-00 (com máscara)
        2 - 00000000000 (sem máscara)
    :param str: doc_num -> string que contém o número do documento (CPF).
    :return bool: True or False. Depende, se tiver no padrão de máscara, retorna True.
    """
    # doc_num: str = validate_input_doc_num(doc_num)
    tam_string: int = len(doc_num)
    if tam_string == 11:
        cpf_pattern_2: str = '[0-9]{11}'
        validate_2: bool = re.findall(string=doc_num,pattern=cpf_pattern_2)
        return False
    elif tam_string == 14:
        cpf_pattern_1: str = '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
        validate_1: bool = re.findall(string=doc_num,pattern=cpf_pattern_1)
        return True


def repeated_digits(doc_num: str) -> bool:
    """
    Verifica se o documento informado contém apenas dígitos repetidos.
    Exemplo: 000.000.000-00 ou 00000000000
    :param doc_num: string com o número do documento (CPF).
    :return True/False: caso contenha apenas dígitos repetidos
    """
    # doc_num = validate_input_doc_num(doc_num)
    return len(set(list(doc_num))) == 1


def create_mask(doc_num: str) -> str:
    """
    Cria a máscara no formato ___.___.___-__
    :param doc_num: string com o número do documento.
    :return: exemplo: 012.345.678-90 
    """
    # doc_num = validate_input_doc_num(doc_num)
    if not have_mask(doc_num):
        doc_num = f'{doc_num[:3]}.{doc_num[3:6]}.{doc_num[6:9]}-{doc_num[9:]}'
    return doc_num


def remove_mask(doc_num: str) -> str:
    """
    Remove os caracteres '.' e '-'.
    :param doc_num: string com os números do documento.
    :return:
    """
    # doc_num = validate_input_doc_num(doc_num)
    if not have_mask(doc_num):
        return doc_num
    
    return re.sub('[.-]', '', doc_num)


def validate(doc_num: str) -> bool:
    """
    Verifica se os dois últimos dígitos do CPF são válidos. 
    :param doc_num: string com os números do documento (CPF).
    :return True/False: se os dois últimos dígitos verificados estiverem corretos, retorna True.
    """
    # doc_num = validate_input_doc_num(doc_num)
    # if repeated_digits(doc_num):
    #     return False
    
    doc_num: str = validate_input_doc_num(doc_num)

    nums_cpf: list = list(doc_num[::-1])[2:]
    for i in list(range(0, 2)):
        to_sum: int = sum([enum * int(num) for enum, num in enumerate(nums_cpf, start=2)])
        quociente, resto =  divmod(to_sum, 11)

        if resto < 2:
            _digit: int = 0
        else:
            _digit: int = 11 - resto
            
        nums_cpf.insert(0, str(_digit))

    return ''.join(nums_cpf[::-1]) == doc_num

