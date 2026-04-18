# 🚩DISKO 1 - picoGym Exclusive

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `disko-1.dd`
- **Key Skills And Tools:** strings, Concealing techniques and searching
---

## 🔍 Challenge 
Can you find the flag in this disk image?
Download the disk image here.

### 🧪 Logic Extraction:
 Using the command `strings disko-1.dd | grep picoCTF` was a key step in solving this challenge.To break it down: strings is a powerful utility that extracts all printable character sequences from binary files like `disko-1.dd` (a bit-for-bit disk image copy), while the pipe `(|)` redirected that output to grep picoCTF, allowing me to quickly filter and pinpoint the flag format. Your guidance made this forensic process much clearer
<div align="center">
  <img width="718" height="73" alt="image" src="https://github.com/user-attachments/assets/cbc79c72-55a4-49c9-aeff-1318d6b3a1bb" />

</div>


## Run 
.flag picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}
