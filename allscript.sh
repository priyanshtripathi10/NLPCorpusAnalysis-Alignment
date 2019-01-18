python final_para2tokensentence.py
MYPATH=`pwd`
export CTK=$MYPATH/champollion-1.2

gcc -o align-eng-hnd.out align-eng-hnd.c 

cd pre-process
./comp.sh replace-stanford-punct

## Testing champollian installation
echo "Testing champollian installation"

cd $CTK
var=`./test_installation | awk '{print $4}'`;
if [ $var = "good." ] ; then
 echo "Installation is good."
else
 echo "Check the installation"
 echo "Exitting"
 exit;
fi
cat ../../sample-data/eng_output > eng_output
cat ../../sample-data/hnd_output > hnd_output
cd ../
./run_sentence_alignment.sh eng_output hnd_output
