# 🚩Timeline 0 - picoCTF 2026

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `partition4.img.gz`
- **Key Skills And Tools:** fls, icat, mactime, reading data
---

## 🔍 Challenge 

Can you find the flag in this disk image? Wrap what you find in the picoCTF flag format.

Download the disk image here.


Download the network capture file: here

### 🧪 Logic Extraction:

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -r -m / partition4.img > body.txt
 
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
body.txt  partition4.img
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ mactime -b body.txt > timeline.txt
Old package separator "'" deprecated at /usr/bin/mactime line 154.
Old package separator "'" deprecated at /usr/bin/mactime line 167.
                                                                                                                                                           
```

<div align="center">
  <img width="1339" height="303" alt="image" src="https://github.com/user-attachments/assets/b024ed6d-bf5b-4ba6-8449-3bb31888029a" />

</div>

# https://wiki.sleuthkit.org/fls/
# https://wiki.sleuthkit.org/mactime/

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat partition4.img 4945

NzFtMzExbjNfMHU3MTEzcl9oM3JfNDNhMmU3YWYK
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ echo "NzFtMzExbjNfMHU3MTEzcl9oM3JfNDNhMmU3YWYK" | base64 -d
71m311n3_0u7113r_h3r_43a2e7af

```

## Run 
.flag picoCTF{71m311n3_0u7113r_h3r_43a2e7af}



