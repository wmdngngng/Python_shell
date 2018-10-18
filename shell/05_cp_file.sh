#!/bin/bash

rm -rf merge_file merge_file.zip

mkdir merge_file

for line in `cat FileList_understand.txt`
do
    cp $line ./merge_file
done

zip -r merge_file.zip ./merge_file
