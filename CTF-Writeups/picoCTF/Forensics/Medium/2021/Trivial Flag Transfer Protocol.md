# 🚩Trivial Flag Transfer Protocol - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `pico_img.png`
- **Key Skills And Tools:** exiftool, data extraction
---

## 🔍 Challenge 

Figure out how they moved the flag.
tftp.pcapng

### 🧪 Logic Extraction:


<div align="center">
  <img width="1316" height="722" alt="image" src="https://github.com/user-attachments/assets/33da2c6a-8dcf-4dd3-bbba-3e12eb41545b" />
</div>



```
┌──(kali㉿kali)-[~/Tools]
└─$ echo "VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF" | tr 'A-Za-z' 'N-ZA-Mn-za-m'                                                 
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```
#

```
┌──(kali㉿kali)-[~/Tools]
└─$ steghide extract -sf picture3.bmp -p DUEDILIGENCE
wrote extracted data to "flag.txt".

┌──(kali㉿kali)-[~/Tools]
└─$ cat flag.txt
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```
## Run 
.flag 
