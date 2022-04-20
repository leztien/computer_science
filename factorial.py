def factorial(n):
    if n <= 1:                 #Abbruchbedingung
        return 1
    return n * factorial(n-1)  #Rekursionsbedingung
