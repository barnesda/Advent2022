#!/bin/sh

mkdir -p input

for day in `seq 1 ${1}`
do
    echo "Downloading day $day input..."
    ./download_input.sh $day > "input/input$day.txt"

    # Be courteous
    sleep 1
done
