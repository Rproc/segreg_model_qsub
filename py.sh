#!/bin/bash



function pause(){
	read -p "$*"
}
sum=0
count=0
allFiles=()
loop=$(($1-1))
ctrl_dir=1
# echo $loop
path_local=/lab/users/renan.procopio/experimentos/output/
termino=*.txt
# files=(base 10-50-40 30-50-20 consolidation=100 decay=100 density=2 density=8 pred=4 pred=6 pred=8 predrandom=50 predrandom=100 steps=4 steps=8 steps2=4 steps2=8 steps3=4 steps3=8)
readarray -t files < array.txt
path_dir=/lab/users/renan.procopio/experimentos/newoutput/
path_results=results
path_shapes=shapes
path_plots=plots
path_tab=tabelas
path_dict=dictionaries
for i in "${files[@]}"; do
    term=$i
    # echo $term
    var_local="$path_local$i/output/";
    var_local="${var_local}"/matrix"*.txt";
    # echo $var_local;
    ctrl_dir=1
    allFiles=()
    count=0
    # $var_local=$var_local$termino
    for f in $var_local; do \
        FILENAME=`basename ${f%%}`;
        FILENAME2=`basename ${f%%.*}`;
        v=$FILENAME
        VAR1=${v::-4}
        # echo $VAR1
        # echo $FILENAME2
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
        count=$((count + 1))
        allFiles+=($VAR1)
        if [ $count == $1 ]
        then
            cd $PWD
            # pause
			# echo ${allFiles[*]}
            export allFiles
            bash -c 'echo "${allFiles[@]}"'
            printf "%s\n" "${allFiles[@]}" > files.txt

            # python test.py 2 "${allFiles[@]}"
            qsub -V -cwd -shell n ./runPython.sh $path_dir $path_local $term 250 50 1 1 "${allFiles[*]}";
            # /lab/users/renan.procopio/anaconda3/bin/python toCSV_SHP.py 
            count=0
            allFiles=()
            # pause 'Press [Enter] key to continue...'

        fi

    done
done
