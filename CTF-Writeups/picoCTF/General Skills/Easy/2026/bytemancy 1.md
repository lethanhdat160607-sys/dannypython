# 🚩 bytemancy 1 - picoCTF 2026

- **Category:** General Skiils ⚙️
- **Difficulty:** Easy 
- **Target File:** `nc foggy-cliff.picoctf.net 49715`
- **Key Skills:** Data Piping

---

## 🔍 Challenge 

Can you conjure the right bytes? The program's source code can be downloaded here.

Connect to the program with netcat: `nc foggy-cliff.picoctf.net 49715`.


### 🧪 Logic Extraction:

I saw it said I had to change the Decimal `101` to ASCII `e` and fill in `1751` with the letter `e`. 

That's a very time-consuming process, but I'll use Python's print command.

<div align="center">
  <img width="565" height="142" alt="image" src="https://github.com/user-attachments/assets/558cbb6e-4b22-465a-912f-3018facc545c" />

</div> 

## code python 

```
~python3 -c "print('e' * 1751)" | nc foggy-cliff.picoctf.net 49715
```

## Run 
.flag picoCTF{h0w_m4ny_e's???_be9356c0}

