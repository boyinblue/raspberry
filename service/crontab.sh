#!/bin/bash

exist="False"

python3 ../led/led.py g on

process=$(ps -ef)

for line in ${process}
do
	if [[ "${line}" == *"python3 service.py"* ]]; then
		exist="True"
	fi
done

if [ "${exist}" == "False" ]; then
	python3 service.py &
fi

#python3 ../led/led.py g off
