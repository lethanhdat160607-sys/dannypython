# 🚩 Password Profiler - picoCTF 2026

- **Category:** General Skills ⚙️
- **Difficulty:** Easy
- **Target File:** `check_password.py` `hash.txt` `userinfo.txt`
- **Key Skills:** cupp
---

## 🔍 Challenge 
We intercepted a suspicious file from a system, but instead of the password itself, it only contains its SHA-1 hash. 
Using OSINT techniques, you are provided with personal details about the target. 
Your task is to leverage this information to generate a custom password list and recover the original password by matching its hash.
Download the following files:
`userinfo.txt`: Contains the personal details.
`hash.txt`: Contains the SHA-1 hash of the password.
`check_password.py`: Script to test passwords against the hash.

### 📋 Open file `check_password.py`
```
#!/usr/bin/env python3
import hashlib

HASH_FILE = "hash.txt"
WORDLIST_FILE = "passwords.txt" # wordlist that was generated using CUPP

def load_hash():
    with open(HASH_FILE, "r") as f:
        return f.read().strip()

def crack_password(target_hash):
    with open(WORDLIST_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for password in f:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == target_hash:
                return password
    return None

if __name__ == "__main__":
    target_hash = load_hash()
    result = crack_password(target_hash)
    if result:
        print(f"Password found: picoCTF{{{result}}}")
    else:
        print("No match found.")
```


## 🛠️ highlights in the code

### 🧪 Logic Extraction:


. ` flag picoCTF{1n_7h3_kk3y_of_08c46aa4}
