# 🚩Operation Orchid - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `disk.img`
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

Download this disk image and find the flag.

Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

Download compressed disk image

### 🧪 Logic Extraction:

I used the `mmls` command to list the items.      
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ mmls disk.flag.img       
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)

```

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 411648                    
d/d 460:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 81: proc
d/d 82: dev
d/d 83: tmp
d/d 84: lib
d/d 87: var
d/d 96: usr
d/d 106:        bin
d/d 120:        sbin
d/d 466:        media
d/d 470:        mnt
d/d 471:        opt
d/d 472:        root
d/d 473:        run
d/d 475:        srv
d/d 476:        sys
d/d 2041:       swap
V/V 51001:      $OrphanFiles
```

```                                                                                             
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 411648 -r | grep flag
+ r/r * 1876(realloc):  flag.txt
+ r/r 1782:     flag.txt.enc
```
```                                                                                             
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 411648 1876          
Error extracting file from image (ext2fs_dir_open_meta: Error reading directory contents: 1876)
```
```                                                                                             
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 411648 1876 -r
Error extracting file from image (ext2fs_dir_open_meta: Error reading directory contents: 1876)
```
```                                                                                             
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat disk.flag.img -o 411648 1876 -r
           -0.881573            34.311733
 ```
```                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat disk.flag.img -o 411648 1782 -r
Salted__�ށ��e��B�J▒�c�$QE&$��4jM�KGeE�1�^Ȥ7� ���؎$�'%
```
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 411648 -r disk.flag.img | grep -C 5 flag

+ d/d 469:      usb
d/d 470:        mnt
d/d 471:        opt
d/d 472:        root
+ r/r 1875:     .ash_history
+ r/r * 1876(realloc):  flag.txt
+ r/r 1782:     flag.txt.enc
d/d 473:        run
d/d 475:        srv
d/d 476:        sys
d/d 2041:       swap
V/V 51001:      $OrphanFiles
```
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat -o 411648 disk.flag.img 1782 > enc_flag.txt
                                                                                              
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
disk.flag.img  enc_flag.txt
```
```                                                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ openssl aes256 -d -salt -in enc_flag.txt -out flag.txt -k unbreakablepassword1234567
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
40C72A99057F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:
                                                                                              
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
disk.flag.img  enc_flag.txt  flag.txt
                                                                                              
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ cat flag.txt 
picoCTF{h4un71ng_p457_5113beab}    
```

## Run 
.flag picoCTF{h4un71ng_p457_5113beab}    

