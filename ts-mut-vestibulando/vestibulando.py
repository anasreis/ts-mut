def verificaVestibulando(nota: int) -> str:
    res = None

    if nota > 400:
        res = 'Você está selecionado'

    elif nota > 0 and nota < 200:
        res = 'Você não foi selecionado'

    elif nota >= 200 and nota <= 400: 
        res = 'Você está na lista de espera'

    elif nota == 0:
        res = 'É necessário procurar a universidade'

    return res