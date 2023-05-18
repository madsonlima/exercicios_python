def aumentar(v=0, t=0, f=True, moeda="R$"):
    res = v + (v * (t / 100))
    if f:
        return real(res, moeda)
    else:
        return res


def diminuir(v=0, t=0, f=True, moeda="R$"):
    res = v - (v * (t / 100))
    if f:
        return real(res, moeda)
    else:
        return res


def dobro(v=0, f=True, moeda="R$"):
    res = v * 2
    return res if not f else real(res, moeda)


def metade(v=0, f=True, moeda="R$"):
    res = v / 2
    return res if not f else real(res, moeda)


def real(v=0, moeda="R$"):
    return f"{moeda}{v:.2f}".replace(".", ",")


def resumo(v=0, aum=0, dim=0):
    print(f"Preço: {real(v)} | Acréscimo: {aum}% | Desconto: {dim}%")
    print(f"Preço com acréscimo:\t{aumentar(v, aum)}")
    print(f"Preço com desconto:\t\t{diminuir(v, dim)}")
    print(f"Preço dobrado:\t\t\t{dobro(v)}")
    print(f"Preço pela metade:\t\t{metade(v)}")
    return
