# 🚩 keygenme-py - picoCTF 2021

- **Category:** Reverse Engineering ⚙️
- **Difficulty:** Medium 🟠
- **Target File:** `keygenme-trial.py`
- **Key Skills:** Static Analysis, Python Scripting, SHA256 Hashing

---

## 🔍 1. Challenge Overview
In this challenge, we are provided with a Python script called `keygenme-trial.py`. It acts as a trial version of an "Arcane Calculator." To unlock the full version and reveal the flag, we must reverse-engineer the license key verification logic.

### 📋 Core Script Highlights
The script defines the following key variables for its "trial" mode:
- `username_trial = "BENNETT"`
- `key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"`
- `key_part_dynamic1_trial = "xxxxxxxx"` (8 characters we need to find)
- `key_part_static2_trial = "}"`

---

## 🛠️ 2. Static Analysis & Reverse Engineering
The heart of the challenge lies within the `check_key(key, username_trial)` function. 



The script validates the 8 dynamic characters by comparing our input against specific indices of the **SHA256 hash** of the username `"BENNETT"`.

### 🧪 Logic Extraction:
By tracing the `if` statements in the code, I identified the exact indices required from the hex-digest of the hash:

1. `key[i]   == hash[4]`
2. `key[i+1] == hash[5]`
3. `key[i+2] == hash[3]`
4. `key[i+3] == hash[6]`
5. `key[i+4] == hash[2]`
6. `key[i+5] == hash[7]`
7. `key[i+6] == hash[1]`
8. `key[i+7] == hash[8]`

---

## 💻 3. The Solver (Python Script)
Instead of manual calculation, I wrote an automation script to generate the dynamic part and reconstruct the full flag:

```python
import hashlib

# 1. Target Data from the source code
username = b"BENNETT"
prefix = "picoCTF{1n_7h3_kk3y_of_"
suffix = "}"

# 2. Generate the SHA256 hash digest
# hashlib.sha256(b"BENNETT").hexdigest()
digest = hashlib.sha256(username).hexdigest()

# 3. Extract characters based on the identified order: 4, 5, 3, 6, 2, 7, 1, 8
order = [4, 5, 3, 6, 2, 7, 1, 8]
dynamic_part = "".join([digest[i] for i in order])

# 4. Resulting Flag
print(f"Full Flag: {prefix}{dynamic_part}{suffix}")
