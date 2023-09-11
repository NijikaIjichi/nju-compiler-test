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

EXTEND_TYPES=(base extend1 extend2 both prf)
LABS=(3 4)

help(){
  echo "Usage: $0 [-r parser] [-e extend] [-l lab] [-ac]"
  echo "parser: the path to your parser, required for first running"
  echo "extend: ${EXTEND_TYPES[*]}"
  echo "lab: ${LABS[*]}"
  echo "a: test advance"
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

while getopts r:e:l:t:cah opt 
do
 case "${opt}" 
 in
 r) RUN=${OPTARG};;
 e) EXTEND_TYPE=${OPTARG};;
 l) LAB=${OPTARG};;
 c) CONTINUE=1;;
 a) ADVANCE=1;;
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

if echo ${EXTEND_TYPES[*]} | grep $EXTEND_TYPE -w -q; then
  true;
else
  help 1
fi

if echo ${LABS[*]} | grep $LAB -w -q; then
  true;
else
  help 1
fi

if ! [ -x $RUN ]
then
  echo "Error: file \"$RUN\" is not executable"
  rm -f ./workdir/saved_binary.sh
  exit 1
fi

echo "RUN=$RUN" > ./workdir/saved_binary.sh
echo "EXTEND_TYPE=$EXTEND_TYPE" >> ./workdir/saved_binary.sh
echo "LAB=$LAB" >> ./workdir/saved_binary.sh
echo "CONTINUE=$CONTINUE" >> ./workdir/saved_binary.sh
echo "ADVANCE=$ADVANCE" >> ./workdir/saved_binary.sh
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
advance=(advance1 advance2)
extend1=(extend1)
extend2=(extend2)
extendboth=(extendboth)
extendprf=(extendprf)

run(){
  cp $1 ./workdir/a.cmm
  cp ${1%.cmm}.json ./workdir/a.json
  rm -f ./workdir/a.ir ./workdir/a.s
  
  let total=$total+1

  if $PREFIX $RUN ./workdir/a.cmm ./workdir/a.s ./workdir/a.ir 2>&1 > ./workdir/a.out; then
    true; #do nothing
  else
    report_error "RE or TLE"
  fi
}

test_group(){
  for dir in $@; do
    for fcmm in ./tests/$dir/*.cmm; do
      run $fcmm

      if ! [ -e ./workdir/a.s ]
      then
        report_error "Should translate"
        continue
      fi;

      if $PREFIX python3 ./check$LAB.py; then
        if [ $LAB = 3 ]
        then
          echo -n $dir test [$(basename $fcmm)] matched "("
          cat workdir/single
          echo " inst)"
        else
          echo $dir test [$(basename $fcmm)] matched
        fi
        let passed=$passed+1
      else
        report_error "mismatch or TLE"
      fi
    done
  done
}

echo -n 0 > workdir/count

passed=0
total=0

test_group ${base[*]}

if ! [ -z $ADVANCE ]
then
  test_group ${advance[*]}
fi

if [ $EXTEND_TYPE == extend1 ]
then
  test_group ${extend1[*]}
fi

if [ $EXTEND_TYPE == extend2 ]
then
  test_group ${extend2[*]}
fi

if [ $EXTEND_TYPE = both ]
then
  test_group ${extend1[*]}
  test_group ${extend2[*]}
  test_group ${extendboth[*]}
fi

if [ $EXTEND_TYPE = prf ]
then
  test_group ${extend1[*]}
  test_group ${extend2[*]}
  test_group ${extendboth[*]}
  test_group ${extendprf[*]}
fi

echo PASSED $passed/$total

if [ $LAB = 3 ]
then
  echo -n "irsim executes about "
  cat workdir/count
  echo " instructions"
fi

