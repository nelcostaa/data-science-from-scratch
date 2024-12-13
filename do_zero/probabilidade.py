def main():
    import enum, random

    class Crianca(enum.Enum):
        MENINO = 0
        MENINA = 1

    def crianca_aleatoria() -> Crianca:
        return random.choice([Crianca.MENINO, Crianca.MENINA])

    ambos_meninas = 0
    menina_mais_velha = 0
    pelo_menos_uma_menina = 0

    random.seed(0)

    for _ in range(10000):
        mais_novo = crianca_aleatoria()
        mais_velho = crianca_aleatoria()

        if mais_velho == Crianca.MENINA:
            menina_mais_velha += 1
        if mais_velho == Crianca.MENINA and mais_novo == Crianca.MENINA:
            ambos_meninas += 1
        if mais_velho == Crianca.MENINA or mais_novo == Crianca.MENINA:
            pelo_menos_uma_menina += 1

    print("P(ambos | mais velho): ", ambos_meninas / menina_mais_velha)
    print("P(ambos | ao_menos_uma): ", ambos_meninas / pelo_menos_uma_menina)


if __name__ == "__main__":
    main()
