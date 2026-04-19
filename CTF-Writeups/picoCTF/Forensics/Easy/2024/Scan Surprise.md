# 🚩Scan Surprise - picoCTF 2024

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `challenge.zip`, `ssh -p 51416 ctf-player@atlas.picoctf.net`
- **Key Skills And Tools:** data analysis
---

## 🔍 Challenge 
I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?
You can download the challenge files here:
`challenge.zip`


The same files are accessible via SSH here:
`ssh -p 51416 ctf-player@atlas.picoctf.net`
Using the password `66abf4a82. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

### 🧪 Logic Extraction:

Once connected, it will give you a QR code image.

<div align="center">
  <img width="784" height="732" alt="image" src="https://github.com/user-attachments/assets/8a18e255-5cbc-4545-824a-b995c1e39ca2" />


</div>
#
I used Google to find the image and found the flag.
<div align="center">
  <img width="1032" height="428" alt="image" src="https://github.com/user-attachments/assets/ec2453e1-86bd-42fd-8525-af4e37b43965" />

</div>

## Run 
.flag picoCTF{p33k_@_b00_7843f77c}
