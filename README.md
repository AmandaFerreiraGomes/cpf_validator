NAME
    CPF



FUNCTIONS
    create_mask(doc_num: str) -> str
        Cria a máscara no formato ___.___.___-__.
        
        Args:
            doc_num (str): string com o número do documento.
        Returns:
            doc_num (str): retorna o cpf com máscara.
            Exemplo: 012.345.678-90
    
    have_mask(doc_num: str) -> bool
        Encontra o padrão da string inserida.
        
        Dois padrões são válidos:
            1 - 000.000.000-00 (com máscara).
            2 - 00000000000 (sem máscara).
        Args:
            - doc_num (str): string que contém o número do documento (CPF).
        Returns:
            (bool) True or False. Depende, se tiver no padrão de máscara, retorna True.
    
    remove_mask(doc_num: str) -> str
        Remove os caracteres '.' e '-'.
        
        Returns:
            (str): string com os números apenas, sem a máscara.


    repeated_digits(doc_num: str) -> bool
        Verifica se o documento informado contém apenas dígitos repetidos.
        
        Exemplo: 000.000.000-00 ou 00000000000.
        Args:
            - doc_num (str): string com o número do documento (CPF).
        Returns:
            (bool): caso contenha apenas dígitos repetidos.

    validate(doc_num: str) -> bool
        Verifica se os dois últimos dígitos do CPF são válidos.

        Args:
            - doc_num (str): string com os números do documento (CPF).
        Returns:
            (bool): se os dois últimos dígitos verificados estiverem corretos, retorna True.

    validate_input_doc_num(doc_num: str) -> str
        Valida a entrada do documento.

        Args:
            doc_num (str): string que contém o número do documento.
        Returns:
            doc_num (str): string caso o número do documento seja válido.