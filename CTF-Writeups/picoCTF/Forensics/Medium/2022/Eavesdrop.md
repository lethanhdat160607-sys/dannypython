# 🚩Eavesdrop - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `capture.flag.pcap`
- **Key Skills And Tools:** wireshark, openssl, reading data
---

## 🔍 Challenge 

Download this packet capture and find the flag.
Download packet capture

### 🧪 Logic Extraction:

Open the pcap file on Wireshark and follow the TCP stream. Then, under `tcp.port == 9002`, you'll find a piece of code: `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`. We need to find the packet containing the transmitted data. Usually, you'll find the raw data in the file `file.des3`.

<div align="center">
  <img width="918" height="582" alt="image" src="https://github.com/user-attachments/assets/135292aa-9992-4f87-b435-f857b0d66b27" />

</div>


# 
It seems to me that this is the content of an encrypted file, based on the `Salted__`, which is a characteristic indicator of (Magic bytes) of a file encrypted with `OpenSSL`. When you use the `-salt` option, OpenSSL adds 8 random `salt` bytes to the beginning of the file to increase security, and it starts with this ASCII string.

<div align="center">
  <img width="910" height="571" alt="image" src="https://github.com/user-attachments/assets/55f59e0c-272d-4c3d-8eaf-efff1ada2e2b" />

</div>


#
Now, to get the Flag, change the `Raw` and save the file as `file.des3`.
<div align="center">
  <img width="911" height="576" alt="image" src="https://github.com/user-attachments/assets/bbbc5cdf-e9bf-4296-92dd-1d016b85ff13" />

</div>

#

We download the file and run the command `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123` to retrieve the flag file and open it. The `openssl` command is the main program. OpenSSl is an extremely powerful cryptographic library that supports most current encryption and decryption protocols. `des3` is an algorithm used, abbreviated as `3DES`. It works by applying the DES algorithm three times to each block of data. `-d` is for fmax encryption, and you can remove this flag or use `-e` for encryption. The parameters `-int file.des3` specify the input file, and `-out file.txt` specify the clean content after decryption. `-salt` adds a random variable to the password during encryption, creating different keys even with the same password, thus protecting against lookup table attacks. `-k supersecretpassword123` is used to provide the password.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
capture.flag.pcap  file.des3

┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
capture.flag.pcap  file.des3  file.txt
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ cat file.txt        
picoCTF{nc_73115_411_5786acc3}
```


## Run 
.flag picoCTF{nc_73115_411_5786acc3}                                                                                                                                                           

