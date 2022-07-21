#!/bin/bash

dd=$(date +%F)

#echo $dd
d=/home/daniele/Scrivania/script
f=AXIOSDATABASE.FDB
scp -r root@172.16.200.200:/home/interbase/$f $d/$f
if [ "$?" != 0 ] ; then
	t="ERRORE: scp -r root@172.16.200.200:/home/interbase/$f $d/"
	echo "$t" | mail -s "INFOSCHOOL" server.backup@itisgrassi.edu.it
	exit $?
fi
scp -r $d/$f r740xd@172.16.200.155:/media/r740xd/SAMSUNG/INFOSCHOOL_VM/$dd-$f
if [ "$?" != 0 ] ; then
	t="ERRORE: scp -r $f r740xd@172.16.200.155:/media/r740xd/SAMSUNG/INFOSCHOOL_VM/$f"
	echo "$t" | mail -s "INFOSCHOOL" server.backup@itisgrassi.edu.it
	exit 0
fi
rm -R $d/$f
echo "Script infoschool eseguito senza errori" | mail -s "INFOSCHOOL" server.backup@itisgrassi.edu.it

