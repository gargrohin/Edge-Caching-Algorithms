#!/bin/bash

for (( i = 0; i < 100; i++ )); do
	wget http://content-server-1/test1/$i
done
