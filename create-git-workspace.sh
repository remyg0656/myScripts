#!/usr/bin/bash

echo "===== Git Init ====="
git init

echo "===== Git config ====="
git config --global user.name "grosOrdi"
git config --global user.email "grosOrdi@ccgr.fr"

echo "===== Gestion des couleurs ====="
git config --global color.ui true

echo "===== Rajout des alias ====="
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.st status

echo "===== Rajout des alias ====="
git config --global core.editor emacs

echo "===== Config de l'editeur ====="
git config --global core.editor "C:\Users\gros-\AppData\Local\Programs\Microsoft VS Code\Code.exe"
 
echo ">>>>>>> fin de $0"
