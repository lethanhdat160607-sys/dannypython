# 🚩Pitter, Patter, Platters - picoCTF 2020

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `pico_img.png`
- **Key Skills And Tools:** exiftool, data extraction
---

## 🔍 Challenge 



### 🧪 Logic Extraction:




```

┌──(kali㉿kali)-[~/Tools]
└─$ file suspicious.dd.sda1
suspicious.dd.sda1: Linux rev 1.0 ext3 filesystem data, UUID=fc168af0-183b-4e53-bdf3-9c1055413b40 (needs journal recovery)

```
#
```                                                                         
┌──(kali㉿kali)-[~/Tools]
└─$ fls -r suspicious.dd.sda1
d/d 11: lost+found
d/d 2009:       boot
+ d/d 2010:     grub
++ r/r 2013:    e2fs_stage1_5
++ r/r 2014:    fat_stage1_5
++ r/r 2015:    ffs_stage1_5
++ r/r 2016:    iso9660_stage1_5
++ r/r 2017:    jfs_stage1_5
++ r/r 2018:    minix_stage1_5
++ r/r 2019:    reiserfs_stage1_5
++ r/r 2020:    stage1
++ r/r 2021:    stage2
++ r/r 2022:    stage2_eltorito
++ r/r 2023:    ufs2_stage1_5
++ r/r 2024:    vstafs_stage1_5
++ r/r 2025:    xfs_stage1_5
++ r/r 2026:    menu.lst
+ r/r 2011:     core.gz
+ r/r 2012:     vmlinuz
d/d 4017:       tce
+ r/r 4018:     mydata.tgz
+ d/d 4019:     optional
++ r/r 4022:    openssh.tcz.dep
++ r/r 4023:    gcc_libs.tcz.md5.txt
++ r/r 4024:    gcc_libs.tcz
++ r/r 4025:    openssl-1.0.0.tcz.md5.txt
++ r/r 4026:    openssl-1.0.0.tcz
++ r/r 4027:    openssh.tcz.md5.txt
++ r/r 4028:    openssh.tcz
++ r/r 4029:    nano.tcz.dep
++ r/r 4030:    ncurses.tcz.dep
++ r/r 4031:    ncurses-common.tcz.md5.txt
++ r/r 4032:    ncurses-common.tcz
++ r/r 4033:    ncurses.tcz.md5.txt
++ r/r 4034:    ncurses.tcz
++ r/r 4035:    nano.tcz.md5.txt
++ r/r 4036:    nano.tcz
++ r/r 4037:    nginx.tcz.dep
++ r/r 4038:    pcre.tcz.dep
++ r/r 4039:    bzip2-lib.tcz.md5.txt
++ r/r 4040:    bzip2-lib.tcz
++ r/r 4041:    pcre.tcz.md5.txt
++ r/r 4042:    pcre.tcz
++ r/r 4043:    nginx.tcz.md5.txt
++ r/r 4044:    nginx.tcz
++ r/r 4045:    fuse.tcz.md5.txt
++ r/r 4046:    fuse.tcz
++ r/r 4047:    libdnet.tcz
++ r/r 4048:    open-vm-tools.tcz
++ r/r 4049:    open-vm-tools-modules-3.8.13-tinycore.tcz
++ r/r 4050:    libtirpc.tcz.md5.txt
++ r/r 4051:    libtirpc.tcz
++ r/r 4052:    glib2.tcz.dep
++ r/r 4053:    libffi.tcz.md5.txt
++ r/r 4054:    libffi.tcz
++ r/r 4055:    glib2.tcz.md5.txt
++ r/r 4056:    glib2.tcz
+ d/d 4020:     ondemand
+ r/r 4021:     onboot.lst
r/r 12: suspicious-file.txt
V/V 8033:       $OrphanFiles
```
#

```                                                                             
┌──(kali㉿kali)-[~/Tools]
└─$ icat suspicious.dd.sda1 12
Nothing to see here! But you may want to look here -->
```
#
```                                                                             
┌──(kali㉿kali)-[~/Tools]
└─$ xxd suspicious.dd.sda1 | grep -e "-->" 
00200430: 7265 202d 2d3e 0a7d 0033 0039 0038 0036  re -->.}.3.9.8.6
01326260: 98d8 b63d 2d2d 3ede d94b 66ba 9bad 5434  ...=-->..Kf...T4
01e8c050: 0a06 4a72 2d2d 3e42 5327 d126 69c4 d96b  ..Jr-->BS'.&i..k
                                                                             
┌──(kali㉿kali)-[~/Tools]
└─$ xxd suspicious.dd.sda1 | grep -e "-->" -C 6 
002003d0: 9271 63ca cec6 b289 4c26 f376 4331 a5a8  .qc.....L&.vC1..
002003e0: 78f4 4620 ff0b ec0b 9f98 4170 5208 2c4a  x.F ......ApR.,J
002003f0: 780c 5922 4343 5d9c 86be b131 ddf8 c4df  x.Y"CC]....1....
00200400: 4e6f 7468 696e 6720 746f 2073 6565 2068  Nothing to see h
00200410: 6572 6521 2042 7574 2079 6f75 206d 6179  ere! But you may
00200420: 2077 616e 7420 746f 206c 6f6f 6b20 6865   want to look he
00200430: 7265 202d 2d3e 0a7d 0033 0039 0038 0036  re -->.}.3.9.8.6
00200440: 0033 0031 0032 0066 005f 0033 003c 005f  .3.1.2.f._.3.<._
00200450: 007c 004c 006d 005f 0031 0031 0031 0074  .|.L.m._.1.1.1.t
00200460: 0035 005f 0033 0062 007b 0046 0054 0043  .5._.3.b.{.F.T.C
00200470: 006f 0063 0069 0070 0000 0000 0000 0000  .o.c.i.p........
00200480: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00200490: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
01326200: 2399 db65 56bc a96d f3ba ca30 3a06 9257  #..eV..m...0:..W
01326210: 6323 fd78 8d84 fe4f 1f51 61a8 3dc6 71ce  c#.x...O.Qa.=.q.
01326220: 5e2e b472 b1ce e3d7 4152 f1e2 e349 cc73  ^..r....AR...I.s
01326230: 8af7 2ac7 595a 8d4f b938 a100 eacd 6ff0  ..*.YZ.O.8....o.
01326240: ebfc 8690 bb9f c337 7610 2a87 2a75 87bc  .......7v.*.*u..
01326250: fd1e 1f5e bc80 d66f e17d e9f2 5852 d010  ...^...o.}..XR..
01326260: 98d8 b63d 2d2d 3ede d94b 66ba 9bad 5434  ...=-->..Kf...T4
01326270: 22ef b0b3 cbd2 5aa2 b3b4 5a2d ad5b 3322  ".....Z...Z-.[3"
01326280: fdd6 c8d7 f6cc cb00 d247 fa59 7a30 d07f  .........G.Yz0..
01326290: a3e5 e817 f648 bf3d f3cb cc7f c0ab c9d9  .....H.=........
013262a0: 0b00 2bd0 2700 e328 8025 4c00 184b 3535  ..+.'..(.%L..K55
013262b0: 235f 8b5e 2252 90e5 9418 4186 2dad cbc1  #_.^"R....A.-...
013262c0: 003d 517e cb9e d901 af06 4bab 479f d911  .=Q~......K.G...
--
01e8bff0: a3f3 88f5 fe7d 3fc2 580a 7168 5285 0988  .....}?.X.qhR...
01e8c000: 332b 671b cb05 345f cce3 019a 5220 2c47  3+g...4_....R ,G
01e8c010: d612 d93f 7c0c 6a25 3162 30bb 106b 8554  ...?|.j%1b0..k.T
01e8c020: ae49 4c28 55d8 7da3 cbac 025e 0b84 3141  .IL(U.}....^..1A
01e8c030: 73da 7f01 5150 fe53 78da ad57 6d6c 1cc5  s...QP.Sx..Wml..
01e8c040: 19de f5ad ed4d b478 0f72 09e7 e0aa 6e20  .....M.x.r....n 
01e8c050: 0a06 4a72 2d2d 3e42 5327 d126 69c4 d96b  ..Jr-->BS'.&i..k
01e8c060: 873b 0321 817e 80e8 2124 303b 491b d810  .;.!.~..!$0;I...
01e8c070: ba3e c993 6145 2a40 42a8 3ffa c350 94a6  .>..aE*@B.?..P..
01e8c080: c46a d360 20a2 4712 7913 94b6 9793 4b5c  .j.` .G.y.....K\
01e8c090: e14a 97f6 8226 dd4b 72c4 56ec 7ce0 e93b  .J...&.Kr.V.|..;
01e8c0a0: b377 8781 54ea 8f9e 74ba d99d 99e7 7de6  .w..T...t.....}.
01e8c0b0: 99f7 ebb2 e826 922c 3867 9521 357e 7e6b  .....&.,8g.!5~~k

```
#

```           
┌──(kali㉿kali)-[~/Tools]
└─$ xxd suspicious.dd.sda1 | grep -e "-->" -A 4 | xxd -r 
re -->
}3986312f_3<_|Lm_111t5_3b{FTCocip�ض=-->��Kf���T4"ﰳ��Z���Z-�[3"��������G�Yz0�����H�=�������
                                                                                          +�'�(�%L▒K55
Jr-->BS'�&i��k�;!�~��!$0;I�>ɓaE*@B�?��P���j�` �Gy����K\�J���&�Kr�V�|��;                                                      

```
#
```
┌──(kali㉿kali)-[~/Tools]
└─$ echo "}3986312f_3<_|Lm_111t5_3b{FTCocip" | rev
picoCTF{b3_5t111_mL|_<3_f2136893}

```


#Run 

.flag 
