#!/bin/bash
FOLDER='/var/www/cycling.bear.army/html/'
OUTFILE='batteries-climate-recent-values.csv'
WORKINGFILE='batteries-climate-working.csv'
YEAR=`date +%Y`
MONTH=`date +%m`
FULLDATE=`date +%Y-%m-%d`
cd $FOLDER
rm $OUTFILE
grep $FULLDATE batteries-climate-$YEAR-$MONTH.csv > $WORKINGFILE
head batteries-climate-$YEAR-$MONTH.csv -n 1 > $OUTFILE
tac $WORKINGFILE | sed '5q;d' | awk -F',' '{print "5 min,"$2"," $3}' >> $OUTFILE
tac $WORKINGFILE | sed '30q;d' | awk -F',' '{print "30 min,"$2"," $3}' >> $OUTFILE
tac $WORKINGFILE | sed '60q;d' | awk -F',' '{print "1 hr,"$2"," $3}' >> $OUTFILE
tac $WORKINGFILE | sed '120q;d' | awk -F',' '{print "2 hr,"$2"," $3}' >> $OUTFILE
tac $WORKINGFILE | sed '360q;d' | awk -F',' '{print "6 hr,"$2"," $3}' >> $OUTFILE
rm $WORKINGFILE