

def format_separators(value, decimal_separator=',', thousand_separator='.'):
    # Função que retorna uma string de um número formatado com separador de milhar e decimal
    if type(value) == float:
        # Troca o decimal separator padrão para D e o thousand separator padrão para T
        value = ('{:,.2f}'.format(float(value))).replace('.', 'D').replace(',', 'T')
        value = value.replace('D', decimal_separator).replace('T', thousand_separator)
    elif type(value) == int:
        value = f'{value:,}'.replace(',', '.')
    
    return value

def format_currency(value, currency='R$', value_format='cents', decimal_separator=',', thousand_separator='.'):
    # Função para formatar uma moeda a partir do seu valor em centavos
    value = value if value_format != 'cents' else value/100
    formated_value = format_separators(float(value), decimal_separator, thousand_separator)
    return f'{currency} {formated_value}'

