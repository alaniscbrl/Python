def par(x): 
    return x % 2 == 0


def par_ou_impar(x):
    if par(x):
        return "par"
    else:
        return "ímpar"


print(par_ou_impar(7))