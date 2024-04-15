import random
import string

def generate_password(length=16, include_upper=True, include_lower=True, include_digits=True, include_symbols=True):
    chars = ''
    if include_upper:
        chars += string.ascii_uppercase
    if include_lower:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += '!@#$%&*()[]+-/=,.;-_?/\\<>{}'

    if not chars:
        raise ValueError("Nenhum conjunto de caracteres selecionado.")

    rnd = random.SystemRandom()
    return ''.join(rnd.choice(chars) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Digite o tamanho da senha desejado: "))
        include_upper = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
        include_lower = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
        include_digits = input("Incluir números? (s/n): ").lower() == 's'
        include_symbols = input("Incluir símbolos? (s/n): ").lower() == 's'

        password = generate_password(length, include_upper, include_lower, include_digits, include_symbols)
        print("Senha gerada:", password)
    except ValueError as ve:
        print("Erro:", ve)
