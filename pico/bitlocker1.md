bitlocker2john bitlocker-1.dd > bitlocker_hash.txt

john --wordlist=/usr/share/wordlists/rockyou.txt bitlocker_hash.txt

sudo cryptsetup bitlkOpen bitlocker-1.dd bitlocker-unlocked
sudo mount /dev/mapper/bitlocker-unlocked /mnt
ls /mnt

cat /mnt/flag.txt
