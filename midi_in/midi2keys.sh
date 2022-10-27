#!/bin/bash 
aseqdump -p "KOMPLETE KONTROL M32" | while IFS=" ," read src ev1 ev2 ch label1 data1 label2 data2 rest; do 
	case "$ev1 $ev2 $data1" in 
		"Note on 41" ) xdotool type a ;; 
		"Note on 42" ) xdotool type q ;; 
		"Note on 43" ) xdotool type s ;; 
		"Note on 44" ) xdotool type w ;; 
		"Note on 72" ) xdotool type   ;; 
	esac 
done
