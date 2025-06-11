import os

def listar_arquivos(diretorio):
    """
    Lista os arquivos em um diretório especificado.

    :param diretorio: Caminho do diretório
    :return: Lista de arquivos encontrados
    """
    try:
        arquivos = [
            arq
            for arq in os.listdir(diretorio)
            if os.path.isfile(os.path.join(diretorio, arq))
        ]
        return arquivos

    except FileNotFoundError:
        print(f"Erro: O diretório '{diretorio}' não foi encontrado.")
        return []

    except PermissionError:
        print(f"Erro: Sem permissão para acessar o diretório '{diretorio}'.")
        return []


def renomear_arquivos(arquivos, diretorio, novo_padrao):
    """
    Renomeia os arquivos de acordo com o novo padrão fornecido.

    :param arquivos: Lista de arquivos a serem renomeados.
    :param diretorio: Caminho do diretório onde os arquivos estão localizados.
    :param novo_padrao: Padrão para renomeação dos arquivos.
    """
    for indice, arq in enumerate(arquivos):
        caminho_antigo = os.path.join(diretorio, arq)
        # Suporta os placeholders {index} e {indice} para o índice
        nome_novo = novo_padrao.format(index=indice, indice=indice, original=arq)
        caminho_novo = os.path.join(diretorio, nome_novo)

        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"Arquivo '{arq}' renomeado para '{nome_novo}'")
        except Exception as e:
            print(f"Erro ao renomear '{arq}': {e}")


def main():
    diretorio = input("Digite o caminho do diretório onde estão os arquivos: ")
    arquivos = listar_arquivos(diretorio)

    if not arquivos:
        print("Nenhum arquivo foi encontrado.")
        return

    print(f"Arquivos encontrados: {', '.join(arquivos)}")
    novo_padrao = input(
        "Digite o novo padrão para renomeação (use '{index}' ou '{indice}' para o índice e '{original}' para o nome original): "
    )
    renomear_arquivos(arquivos, diretorio, novo_padrao)


if __name__ == "__main__":
    main()
