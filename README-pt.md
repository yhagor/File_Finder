Select Language : [:us:](https://github.com/yhagor/File_Finder/blob/main/README.md) [:brazil:](https://github.com/yhagor/File_Finder/blob/main/README-pt.md)
<h1 align="center">
  <p align="center">Localizador de Arquivos</p>
</h1>

Este script foi desenvolvido com o objetivo de auxiliar na busca de arquivos, permitindo a busca por nome ou parte do nome.

Se você estiver procurando por um arquivo que contenha espaços entre as palavras, o nome deve ser colocado entre aspas, por exemplo, "documentação do projeto".

Além disso, é possível utilizar este programa para encontrar arquivos com uma extensão específica. Basta inserir o parâmetro "-wn .pdf" para buscar arquivos com extensão PDF, por exemplo, e utilizar o parâmetro "-ew" para especificar a extensão.

Os arquivos encontrados serão exibidos com seu caminho completo, tamanho em bytes e data da última modificação.

Para visualizar as informações dos arquivos de forma mais organizada, você também pode solicitar que o programa crie um arquivo .tsv contendo essas informações. Os dados serão apresentados em uma tabela simples.

O arquivo será salvo no mesmo diretório do programa. No entanto, é importante lembrar de renomear o arquivo solicitado anteriormente para evitar a sobrescrição indesejada.

## Parameters Argparse

- -v or --version : Optional[bool]
  - Versão do programa.
- -rd or --rootdir : str
  - Diretório raiz onde será realizada a busca dos arquivos.
- -wn or --wantedname : str
  - Nome, parte do nome do arquivo ou extensão do arquivo.
- -gf or --getfile : Optional[bool]
  - Salve o caminho dos arquivos em um arquivo.
        
## Parameters Argparse - Mutually Exclusive Group

- -rm or --rmatch : Optional[bool]
  - Verifica uma correspondência apenas no início da string.
- -rs or --rsearch : Optional[bool]
  - Verifica uma correspondência em qualquer lugar na string.
- -ew or --endswith : Optional[bool]
  - verifique a extensão do arquivo.

## Usando o Programa

Os exemplos a seguir contêm o ```argumento opcional -gf```, que serve para gerar um arquivo .tsv com o intuito de demonstração.


### Parametro ```-rm or --rmatch```
Para realizar a busca dos arquivos que começão com a palavra class ou com qualquer outra palavra, você pode utilizar o seguinte recurso:
```
python3 file_finder.py -rd /home/gnome/Documentos/workspace -gf -rm -wn class
```
 ![](https://github.com/yhagor/File_Finder/blob/main/docs/start_of_string.gif)
 
Ele permitirá encontrar arquivos cujos nomes comecem com qualquer palavra, tanto em letras maiúsculas quanto minúsculas.

Exemplo do arquivo .tsv:
```.tsv
File Finder Ver 1.0.0 processing
Root Directory : /home/gnome/Documentos/workspace
Wanted Name    : class
Regex Match    : True
Regex Search   : False
Ends With      : False

Full File Path                                                                Size Bytes         Data Modification
/home/gnome/Documentos/workspace/project_01/client/Script/Class_db.py           439268          2023.06.21 19:05:36
/home/gnome/Documentos/workspace/project_01/client/Script/Class_xyz.py           8486           2023.06.21 19:07:46
/home/gnome/Documentos/workspace/project_01/server/Script/Class_db.py           439268          2023.06.21 19:05:36
/home/gnome/Documentos/workspace/project_01/server/Script/Class_xyz.py           8486           2023.06.21 19:07:46
/home/gnome/Documentos/workspace/project_02/Script/Class_xyz.py                  8486           2023.06.21 19:07:46
/home/gnome/Documentos/workspace/project_03/Script/Class_db.py                  439268          2023.06.21 19:05:36
/home/gnome/Documentos/workspace/project_04/Script/Class_db.py                  439268          2023.06.21 19:05:36
/home/gnome/Documentos/workspace/project_05/Script/Class_db.py                  439268          2023.06.21 19:05:36
/home/gnome/Documentos/workspace/project_05/Script/Class_xyz.py                  8486           2023.06.21 19:07:46
/home/gnome/Documentos/workspace/project_06/Script/Class_db.py                  439268          2023.06.21 19:05:36
/home/gnome/Documentos/workspace/project_06/Script/Class_xyz.py                  8486           2023.06.21 19:07:46
/home/gnome/Documentos/workspace/repository/library/Class_db.py                 439268          2023.06.21 19:05:36
/home/gnome/Documentos/workspace/repository/library/Class_xyz.py                 8486           2023.06.21 19:07:46
```


### Parametro ```-rs or --rsearch```
É possível realizar a busca em qualquer lugar do nome do arquivo, procurando por uma parte específica da palavra pesquisada.
```
python3 file_finder.py -rd /home/gnome/Documentos/workspace -gf -rs -wn main
```
 ![](https://github.com/yhagor/File_Finder/blob/main/docs/anywhere_in_the_string.gif)
 
 Isso permitirá encontrar arquivos que contenham a sequência de caracteres desejada em qualquer posição do seu nome.
 
Exemplo do arquivo .tsv:
```.tsv
File Finder Ver 1.0.0 processing
Root Directory : /home/gnome/Documentos/workspace
Wanted Name    : main
Regex Match    : False
Regex Search   : True
Ends With      : False

Full File Path                                                                     Size Bytes         Data Modification
/home/gnome/Documentos/workspace/project_01/client/Script/basic_main_window.ui        7524           2022.09.23 09:48:12
/home/gnome/Documentos/workspace/project_02/Script/basic_main_window.ui               7524           2022.09.23 09:48:12
/home/gnome/Documentos/workspace/project_03/Script/basic_main_window.ui               7524           2022.09.23 09:48:12
/home/gnome/Documentos/workspace/project_04/Script/basic_main_window.ui               7524           2022.09.23 09:48:12
/home/gnome/Documentos/workspace/project_05/Script/basic_main_window.ui               7524           2022.09.23 09:48:12
/home/gnome/Documentos/workspace/project_06/Script/basic_main_window.ui               7524           2022.09.23 09:48:12
/home/gnome/Documentos/workspace/repository/library/basic_main_window.ui              7524           2022.09.23 09:48:12
```


### Parametro ```-ew or --endswith```
Por último, mas não menos importante, é possível realizar a busca por arquivos com uma extensão específica.
```
python3 file_finder.py -rd /home/gnome/Documentos/workspace -gf -ew -wn .webm
```
 ![](https://github.com/yhagor/File_Finder/blob/main/docs/file_extension.gif)

Isso permitirá filtrar os resultados para encontrar apenas os arquivos que correspondam à extensão desejada.

Exemplo do arquivo .tsv:
```.tsv
File Finder Ver 1.0.0 processing
Root Directory : /home/gnome/Documentos/workspace
Wanted Name    : .webm
Regex Match    : False
Regex Search   : False
Ends With      : True

Full File Path                                                                  Size Bytes         Data Modification
/home/gnome/Documentos/workspace/File_Finder/anywhere_in_the_string.webm          218366          2023.06.27 17:19:41
/home/gnome/Documentos/workspace/File_Finder/start_of_string.webm                 350248          2023.06.27 17:11:32
```
