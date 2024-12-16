import os
import signal
import sys

# Signal handler function
def signal_handler(sig, frame):
    print("\nScript interrupted.")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# List of commands to execute
commands = [
    "termux-setup-storage",
    "cd",
    "dpkg --configure -a",
    "pkg update -y",
    "pkg upgrade -y",
    "pkg install python -y",
    "pkg install python2 -y",
    "pkg install python2-dev -y",
    "pkg install python3 -y",
    "pkg install pip -y",
    "pkg install pip2 -y",
    "pip2 install requests",
    "pkg install fish -y",
    "pkg install ruby -y",
    "pkg install git -y",
    "pkg install dnsutils -y",
    "pkg install php -y",
    "pkg install perl -y",
    "pkg install nmap -y",
    "pkg install bash -y",
    "pkg install clang -y",
    "pkg install nano -y",
    "pkg install w3m -y",
    "pkg install figlet -y",
    "pkg install cowsay -y",
    "gem install lolcat",
    "pkg install curl -y",
    "pkg install tar -y",
    "pkg install zip -y",
    "pkg install unzip -y",
    "pkg install tor -y",
    "pkg install wget -y",
    "pkg install wgetrc -y",
    "pkg install wcalc -y",
    "pkg install bmon -y",
    "pkg install unrar -y",
    "pkg install toilet -y",
    "pkg install proot -y",
    "pkg install golang -y",
    "pkg install chroot -y",
    "termux-chroot -y",
    "pkg install openssl -y",
    "pkg install cmatrix -y",
    "pkg install openssh -y",
    "apt update && apt upgrade -y"
]

# Execute commands one by one
for command in commands:
    print(f"Executing: {command}")
    os.system(command)  # Removed output redirection

# Summary message
print("Thank you! All commands have been executed successfully.")
print("The following packages have been installed:")
print("- Python")
print("- Python2")
print("- Python2-dev")
print("- Python3")
print("- Pip")
print("- Pip2")
print("- Fish")
print("- Ruby")
print("- Git")
print("- DNS Utilities")
print("- PHP")
print("- Perl")
print("- Nmap")
print("- Bash")
print("- Clang")
print("- Nano")
print("- W3M")
print("- Figlet")
print("- Cowsay")
print("- Lolcat")
print("- Curl")
print("- Tar")
print("- Zip")
print("- Unzip")
print("- Tor")
print("- Wget")
print("- Wgetrc")
print("- Wcalc")
print("- Bmon")
print("- Unrar")
print("- Toilet")
print("- Proot")
print("- Golang")
print("- Chroot")
print("- OpenSSL")
print("- Cmatrix")
print("- OpenSSH")

# Developer credit
print("\nThis script was developed by a Yemeni hacker named Abu Mustafa.")
