# 🚩WhitePages - picoCTF 2019

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `whitepages.txt`
- **Key Skills And Tools:** xxd, python, data encryption
---

## 🔍 Challenge 

I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

### 🧪 Logic Extraction:

This challenge has a .txt file containing hidden data, seemingly including accounts. I used the `xxd` function to extract the data and found the numbers `e2, 80, 83, 20`. This could be one of the flags to be flagged.

<div align="center"> 

  <img width="664" height="278" alt="image" src="https://github.com/user-attachments/assets/3ac4f95e-cc18-464c-aa3f-854ae26273df" />

</div>

I'm using a Python code snippet for encoding. Actually, to understand the code, you can use a trial-and-error method to replace each binary instance. Take the first 8 bits: "01110000". Convert to decimal: 112. Look up the ASCII table: 112 is the letter 'p' (the first letter of picoCTF).

```
from pwn import *

with open("whitepages.txt", "rb") as bin_file:
    data = bytearray(bin_file.read())
    data = data.replace(b'\xe2\x80\x83', b'0')
    data = data.replace(b'\x20', b'1')
    data = data.decode("ascii")
    print(unbits(data))
```

## Run 
.flag picoCTF{not_all_spaces_are_created_equal_57203502a1f295faf0d8cf42a1d4c769}
