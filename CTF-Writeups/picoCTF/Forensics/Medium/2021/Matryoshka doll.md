# 🚩Matryoshka doll.md - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `dolls.jpg`
- **Key Skills And Tools:** binwalk, extract hidden data
---

## 🔍 Challenge 

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?
Image: dolls.jpg

### 🧪 Logic Extraction:

I use the `binwalk` command to scan the binary code of the file to see hidden characters or files, while `-e` (short for `--extract`) is a parameter that tells `Binwalk` to automatically extract any files it finds inside the original file.

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ binwalk -e dolls.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378933, uncompressed size: 383920, name: base_images/2_c.jpg

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

                                                                                                                                                   

```

We already have the file `_dolls.jpg.extracted`. Inside, we find `4286C.zip` and `base_images`. I then go into the `base_images` file and find another image inside. I use the `binwalk` command to view the hidden data and see if there's anything else hidden.

```         

┌──(kali㉿kali)-[~/Tools/CTF]
└─$ ls
dolls.jpg  _dolls.jpg.extracted
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ cd _dolls.jpg.extracted
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF/_dolls.jpg.extracted]
└─$ ls
4286C.zip  base_images
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF/_dolls.jpg.extracted]
└─$ cd base_images         
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF/_dolls.jpg.extracted/base_images]
└─$ ls
2_c.jpg
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF/_dolls.jpg.extracted/base_images]
└─$ binwalk 2_c.jpg     

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196025, uncompressed size: 201427, name: base_images/3_c.jpg
383787        0x5DB2B         End of Zip archive, footer length: 22
383898        0x5DB9A         End of Zip archive, footer length: 22
```

I used the command `binwalk -e -M 2_c.jpg` with the additional command `-M` to open more hidden files inside until half of the hidden files were gone.

```
┌──(kali㉿kali)-[~/Tools/CTF/_dolls.jpg.extracted/base_images]
└─$ binwalk -e -M 2_c.jpg 

Scan Time:     2026-05-03 03:50:58
Target File:   /home/kali/Tools/CTF/_dolls.jpg.extracted/base_images/2_c.jpg
MD5 Checksum:  e3fa93b59d62b25117c563f028cdf8ed
Signatures:    436

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196025, uncompressed size: 201427, name: base_images/3_c.jpg

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented


Scan Time:     2026-05-03 03:50:58
Target File:   /home/kali/Tools/CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/3_c.jpg
MD5 Checksum:  fdbf99dfe0b7d1597c3eb005cbefccab
Signatures:    436

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77633, uncompressed size: 79786, name: base_images/4_c.jpg

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented


Scan Time:     2026-05-03 03:50:58
Target File:   /home/kali/Tools/CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/4_c.jpg
MD5 Checksum:  dbc103a52d4ea7741386f2b409fe0c68
Signatures:    436

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
79578         0x136DA         Zip archive data, at least v1.0 to extract, compressed size: 42, uncompressed size: 42, name: flag.txt

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented


Scan Time:     2026-05-03 03:50:59
Target File:   /home/kali/Tools/CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt
MD5 Checksum:  c8974fd9d4f96521b3fe75e817437d77
Signatures:    436

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

```
I discovered a hidden flag file.

```
Scan Time:     2026-05-03 03:50:59
Target File:   /home/kali/Tools/CTF/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt
```
Use the `cat` command to access the file and get the flag.
```
┌──(kali㉿kali)-[~/Tools/CTF/_dolls.jpg.extracted/base_images]
└─$ cat _2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt 
picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}
```
## Run 
.flag picoCTF{LL9lb1dR4QbGe4l4iWCvGq9pdtwt7392}

