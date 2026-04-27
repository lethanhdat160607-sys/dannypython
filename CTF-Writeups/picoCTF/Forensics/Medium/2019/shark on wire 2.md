# 🚩shark on wire 2 - picoCTF 2019

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `pico_img.png`
- **Key Skills And Tools:** exiftool, data extraction
---

## 🔍 Challenge 

Find the flag in this picture.


### 🧪 Logic Extraction:

<div align="center">
   <img width="776" height="382" alt="image" src="https://github.com/user-attachments/assets/4936cdc4-6fe5-4b6c-9da9-ccf8540bded7" />

</div>

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -r ./capture.pcap -T fields -e udp.srcport -Y "udp.dstport == 22"
5000
5112
5105
5099
5111
5067
5084
5070
5123
5112
5049
5076
5076
5102
5051
5114
5051
5100
5095
5100
5097
5116
5097
5095
5118
5049
5097
5095
5115
5116
5051
5103
5048
5125
5000
```


## Run 
.flag picoCTF{s0_m3ta_9a8b5aa1}
