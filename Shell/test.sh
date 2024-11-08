#!/bin/sh

shopt -s extglob    # comment out this line to test unset extglob.
shopt -p extglob

s1="*foo*"; s2="*bar*"
list=("site1" "site2" "quit")

site="toto"
string="*foo*"
string="*foo*|*bar*"
string='@(*foo*|*bar)'
string='*@(foo|bar)*'
printf "%s\n" "$string"

function showMenu() {
    PS3=$1
    shift
    options=("$@")
    select opt in "${options[@]}"
    do
        case $opt in
            ${options[0]})
                echo "A: ${options[0]}"
                break
                ;;
            ${options[1]})
                echo "B: ${options[1]}"
                break
                ;;
            ${options[2]})
                echo "C: ${options[2]}"
                break
                ;;
            ${options[3]})
                echo "D: ${options[3]}"
                break
                ;;
            *)  # just loop ...
                ;;
        esac
    done
	echo "REPLY: $REPLY"
}

function showMenu2() {
    PROMPT=$1
    shift
    options=("$@")
    numOptions=${#options[@]}
    read -p "${PROMPT}: " response
	echo "AAA"
    echo "${options[$response]}"
	echo "BBB"
}

function oracle () {
COLORS=("red" "blue" "green" "yellow")

ORACLE_SID=''
PS3='Select target (test) database being refreshed: '
#
while [[ $ORACLE_SID = "" ]]; do
  select ORACLE_SID in "${COLORS[@]}" ; do
    if [[ $ORACLE_SID = "" ]]; then
         echo
         echo "Please enter a valid number.  Retry.";
         echo
    elif [[ $ORACLE_SID = "None of the above" ]]; then
         exit ;
    else {
          break ;
         }
    fi
    break
    done
done
echo "ORACLE_SID: $ORACLE_SID"
}

function mySelect () {

currentItem=''
PS3='Select a site: '

items=("$@")

while [[ $currentItem = "" ]]; do
  select currentItem in "${items[@]}" ; do
    if [[ $currentItem = "" ]]; then
         echo
         echo "Please enter a valid number.  Retry.";
         echo
    elif [[ $currentItem = "None of the above" ]]; then
         exit ;
    else {
          break ;
         }
    fi
    break
    done
	set currentItem
done
echo "$currentItem"
#return "$currentItem";
}
main ()
{
sites=("site1" "site2")
site=$(mySelect "${sites[@]}")
#oracle(@COLORS)
echo "Site FINAL: $site"

echo "Enter selectMachine"
machines=("tableau1" "tableau2")
machine=$(mySelect "${machines[@]}")
echo "Machine FINAL: $machine"

 echo "ssh $site-$machine.truc.fr"
 eval "ssh $site-$machine.truc.fr"
#main2
}

main2()
{
COLORS=("red" "blue" "green" "yellow")
COLOR=$(showMenu 'Choose a color' "${COLORS[@]}")
# if user inputs a '1', then COLOR would be blue
echo "Fuck Color => $COLOR"
}
main


function toto() {
	while IFS= read -r choice; do
		case $choice in
			"$s1"|"$s2" )   printf 'A first choice %-20s' "$choice"; ;;&
			$string )   printf 'String  choice %-20s' "$choice"; ;;&
			$s1|$s2 )   printf 'Two val choice %-20s' "$choice"; ;;
			*)      printf 'A Bad  choice! %-20s' "$choice"; exit; ;;
		esac
		echo "XXXXX"
	done
}