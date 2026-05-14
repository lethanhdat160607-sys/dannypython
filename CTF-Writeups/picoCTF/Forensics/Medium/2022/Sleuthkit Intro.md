# 🚩Sleuthkit Intro - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `disk.img`
- **Key Skills And Tools:** mmls, reading data
---

## 🔍 Challenge 

Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.

Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

Download disk image

Access checker program: `nc saturn.picoctf.net 52943`

### 🧪 Logic Extraction:

This is a disk file, so I'm using the `mmls` command to see if the table contains any data.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)

```
During the challenge, they provided a link to access the server, and I tried it. It required a password to log in, so I used `start 2048` and `Length 202752` and successfully logged in, but a flag appeared.

```                                                                                                                                                      
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ nc saturn.picoctf.net 52943
What is the size of the Linux partition in the given disk image?
Length in sectors: 2048
2048
That is not correct. Feel free to try again.
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ nc saturn.picoctf.net 52943
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752  
202752  
Great work!
picoCTF{mm15_f7w!}
                     
```


## Run 
.flag picoCTF{mm15_f7w!}

