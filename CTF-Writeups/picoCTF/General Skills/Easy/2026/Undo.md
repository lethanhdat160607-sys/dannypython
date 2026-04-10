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
When connecting to the challenge, I saw a code that was the current flag: `KTY4ODhyMjFuLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj`,
also with base64 encoding. So I tried changing it to base64 and added the newly changed code to see if it would show a Linux command to reverse.


## 💻 The Solver (Python Script)
