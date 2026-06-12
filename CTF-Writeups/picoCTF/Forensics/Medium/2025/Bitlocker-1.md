# 🚩PcapPoisoning - picoCTF 2025

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `bitlocker-1.dd`
- **Key Skills And Tools:** file, bitlocker2john, reading data
---

## 🔍 Challenge 

Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!

Download the disk image here                                                                                                                                                    


### 🧪 Logic Extraction:

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file bitlocker-1.dd

bitlocker-1.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "-FVE-FS-", sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, sectors/track 63, heads 255, hidden sectors 124499968, FAT (32 bit), sectors/FAT 8160, serial number 0, unlabeled; NTFS, sectors/track 63, physical drive 0x1fe0, $MFT start cluster 393217, serial number 02020454d414e204f, checksum 0x41462020


```                                                                                                                                                   
                                                                                                                                                   
```                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ bitlocker2john -i bitlocker-1.dd > bitlocker.hash

Signature found at 0x3
Version: 8 
Invalid version, looking for a signature with valid version...

Signature found at 0x2195000
Version: 2 (Windows 7 or later)

VMK entry found at 0x21950c5

VMK encrypted with Recovery Password found at 0x21950e6
Searching AES-CCM from 0x2195102
Trying offset 0x2195195....
VMK encrypted with AES-CCM!!

VMK entry found at 0x2195241

VMK encrypted with User Password found at 2195262
VMK encrypted with AES-CCM

Signature found at 0x2c1d000
Version: 2 (Windows 7 or later)

VMK entry found at 0x2c1d0c5

VMK entry found at 0x2c1d241

Signature found at 0x373a000
Version: 2 (Windows 7 or later)

VMK entry found at 0x373a0c5

VMK entry found at 0x373a241

```

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ sudo mkdir /mnt/bitlocker
[sudo] password for kali: 
mkdir: cannot create directory ‘/mnt/bitlocker’: File exists
```

```                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ sudo bdemount -p 'jacqueline' bitlocker-1.dd /mnt/bitlocker
bdemount 20240502
```
```                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ sudo su
```
```
┌──(root㉿kali)-[/home/kali/Tools/CTF1]
└─# ls -la                     
total 102424
drwxrwxr-x 2 kali kali      4096 Jun 11 23:52 .
drwxrwxr-x 5 kali kali     12288 Jun 11 23:48 ..
-rw-rw-r-- 1 kali kali 104857600 Mar  6  2025 bitlocker-1.dd
-rw-rw-r-- 1 kali kali      1510 Jun 11 23:53 bitlocker.hash
```
```                                                                                                                                                            
┌──(root㉿kali)-[/home/kali/Tools/CTF1]
└─# cd /mnt/extracted_files
```
```           
┌──(root㉿kali)-[/mnt/extracted_files]
└─# ls -la
total 13
drwxrwxrwx 1 root root 4096 Jul 15  2024  .
drwxr-xr-x 4 root root 4096 Jun 11 22:25  ..
drwxrwxrwx 1 root root    0 Jul 15  2024 '$RECYCLE.BIN'
-rwxrwxrwx 1 root root   43 Jul 15  2024  flag.txt
drwxrwxrwx 1 root root 4096 Jul 15  2024 'System Volume Information'
```
```                                                                                                                                                            
┌──(root㉿kali)-[/mnt/extracted_files]
└─# cat /mnt/extracted_files/flag.txt
picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1} 
```
## Run 
.flag picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}                                                                                                                                                            

