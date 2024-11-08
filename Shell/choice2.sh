#!/bin/bash

scriptName="~/choice(2).sh"
echo "Sourcing $scriptName. Script helping connection to servers"

site=""
machine=""
environment=""
tenant=""
cmd=""

listSite=("site1" "site2")
listMachine=("tableau1" "tableau2")
listEnv=("env1" "env2" "env2=3")

_selectTruc()
{
	select val in $@
	do
		echo "$val"
		return 0
	done
}

_processTenant()
{
	if [ $environment = "zmt" ]; then
		tenant="tenant"
	else
        tenant=$environment
	fi
	echo "$tenant"
}

_basicCheck()
{
	echo "site value: $site"
	echo "Machine value: $machine"
	echo "Env value: $environment"
	echo "Tenant value: $tenant"
	if [[-z "$site"] || [-z "$machine"] || [-z "$environment"] || [-z "$tenant"]]; then
		echo "T'es con ou quoi, il faut entrer 1,2 ..."
	fi
	return 0
}

choice2()
{
	echo "================================================"
	echo "=========    Start ~/bin/choice2.sh   ========="
	echo "================================================"
	echo "==                                            =="
	echo "==  Le but de ce script est de faire un ssh   =="
	echo "==      sur une machine                       =="
	echo "==                                            =="
	echo "==   Selectionner 1, 2, 3 ... pour le choix   =="
	echo "==             de l'environnement             =="
	echo "==                                            =="
	echo "================================================"

	site=$(_selectTruc ${listSite[@]})
	echo "	=> Site selected: $site"
	echo ""
	environment=$(_selectTruc ${listEnv[@]})
	echo "	=> Env selected: $environment"
	echo ""
	machine=$(_selectTruc ${listMachine[@]})
	echo "	=> Machine selected: $machine"
	echo ""
	tenant=$(_processTenant)
	echo "	=> Tenant selected: $tenant"
	echo ""

	_basicCheck()

	cmd="ssh $environment-$machine.truc-$tenant.$site.fr"
	echo "   ==> Run command: $cmd <== "
	echo "================================================"

	$cmd
	#read -p "Press key to continue.. " -n1 -s
	#echo "Exit Main"

	exit 0
}
