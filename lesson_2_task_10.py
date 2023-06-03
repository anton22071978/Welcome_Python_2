def bank (X,Y):
    deposit = X
    koef = 1.1
    year = 1
    while (year <= Y):
        deposit = koef * deposit
        year += 1
    return deposit    