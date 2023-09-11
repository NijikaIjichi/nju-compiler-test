#!/bin/bash

trap '
  trap - INT # restore default INT handler
  kill -s INT "$$"
' INT

RED='\033[0;31m'
NC='\033[0m'
BOLD=$(tput bold)
NORMAL=$(tput sgr0)

cd $(dirname $0)

LABS=(3 5)

help(){
  echo "Usage: $0 [-r parser] [-l lab] [-c] [-t timeout]"
  echo "parser: the path to your parser, required for first running"
  echo "lab: ${LABS[*]}"
  echo "c: do not stop when test failed"
  echo "t: time limit for compile one test case, default 30s"
  if ! [ -z $1 ]
  then
    rm -f ./workdir/saved_binary.sh
    exit 1
  fi
  exit 0
}

TIMELIMIT=30

if [ -z $1 ]
then
  if [ -e ./workdir/saved_binary.sh ]
  then
    source ./workdir/saved_binary.sh
  fi
fi

while getopts r:l:t:ch opt 
do
 case "${opt}" 
 in
 r) RUN=${OPTARG};;
 l) LAB=${OPTARG};;
 c) CONTINUE=1;;
 t) TIMELIMIT=${OPTARG};;
 h) help;;
 esac
done

echo "Making(Updating) irsim"
make -C irsim

mkdir -p ./workdir

if [ -z $RUN ]
then
  help 1
fi

if ! [ -x $RUN ]
then
  echo "Error: file \"$RUN\" is not executable"
  rm -f ./workdir/saved_binary.sh
  exit 1
fi

if echo ${LABS[*]} | grep $LAB -w -q; then
  true;
else
  help 1
fi

echo "RUN=$RUN" > ./workdir/saved_binary.sh
echo "LAB=$LAB" >> ./workdir/saved_binary.sh
echo "CONTINUE=$CONTINUE" >> ./workdir/saved_binary.sh
echo "TIMELIMIT=$TIMELIMIT" >> ./workdir/saved_binary.sh

report_error(){
  echo -e "${RED}${BOLD} $dir test [$(basename $fcmm)]" "$1" "${NC}${NORMAL}"
  if [ -z $CONTINUE ]
  then
    read -p "Enter [c] to continue, or [Enter] to abort: " txt
    if [ -z "$txt" ] || [ $txt != 'c' ]
    then
      exit 1
    fi
  fi
}

if timeout --help > /dev/null 2>&1; then #if has `timeout` command
  PREFIX="timeout $TIMELIMIT ";
else
  echo "timeout command is not support in current environment"
  echo "running time will not be counted"
  PREFIX="";
fi;

base=(sample normal1 normal2 normal3 normal4 handmade)
extend1=(extend1)
extend2=(extend2)
extendboth=(extendboth)

run5(){
  cp $1 ./workdir/b.ir
  cp ${1%.ir}.json ./workdir/a.json
  rm -f ./workdir/a.ir

  if [ -e ${1%.ir}.cmm ]
  then
    cp ${1%.ir}.cmm ./workdir/a.cmm
  else
    rm -f ./workdir/a.cmm
  fi;
  
  let total=$total+1

  if $PREFIX $RUN ./workdir/b.ir ./workdir/a.ir 2>&1 > ./workdir/a.out; then
    true; #do nothing
  else
    report_error "RE or TLE"
  fi
}

test_group5(){
  for dir in $@; do
    for fcmm in ./tests/$dir/*.ir; do
      run5 $fcmm

      if ! [ -e ./workdir/a.ir ]
      then
        report_error "Should translate"
        continue
      fi;

      if $PREFIX python3 ./check3.py; then
        echo -n $dir test [$(basename $fcmm)] matched "("
        echo -n `cat ./workdir/a.ir | wc -l`/`cat ./workdir/b.ir | wc -l` "size, "
        echo `cat workdir/single`/`cat ${fcmm%.ir}.txt` "inst)"
        let passed=$passed+1
        let origin_inst=$origin_inst+`cat ${fcmm%.ir}.txt`
      else
        report_error "mismatch or TLE"
      fi
    done
  done
}

run3(){
  cp $1 ./workdir/a.cmm
  cp ${1%.cmm}.ir ./workdir/b.ir
  cp ${1%.cmm}.json ./workdir/a.json
  rm -f ./workdir/a.ir ./workdir/a.s
  
  let total=$total+1

  if $PREFIX $RUN ./workdir/a.cmm ./workdir/a.s ./workdir/a.ir 2>&1 > ./workdir/a.out; then
    true; #do nothing
  else
    report_error "RE or TLE"
  fi
}

test_group3(){
  for dir in $@; do
    for fcmm in ./tests/$dir/*.cmm; do
      run3 $fcmm

      if ! [ -e ./workdir/a.ir ]
      then
        report_error "Should translate"
        continue
      fi;

      if $PREFIX python3 ./check3.py; then
        echo -n $dir test [$(basename $fcmm)] matched "("
        echo -n `cat ./workdir/a.ir | wc -l`/`cat ./workdir/b.ir | wc -l` "size, "
        echo `cat workdir/single`/`cat ${fcmm%.cmm}.txt` "inst)"
        let passed=$passed+1
        let origin_inst=$origin_inst+`cat ${fcmm%.cmm}.txt`
      else
        report_error "mismatch or TLE"
      fi
    done
  done
}

echo -n 0 > workdir/count

passed=0
total=0
origin_inst=0

test_group$LAB ${base[*]}
test_group$LAB ${extend1[*]}
test_group$LAB ${extend2[*]}
test_group$LAB ${extendboth[*]}

echo PASSED $passed/$total

echo -n "irsim executes about "
cat workdir/count
echo "/$origin_inst instructions"

