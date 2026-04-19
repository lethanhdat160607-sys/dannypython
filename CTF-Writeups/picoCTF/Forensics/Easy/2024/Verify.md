# 🚩Verify - picoCTF 2024

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `pcap file`
- **Key Skills And Tools:** SHA-256, 
---

## 🔍 Challenge 

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the `SHA-256` hash and a decrypt script to help you know that my flags are legitimate.
`ssh -p 64996 ctf-player@rhea.picoctf.net`

Using the password `83dcefb7`. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

Checksum: `467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02`

To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file`.

### 🧪 Logic Extraction:

We're checking what's in this server, and I've opened the files to examine them. They contain some rather strange code and instructions. The challenge mentioned providing a `SHA-256` hash, so we'll focus on that.

<div align="center">
  <img width="1135" height="596" alt="image" src="https://github.com/user-attachments/assets/1f3d70a6-6fb5-471e-bbad-6a835106d745" />

</div>

#
We use the command `sha256sum files/* | Use `grep "467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02"` to search for hash codes in `files/*`. This searches all files on the provided server. Alternatively, use `grep "467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02"` to search for content and hash codes provided in the `checksum.txt` file. Next, use `./decrypt.sh files/c6c8b911` to exploit and obtain the `decrypt.sh` flag. This is a pre-written shell script that runs automatically to check files and verify hash codes, as in the previous example. `./` means to run this file directly in the directory where I am currently stopped, while `files/c6c8b911` (Arguments/Parameters) `files/` is the name of the directory containing the file, and `c6c8b911` is the name of the specific file I found above.
<div align="center">
  <img width="1019" height="101" alt="image" src="https://github.com/user-attachments/assets/a1f6403f-ee24-43a8-bffa-16530da49309" />

</div>


```
ctf-player@pico-chall$ sha256sum files/* | grep "467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02"
467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02  files/c6c8b911
ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
ctf-player@pico-chall$ ./decrypt.sh files/c6c8b911
picoCTF{trust_but_verify_c6c8b911}
```
  
## Run 
.flag picoCTF{}
