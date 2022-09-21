#!/usr/bin/sh

echo "============================================"
echo "= Debut du script d'install env VirtualBox ="
echo "============================================"

echo "=            Install de python3            ="
echo "============================================"

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user

echo "=             Install d'Ansible            ="
echo "============================================"
python3 -m pip install --upgrade --user ansible