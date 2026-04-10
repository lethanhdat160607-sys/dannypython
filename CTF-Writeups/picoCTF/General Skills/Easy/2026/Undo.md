# 🚩 Undo - picoCTF 2022

- **Category:** General Skills⚙️
- **Difficulty:** Easy 
- **Target File:** `nc foggy-cliff.picoctf.net 63770`
- **Key Skills:** Base64, ROT13, Reverse

---

## 🔍 Challenge 

Can you reverse a series of Linux text transformations to recover the original flag?.

Start searching for the flag here `nc foggy-cliff.picoctf.net 63770`.

### 🧪 Logic Extraction:
When connecting to the challenge

I saw a code that was the current flag: `KTY4ODhyMjFuLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj`,also with base64 encoding. 

<div align="center">
  <img width="881" height="303" alt="image" src="https://github.com/user-attachments/assets/1abf5f99-112b-43b7-99a7-16b36485e9aa" />
  <p> Convert base64 from Cyberchef </p>
</div> 

<div align="center">
  <img width="777" height="240" alt="image" src="https://github.com/user-attachments/assets/3e095b97-093c-4980-bfa5-4b058fb5a99a" />

</div> 


After adding the base64 conversion code, it showed that I needed to reverse it, so I reversed the code halfway to see what would happen.


<div align="center">
  <img width="871" height="337" alt="image" src="https://github.com/user-attachments/assets/e0a94636-39de-4680-b143-5b6ecc71d2ed" />
    <p> Convert Reverse from Cyberchef </p>

</div> 



<div align="center">
  <img width="768" height="84" alt="image" src="https://github.com/user-attachments/assets/37a38ac9-9105-4aca-b7c9-f5a248babdb3" />

</div>

After decoding the first layer, we obtain the string: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-n12r8886).

Based on the string structure, we find that this format perfectly corresponds to the competition flag format picoCTF{...}. 

Specifically, the phrase cvpbPGS matches picoCTF in both the number of characters and the capitalization position When checking 

the distance between the actual character (c) and the expected character (p), we find a deviation of exactly 13 alphabetical units.

Based on the structural characteristics, I identified the algorithm as ROT13. This is a variant of the Caesar cipher with an offset of 13. With 

its 26-character Latin alphabet, ROT13 is a symmetrical operation (encryption is also decryption). This algorithm hides the content while 

preserving formatting elements such as digits and special characters, making it easy to identify the flag's format.

<div align="center">
  <img width="871" height="382" alt="image" src="https://github.com/user-attachments/assets/c3741508-cfd0-4218-8478-3290049223f9" />

</div> 

When the flag appeared, I changed the minus sign to an underscore, and that made it a flag.


## Run


.flag picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_a12e8886}
