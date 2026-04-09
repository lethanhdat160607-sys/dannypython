# 🚩 SUDO MAKE ME A SANDWICH - picoCTF 2026

- **Category:** General Skills⚙️
- **Difficulty:** Easy
- **Target File:** `ssh -p 54369 ctf-player@green-hill.picoctf.net`
- **Key Skills:** Enumeration

---

## 🔍 Challenge 
Can you read the flag? I think you can!
`ssh -p 54369 ctf-player@green-hill.picoctf.net` using password `f99cd115`


### 🧪 Logic Extraction:
When you connect to the challenge, I used the `ls` command to check and a file named `flag.txt` appeared, but the `cat` 
command couldn't open the file. So I tried `sudo -l` to see what lists were inside, and Emac gave me the highest privileges to edit.
<div align="center">

  <img width="942" height="324" alt="image" src="https://github.com/user-attachments/assets/770a29b9-b382-4382-a16e-473b4c3feedd" />
</div>.
```
 sudo emacs flag.txt
```.
## Run 
.flag picoCTF{ju57_5ud0_17_f6cc9dec}
