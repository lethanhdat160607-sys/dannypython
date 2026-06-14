# 🚩Bitlocker-2 - picoCTF 2025

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `bitlocker-2.dd`, `memdump.mem.gz`
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

Jacky has learnt about the importance of strong passwords and made sure to encrypt the BitLocker drive with a very long and complex password. We managed to capture the RAM while this drive was opened however. See if you can break through the encryption!

Download the disk image here
 and the RAM dump here

### 🧪 Logic Extraction:

I used the `strings` command and got the flag immediately.
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ strings memdump.mem | grep 'picoCTF{'          
picoCTF{B1tl0ck3r_dr1v3_d3crypt3d_9029ae5b}

```

## Run 
.flag picoCTF{B1tl0ck3r_dr1v3_d3crypt3d_9029ae5b}

