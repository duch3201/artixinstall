#!/bin/bash

cfdisk /dev/sda

mkfs.ext4 -L BOOT /dev/sda1
mkswap -L SWAP /dev/sda2  
mkfs.fat -F 32 /dev/sda4
fatlabel /dev/sda4 BOOT

basestrap /mnt base base-devel openrc elogind-openrc

basestrap /mnt linux-zen linux-firmware

fstabgen -U /mnt >> /mnt/etc/fstab
read -p "Press any key to resume ..."
