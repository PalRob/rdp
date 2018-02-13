"""Creates table of contents for Reddit Daily Programmer repository.
Goes throught local files within this repo and finds all files named
with template "dp_number_difficulty.extension".
Must be placed at the top of rdp derectory tree to work.

TODO:
With regex search throught file for 'Status: Done' comment to mark
the chellange finished, consider task unfinished otherwise;
Additionaly, log time of the last change in the file and of the last
walk throught the folder to skip reading through files that were not
changed since;
Find a way to deal with the errors in the rdp structure;
Add automatic insertion of the challenge name and shortened url
into docstring of the file, will requaire walking through the
reddit's page to log all of the challenges
"""

import os
import re

LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))
README = 'readme.md'
README_FILE = os.path.join(LOCAL_DIR, README)
EXTENTIONS = ['.py']
DIFFICULTY = {'easy': 0, 'int': 1, 'hard': 2}

def get_rdp_files(rdp_dir, extentions=EXTENTIONS, difficulty=DIFFICULTY):
    """Goes through rdp_dir and finds all rdp challenge files.
    Args:
        rdp_dir(str): path to local rdp repository;
        extentions(list): extentions of the challenge files. Defaults to
            global constant EXTENTIONS;
        difficulty(dict): dictionary in form
            {diff_level: col_number (starts at 0)}. Defaults to global
            constant DIFFICULTY.
    Returns:
        rdp_files(dict): dictionary in form
            {challenge number(int), [difficulty[0] or "", ...], ...}.
            Empty of no files were found.
    """
    difficulty = {'easy': 0, 'int': 1, 'hard': 2}

    difficulty_str = "|".join(list(difficulty.keys()))
    extentions_str = "|".join(extentions)
    # Three groups:
    # challenge number, difficulty, file extention
    regex_pattern = 'dp_(\d+)_({})({})'.format(difficulty_str, extentions_str)
    rdp_regex = re.compile(regex_pattern)

    rdp_files = {}

    for (dirpath, dirnames, filenames) in os.walk(rdp_dir):
        for filename in filenames:
            match = rdp_regex.search(filename)
            if match:
                path = os.path.join(dirpath, filename)
                num = int(match.group(1))
                diff = match.group(2)
                # Extention may be useful someday
                # ext = match.group(3)

                if not num in rdp_files:
                    rdp_files[num] = [""]*len(difficulty)
                rdp_files[num][difficulty[diff]] = path

    return rdp_files

def finished(path):
    """Checks if challenge in given path is finished.
    Args:
        path(str):
    Returns:
        (bool): Trues if challenge is finished, False otherwise
    """
    # TODO:
    # Write a fucntion that determines whether or not challenge is finished
    if not os.path.isfile(path):
        return False
    else:
        return True

def make_table(rdp_files, difficulty=DIFFICULTY):
    """Creates table from all found files in rdp_files
    Args:
        rdp_files(dict):
        difficulty(dict): dictionary in form
            {diff_level: col_number (starts at 0)}. Defaults to global
            constant DIFFICULTY.
    Returns:
        table(str): multiline string containing table of challanges
            with headers.
    """
    diff = sorted(difficulty, key=lambda i: difficulty[i])
    diff = " | ".join(diff)
    table_header = "   |{}".format(diff)
    num_of_col = len(difficulty)+1
    table_sep = "|".join(["---"]*num_of_col)

    challanges = []
    for i in range(min(rdp_files), max(rdp_files)+1):
        if i not in rdp_files:
            ch = " | " * (len(difficulty)-1)
        else:
            ch = " | ".join(
                ["" if x=="" else "done" if  finished(x)
                    else "unfinished" for x in rdp_files[i]])

        row = "{0} | {1}".format(i, ch)
        challanges.append(row)

    challanges = "\n".join(challanges)
    table = "\n".join((table_header, table_sep, challanges))

    return table


def make_readme(rdp_dir, readme_file=README_FILE):
    """Makes readme and writes it in readme_file.
    Args:
        rdp_dir(str): path to top of the local rdp repo
        readme_file(str): path to the readme file. Defaults to global
            constant README_FILE.
    Returns:
        None
    """
    header = ("# Reddit Daily Programmer\n",
        "Repository for [r/DailyProgrammer](https://www.reddit.com/r/dailyprogrammer) challenges.\n")
    header = "".join(header)

    table = make_table(get_rdp_files(rdp_dir))
    contents = "\n".join((header, table))
    with open(readme_file, 'w') as file:
        for line in contents:
            file.write(line)


if __name__ == '__main__':
    make_readme(LOCAL_DIR, README_FILE)
