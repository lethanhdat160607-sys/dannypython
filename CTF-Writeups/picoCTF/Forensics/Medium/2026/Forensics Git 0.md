






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
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 172
r/r 4944:       .ash_history
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 172
r/r 4944:       .ash_history
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat -o 1140736 disk.img 4944
apk add git
poweroff
                                                                                                                                                           
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
r/r 65662:      index
r/r 65693:      COMMIT_EDITMSG
d/d 65703:      logs
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls -o 1140736 disk.img 65703
r/r 65704:      HEAD
d/d 65705:      refs
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat -o 1140736 disk.img 65704
0000000000000000000000000000000000000000 327681bb38cf467cec328eec9707b240e3e74ced ctf-player <ctf-player@example.com> 1763542167 +0000  commit (initial): Wrap this phrase in the flag format: g17_1n_7h3_d15k_041217d8

```
