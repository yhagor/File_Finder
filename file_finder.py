#!python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import re

from os.path import realpath, isdir
from datetime import datetime
from prettytable import PrettyTable, PLAIN_COLUMNS
from typing import (List, Union)

PROGRAM_NAME     = 'File Finder'
MAJOR_VERSION    = '1'
MINOR_VERSION    = '0'
REVISION_VERSION = '0'

PROGRAM_VERSION = f"{MAJOR_VERSION}.{MINOR_VERSION}.{REVISION_VERSION}"

FILE_PATH = realpath(__file__).replace('.py','.tsv') 

def save_file(root_directory : str, wanted_name : str, rmatch : bool, rsearch : bool, ends_with : bool , table : PrettyTable) -> None:
    """
        Method responsible for saving the file table to a file.

        Parameters
        ----------         
        root_directory : str 
            root directory.

        wanted_name : str
            Name or part of file name.
        
        rmatch : bool
            Checks for a match only at the beginning of the string.
        
        rsearch : bool
            Checks for a match anywhere in the string.
        
        ends_with : bool
            Check the file extension.        
        
        table : PrettyTable
            Object containing tables in a simple way and in a non-graphical
            format with the information of the files.
    """
    with open(FILE_PATH, 'w') as f:
        f.write(f"{PROGRAM_NAME} Ver {PROGRAM_VERSION} processing\n")
        f.write(f"Root Directory : {root_directory}\n")
        f.write(f"Wanted Name    : {wanted_name}\n")
        f.write(f"Regex Match    : {rmatch}\n")
        f.write(f"Regex Search   : {rsearch}\n")
        f.write(f"Ends With      : {ends_with}\n\n")
        f.write(table.get_string())
        f.write("\n\n")

    print(f"\nThe log file is in: {FILE_PATH}")

def get_table(found_files : List[List[Union[str, int]]]) -> PrettyTable:
    """
        Method that will assemble the table with the information from the files.

        Parameters
        ----------
        found_files : List[List[Union[str, int]]]
            List containing the complete file path,
            size in Bytes and modification date of each duplicate file found.

        Returns
        -------
        PrettyTable
            Object containing tables in a simple way and in a non-graphical
            format with the information of the files.
    """
    table = PrettyTable(["Full File Path", "Size Bytes", "Data Modification"])
    
    table.align["Full File Path"]    = "l"
    table.align["Size Bytes"]        = "c"
    table.align["Data Modification"] = "c"

    table.set_style(PLAIN_COLUMNS)

    table.add_rows(found_files)

    return table   

def processa(root_directory : str, wanted_name : str, get_file : bool, rmatch : bool, rsearch : bool, ends_with : bool) -> None:
    """
        Method where files are searched.      
        
        Parameters
        ----------
        root_directory : str
            Root directory where the search for files will be performed.
        
        wanted_name : str
            Name or part of file name.

        get_file : bool
            Value that indicates whether to save the information to a file.
        
        rmatch : bool
            Checks for a match only at the beginning of the string.
        
        rsearch : bool
            Checks for a match anywhere in the string.
        
        ends_with : bool
            Check the file extension.
    """
    if ends_with:
        fetch_type = lambda name: name.endswith((wanted_name.lower(), wanted_name.upper()))

    else:
        wanted = re.compile(wanted_name, re.IGNORECASE)
        if rmatch:
            fetch_type = lambda name: wanted.match(name)
        
        else:
            fetch_type = lambda name: wanted.search(name)

    
    print("Searching the files !\n")

    found_files = []
    searched_files = 0
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if fetch_type(filename):
                file_path = os.path.join(dirpath, filename)
                try:
                    stats = os.stat(file_path)
                    data_modification = datetime.fromtimestamp(stats.st_mtime).strftime("%Y.%m.%d %H:%M:%S")
                    size = stats.st_size
                except:
                    size = "-"
                    data_modification = "-"

                print(f"{file_path} - {size} Bytes - {data_modification}")
                found_files.append([file_path, size, data_modification])
            
            searched_files += 1

    if get_file:
        if found_files:
            found_files = sorted(found_files, key = lambda file: file[0])
            table = get_table(found_files)
            save_file(root_directory, wanted_name, rmatch, rsearch, ends_with, table)
    
        else:     
            print("The file was not generated because no duplicate files were found.")    

    print(f"\nFound {len(found_files)} out of {searched_files} files.")
    print("Finished process !")  

def validator(root_directory : str) -> None:
    """
        Method used to evaluate the existence of the root directory.
        
        Parameters
        ----------
        root_directory : str
            Root directory where the search for files will be performed.
    """
    if not isdir(root_directory):
        print("Root directory not found.")
        sys.exit(1)

def print_parameters(root_directory : str, wanted_name : str, get_file : bool, rmatch : bool, rsearch : bool, ends_with : bool) -> None:
    """
        Method that will display the options chosen when running the software.
        
        Parameters
        ----------
        root_directory : str
            Root directory where the search for files will be performed.
        
        wanted_name : str
            Name or part of file name.

        get_file : bool
            Value that indicates whether to save the information to a file.
        
        rmatch : bool
            Checks for a match only at the beginning of the string.
        
        rsearch : bool
            Checks for a match anywhere in the string.
        
        ends_with : bool
            Check the file extension.
    """
    print(f"\n{PROGRAM_NAME} Ver {PROGRAM_VERSION} processing")
    print(f"Root Directory : {root_directory}")
    print(f"Wanted Name    : {wanted_name}")
    print(f"Get File       : {FILE_PATH}") if get_file else print(f"Get File       : {get_file}")
    print(f"Regex Match    : {rmatch}")
    print(f"Regex Search   : {rsearch}")
    print(f"Ends With      : {ends_with}\n")

def main() -> None:
    """
        This script was developed in order to help in the search for files, doing the search by name or part of the name.

        If you are looking for a file that has spaces between words then the name must be in quotes "project documentation".

        You can also use this program to find files with a specific type of extension just put it in -wn .pdf and use -ew.

        Parameters Argparse
        -------------------
        -v or --version : Optional[bool]
            Program version.

        -rd or --rootdir : str
            Root directory where the search for files will be performed.

        -wn or --wantedname : str
            Name or part of file name.

        -gf or --getfile : Optional[bool]
            Save files path to one file.
        
        Parameters Argparse Mutually Exclusive Group
        --------------------------------------------
        -rm or --rmatch : Optional[bool]
            Checks for a match only at the beginning of the string.

        -rs or --rsearch : Optional[bool]
            Checks for a match anywhere in the string.

        -ew or --endswith : Optional[bool]
            Check the file extension.
    """
    parser = argparse.ArgumentParser(description='Fetch File')
    parser.add_argument("-v", "--version", action="version", version="%(prog)s " + f"Ver {PROGRAM_VERSION} processing.")
    parser.add_argument("-rd", "--rootdir", dest='root_directory', type=str, help='Root directory where the search for files will be performed.', required=True, default="")
    parser.add_argument("-wn", "--wantedname", dest='wanted_name', type=str, help='Name or part of file name, If you are looking for a file that has spaces between words then the name must be in quotes "project documentation".', required=True, default="")
    parser.add_argument("-gf", "--getfile", dest='get_file', help="Save files path to one file.", required=False, action="store_true")

    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument("-rm", "--rmatch", action="store_true", help="Checks for a match only at the beginning of the string.")
    group.add_argument("-rs", "--rsearch", action="store_true", help="checks for a match anywhere in the string.")
    group.add_argument("-ew", "--endswith", dest="ends_with", action="store_true", help="Check the file extension.")

    args = parser.parse_args()

    print_parameters(args.root_directory, args.wanted_name, args.get_file, args.rmatch, args.rsearch, args.ends_with)

    validator(args.root_directory)
    
    processa(args.root_directory, args.wanted_name, args.get_file, args.rmatch, args.rsearch, args.ends_with)

if __name__ == "__main__":
    main()