def identificar_string(texto):
    """
    Analisa uma string e retorna uma lista formatada com todas as características identificadas.
    
    Args:
        texto (str): String a ser analisada
        
    Returns:
        list: Lista de tuplas contendo (descrição, resultado)
    """
    verificacoes = [
        ("É alfabético?", texto.isalpha()),
        ("É numérico?", texto.isnumeric()),
        ("É alfanumérico?", texto.isalnum()),
        ("Está em maiúsculo?", texto.isupper()),
        ("Está em minúsculo?", texto.islower()),
        ("É um número decimal?", texto.isdecimal()),
        ("É um identificador válido?", texto.isidentifier()),
        ("Pode ser impresso?", texto.isprintable()),
        ("Está em formato de título?", texto.istitle()),
        ("É um dígito?", texto.isdigit()),
        ("Contém apenas espaços?", texto.isspace())
    ]
    
    return verificacoes


def exibir_resultados(texto, resultados):
    """
    Exibe os resultados da análise de forma formatada e organizada.
    
    Args:
        texto (str): String analisada
        resultados (list): Lista de tuplas com os resultados
    """
    print("\n" + "="*60)
    print(f"📝 ANÁLISE DA STRING: '{texto}'")
    print(f"🔤 Tipo: {type(texto).__name__}")
    print("="*60)
    
    # Encontra o tamanho da maior descrição para alinhar
    max_len = max(len(desc) for desc, _ in resultados)
    
    print("\n✨ CARACTERÍSTICAS:\n")
    for descricao, resultado in resultados:
        simbolo = "✅" if resultado else "❌"
        print(f"  {simbolo} {descricao:<{max_len}} → {resultado}")
    
    print("\n" + "="*60)


def main():
    """Função principal do programa."""
    print("🔍 IDENTIFICADOR DE STRINGS EM PYTHON\n")
    
    entrada = input("Digite alguma coisa para análise: ")
    
    # Realiza a análise
    resultados = identificar_string(entrada)
    
    # Exibe os resultados formatados
    exibir_resultados(entrada, resultados)


if __name__ == "__main__":
    main()
