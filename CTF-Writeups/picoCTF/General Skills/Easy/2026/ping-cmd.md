# 🚩 ping-cmd - picoCTF 2026

- **Category:** General Skills ⚙️
- **Difficulty:** Easy
- **Link:** `nc mysterious-sea.picoctf.net 64791`
- **Key Skills:** Network and DNS
---

## 🔍 Challenge 
Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?
You can connect to the service here `nc mysterious-sea.picoctf.net 64791`

### 🧪 Logic Extraction:
The challenge in the problem reveals the network configuration, and based on what we've learned 
it might be hiding something, so let's check if it's concealing any files.

- Perform
```
nc mysterious-sea.picoctf.net 64791
```
When you execute it, you'll see that it displays a network address, `8.8.8.8`, according to the DNS configuration.
<div align="center">
   <img width="840" height="159" alt="image" src="https://github.com/user-attachments/assets/aa16b7cc-9b49-4b7b-b666-a6265e978f2c" />

</div> 

#
We then tried checking what was inside the network using the `ls` command, and it revealed several files, including flag.txt.

<div align="center">
    <img width="838" height="195" alt="image" src="https://github.com/user-attachments/assets/942ac4fb-a433-4dac-bdea-7462061eb42d" />

</div> 

#
After seeing the flag file, we proceed to view the flag file and see the flags.
<div align="center">
    <img width="907" height="181" alt="image" src="https://github.com/user-attachments/assets/064c1cac-d35c-40ed-8959-a288f4ee6f79" />

</div> 

## Run 
.flag picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_a9326567}
