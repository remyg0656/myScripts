#!/bin/bash

CURRENT=`pwd`
echo "Current Directory is $CURRENT"
DIRNAME=`dirname $0`
echo "MYDIRNAME Directory is $DIRNAME"
MYWORKDIR=$CURRENT"/"$DIRNAME
echo "MYWORKDIR Directory is $MYWORKDIR"
BUILDDIR=$MYWORKDIR"/build"
echo "BUILDDIR Directory is $BUILDDIR"
DISTDIR=$MYWORKDIR"/dist"
echo "DISTDIR Directory is $DISTDIR"

EXENAME="mouseMove"

if [[ -d $BUILDDIR ]]; then
    echo "Removing old $BUILDDIR"
    rm -fr $BUILDDIR
fi

if [[ -d $DISTDIR ]]; then
    echo "Removing old $DISTDIR"
    rm -fr $DISTDIR
fi

MOVESPEC=$MYWORKDIR"/"$EXENAME".spec"
if [[ -e $MOVESPEC ]]; then
    echo "Removing old $MOVESPEC"
    rm -f  $MOVESPEC
fi

pyinstaller.exe $MYWORKDIR"/../"$EXENAME".py"    \
                --noconsole     \
                --noconfirm     \
                --onefile       \
                --clean         \
                --distpath $DISTDIR     \
                --workpath $BUILDDIR    \
                --name $EXENAME

$DISTDIR/$EXENAME.exe  &
