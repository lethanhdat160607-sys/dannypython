# 🚩What Lies Within - picoCTF 2019

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `buildings.png`
- **Key Skills And Tools:** xxd, zsteg, data extraction
---

## 🔍 Challenge 

There's something in the building. Can you retrieve the flag?


### 🧪 Logic Extraction:

I used the `xxd` command to extract the data because I saw it was an image file and everything seemed fine, nothing suspicious.

```
                                                                             
┌──(kali㉿kali)-[~/Tools]
└─$ xxd buildings.png | head -n20
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0291 0000 01b6 0806 0000 0027 6add  .............'j.
00000020: d800 0020 0049 4441 5478 5eac bd4d 8b24  ... .IDATx^..M.$
00000030: 6b96 2676 d2ca dada daca da70 b95c 2ec7  k.&v.......p.\..
00000040: e504 4128 95a4 2e97 a210 4d33 2b21 b41a  ..A(......M3+!..
00000050: f403 b4d6 cf98 8516 6216 4208 2d06 a185  ........b.B.-...
00000060: 16c3 d088 6218 865e 348d 6886 6610 4333  ....b..^4.h.f.C3
00000070: 1445 5134 cde5 9224 4910 0431 8ecb 71f9  .EQ4...$I..1..q.
00000080: f8f8 d858 59db b5b2 b214 cf73 ce6b ef6b  ...XY......s.k.k
00000090: e6ee 91f7 7677 d447 64b8 dbc7 fb79 cef3  ....vw.Gd....y..
000000a0: 3ee7 ebcd c37f fe1f 7dfe 77ff df7f 90bf  >.......}.w.....
000000b0: ae13 f9fd 1fcf 25fe 512a 87d3 ff2b 59f6  ......%.Q*...+Y.
000000c0: 467e fddd af25 4962 8993 587e db7c 96e4  F~...%Ib..X~.|..
000000d0: 7752 f9dc 7e96 df76 223f febd df93 1fff  wR..~..v"?......
000000e0: 5e22 bffe 4d25 d19b cff2 5df5 d792 fffe  ^"..M%....].....
000000f0: ef4b f9ef 2bb9 7bb8 9797 ed8b fca6 ff8d  .K..+.{.........
00000100: c4c9 efc8 9bfe b7f2 f973 24bf 1bc5 f23b  .........s$....;
00000110: 492a c9ef 26f2 dbdf b6f2 dd6f bf93 febb  I*..&......o....
00000120: 5a9a a693 1ffd e88d c89b 487e 9cff be7c  Z.........H~...|
00000130: f7eb 523e bfe9 e5f7 1291 fff2 bf78 2bff  ..R>.........x+.
```

#
I then used the `zsteg` command to extract the data it extracted into the image's color points, and it produced a flag.
<div align="center">
  <img width="579" height="252" alt="image" src="https://github.com/user-attachments/assets/af209efb-af5a-4d48-b3f3-00a0de3f5095" />

</div>


## Run 
.flag picoCTF{h1d1ng_1n_th3_b1t5}
