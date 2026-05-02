# 🚩Disk, disk, sleuth! - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `dds1-alpine.flag.img.gz`
- **Key Skills And Tools:** file, grep, reading data
---

## 🔍 Challenge 

Use srch_strings from the sleuthkit and some terminal-fu to find a flag in this disk image.
dds1-alpine.flag.img.gz

### 🧪 Logic Extraction:

I used the `gunzip` command to extract the file.
```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ gunzip dds1-alpine.flag.img.gz
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ ls 
dds1-alpine.flag.img
```
I used the `file` command to check and it contains data.

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ file dds1-alpine.flag.img
dds1-alpine.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x10,81,1), startsector 2048, 260096 sectors
```
I used the `grep` command to search and it immediately showed the flag.

<div align="center">
  <img width="482" height="98" alt="image" src="https://github.com/user-attachments/assets/dac1c1c2-43d9-43b0-8e30-c043dd200cec" />

</div>


## Run 
.flag picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}

