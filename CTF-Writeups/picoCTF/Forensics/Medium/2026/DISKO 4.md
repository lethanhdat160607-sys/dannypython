# 🚩DISKO 4 - picoCTF 2026

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `disko-4.dd.gz`
- **Key Skills And Tools:** fls, icat, zcat, fsstat, reading data disk
---

## 🔍 Challenge 

Can you find the flag in this disk image? This time I deleted the file! Let see you get it now!

Download the disk image here.

### 🧪 Logic Extraction:

I used the `file` command to check the contents of the file and the `fsstat` command, which is a tool in the Sleuth Kit that displays the block size and partition status. I also used `head -n 40` to limit the displayed results, only showing the first 40 lines of useful information.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file disko-4.dd
fsstat disko-4.dd | head -n 40 
disko-4.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat", Media descriptor 0xf8, sectors/track 32, heads 8, sectors 204800 (volumes > 32 MB), FAT (32 bit), sectors/FAT 1576, serial number 0x49838d0b, unlabeled
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: FAT32

OEM Name: mkfs.fat
Volume ID: 0x49838d0b
Volume Label (Boot Sector): NO NAME    
Volume Label (Root Directory):
File System Type Label: FAT32   
Next Free Sector (FS Info): 36435
Free Sector Count (FS Info): 1375

Sectors before file system: 0

File System Layout (in sectors)
Total Range: 0 - 204799
* Reserved: 0 - 31
** Boot Sector: 0
** FS Info Sector: 1
** Backup Boot Sector: 6
* FAT 0: 32 - 1607
* FAT 1: 1608 - 3183
* Data Area: 3184 - 204799
** Cluster Area: 3184 - 204799
*** Root Directory: 3184 - 3184

METADATA INFORMATION
--------------------------------------------
Range: 2 - 3225862
Root Directory: 2

CONTENT INFORMATION
--------------------------------------------
Sector Size: 512
Cluster Size: 512
Total Cluster Range: 2 - 201617

FAT CONTENTS (in sectors)
--------------------------------------------
3184-3184 (1) -> EOF
```
Next, I used the `fls` command to list the files on the disk, `-r` for recursive scanning, and `-d`, the most important parameter for selecting what to display, which was marked as deleted, but the actual data was still on the hard drive and had not been written to.

```        
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -r -d disko-4.dd
r/r * 522629:   log/messages
r/r * 532021:   log/dont-delete.gz
```

I then used the `icat` command to extract the raw data of a file and redirected it from that inode to a file named `recovered_dont-delete.gz`. I used the `file` command to check what type of file the extracted file was, whether it was deleted, had an extension, or was corrupted. Finally, I used the `zcat` command to read the contents of a compressed file without decompressing it to disk if the extracted file was indeed a compressed text file and had a flag.

```        
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat disko-4.dd 532021 > recovered_dont-delete.gz
file recovered_dont-delete.gz
zcat recovered_dont-delete.gz
recovered_dont-delete.gz: gzip compressed data, was "dont-delete", last modified: Wed Feb  4 21:55:17 2026, from Unix, original size modulo 2^32 55
Here is your flag
picoCTF{d3l_d0n7_h1d3_w3ll_4b0a805d}
                                        
```

## Run 
.flag picoCTF{d3l_d0n7_h1d3_w3ll_4b0a805d}


