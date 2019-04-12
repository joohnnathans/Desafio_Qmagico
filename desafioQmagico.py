
def piramide(a):
    b = a-1
    c = 1
    for i in range(a):
        while b > -1: 
            print ("%s %s %s" % (('_' * b), ('*' * c), ('_' * b)))
            b -= 1
            c += 2
