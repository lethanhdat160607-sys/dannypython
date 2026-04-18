# 🚩 Password Profiler - picoCTF 2026

- **Category:** General Skills ⚙️
- **Difficulty:** Easy
- **Target File:** `check_password.py` `hash.txt` `userinfo.txt`
- **Key Skills And Tools:** cupp
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
We see a note `#wordlist that was generated using CUPP`
The code mentions that a file `password` file is needed to open it and executes the logic to return the code.
```
def crack_password(target_hash):
    with open(WORDLIST_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for password in f:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == target_hash:
                return password
```

### 🧪 Logic Extraction:
We will use the Cupp tool based on the notes and a `userinfo.txt` file provided in the problem statement.

<div align="center">
    <img width="557" height="129" alt="image" src="https://github.com/user-attachments/assets/5c483cc5-5e6d-45f6-b803-2977386f6dcb" />
</div> 

<div align="center">
        <img width="784" height="717" alt="image" src="https://github.com/user-attachments/assets/ae8a2f7e-bf54-42d5-896b-68054d0113b1" />        
</div>

#
After declaring it, it will create a file named alice.txt
<div align="center">
    <img width="656" height="85" alt="image" src="https://github.com/user-attachments/assets/e75f9c82-5eaa-4273-8e93-6bd5b527c00e" />

</div>

- **CP:** We use the `cp` function to copy the passwords file so that the Python file can call it.
- `~cp alice.txt passwords.txt`.
- `~python3 check_password.py`.
## Run 
. ` flag picoCTF{Aj_15901990}
