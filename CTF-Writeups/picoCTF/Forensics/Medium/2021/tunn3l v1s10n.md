# 🚩tunn3l v1s10n - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `tunn3l_v1s10n`
- **Key Skills And Tools:** 
---

## 🔍 Challenge 

We found this file. Recover the flag.
tunn3l_v1s10n

### 🧪 Logic Extraction:

I used the `exiftool` command to treat this as a `BMP` file.

<div align="center">  
  <img width="574" height="332" alt="image" src="https://github.com/user-attachments/assets/739b2feb-a633-4ea7-9af8-80fc6258e1cc" />
</div>

#
I used the `xxd` command to view the ciphertext, and it seems to be messing up the bit ciphertext.

```  
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ xxd tunn3l_v1s10n | head -n20
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 bad0  BM.&,...........
00000010: 0000 6e04 0000 3201 0000 0100 1800 0000  ..n...2.........
00000020: 0000 5826 2c00 2516 0000 2516 0000 0000  ..X&,.%...%.....
00000030: 0000 0000 0000 231a 1727 1e1b 2920 1d2a  ......#..'..) .*
00000040: 211e 261d 1a31 2825 352c 2933 2a27 382f  !.&..1(%5,)3*'8/
00000050: 2c2f 2623 332a 262d 2420 3b32 2e32 2925  ,/&#3*&-$ ;2.2)%
00000060: 3027 2333 2a26 382c 2836 2b27 392d 2b2f  0'#3*&8,(6+'9-+/
00000070: 2623 1d12 0e23 1711 2916 0e55 3d31 9776  &#...#..)..U=1.v
00000080: 668b 6652 996d 569e 7058 9e6f 549c 6f54  f.fR.mV.pX.oT.oT
00000090: ab7e 63ba 8c6d bd8a 69c8 9771 c193 71c1  .~c..m..i..q..q.
000000a0: 9774 c194 73c0 9372 c08f 6fbd 8e6e ba8d  .t..s..r..o..n..
000000b0: 6bb7 8d6a b085 64a0 7455 a377 5a98 6f56  k..j..d.tU.wZ.oV
000000c0: 7652 3a71 523d 6c4f 406d 5244 6e53 4977  vR:qR=lO@mRDnSIw
000000d0: 5e54 5339 3370 5852 7661 5973 5f54 7e6b  ^TS93pXRvaYs_T~k
000000e0: 5e86 7463 7e6a 5976 6250 765e 4c7a 6250  ^.tc~jYvbPv^LzbP
000000f0: 876d 5d83 6959 8d73 639b 8171 9e84 7498  .m].iY.sc..q..t.
00000100: 7e6e 9b81 718d 7363 735a 4a70 5747 5a41  ~n..q.scsZJpWGZA
00000110: 314f 3626 4e37 274f 3828 4f38 2851 3a2a  1O6&N7'O8(O8(Q:*
00000120: 5039 294f 3829 4b35 2950 3a2f 4b35 2a3f  P9)O8)K5)P:/K5*?
00000130: 291e 422e 234b 372c 4531 263f 2b20 432f  ).B.#K7,E1&?+ C/
```

I used the `ghex` command to modify the code; it's quite similar to the `HxD` tool for modifying code.

<div align="center">
  <img width="1317" height="488" alt="image" src="https://github.com/user-attachments/assets/a638b5c8-3d82-46cf-9635-685ce272510b" />

</div>

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ xxd tunn3l_v1s10n | head -n2 
00000000: 424d 8e26 2c00 0000 0000 36d0 0000 2800  BM.&,.....6...(.
00000010: 0000 6e04 0000 5203 0000 0100 1800 0000  ..n...R.........
```

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ feh tunn3l_v1s10n      
                       
```
<div align="center"> 
  <img width="1234" height="587" alt="image" src="https://github.com/user-attachments/assets/1b60886b-d92d-42f3-b1c0-80e06c037415" />

</div>

## Run 
.flag 
