import random


def obtener_palabra_secreta() -> str:
    palabras = [
        "python",
        "java",
        "angular",
        "django",
        "tensorflow",
        "react",
        "typescrit",
        "git",
        "flask",
    ]
    return random.choice(palabras)


def mostar_avanzce(palabra_secreta, letras_advininadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_advininadas:
            adivinado += letra
        else:
            adivinado += "_"

    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(
        mostar_avanzce(palabra_secreta, letras_adivinadas),
        "la cantidad de letras de la palabra es:",
        len(palabra_secreta),
    )

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce uyna letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra válida(sólo escribir la letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(
                    f"¡ haz acertado, la letra {adivinanza} está presente en la palbra"
                )
            else:
                intentos -= 1
                print(
                    f"Lo siento mucho la letra {adivinanza} no está presente en la palabra secreta"
                )
                print(f"Te quedan {intentos} intentos")

        progeso_actual = mostar_avanzce(palabra_secreta, letras_adivinadas)
        print(progeso_actual)

        if "_" not in progeso_actual:
            juego_terminado = True
            print(
                f"¡Felicitaciones has ganado! La palabra secreta es: {palabra_secreta}"
            )
    if intentos == 0:
        print(
            f"Lo sentimos mucho se te han acabo los intentos, la palabra secreta era: {palabra_secreta}"
        )


juego_ahorcado()
