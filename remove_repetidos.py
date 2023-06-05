def remove_repetidos(v):
    v_limpa = []
    for x in v:
        if x not in v_limpa:
            v_limpa.append(x)
    return v_limpa
