#!/bin/bash

echo "Ssh connection"
site=""
machne=""
debug=1
s1="Site1"; s2="Site2" 
sites=("Site1" "Site2")
machines=("tableau1" "tableau2")


mySelect () {
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
}

selectItem2()
{
	echo "enter selectItem2"
	#read choice
	select val in "$@"; do
	echo "A"
	read choice
	echo "B"
	case $choice in
		
		$s1|$s2 )    
			echo "You selected: $choice"; 
		;;  # not "$s1"|"$s2"
		* )
			echo "A Bad  choice! $choice";
			exit;	
		;;
	esac
	done
	echo "exit selectItem2"
}

selectItem()
{
	echo "enter selectItem"
	
#	for item in $@
#	do
#		echo "Current item" $item
#	done
	
	select val in "$@"; do
		case $val in
			"Site1")
				echo "===> Site1 selected"
				site=$val
				echo ""
				return 0
				;;
			"Site2")
				echo "===> Site2 selected"
				site=$val
				echo ""
				return 0
				;;
			"quit")
				echo "===> Exit requested"
				exit
				;;
			*) echo "Invalid option $REPLY";;
		esac
	done
	echo "exit selectItem"
}

selectSite()
{
	echo "Enter selectSite"
	echo "Choix: \"Site1\" \"Site2\" \"quit\""
	sites=("Site1" "Site2" "quit")
	select val in "${sites[@]}"; do
		case $val in
			"Site1")
				echo "===> Site1 selected"
				site=$val
				echo ""
				return 0
				;;
			"Site2")
				echo "===> Site2 selected"
				site=$val
				echo ""
				return 0
				;;
			"quit")
				echo "===> Exit requested"
				exit
				;;
			*) echo "Invalid option $REPLY";;
		esac
	done
	echo "Exit selectSite"

}

selectMachine()
{
	echo "Enter selectMachine"
	echo "Choix: \"tableau1\" \"tableau2\""
	sites=("tableau1" "tableau2")
	select val in "${sites[@]}"; do
		case $val in
			"tableau1")
				echo "===> tableau1 selected"
				echo ""
				machne=$val
				return 0
				;;
			"tableau2")
				echo "===> tableau2 selected"
				echo ""
				machne=$val
				return 0
				;;

			"quit")
				echo "===> Exit requested"
				quit
				;;
			*) echo "Invalid option $REPLY";;
		esac
	done
	echo "Exit selectMachine"

}


main()
{
	echo "Enter Main"
	mySelect ${list[@]}
	mySelect ${list[@]}
#	selectItem(@list)
#	selectSite
#	selectMachine
	echo "site value: $site"
	echo "Machine value: $machne"
	echo "Exit Main"
	$SHELL
}

main