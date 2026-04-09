# 🚩 Piece by Piece - picoCTF 2026
- **Category:** General Skills ⚙️
- **Difficulty:** Easy
- **Target File:** `ssh -p 58486 ctf-player@dolphin-cove.picoctf.net`
- **Key Skills:** Using mathematical operations and data grouping.
---

## 🔍 Challenge 
After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.
SSH to `dolphin-cove.picoctf.net:58486` and login as `ctf-player` with password `6abf4a82`.


### 🧪 Logic Extraction:
After connecting to the server, I used the `ls` command to check and found quite a few files. One file, `instructions.txt`, seemed unusual compared 
to the others. I investigated further and found a clue. Pay attention to this part; the flag is divided into several parts within a compressed 
file. We might need it: The compressed file is password protected. Let's use this "super secret" password to decompress the compressed file.

<div align="center">
    <img width="763" height="163" alt="image" src="https://github.com/user-attachments/assets/fd52cbc1-1978-4557-b934-63204ce8c48b" />

</div>

<div align="center">
    <img width="613" height="401" alt="image" src="https://github.com/user-attachments/assets/5a5bf76c-2118-4d8d-b244-18205a3ac022" />

</div>

<div align="center">
    <img width="1034" height="249" alt="image" src="https://github.com/user-attachments/assets/f504b928-cc07-4a50-a279-b75bebb7e5e0" />

</div>

## Run 
.flag picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_2d6c5d3f}.
