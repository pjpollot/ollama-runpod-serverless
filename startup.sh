#!/bin/sh


ollama serve &
sleep 5

python -u handler.py