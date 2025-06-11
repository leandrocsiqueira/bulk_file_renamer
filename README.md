# Bulk File Renamer

## Descrição

O **Bulk File Renamer** é um script Python simples e eficiente para renomeação em massa de arquivos em um diretório. Ele permite que os usuários definam um padrão de renomeação personalizado usando placeholders dinâmicos, como índices sequenciais ou o nome original dos arquivos. Esse programa é útil para organizar arquivos de forma rápida e consistente, evitando nomes duplicados ou confusos.

## Funcionalidades

- **Listagem de Arquivos**: Lista todos os arquivos em um diretório especificado pelo usuário.
- **Renomeação em Massa**: Renomeia todos os arquivos listados de acordo com o padrão fornecido pelo usuário.
- **Placeholders Personalizados**: Suporte para placeholders `{index}` (ou `{indice}`) e `{original}`, permitindo criar nomes únicos para cada arquivo.
- **Tratamento de Erros**: Mensagens de erro amigáveis para diretórios inexistentes ou permissões insuficientes.

## Como Usar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `bulk_file_renamer.py`.
3. Execute o script a partir da linha de comando:
   ```bash
   python bulk_file_renamer.py
   ```
4. Insira o caminho do diretório que contém os arquivos a serem renomeados.
5. Insira o novo padrão de renomeação. Você pode usar:
   * `{index}` ou `{indice}`: Para incluir um índice sequencial único.
   * `{original}`: Para manter parte ou todo o nome original do arquivo.

## Exemplo de Padrões de Renomeação

* `novo_nome_{index}`: Renomeará os arquivos para `novo_nome_0`, `novo_nome_1`, etc. (também é possível usar `{indice}`)
* `copia_{original}`: Renomeará os arquivos para `copia_nome_original.ext`.

## Exemplo de Execução

```plaintext
Digite o caminho do diretório onde estão os arquivos: C:\meus_arquivos
Arquivos encontrados: arquivo1.txt, arquivo2.txt, arquivo3.txt
Digite o novo padrão de renomeação (use '{index}' ou '{indice}' para o índice e '{original}' para o nome original): novo_{index}
Arquivo 'arquivo1.txt' renomeado para 'novo_0.txt'
Arquivo 'arquivo2.txt' renomeado para 'novo_1.txt'
Arquivo 'arquivo3.txt' renomeado para 'novo_2.txt'
```

## Requisitos

* Python 3.x

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License.
