# 🚩Eavesdrop - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `drawing.flag.svg`
- **Key Skills And Tools:** wireshark, 
---

## 🔍 Challenge 

Download this packet capture and find the flag.
Download packet capture

### 🧪 Logic Extraction:



```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
capture.flag.pcap  file.des3  file.txt
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ cat file.txt        
picoCTF{nc_73115_411_5786acc3}
```


## Run 
.flag picoCTF{nc_73115_411_5786acc3}                                                                                                                                                           

