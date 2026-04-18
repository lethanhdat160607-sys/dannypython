# 🚩 information - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `pcap file`
- **Key Skills And Tools:** Aircrack-ng, Wireshark ,Password cracking and decryption
---

## 🔍 Challenge 

Files can always be changed in a secret way. Can you find the flag?
cat.jpg

### 🧪 Logic Extraction:
After downloading the image, I opened it but didn't see the flag. So, I used the `exiftool cat.jpg` command to open the image and suspected I saw two things: `Current IPTC Digest` and `License`. Because they were long and contained many characters, I encoded them into a flag. Based on the code analysis of `Current IPTC Digest` and `License`, the `Current IPTC Digest` code consists of 32 characters, including both numbers and letters from a to f. This is characteristic of `MD5`, which only allows 32 characters, quite restrictive. Therefore, I leaned towards `License` and analyzed the code, concluding it was `base64`. Why? I guessed it was `base64` because it displays `a-z`, `A-Z`, `0-9`, `+`, and `-`. Typically, it will display the characters I've listed. If you see a long string with no spaces and no unusual special characters (like !, @, #, $, %, ^, *), it's most likely base64 code. Another characteristic is that if there's an `=` or `==` symbol, there's a 99% chance it's base64 code.

<div align="center">
  <img width="731" height="498" alt="image" src="https://github.com/user-attachments/assets/a78b5f4a-6a79-4107-8374-a90412c40a70" />


</div>


## Run 
.flag picoCTF{}
