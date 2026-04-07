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
 

## Run 
.flag picoCTF{5tRIng5_1T_60eA8fdA}
