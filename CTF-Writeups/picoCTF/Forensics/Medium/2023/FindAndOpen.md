# 🚩FindAndOpen.md - picoCTF 2023

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `dump.pcap`,  `flag.zip`
- **Key Skills And Tools:** tshark, string, base64, hex, reading data
---

## 🔍 Challenge 

Someone might have hidden the password in the trace file.

Find the key to unlock this file. This tracefile might be good to analyze.

### 🧪 Logic Extraction:



<div align="center">
  <img width="1365" height="401" alt="image" src="https://github.com/user-attachments/assets/2e5aa5e1-f168-4ca3-a0ea-38ec56cfc178" />

</div>


<div align="center">
  <img width="692" height="501" alt="image" src="https://github.com/user-attachments/assets/4b547408-7424-430c-9292-f7a6947c032a" />

</div>


```
tshark -r dump.pcap -Y 'eth.type == 0x4c4b' -T fields -e data.data | uniq | xxd -r -p | base64 -d
This is the secret: picoCTF{R34DING_LOKd_                                                                                                                                                           
```

#

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ unzip flag.zip 
Archive:  flag.zip
[flag.zip] flag password: 
 extracting: flag                    
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
dump.pcap  flag  flag.zip
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ cat flag     
picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}

```


## Run 
.flag picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}

