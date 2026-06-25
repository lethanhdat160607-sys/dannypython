# 🚩Forensics Git 1 - picoCTF 2026

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `disk.img.gz`
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

Can you find the flag in this disk image?

Download the disk image here.

### 🧪 Logic Extraction:

I used the `mmls` command to list the files and see if they were compressed.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ mmls disk.img
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

I used the `fls` command to list the partitions and used `-o` to select the partition I wanted to scan.
                                                                                                                                    
```                                                                                                                                    
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img      
d/d 64770:      home
d/d 11: lost+found
d/d 64769:      boot
d/d 32385:      etc
d/d 13: proc
d/d 64772:      dev
d/d 14: tmp
d/d 15: lib
d/d 64773:      var
d/d 22: bin
d/d 24: sbin
d/d 64778:      usr
d/d 64948:      media
d/d 170:        mnt
d/d 171:        opt
d/d 172:        root
d/d 173:        run
d/d 64952:      srv
d/d 174:        sys
d/d 65275:      swap
V/V 119417:     $OrphanFiles
```
I used the `fls` command to list the files, `-o` to select the partition to scan, `-r` to enter a string and file, and `grep -i "\.git"` to find the file with the .git dot as suggested in the problem, and based on the drive letter, I searched deeper.
```           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -r -o 1140736 disk.img | grep -i "\.git"
++++ d/d 65665: .git
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 65665
d/d 65666:      branches
r/r 65667:      description
d/d 65668:      hooks
d/d 65682:      info
d/d 65684:      refs
r/r 65685:      config
d/d 65689:      objects
r/r 65688:      HEAD
r/r 65696:      index
r/r 65693:      COMMIT_EDITMSG
d/d 65703:      logs
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 65693
Error extracting file from image (ext2fs_dir_open_meta: Error reading directory contents: 65693
)

                                                                                                                                                          
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 65665
d/d 65666:      branches
r/r 65667:      description
d/d 65668:      hooks
d/d 65682:      info
d/d 65684:      refs
r/r 65685:      config
d/d 65689:      objects
r/r 65688:      HEAD
r/r 65696:      index
r/r 65693:      COMMIT_EDITMSG
d/d 65703:      logs
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 65694
r/r 65695:      50f47a5dabfb4397706aa18905df936595a86e
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 65689
d/d 65690:      pack
d/d 65691:      info
d/d 65694:      f1
d/d 65697:      a6
d/d 65699:      17
d/d 65701:      4b
d/d 65692:      5f

```

```           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 65694
r/r 65695:      50f47a5dabfb4397706aa18905df936595a86e
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat -o 1140736 disk.img 65695 > flag
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ openssl zlib -d < flag
blob 31picoCTF{g17_r3m3mb3r5_d4ddf904}    
```
## Run 
.flag picoCTF{g17_r3m3mb3r5_d4ddf904} 

