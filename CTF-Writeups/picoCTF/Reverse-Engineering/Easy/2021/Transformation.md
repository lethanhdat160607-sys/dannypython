# 🚩Transformation - picoCTF 2021

- **Category:** Reverse Engineering ⚙️
- **Difficulty:** Easy
- **Target File:** `enc`
- **Key Skills And Tools:** python, 
---

## 🔍 Challenge 
I wonder what this really is...
enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

### 🧪 Logic Extraction:




<div align="center">
  <img width="1050" height="501" alt="image" src="https://github.com/user-attachments/assets/52b58a86-201c-496a-a580-67de1207f490" />

</div>

```
with open("enc", "r", encoding="utf-8") as f:
    encoded_content = f.read()

decoded = ""
for char in encoded_content:
    decoded += chr(ord(char) >> 8)
    decoded += chr(ord(char) & 0xFF)

print("flag", decoded)
```

## Run 
.flag picoCTF{16_bits_inst34d_of_8_b7f62ca5}.

