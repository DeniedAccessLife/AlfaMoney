#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

if [ ! -f "venv/installed" ]; then
    if [ -f "requirements.txt" ]; then
        echo "Installing dependencies..."
        pip3 install -r requirements.txt
        touch venv/installed
    else
        echo "requirements.txt not found, skipping dependency installation."
    fi
else
    echo "Dependencies already installed, skipping installation."
fi

while true
do
	python3 AlfaMoney.py
	echo Restarting the program in 10 seconds...
	sleep 10
done