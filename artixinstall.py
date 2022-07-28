import os
from secrets import choice
#import psutil
#import platform
import urllib.request
import time

def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False

def eth():
    os.system("clear")
    print("please connect the cable and press enter")
    input("press enter to continue")
    if connect() == True:
        print("connected to internet, continuing install")
    elif connect() == False:
        print("failed to connect")
        print("retrying")
        eth()

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


#os.system(mkfs_root + root)
#os.system(mkfs_boot + boot)
#os.system("fatlabel " + boot + " BOOT")
#os.system(mkfs_swap + swap)

os.system("swapon /dev/disk/by-label/SWAP")
os.system("mount /dev/disk/by-label/ROOT /mnt")
os.system("mkdir /mnt/boot")
os.system("mount /dev/disk/by-label/BOOT /mnt/boot")

if connect() == True:
    pass
elif connect() == False:
    #Has_internet_connection = False
    print("you are not connected to the internet")
    eth()

print("installing base system...")
time.sleep(1)
os.system("basestrap /mnt base base-devel openrc elogind-openrc")

print("installing the Kernel")
print("1.linux")
print("2.linux-zen")
print("3.linux-lts")
kernel_choice = input(":")
if kernel_choice == 1:
    os.system("basestrap /mnt linux linux-firmware")
if kernel_choice == 2:
    os.system("basesystem /mnt linux-zen linux-firmware")
if kernel_choice == 3:
    os.system("basesystem /mnt linux-lts linux-firmware")

os.system("fstabgen -U /mnt >> /mnt/etc/fstab")

os.system("artix-chroot /mnt # formerly artools-chroot")

os.system("ln -sf /usr/share/zoneinfo/Region/City /etc/localtime")

os.system("pacman -S nano")

os.system("nano /etc/locale.gen")

os.system("locale-gen")


print("installing the bootloader")
time.sleep(1)
os.system("pacman -S grub os-prober efibootmgr")
#os.system("grub-install --recheck /dev/sda") for bios systems
os.system("grub-install --target=x86_86-efi --efi-directory=/boot --bootloader-id=grub")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")

print("adding users")
usrname = input("Username: ")
os.system("useradd -m " + usrname)
os.system("passwd " + usrname)

print("set root password")
os.system("passwd")

print("set Hostname")
hostname = input(": ")
with open("/etc/hostname", 'w') as hostname_file:
    hostname_file.write(hostname)

with open("/etc/hosts", 'w') as hosts:
    data = ""
    data[3] = "127.0.0.1       localhost"
    data[4] = "::1             localhost"
    data[5] = "127.0.1.1       " + usrname + "." + hostname + "  " + hostname
    hosts.writelines( data )

print("installing dhcp")
os.system("pacman -S dhclient")


print("installing connman")
os.system("pacman -S connman-openrc connman-gtk")
os.system("rc-update add connmand")

print("installing xorg")
os.system("pacman -S xorg")

print("installing the desktop enviroment")
print("1. kde 2.mate 3.gnome 4.xfce4 5.lxqt")
usr_choice_de = input(": ")
if usr_choice_de == 1:
    os.system("pacman -S plasma kde-applications")
elif usr_choice_de == 2:
    os.system("pacman -S mate mate-extra system-config-printer blueman connman-gtk")
elif usr_choice_de == 3:
    os.system("pacman -S gnome")
elif usr_choice_de == 4:
    os.system("pacman -S xfce4 xfce4-goodies")
elif usr_choice_de == 5:
    os.system("pacman -S lxqt")

print("downloading display manager")
os.system("pacman -S sddm-openrc or sddm-runit or sddm-s6 or sddm-suite66")

print("installing usr packages")
os.system("pacman -S firefox")
os.system("pacman -S visual-studio-code")

input("installation complete! press any key continue")
os.system("sudo reboot")
