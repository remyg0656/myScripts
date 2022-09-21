#!/bin/bash

echo "Ssh connection"
site=""
machne=""
debug=1
s1="pcy"; s2="noe" 
sites=("pcy" "noe")
machines=("tableau-gw" "tableau-wk" "et1" "ws1" "ws2" "haproxy1" "haproxy2")


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
			"pcy")
				echo "===> PACY selected"
				site=$val
				echo ""
				return 0
				;;
			"noe")
				echo "===> NOE selected"
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
	echo "Choix: \"pcy\" \"noe\" \"quit\""
	sites=("pcy" "noe" "quit")
	select val in "${sites[@]}"; do
		case $val in
			"pcy")
				echo "===> PACY selected"
				site=$val
				echo ""
				return 0
				;;
			"noe")
				echo "===> NOE selected"
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
	echo "Choix: \"tableau-gw\" \"tableau-wk\" \"et1\" \"ws1\" \"ws2\" \"haproxy1\" \"haproxy2\""
	sites=("tableau-gw" "tableau-wk" "et1" "ws1" "ws2" "haproxy1" "haproxy2")
	select val in "${sites[@]}"; do
		case $val in
			"tableau-gw")
				echo "===> tableau-gw selected"
				echo ""
				machne=$val
				return 0
				;;
			"tableau-wk")
				echo "===> tableau-wk selected"
				echo ""
				machne=$val
				return 0
				;;
			"et1")
				echo "===> et1 selected"
				echo ""
				machne=$val
				return 0
				;;
			"ws1")
				echo "===> ws1 selected"
				echo ""
				machne=$val
				return 0
				;;
			"ws2")
				echo "===> ws2 selected"
				echo ""
				machne=$val
				return 0
				;;
			"haproxy1")
				echo "===> haproxy1 selected"
				echo ""
				machne=$val
				return 0
				;;
			"haproxy2")
				echo "===> haproxy2 selected"
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