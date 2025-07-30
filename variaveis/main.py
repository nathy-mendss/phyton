def main():
    nome = input("digite seu nome: ")
    idade = int(input("digite a sua idade :"))
    peso = float (input("digite o seu peso: "))
    isEmpregado = input("Vc possui um emprego? ")

    print("o", nome, "tem", idade," anos de idade, pesa",peso)

    if isEmpregado:
        print("ele possui um emprego")
    else:
        print("ele não possui emprego")

    return 0
main()