# 🚩shark on wire 1 - picoCTF 2019

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `capture.pcap`
- **Key Skills And Tools:** wireshark, 
---

## 🔍 Challenge 

We found this packet capture. Recover the flag.

### 🧪 Logic Extraction:

I approached this challenge with a file containing a single packet, so I used the `wireshark` tool to read it. From a quick read, I found there were up to 2000 packets quite a large number.

<div align="center">
  <img width="1363" height="584" alt="image" src="https://github.com/user-attachments/assets/24eab905-3035-492d-a681-d2333e127f79" />

</div>

#
I tried to examine the data and became suspicious because they usually hide the information in flags here.
<div align="center">
  <img width="1364" height="546" alt="image" src="https://github.com/user-attachments/assets/2177e699-2f16-4d05-9ed6-f43d20ed64c2" />

</div>

#
Let's check the UDP stream to see if there's any unusual data.
<div align="center">
    <img width="952" height="599" alt="image" src="https://github.com/user-attachments/assets/90b90f90-ec7a-495a-939c-309df51678fe" />

</div>

#

<div align="center">
    <img width="918" height="593" alt="image" src="https://github.com/user-attachments/assets/3e4dc0cc-df9c-4e1d-a006-b429b6d7f651" />


</div>


## Run 
.flag picoCTF{StaT31355_636f6e6e}
