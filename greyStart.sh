# Restarts greyPlot.py when it stops
echo Starting greyPlot.py
until ./greyPlot.py ; do
    date
    echo "Restarting greyPlot exit code $?. " >&2
    sleep 1
done
