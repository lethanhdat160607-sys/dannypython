# 🚩Operation Oni - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `disk.img`
- **Key Skills And Tools:** autopsy, mmls, fls, icat, reading disk data
---

## 🔍 Challenge 

Download this disk image, find the key and log into the remote machine.

Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

Download disk image
Remote machine: `ssh -i key_file -p 49406 ctf-player@saturn.picoctf.net`

### 🧪 Logic Extraction:

I used the tool `autopsy` to retrieve files hidden on the disk.

<div align="center">
   <img width="359" height="557" alt="image" src="https://github.com/user-attachments/assets/f3d8932f-3d06-4101-9313-9b8552f88892" />
</div>

#
I opened it and found an `ssh` file. Since it contained a `ssh` and `server` string, I used it to generate a key to access the server.

<div align="center">
   <img width="998" height="615" alt="image" src="https://github.com/user-attachments/assets/4bfb81b2-b7a4-4823-931a-82f9270b2077" />


</div>

#
This is the key to log into the server, and please remember the code to avoid misinterpreting it; it's shown on lines 8 and 9.
<div align="center">
   <img width="693" height="383" alt="image" src="https://github.com/user-attachments/assets/12b26e33-25ed-4803-8c3f-f417085f8594" />

</div>

#
I used the `chmod 600` command to grant the highest possible permissions to your server. 
document:<a href="https://mangohost.net/blog/chmod-600-specific-permission-setting/"> Google </a>
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ chmod 600 key_file 

```

Once you've logged into the server, use the `ls` command to view the list and retrieve the flags.

<div align="center">
   <img width="967" height="355" alt="image" src="https://github.com/user-attachments/assets/9b665428-efbc-47b6-9afb-8744cf8274ef" />

</div>

#
I used the `mmls` command to read the partition table displayed on the hard drive.
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
```

I used the `fls` command to list the directory names and added `-o` (the abbreviation for Offset) to browse the beginning of the list, as the '-' starts and the number is the link to access that file.
```
                                                                                                                                       
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.img -o 206848         
d/d 458:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles
```
Next, we use `-r` (abbreviation for Recursive) to list the files and directories located at the very edge of the root directory of that partition, and combine it with `grep ssh` to find the `ssh` string, which is the SSH key file located deep inside the `/root/.ssh` directory.
```                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.img -o 206848 -r | grep ssh
++ r/r 2147:    sshd
+++ l/l 54:     sshd
++ r/r 2148:    sshd
+ d/d 14:       ssh
++ r/r 15:      ssh_host_ed25519_key
++ r/r 16:      ssh_host_ed25519_key.pub
++ r/r 17:      ssh_host_ecdsa_key
++ r/r 18:      ssh_host_ecdsa_key.pub
++ r/r 19:      ssh_host_dsa_key
++ r/r 20:      ssh_host_dsa_key.pub
++ r/r 21:      ssh_host_rsa_key
++ r/r 22:      ssh_host_rsa_key.pub
++ r/r 2136:    ssh_config
++ r/r 2149:    sshd_config
++ r/r 2084:    ssh-keygen
++ r/- * 0:     ssh-copy-id
++ r/- * 0:     ssh-keyscan
++ r/- * 0:     ssh-pkcs11-helper
++ r/r 2140:    ssh-add
++ r/r 2145:    ssh
++ r/r 2144:    ssh-pkcs11-helper
++ r/r 2143:    ssh-keyscan
++ r/r 2142:    ssh-copy-id
++ r/r 2141:    ssh-agent
++ r/r 2150:    sshd
+++++ r/r 676:  sshd
++ d/d 3907:    ssh
+++ r/r 2152:   ssh-sk-helper
+++ r/r 2151:   ssh-pkcs11-helper
+ r/r 712:      setup-sshd
+ d/d 3916:     .ssh
```
Once I had the `ssh` file link, I used the `fls` command to list the files and then used `-r` to see what was inside.
```                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.img -o 206848 3916 -r      
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub

```
I used the `icat` command to extract the data from the `ssh` file that I found, and I saw the key.
```                                                                                                                                                          
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat disk.img -o 206848 2345      
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
 
```
If you don't want to copy the key, you can convert it to a separate file using the `icat` command, which is the `> file` symbol.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat disk.img -o 206848 2345 > key_file 
```

## Run 
.flag picoCTF{k3y_5l3u7h_b5066e83}

