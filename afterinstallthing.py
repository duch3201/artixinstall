import os

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

os.system("nano etc/hosts")

os.system("pacman -S grub os-prober efibootmgr")
#os.system("grub-install --recheck /dev/sda") for bios systems
os.system("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")

print("installing dhcp")
os.system("pacman -S dhclient")


print("installing connman")
os.system("pacman -S connman-openrc connman-gtk")
os.system("rc-update add connmand")

print("installing xorg")
os.system("pacman -S xorg")

print("installing the desktop enviroment")

os.system("pacman -S gnome gnome-extra")

print("downloading display manager")
os.system("pacman -S gdm-openrc")
os.system("rc-update add gdm-openrc")

print("installing netorkmanager")
os.system("pacman -S netwokmanager netwokmanager-openrc")
os.system("rc-update NetworkManager add")

print("installing usr packages")
os.system("pacman -S firefox")
os.system("git clone https://aur.archlinux.org/visual-studio-code-bin.git")
os.chdir("visual-studio-code-bin")

#os.system("pacman -S visual-studio-code")

input("installation complete! press any key continue")
os.system("exit")
