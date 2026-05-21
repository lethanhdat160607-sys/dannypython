# 🚩PcapPoisoning - picoCTF 2023

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `trace.pcap`
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

How about some hide and seek heh?

Download this file and find the flag.

### 🧪 Logic Extraction:

The challenge was to give me a packet file. I used the `wireshark` tool and didn't see anything unusual. Then I tried the command `strings<file> | grep pico` and it immediately showed a flag.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls                
trace.pcap
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ strings trace.pcap | grep pico
picoCTF{P64P_4N4L7S1S_SU55355FUL_31010c46}F~

```

## Run 
.flag picoCTF{P64P_4N4L7S1S_SU55355FUL_31010c46}

