# 🚩endianness-v2 - picoCTF 2024

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `challengefile`
- **Key Skills And Tools:** xxd, file, python, reading data
---

## 🔍 Challenge 

Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is.

Download it here and see what you can get out of it

### 🧪 Logic Extraction:

First, I used the `file` and `xxd` commands to check, and it reported that the data was corrupted. I used the `xxd` command to check if the bits were corrupted or incorrect, and the segment `e0 ff d8 ff 46 4a 10 00 01 00 46 49 01 00 00 01 ....FJ....FI....` was there because I had to see it, but I was expecting it to be an image file.

```

┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file challengefile
challengefile: data
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ xxd -g 1 ./challengefile | head -n20 
00000000: e0 ff d8 ff 46 4a 10 00 01 00 46 49 01 00 00 01  ....FJ....FI....
00000010: 00 00 01 00 43 00 db ff 06 06 08 00 08 05 06 07  ....C...........
00000020: 09 07 07 07 0c 0a 08 09 0b 0c 0d 14 12 19 0c 0b  ................
00000030: 1d 14 0f 13 1d 1e 1f 1a 20 1c 1c 1a 20 27 2e 24  ........ ... '.$
00000040: 1c 23 2c 22 29 37 28 1c 34 31 30 2c 27 1f 34 34  .#,")7(.410,'.44
00000050: 32 38 3d 39 34 33 2e 3c 00 db ff 32 09 09 01 43  28=943.<...2...C
00000060: 0c 0b 0c 09 18 0d 0d 18 21 1c 21 32 32 32 32 32  ........!.!22222
00000070: 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32  2222222222222222
00000080: 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32  2222222222222222
00000090: 32 32 32 32 32 32 32 32 32 32 32 32 c0 ff 32 32  222222222222..22
000000a0: 00 08 11 00 03 2c 01 96 02 00 22 01 11 03 01 11  .....,....".....
000000b0: 00 c4 ff 01 01 00 00 1f 01 01 01 05 00 01 01 01  ................
000000c0: 00 00 00 00 01 00 00 00 05 04 03 02 09 08 07 06  ................
000000d0: c4 ff 0b 0a 00 10 b5 00 03 03 01 02 05 03 04 02  ................
000000e0: 00 04 04 05 01 7d 01 00 04 00 03 02 21 12 05 11  .....}......!...
000000f0: 13 06 41 31 22 07 61 51 81 32 14 71 23 08 a1 91  ..A1".aQ.2.q#...
00000100: 15 c1 b1 42 24 f0 d1 52 82 72 62 33 17 16 0a 09  ...B$..R.rb3....
00000110: 25 1a 19 18 29 28 27 26 36 35 34 2a 3a 39 38 37  %...)('&654*:987
00000120: 46 45 44 43 4a 49 48 47 56 55 54 53 5a 59 58 57  FEDCJIHGVUTSZYXW
00000130: 66 65 64 63 6a 69 68 67 76 75 74 73 7a 79 78 77  fedcjihgvutszyxw
```
<a href="https://en.wikipedia.org/wiki/List_of_file_signatures"> Google </a>


<div align="center">
  <img width="1346" height="587" alt="image" src="https://github.com/user-attachments/assets/53153746-75ca-4db4-8d01-d78ecc9cf688" />


</div>


```
new_hex = ""
 
with open("challengefile", "rb") as file:
    hexdata = file.read().hex()
 
hex_chunks = [hexdata[i:i+8] for i in range(0, len(hexdata), 8)]
 
for chunk in hex_chunks:
    for i in range(len(chunk)-2,-1,-2):
        new_hex += chunk[i] + chunk[i+1]
 
with open("solved.jpg", "wb") as file:
    file.write(bytes.fromhex(new_hex))
 
print("File created successfully")
```


## Run 
.flag picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_f72c4bf7}

