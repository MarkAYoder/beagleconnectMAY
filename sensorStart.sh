# Restarts sensorPlot.py when it stops
echo Starting sensorPlot.py
until ./sensorPlot.py ; do
    date
    echo "Restarting sensorPlot exit code $?. " >&2
    sleep 1
done
