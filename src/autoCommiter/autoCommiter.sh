#!/bin/bash

cd ~/PixelArt

read -p "How many times:" count
while [ $count -gt 0 ]
do
    echo "." >> dots
    git add dots
    git commit -am "Add a dot"
    ((count--))
done

git push origin main
