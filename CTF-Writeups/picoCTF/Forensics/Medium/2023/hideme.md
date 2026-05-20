# 🚩hideme - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `flag.png`
- **Key Skills And Tools:** file, zsteg, reading data image
---

## 🔍 Challenge 

Every file gets a flag.

The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.


### 🧪 Logic Extraction:

Open the challenge image file.

<div align="center">

   <img width="881" height="475" alt="image" src="https://github.com/user-attachments/assets/498d3c75-0b7e-4a60-a101-37337f2c782b" />


</div>

We used the `file` command to check if there was anything there; it was just a normal image file.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file flag.png 
flag.png: PNG image data, 512 x 504, 8-bit/color RGBA, non-interlaced
```
I used the `zsteg` command to extract bit data and found that it still contained a compressed file.

```     
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ zsteg flag.png        
[?] 3198 bytes of extra data after image end (IEND), offset = 0x9b3b
extradata:0         .. file: Zip archive data, made by v3.0 UNIX, extract using at least v1.0, last modified Mar 16 2023 02:01:50, uncompressed size 0, method=store
    00000000: 50 4b 03 04 0a 00 00 00  00 00 39 10 70 56 00 00  |PK........9.pV..|
    00000010: 00 00 00 00 00 00 00 00  00 00 07 00 1c 00 73 65  |..............se|
    00000020: 63 72 65 74 2f 55 54 09  00 03 8d 78 12 64 8d 78  |cret/UT....x.d.x|
    00000030: 12 64 75 78 0b 00 01 04  00 00 00 00 04 00 00 00  |.dux............|
    00000040: 00 50 4b 03 04 14 00 00  00 08 00 39 10 70 56 0f  |.PK........9.pV.|
    00000050: 5a d1 78 3c 0b 00 00 d5  0b 00 00 0f 00 1c 00 73  |Z.x<...........s|
    00000060: 65 63 72 65 74 2f 66 6c  61 67 2e 70 6e 67 55 54  |ecret/flag.pngUT|
    00000070: 09 00 03 8d 78 12 64 8d  78 12 64 75 78 0b 00 01  |....x.d.x.dux...|
    00000080: 04 00 00 00 00 04 00 00  00 00 cd 56 55 5c d3 8d  |...........VU\..|
    00000090: 1a fe 83 0a a3 27 48 7c  84 80 94 32 7a 12 32 a9  |.....'H|...2z.2.|
    000000a0: 09 92 03 1c 29 21 21 30  69 a4 26 35 40 42 90 54  |....)!!0i.&5@B.T|
    000000b0: 3f 44 40 24 86 c0 a8 d1  08 23 94 10 46 c8 87 12  |?D@$.....#..F...|
    000000c0: d2 18 1b 63 a4 92 92 67  e7 dc 9d 8b 73 7f de 8b  |...c...g....s...|
    000000d0: 37 9f f7 e6 f9 3d ef ef  f7 26 9b 9b ea b3 31 f3  |7....=...&....1.|
    000000e0: 33 03 00 c0 66 68 a0 8b  04 00 7a 5b 5a ae 04 a6  |3...fh....z[Z...|
    000000f0: 39 60 d7 57 d2 9a 16 ce  a3 74 10 3a 00 50 97 c1  |9`.W.....t.:.P..|
chunk:0:IHDR        .. file: Adobe Photoshop Color swatch, version 0, 512 colors; 1st RGB space (0), w 0x1f8, x 0x806, y 0, z 0; 2nd RGB space (0), w 0, x 0, y 0, z 0                                                                                                                                                
```
I extracted the file.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ unzip flag.png 
Archive:  flag.png
warning [flag.png]:  39739 extra bytes at beginning or within zipfile
  (attempting to process anyway)
   creating: secret/
  inflating: secret/flag.png  
```
Open the file to get the flag.
<div align="center">

  <img width="980" height="377" alt="image" src="https://github.com/user-attachments/assets/78ac69d6-41aa-4d21-ae4e-8b52699152cc" />


</div>

## Run 
.flag picoCTF{Hiddinng_An_imag3_within_@n_ima9e_d55982e8}
