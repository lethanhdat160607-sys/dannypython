# 🚩Dear Diary.md - picoCTF 2024

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `disk.flag.img.gz`
- **Key Skills And Tools:** mml, fls, icat, strings, xxd, reading data disk
---

## 🔍 Challenge 

If you can find the flag on this disk image, we can close the case for good!

Download the disk image here.

### 🧪 Logic Extraction:

This was a disk challenge, so I used the `mmls` command to probe what files were inside.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000616447   0000614400   Linux (0x83)
003:  000:001   0000616448   0001140735   0000524288   Linux Swap / Solaris x86 (0x82)
004:  000:002   0001140736   0002097151   0000956416   Linux (0x83)

```

I used the `fls` command again to extract the file and see what files were inside.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736                                                  
d/d 32513:      home
d/d 11: lost+found
d/d 32385:      boot
d/d 64769:      etc
d/d 32386:      proc
d/d 13: dev
d/d 32387:      tmp
d/d 14: lib
d/d 32388:      var
d/d 21: usr
d/d 32393:      bin
d/d 32395:      sbin
d/d 32539:      media
d/d 203:        mnt
d/d 32543:      opt
d/d 204:        root
d/d 32544:      run
d/d 205:        srv
d/d 32545:      sys
d/d 32530:      swap
V/V 119417:     $OrphanFiles

```
I used the `fls` command to extract each column of numbers from the file, and the number 8 indicates a flag, but I'm not sure what it means.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 1 | strings
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 2 | strings
d/d 32513:      home
d/d 11: lost+found
d/d 32385:      boot
d/d 64769:      etc
d/d 32386:      proc
d/d 13: dev
d/d 32387:      tmp
d/d 14: lib
d/d 32388:      var
d/d 21: usr
d/d 32393:      bin
d/d 32395:      sbin
d/d 32539:      media
d/d 203:        mnt
d/d 32543:      opt
d/d 204:        root
d/d 32544:      run
d/d 205:        srv
d/d 32545:      sys
d/d 32530:      swap
V/V 119417:     $OrphanFiles
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 3 | strings
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 4 | strings
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 5 | strings
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 6 | strings
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 7 | strings
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 8 | strings

r/r 1845:       pic
-/- * 0:
r/r 1845:       oCT
-/- * 0:
-/- 18327:      d.
r/r 1845:       F{1
-/- * 0:        ^^
-/- 46451:      $?
r/r 1845:       _53
-/- * 0:        D^
r/r 1845:       3_n
-/- * 0:        ]^
-/- 13793:
-/- 3215:       |
w6q^
r/r 1845:       4m3
-/- * 0:        v^
r/r 1845:       5_8
-/- * 0:
r/r 1845:       0d2
-/- * 0:
r/r 1845:       4b3
-/- * 0:
r/r 1845:       0}
-/- * 0:
r/r 1845:       its-all-in-the-name
-/- * 0:        ^^
-/- 3016:       h*.
-/- 61306:

```
I used the `fls` command again to extract the file. I also used the `sort` command to sort it, and `uniq` to avoid duplicate files, and I found a very suspicious file: `innocuous-file.txt`.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls disk.flag.img -o 1140736 8 | strings | sort | uniq | grep "file"          
d/d 1015:       filelayout
d/d 1017:       flexfilelayout
d/d 64880:      profile.d
d/d 966:        cachefiles
r/r 1016:       nfs_layout_nfsv41_files.ko.gz
r/r 1018:       nfs_layout_flexfiles.ko.gz
r/r 1844:       innocuous-file.txt
r/r 1845:       original-filename
r/r 242:        ewaitfile
r/r 64849:      profile
r/r 65007:      base.files
r/r 65009:      bootchart.files
r/r 65010:      btrfs.files
r/r 65014:      cryptkey.files
r/r 65015:      cryptsetup.files
r/r 65018:      dhcp.files
r/r 65027:      https.files
r/r 65029:      keymap.files
r/r 65031:      lvm.files
r/r 65034:      nbd.files
r/r 65036:      network.files
r/r 65042:      raid.files
r/r 65050:      wireguard.files
r/r 65053:      xfs.files
r/r 65056:      zfs.files
r/r 967:        cachefiles.ko.gz    
```

From the `fls` command we learned earlier, the flag is spread across many files, so we won't use the usual `icat` command. Instead, we'll use `icat disk.flag.img -o 1140736 8 | xxd | grep ".txt" -A3` and use `xxd` to convert all the raw data into a hexdump format displayed as readable columns. Then we'll use the `grep ".txt" -A3` command to read the txt files, extract the next three lines below, and check the following line as well. And there you have it, the flag!
```


┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat disk.flag.img -o 1140736 8 | xxd | grep ".txt" -A3 
001f8840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
001f8850: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001f8860: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001f8870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
001fbc40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
001fbc50: a803 1101 6f72 6967 696e 616c 2d66 696c  ....original-fil
001fbc60: 656e 616d 6500 0000 0000 0000 0000 0000  ename...........
001fbc70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
001fdc40: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
001fdc50: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001fdc60: 0000 0000 0000 0000 3507 0000 8c03 0301  ........5.......
001fdc70: 7069 6300 0000 0000 0000 0000 0000 0000  pic.............
--
001ff440: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
001ff450: a803 0301 6f43 5400 0000 0000 0000 0000  ....oCT.........
001ff460: 0000 0000 0000 0000 0000 0000 0000 0000  ................
001ff470: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00201840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00201850: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
00201860: 467b 3100 0000 0000 0000 0000 0000 0000  F{1.............
00201870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00203c40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00203c50: a803 0301 5f35 3300 0000 0000 0000 0000  ...._53.........
00203c60: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00203c70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00206040: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00206050: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
00206060: 335f 6e00 0000 0000 0000 0000 0000 0000  3_n.............
00206070: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00207840: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
00207850: a803 0301 346d 3300 0000 0000 0000 0000  ....4m3.........
00207860: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00207870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00209c40: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00209c50: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
00209c60: 355f 3800 0000 0000 0000 0000 0000 0000  5_8.............
00209c70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
0020b440: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
0020b450: a803 0301 3064 3200 0000 0000 0000 0000  ....0d2.........
0020b460: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0020b470: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
0020d840: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
0020d850: 0000 0000 0000 0000 3507 0000 9c03 0301  ........5.......
0020d860: 3462 3300 0000 0000 0000 0000 0000 0000  4b3.............
0020d870: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
0020fc40: 732d 6669 6c65 2e74 7874 0000 3507 0000  s-file.txt..5...
0020fc50: a803 0201 307d 0000 0000 0000 0000 0000  ....0}..........
0020fc60: 0000 0000 0000 0000 0000 0000 0000 0000  ................
0020fc70: 0000 0000 0000 0000 0000 0000 0000 0000  ................
--
00211440: 732d 6669 6c65 2e74 7874 0000 0000 0000  s-file.txt......
00211450: 0000 0000 0000 0000 3507 0000 9c03 1301  ........5.......
00211460: 6974 732d 616c 6c2d 696e 2d74 6865 2d6e  its-all-in-the-n
00211470: 616d 6500 0000 0000 0000 0000 0000 0000  ame.............
                                                                     
```

## Run 
.flag picoCTF{1_533_n4m35_80d24b30}

