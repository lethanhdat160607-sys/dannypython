# 🚩Packets Primer - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `network-dump.flag.pcap`
- **Key Skills And Tools:** wireshark, reading data
---

## 🔍 Challenge 

Download the packet capture file and use packet analysis software to find the flag.

Download packet capture

### 🧪 Logic Extraction:

This is a packet file, so I'm using the `wireshark` tool to read the packets and see what data is inside.

<div align="center">
  <img width="1365" height="425" alt="image" src="https://github.com/user-attachments/assets/16f5944d-0e27-425f-9f45-ecbcbbfd1ed4" />
</div>

#
The flag is hidden in the data bytes.
<div align="center">

  <img width="1365" height="647" alt="image" src="https://github.com/user-attachments/assets/786ca937-63af-496d-8a25-efdce9daa455" />

</div>

## Run 
.flag picoCTF{p4ck37_5h4rk_01b0a0d6}
                                                                                                                                                     

