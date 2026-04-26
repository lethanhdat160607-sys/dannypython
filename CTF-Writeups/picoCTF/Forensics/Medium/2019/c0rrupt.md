# 🚩c0rrupt - picoCTF 2019

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `mystery`
- **Key Skills And Tools:** xxd, mv, exiftool, data extraction
---

## 🔍 Challenge 

We found this file. Recover the flag.

### 🧪 Logic Extraction:

I used the `xxd` command to extract the data from the first 20 lines of the file.
```                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools]
└─$ xxd mystery | head -n 20
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..
000000a0: 3871 2232 eb4f 57cf 14e6 25ff e5ff 5b2c  8q"2.OW...%...[,
000000b0: 168b c562 b158 2c16 8bc5 62b1 582c 161d  ...b.X,...b.X,..
000000c0: d6d7 678b c562 b158 2c16 8bc5 62b1 582c  ..g..b.X,...b.X,
000000d0: 168b 4597 f5f5 d962 b158 2c16 8bc5 62b1  ..E....b.X,...b.
000000e0: 582c 168b c562 d165 7d7d b658 2c16 8bc5  X,...b.e}}.X,...
000000f0: 62b1 582c 168b c562 b158 7459 5f9f 2d16  b.X,...b.XtY_.-.
00000100: 8bc5 62b1 582c 168b c562 b158 2c16 5dd6  ..b.X,...b.X,.].
00000110: d767 8bc5 62b1 582c 168b c562 b158 2c16  .g..b.X,...b.X,.
00000120: 8b45 97f5 f5d9 62b1 582c 168b c562 b158  .E....b.X,...b.X
00000130: 2c16 8bc5 62d1 657d 7db6 582c 168b c562  ,...b.e}}.X,...b

```
#
I used the `xxd` command to extract the data from the last 20 lines of the file.
```
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools]
└─$ xxd mystery | tail -n 20
00031780: 65fb 0c00 0000 00a6 6c9f 0100 0000 c094  e.......l.......
00031790: ed33 0000 0000 98b2 7d06 0000 0000 53b6  .3......}.....S.
000317a0: cf00 0000 0060 caf6 1900 0000 004c d93e  .....`.......L.>
000317b0: 0300 0000 8029 db67 0000 0000 3065 fb0c  .....).g....0e..
000317c0: 0000 0000 a66c 9f01 0000 00c0 94ed 3300  .....l........3.
000317d0: 0000 0098 b27d 0600 0000 0053 b6cf 0000  .....}.....S....
000317e0: 0000 60ca f619 0000 0000 4cd9 3e03 0000  ..`.......L.>...
000317f0: 0080 29db 6700 0000 0030 65fb 0c00 0000  ..).g....0e.....
00031800: 00a6 6c9f 0100 0000 c094 ed33 0000 0000  ..l........3....
00031810: 98b2 7d06 0000 0000 53b6 cf00 0000 0060  ..}.....S......`
00031820: caf6 1900 0000 004c d93e 0300 0000 8029  .......L.>.....)
00031830: db67 0000 0000 3065 fb0c 0000 0000 a66c  .g....0e.......l
00031840: 9f01 0000 00c0 94ed 3300 0000 0098 b27d  ........3......}
00031850: 0600 0000 0053 b6cf 0000 0000 60ca f619  .....S......`...
00031860: 0000 0000 4cd9 3e03 0000 0080 29db 6700  ....L.>.....).g.
00031870: 0000 0030 65fb 0c00 0000 00a6 6c9f 0100  ...0e.......l...
00031880: 0000 c094 ed33 0000 0000 98b2 7d06 0000  .....3......}...
00031890: 0000 53b6 cf00 0000 0060 caf6 1900 0000  ..S......`......
000318a0: 004c fcbf fff7 ff01 cf09 313c 6ff1 75b8  .L........1<o.u.
000318b0: 0000 0000 4945 4e44 ae42 6082            ....IEND.B`.

```

#
Use the `hexedit` command to modify the file's data, and the `pngcheck` command to extract the data to check if the image file formats (PNG, IHDR, IDAT, etc.) are correct.

```
┌──(kali㉿kali)-[~/Tools]
└─$ hexedit mystery

┌──(kali㉿kali)-[~/Tools]
└─$ pngcheck -v mystery

```
#

```
┌──(kali㉿kali)-[~/Tools]
└─$ xxd mystery | head -n20 
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 0000 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f000 00ff a549 4441 5478 5eec bd3f  R$.....IDATx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..
000000a0: 3871 2232 eb4f 57cf 14e6 25ff e5ff 5b2c  8q"2.OW...%...[,
000000b0: 168b c562 b158 2c16 8bc5 62b1 582c 161d  ...b.X,...b.X,..
000000c0: d6d7 678b c562 b158 2c16 8bc5 62b1 582c  ..g..b.X,...b.X,
000000d0: 168b 4597 f5f5 d962 b158 2c16 8bc5 62b1  ..E....b.X,...b.
000000e0: 582c 168b c562 d165 7d7d b658 2c16 8bc5  X,...b.e}}.X,...
000000f0: 62b1 582c 168b c562 b158 7459 5f9f 2d16  b.X,...b.XtY_.-.
00000100: 8bc5 62b1 582c 168b c562 b158 2c16 5dd6  ..b.X,...b.X,.].
00000110: d767 8bc5 62b1 582c 168b c562 b158 2c16  .g..b.X,...b.X,.
00000120: 8b45 97f5 f5d9 62b1 582c 168b c562 b158  .E....b.X,...b.X
00000130: 2c16 8bc5 62d1 657d 7db6 582c 168b c562  ,...b.e}}.X,...b
```


<div> 
  <img width="1009" height="389" alt="image" src="https://github.com/user-attachments/assets/eb2d218b-3b4b-4724-ae93-468c07f09c01" />

</div>

## Run 
.flag picoCTF{now_you_know_about_extensions}
