PYSRC=/opt/miniconda3/envs/common_libs/bin/python3
PYFILE=/Users/yash/personal_projects/crypto_monitor/src/crazy_crypto.py
LOGFILE=/Users/yash/personal_projects/crypto_monitor/out/crypto_logs.txt

if test -f "$LOGFILE"; then
    rm -rf /$LOGFILE
    $PYSRC $PYFILE >> $LOGFILE && chmod u-w $LOGFILE && open $LOGFILE
else
    $PYSRC $PYFILE >> $LOGFILE && chmod u-w $LOGFILE && open $LOGFILE
fi