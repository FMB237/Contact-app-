#!/bin/bash
#This is a basg script to restore me DNS since i have some problems with due to me work with the swicth in school
sudo resolvectl dns wlo1 8.8.8.8 1.1.1.1 # This command will set me Dns to 8.8.8.8 and 1.1.1.1 So that i will able to install react-app
resolvectl status # Use to check up the DNS changes


