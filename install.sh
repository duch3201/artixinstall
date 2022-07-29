#!/bin/bash

cfdisk /dev/sda

read -p 'ROOT ' rootpath
read -p 'SWAP ' swappath
read -p 'BOOT ' swappath

rootcmd='mkfs.ext4 -L ROOT /dev/sda2'
swapcmd='mkswap -L SWAP /dev/sda1'
bootcmd='mkfs.fat -F 32 /dev/sda4'

rootpathcomplete='${rootcmd//[/dev/sda2]/rootcmd}'
swapcmdpathcomplete='${swappath//[/dev/sda1]/swapcmd}'
bootpathcomplete='${swappath//[/dev/sda4]/bootcmd}'

echo $rootpathcomplete
echo $swapcmdpathcomplete
echo $bootpathcomplete

read -p "Press any key to resume ..."

mkfs.ext4 -L BOOT /dev/sda1
mkswap -L SWAP /dev/sda2  
mkfs.fat -F 32 /dev/sda4
fatlabel /dev/sda4 BOOT

basestrap /mnt base base-devel openrc elogind-openrc

basestrap /mnt linux-zen linux-firmware

fstabgen -U /mnt >> /mnt/etc/fstab
read -p "Press any key to resume ..."
