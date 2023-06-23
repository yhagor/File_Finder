Select Language : [:us:]() [:brazil:]()
<h1 align="center">
  <p align="center">:construction: Localizador de Arquivos :construction:</p>
</h1>

Este script foi desenvolvido com o objetivo de auxiliar na busca de arquivos, permitindo a busca por nome ou parte do nome.

Se você estiver procurando por um arquivo que contenha espaços entre as palavras, o nome deve ser colocado entre aspas, por exemplo, "documentação do projeto".

Além disso, é possível utilizar este programa para encontrar arquivos com uma extensão específica. Basta inserir o parâmetro "-wn .pdf" para buscar arquivos com extensão PDF, por exemplo, e utilizar o parâmetro "-en" para especificar a extensão.

Os arquivos encontrados serão exibidos com seu caminho completo, tamanho em bytes e data da última modificação.

Para visualizar as informações dos arquivos de forma mais organizada, você também pode solicitar que o programa crie um arquivo .tsv contendo essas informações. Os dados serão apresentados em uma tabela simples.

E o arquivo será salvo no mesmo diretório do programa.

## Parameters Argparse

- -v or --version : Optional[bool]
  - Versão do programa.
- -rd or --rootdir : str
  - Diretório raiz onde será realizada a busca dos arquivos.
- -wn or --wantedname : str
  - Nome, parte do nome do arquivo ou extensão do arquivo. []
- -gf or --getfile : Optional[bool]
  - Salve o caminho dos arquivos em um arquivo. []
        
## Parameters Argparse Mutually Exclusive Group

- -rm or --rmatch : Optional[bool]
  - Verifica uma correspondência apenas no início da string.
- -rs or --rsearch : Optional[bool]
  - Verifica uma correspondência em qualquer lugar na string.
- -en or --endswith : Optional[bool]
  - verifique a extensão do arquivo.
