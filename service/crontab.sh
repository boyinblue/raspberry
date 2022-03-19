#!/bin/bash

exist="False"

python3 ../led/led.py g on

process=$(ps -ef)

if [[ "${process}" == *"python3 service.py"* ]]; then
	exist="True"
fi

if [ "${exist}" == "False" ]; then
	echo "Not exists. Run!"
	python3 service.py &
else
	echo "Already exists"
fi

#python3 ../led/led.py g off
