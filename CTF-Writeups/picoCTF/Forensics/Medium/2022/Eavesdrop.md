# 🚩Eavesdrop - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `capture.flag.pcap`
- **Key Skills And Tools:** wireshark, 
---

## 🔍 Challenge 

Download this packet capture and find the flag.
Download packet capture

### 🧪 Logic Extraction:


<div align="center">
  <img width="918" height="582" alt="image" src="https://github.com/user-attachments/assets/135292aa-9992-4f87-b435-f857b0d66b27" />

</div>


# 


<div align="center">
  <img width="910" height="571" alt="image" src="https://github.com/user-attachments/assets/55f59e0c-272d-4c3d-8eaf-efff1ada2e2b" />

</div>


#

<div align="center">
  <img width="911" height="576" alt="image" src="https://github.com/user-attachments/assets/bbbc5cdf-e9bf-4296-92dd-1d016b85ff13" />

</div>

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

