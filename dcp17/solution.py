#!/bin/python3
# -*- encoding: utf-8 -*-

def longestAbsolutePath(strPath: str) -> int:
    if (len(strPath) == 0):
        return 0
    maxStrpathLenght =0
    levelSistem = []
    records = strPath.split('\n')
    for tmp_record in records:
        tmp_deep_list = tmp_record.split('\t')
        tmp_deep_level = len(tmp_deep_list)
        tmp_record_length = len(tmp_deep_list[-1])
        if (tmp_deep_level > 1):
            tmp_record_length += levelSistem[tmp_deep_level-2]

        if (tmp_deep_list[-1].find('.') == -1):
            tmp_record_length += 1
        else:
            maxStrpathLenght = maxStrpathLenght if maxStrpathLenght > tmp_record_length else   tmp_record_length

        if (len(levelSistem) < tmp_deep_level):
            levelSistem.append(tmp_record_length)
        else:
            levelSistem[tmp_deep_level - 1] = tmp_record_length

    return maxStrpathLenght


print(longestAbsolutePath(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

"""
dir\n
\t  file1.txt
\t  cosamp
"""

"""
dir\n
\t  subdir1\n
\t  \t  file1.ext\n
\t  \t  subsubdir1\n
\t  subdir2\n
\t  \t  subsubdir2\n
\t  \t  \t  file2.ext
"""
