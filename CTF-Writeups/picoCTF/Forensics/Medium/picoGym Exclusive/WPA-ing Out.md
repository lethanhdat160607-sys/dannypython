# 🚩WPA-ing Out - picoGym Exclusive

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `wpa-ing_out.pcap`
- **Key Skills And Tools:** Aircrack-ng, Wireshark ,Password cracking and decryption
---

## 🔍 Challenge 
I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.
Use this `pcap file`and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.

### 🧪 Logic Extraction:

We first begin by downloading the wpa-ing_out.pcap file. I proceeded to open it in Wireshark, and observed that this file contains 23523 packets from an internal network.

<div align="center">

   <img width="1718" height="920" alt="image" src="https://github.com/user-attachments/assets/dda8dd43-c641-408a-aa30-19f43038b37f" />

</div>

#
You need to download the `rockyou.txt` file because it contains over 14 million passwords from a brute-force attack.

<div align="center">
   <img width="1002" height="442" alt="image" src="https://github.com/user-attachments/assets/772cc550-0525-4db8-9b2a-57bea7a001f7" />
   <p> I found and downloaded the file `rockyou.txt` to my computer. </p>
   <img width="874" height="105" alt="image" src="https://github.com/user-attachments/assets/1bb98e5e-dfc5-4562-9917-3d1dd4e36359" />

</div>

#
We perform password cracking using the `aircrack-ng` tool and combine it with the password file `rockyou.txt` to perform password scraping and scraping in all cases, like performing multiple loops, and then we get the flag.
<div align="center">
   <img width="581" height="158" alt="image" src="https://github.com/user-attachments/assets/9913bca2-007d-473b-925e-663b5b5844f5" />

</div>


Then password is found very fast and is redacted below.

```text
                               Aircrack-ng 1.7

      [00:00:04] 1309/14344391 keys tested (292.73 k/s)

      Time left: 13 hours, 38 minutes, 40 seconds                0.01%

                          KEY FOUND! [ <REDACTED> ]


      Master Key     : 4B 09 F8 03 77 6A 36 B0 6D 45 9E FC F0 B1 05 69
                       03 DD BC 71 E2 2A CE 4E C4 79 FA AF CB CC C7 F2

      Transient Key  : A3 A3 A3 A3 A3 A3 A3 A3 6A 67 C4 76 95 75 A6 09
                       BF 0E 6E E9 BC 90 73 44 22 CE 81 80 B7 84 0E 0D
                       7D FF B4 7E 0A 9C EE F3 B6 AA BB ED 93 EF 79 25
                       2B A9 21 97 45 C2 27 5D 5E E9 1F 1F D5 07 FB 8E

      EAPOL HMAC     : C5 46 D2 AF 2E 21 BC 3E 0D 3E F4 6E 10 AB BA DA
```

## Run 
.flag picoCTF{mickeymouse}


