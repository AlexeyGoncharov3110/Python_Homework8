
def expression_pars(exp: str):
    exp = exp.replace(' ', '').replace('+', ' + ').replace('-',
                                                           ' - ').replace('*', ' * ').replace('/', ' / ')
    if exp.startswith(' - '):
        exp = '-' + exp[3:]
    exp = exp.split()
    return exp


def mult(mult: list):
    i = 0
    while i < len(mult):
        if mult[i] == '*':
            mult[i-1] = int(mult[i-1])*int(mult[i+1])
            mult.pop(i)
            mult.pop(i)
            i -= 1
        i += 1
    return mult


def div(div: list):
    i = 0
    while i < len(div):
        if div[i] == '/':
            div[i-1] = int(div[i-1])//int(div[i+1])
            div.pop(i)
            div.pop(i)
            i -= 1
        i += 1
    return div


def sub(sub: list):
    i = 0
    while i < len(sub):
        if sub[i] == '-':
            sub[i-1] = int(sub[i-1])-int(sub[i+1])
            sub.pop(i)
            sub.pop(i)
            i -= 1
        i += 1
    return sub


def addit(addit: list):
    i = 0
    while i < len(addit):
        if addit[i] == '+':
            addit[i-1] = int(addit[i-1])+int(addit[i+1])
            addit.pop(i)
            addit.pop(i)
            i -= 1
        i += 1
    return addit
