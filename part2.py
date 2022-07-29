import os
import time

def part2():
    #os.system("ln -sf /usr/share/zoneinfo/Region/City /etc/localtime")

    #os.system("hwclock --systohc")

    os.system("pacman -S nano")

    os.system("nano /etc/locale.gen")

    os.system("locale-gen")


    print("installing the bootloader")
    time.sleep(1)
    os.system("pacman -S grub os-prober efibootmgr")
    #os.system("grub-install --recheck /dev/sda") for bios systems
    os.system("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub")
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
        
    print("please modify /etc/hosts file")
    os.system("nano /etc/hosts")

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
    if usr_choice_de == "1":
        os.system("pacman -S plasma kde-applications")
    elif usr_choice_de == "2":
        os.system("pacman -S mate mate-extra system-config-printer blueman connman-gtk")
    elif usr_choice_de == "3":
        os.system("pacman -S gnome")
    elif usr_choice_de == "4":
        os.system("pacman -S xfce4 xfce4-goodies")
    elif usr_choice_de == "5":
        os.system("pacman -S lxqt")

    print("downloading display manager")
    os.system("pacman -S gdm-openrc")
    os.system("rc-update add gdm-openrc")

    print("installing usr packages")
    os.system("pacman -S firefox")
    os.system("pacman -S visual-studio-code")

    input("installation complete! press any key continue")
    os.system("sudo reboot")
              
part2()
