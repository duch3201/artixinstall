import os
from secrets import choice
#import psutil
#import platform
import urllib.request
import time

os.system("cfdisk")

root = input("ROOT: ")
swap = input("SWAP: ")
boot = input("BOOT: ")

mkfs_root = "mkfs.ext4 -L ROOT "
mkfs_boot = "mkfs.fat -F 32 "
mkfs_swap = "mkswap -L SWAP "

print(mkfs_root + root)
print(mkfs_boot + boot)
print("fatlabel " + boot + " Boot")
print(mkfs_swap + swap)


os.system(mkfs_root + root)
os.system(mkfs_boot + boot)
os.system("fatlabel " + boot + " BOOT")
os.system(mkfs_swap + swap)

os.system("swapon /dev/disk/by-label/SWAP")
os.system("mount /dev/disk/by-label/ROOT /mnt")
os.system("mkdir /mnt/boot")
 os.system("mount /dev/disk/by-label/BOOT /mnt/boot")

print("installing base system...")
time.sleep(1)
os.system("basestrap /mnt base base-devel openrc elogind-openrc")

print("installing the Kernel")
os.system("basestrap /mnt linux-zen linux-firmware")
os.system("fstabgen -U /mnt >> /mnt/etc/fstab")

