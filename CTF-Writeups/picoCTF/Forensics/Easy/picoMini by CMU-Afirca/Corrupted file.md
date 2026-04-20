# 🚩Corrupted file - picoMini by CMU-Afirca 

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `file`
- **Key Skills And Tools:** 
---

## 🔍 Challenge 

This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file here.

### 🧪 Logic Extraction:

We checked using the `file` command and found no data because the test said it was missing data, so I used the `xxd` command to check.
<div align="center">
  <img width="641" height="228" alt="image" src="https://github.com/user-attachments/assets/9d12cbb7-d966-4d07-804e-f02726ad7dd5" />
  <p>Regarding the data checked using the `xxd` command, I see `JFIF` which is an ASCII code block. This is an indication of a JPEG file, but the anomaly here is that the standard Magic byte format for JPEG files is usually `FF D8 FF`. However, your file starts with `5C 78 FF E0`.</p>
  <img width="607" height="310" alt="image" src="https://github.com/user-attachments/assets/18d30add-06f8-405c-a252-8bd485cab7cb" />
  <p>The end point of the file is fine; it's correct according to the standard `FF D9` format.</p>
</div>

#

```
┌──(kali㉿kali)-[~/Tools]
└─$ hexedit file 
         
┌──(kali㉿kali)-[~/Tools]
└─$ file file 
file: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 800x500, components 3

┌──(kali㉿kali)-[~/Tools]
└─$ mv file file.jpeg  
```

## Run 
.flag picoCTF{r3st0r1ng_th3_by73s_efd8c6c0}
