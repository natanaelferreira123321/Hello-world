# calculadora.py
def somar(a, b):
    return a + b

# Um teste simples que a pipeline vai rodar
if __name__ == "__main__":
    resultado = somar(2, 3)
    print(f"Testando soma: 2 + 3 = {resultado}")
    assert resultado == 10, "Erro: A soma deveria ser 5!"
    print("Teste passou com sucesso!")
