# 🚩Ph4nt0m 1ntrud3r - picoCTF 2025

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** ` myNetworkTraffic.pcap`
- **Key Skills And Tools:** Aircrack-ng, Wireshark ,Password cracking and decryption
---

## 🔍 Challenge 

A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.
To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!
Find the PCAP file here Network Traffic PCAP file and try to get the flag.


### 🧪 Logic Extraction:


<div align="center">
    <img width="1365" height="734" alt="image" src="https://github.com/user-attachments/assets/1bc44992-6bca-4f22-8ab6-9f29e006107c" />

</div> 

#
From the keys in the file, we find a way to convert them to base64 encoding.
```
Frame 2: bnRfdGg0dA== --> nt_th4t
Frame 3 : fQ== --> } 
Frame 5: ZTFmZjA2Mw== --> e1ff063
Frame 9: XzM0c3lfdA== --> _34sy_t
Frame 10: ezF0X3c0cw== --> {1t_w4s
Frame 12: cGljb0NURg== --> picoCTF
Frame 21: YmhfNHJfMg== --> bh_4r_2
```

## 💻 The Solver (Python Script)
Because the flag is somewhat noisy, I used code to exhaust all flag possibilities and tested it to determine when a flag is found.
```
import itertools

def generate_pico_flags(data_list):
    """
    Generates all permutations and formats them as picoCTF{}
    """
    # Create all possible permutations of the input list
    permutations = list(itertools.permutations(data_list))
    
    flag_list = []
    for p in permutations:
        # Join segments into the variable part
        variable_content = "".join(map(str, p))
        
        # Correct f-string syntax:
        # picoCTF{1t_w4s -> Fixed prefix
        # {variable_content} -> The moving parts
        # } -> Closing bracket
        full_flag = f"picoCTF{{1t_w4s{variable_content}}}" # f"picoCTF{{key{ble_content}}}"
        
        flag_list.append(full_flag)
    
    return flag_list

# Your input data segments
input_data = ["nt_th4t", "e1ff063", "_34sy_t", "bh_4r_2"]

# Execute generation
results = generate_pico_flags(input_data)

# Print results to console
print(f"--- Total Flags Generated: {len(results)} ---")
for index, flag in enumerate(results, 1):
    print(f"{index}: {flag}")

# Export to file
filename = "flags_wordlist.txt"
try:
    with open(filename, "w") as f:
        for flag in results:
            f.write(flag + "\n")
    print(f"\n[!] Success: Saved to '{filename}'")
except IOError as e:
    print(f"\n[!] Error saving file: {e}")
```

## Run 
.flag picoCTF{1t_w4snt_th4t_34sy_tbh_4r_2e1ff063}
