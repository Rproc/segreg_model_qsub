#!/bin/bash

path_dir=$1
path_local=$2;
term=$3;
count=0
allFiles=()
ctrl_dir=1
termino=*.txt
path_results=results
path_shapes=shapes
path_plots=plots
path_tab=tabelas
path_dict=dictionaries

var_local="$path_local$term/output/";
var_local="${var_local}"/matrix"*.txt";

for f in $var_local; do \
    FILENAME=`basename ${f%%}`;
    FILENAME2=`basename ${f%%.*}`;
    v=$FILENAME
    VAR1=${v::-4}
    if [ $ctrl_dir == 1 ]
    then
    	mkdir $path_dir/$term
        mkdir $path_dir/$term/$path_shapes
        mkdir $path_dir/$term/$path_results
        mkdir $path_dir/$term/$path_plots
        mkdir $path_dir/$term/$path_results/$path_tab
        mkdir $path_dir/$term/$path_results/$path_dict
    	ctrl_dir=0
    fi
    allFiles+=($VAR1)
    if [ $count == $4 ]
    then
        export allFiles
        bash -c 'echo "${allFiles[@]}"'
        /lab/users/renan.procopio/anaconda3/bin/python toCSV_SHP.py $path_dir $path_local $term 250 50 1 1 AGENT_RED AGENT_YELLO AGENT_BLUE AGENT_CYAN "${allFiles[@]}";
        count=0
        allFiles=()
    fi
    count=$((count + 1))


done

