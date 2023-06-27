Select Language : [:us:](https://github.com/yhagor/File_Finder/blob/main/README.md) [:brazil:](https://github.com/yhagor/File_Finder/blob/main/README-pt.md)
<h1 align="center">
  <p align="center">File Finder</p>
</h1>

This script was developed with the aim of assisting in file searching, allowing you to search by name or part of the name.

If you are looking for a file that contains spaces between the words, the name must be enclosed in quotation marks, for example, "project documentation".

Additionally, you can use this program to find files with a specific extension. Simply insert the parameter "-wn .pdf" to search for files with a PDF extension, for example, and use the parameter "-ew" to specify the extension.

The found files will be displayed with their full path, size in bytes, and date of last modification.

To view the file information in a more organized manner, you can also request the program to create a .tsv file containing this information. The data will be presented in a simple table format.

The file will be saved in the same directory as the program. However, it is important to remember to rename the previously requested file to avoid unwanted overwriting.

## Parameters Argparse

- -v or --version : Optional[bool]
  - Program Version.
- -rd or --rootdir : str
  - Root directory where the file search will be performed.
- -wn or --wantedname : str
  - Name, part of the file name, or file extension.
- -gf or --getfile : Optional[bool]
  - Save the file paths to a file.
        
## Parameters Argparse - Mutually Exclusive Group

- -rm or --rmatch : Optional[bool]
  - Check for a match only at the beginning of the string.
- -rs or --rsearch : Optional[bool]
  - Check for a match anywhere in the string.
- -ew or --endswith : Optional[bool]
  - Check the file extension.

## Using the Program.

The following examples include the ```optional argument -gf```, which is used to generate a .tsv file for demonstration purposes.


### Parameter ```-rm or --rmatch```
To perform the search for files that start with the word "class" or any other word, you can use the following feature:
```
python3 file_finder.py -rd /home/gnome/Documentos/workspace -gf -rm -wn class
```
 ![](https://github.com/yhagor/File_Finder/blob/main/docs/start_of_string.gif)
 
It will allow you to find files whose names start with any word, regardless of uppercase or lowercase letters.

File example .tsv:
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

### Parameter ```-rs or --rsearch```
It is possible to search anywhere in the file name, looking for a specific part of the searched word.
```
python3 file_finder.py -rd /home/gnome/Documentos/workspace -gf -rs -wn main
```
 ![](https://github.com/yhagor/File_Finder/blob/main/docs/anywhere_in_the_string.gif)
 
This will allow you to find files that contain the desired character sequence in any position of their name.
 
File example .tsv:
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

### Parameter ```-ew or --endswith```
Last but not least, it is possible to search for files with a specific extension.
```
python3 file_finder.py -rd /home/gnome/Documentos/workspace -gf -ew -wn .webm
```
 ![](https://github.com/yhagor/File_Finder/blob/main/docs/file_extension.gif)

This will allow you to filter the results to find only files that match the desired extension.

File example .tsv:
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
