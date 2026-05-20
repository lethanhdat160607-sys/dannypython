# 🚩MSB - picoCTF 2023

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png`
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...

Download the image here

### 🧪 Logic Extraction:

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png: PNG image data, 1074 x 1500, 8-bit/color RGB, non-interlaced
```

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ zsteg Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png                                                      
imagedata           .. text: "~~~|||}}}"
chunk:0:IHDR        .. file: Adobe Photoshop Color swatch, version 0, 1074 colors; 1st RGB space (0), w 0x5dc, x 0x802, y 0, z 0; 2nd space (32768), w 0x8000, x 0x8080, y 0x80, z 0                                                                                                                                  
b1,g,lsb,xy         .. file: Common Data Format (Version 2.5 or earlier) data
b1,g,msb,xy         .. file: Common Data Format (Version 2.5 or earlier) data
b2,r,lsb,xy         .. text: ["U" repeated 8 times]
b2,g,lsb,xy         .. file: Matlab v4 mat-file (little endian) \252\252\252\252\252\252\252\252, numeric, rows 4294967295, columns 4294967295
b2,g,msb,xy         .. file: Matlab v4 mat-file (little endian) UUUUUUUU, numeric, rows 4294967295, columns 4294967295
b2,b,lsb,xy         .. text: ["U" repeated 8 times]
b4,r,lsb,xy         .. text: ["w" repeated 8 times]
b4,r,msb,xy         .. text: ["U" repeated 12 times]
b4,g,msb,xy         .. text: ["w" repeated 16 times]
b4,b,lsb,xy         .. text: "\"\"\"\"\"\"\"\"4DC\""
b4,b,msb,xy         .. text: "wwwwwwww3333"

```


```

┌──(kali㉿kali)-[~/Tools/CTF1]
└─$  pngcheck -v Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png  
File: Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png (3354312 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1074 x 1500 image, 24-bit RGB, non-interlaced
  chunk IDAT at offset 0x00025, length 65536
    zlib: deflated, 32K window, default compression
  chunk IDAT at offset 0x10031, length 65536
  chunk IDAT at offset 0x2003d, length 65536
  chunk IDAT at offset 0x30049, length 65536
  chunk IDAT at offset 0x40055, length 65536
  chunk IDAT at offset 0x50061, length 65536
  chunk IDAT at offset 0x6006d, length 65536
  chunk IDAT at offset 0x70079, length 65536
  chunk IDAT at offset 0x80085, length 65536
  chunk IDAT at offset 0x90091, length 65536
  chunk IDAT at offset 0xa009d, length 65536
  chunk IDAT at offset 0xb00a9, length 65536
  chunk IDAT at offset 0xc00b5, length 65536
  chunk IDAT at offset 0xd00c1, length 65536
  chunk IDAT at offset 0xe00cd, length 65536
  chunk IDAT at offset 0xf00d9, length 65536
  chunk IDAT at offset 0x1000e5, length 65536
  chunk IDAT at offset 0x1100f1, length 65536
  chunk IDAT at offset 0x1200fd, length 65536
  chunk IDAT at offset 0x130109, length 65536
  chunk IDAT at offset 0x140115, length 65536
  chunk IDAT at offset 0x150121, length 65536
  chunk IDAT at offset 0x16012d, length 65536
  chunk IDAT at offset 0x170139, length 65536
  chunk IDAT at offset 0x180145, length 65536
  chunk IDAT at offset 0x190151, length 65536
  chunk IDAT at offset 0x1a015d, length 65536
  chunk IDAT at offset 0x1b0169, length 65536
  chunk IDAT at offset 0x1c0175, length 65536
  chunk IDAT at offset 0x1d0181, length 65536
  chunk IDAT at offset 0x1e018d, length 65536
  chunk IDAT at offset 0x1f0199, length 65536
  chunk IDAT at offset 0x2001a5, length 65536
  chunk IDAT at offset 0x2101b1, length 65536
  chunk IDAT at offset 0x2201bd, length 65536
  chunk IDAT at offset 0x2301c9, length 65536
  chunk IDAT at offset 0x2401d5, length 65536
  chunk IDAT at offset 0x2501e1, length 65536
  chunk IDAT at offset 0x2601ed, length 65536
  chunk IDAT at offset 0x2701f9, length 65536
  chunk IDAT at offset 0x280205, length 65536
  chunk IDAT at offset 0x290211, length 65536
  chunk IDAT at offset 0x2a021d, length 65536
  chunk IDAT at offset 0x2b0229, length 65536
  chunk IDAT at offset 0x2c0235, length 65536
  chunk IDAT at offset 0x2d0241, length 65536
  chunk IDAT at offset 0x2e024d, length 65536
  chunk IDAT at offset 0x2f0259, length 65536
  chunk IDAT at offset 0x300265, length 65536
  chunk IDAT at offset 0x310271, length 65536
  chunk IDAT at offset 0x32027d, length 65536
  chunk IDAT at offset 0x330289, length 11307
  chunk IEND at offset 0x332ec0, length 0
No errors detected in Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png (54 chunks, 30.6% compression).

```


```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ stegoveritas Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
Running Module: SVImage
+---------------------------+------+
|        Image Format       | Mode |
+---------------------------+------+
| Portable network graphics | RGB  |
+---------------------------+------+
Found something worth keeping!
ASCII text
+--------+------------------+-----------------------------------------------------------------------------------------------+-----------+
| Offset | Carved/Extracted | Description                                                                                   | File Name |
+--------+------------------+-----------------------------------------------------------------------------------------------+-----------+
| 0x460d | Carved           | LZMA compressed data, properties: 0xBE, dictionary size: 0 bytes, uncompressed size: 64 bytes | 460D.7z   |
| 0x460d | Extracted        | LZMA compressed data, properties: 0xBE, dictionary size: 0 bytes, uncompressed size: 64 bytes | 460D      |
+--------+------------------+-----------------------------------------------------------------------------------------------+-----------+
Found something worth keeping!
Common Data Format (Version 2.5 or earlier) data
Found something worth keeping!
Matlab v4 mat-file (little endian) UUUUUUUU, numeric, rows 4294967295, columns 4294967295
Running Module: MultiHandler

Exif
====
+---------------------+-------------------------------------------------------------------------------+
| key                 | value                                                                         |
+---------------------+-------------------------------------------------------------------------------+
| SourceFile          | /home/kali/Tools/CTF1/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png |
| ExifToolVersion     | 13.5                                                                          |
| FileName            | Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png                       |
| Directory           | /home/kali/Tools/CTF1                                                         |
| FileSize            | 3.4 MB                                                                        |
| FileModifyDate      | 2023:08:04 17:25:39-04:00                                                     |
| FileAccessDate      | 2026:05:20 16:06:45-04:00                                                     |
| FileInodeChangeDate | 2026:05:20 16:06:24-04:00                                                     |
| FilePermissions     | -rw-rw-r--                                                                    |
| FileType            | PNG                                                                           |
| FileTypeExtension   | png                                                                           |
| MIMEType            | image/png                                                                     |
| ImageWidth          | 1074                                                                          |
| ImageHeight         | 1500                                                                          |
| BitDepth            | 8                                                                             |
| ColorType           | RGB                                                                           |
| Compression         | Deflate/Inflate                                                               |
| Filter              | Adaptive                                                                      |
| Interlace           | Noninterlaced                                                                 |
| ImageSize           | 1074x1500                                                                     |
| Megapixels          | 1.6                                                                           |
+---------------------+-------------------------------------------------------------------------------+
Found something worth keeping!
PNG image data, 1074 x 1500, 8-bit/color RGB, non-interlaced
+--------+------------------+-------------------------------------------+-----------+
| Offset | Carved/Extracted | Description                               | File Name |
+--------+------------------+-------------------------------------------+-----------+
| 0x29   | Carved           | Zlib compressed data, default compression | 29.zlib   |
| 0x29   | Extracted        | Zlib compressed data, default compression | 29        |
+--------+------------------+-------------------------------------------+-----------+

```

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ grep -iR 'picoCTF{' results
results/keepers/1779308608.546615-4d5feab62d314b9430933dbfd1ddbe8a:picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ea7deb4c}
```




## Run 
.flag picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ea7deb4c}
