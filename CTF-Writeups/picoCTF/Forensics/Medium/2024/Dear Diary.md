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
-/- * 0:        ^
-/- * 0:         
d/d 11: lost+found
d/d 32385:      boot
d/d 64769:      etc
d/d 64770:      runlevels
d/d 64775:      apk
r/r 64785:      inittab
d/d 64786:      network
d/d 64788:      conf.d
d/d 64790:      keymap
r/r 64792:      resolv.conf
d/d 64793:      zoneinfo
r/r 64795:      hosts
r/r 64796:      passwd-
r/r 64797:      passwd
r/r 64798:      shadow-
r/r 64799:      shadow
r/r 64800:      group-
r/r 64801:      group
d/d 64802:      ssh
r/r 64783:      fstab
l/l 64833:      localtime
r/r 64810:      fstab.old
d/d 64815:      mkinitfs
r/r 64837:      update-extlinux.conf
d/d 64771:      sysinit
d/d 64772:      boot
d/d 64773:      shutdown
d/d 64774:      default
l/l 64811:      devfs
l/l 64812:      dmesg
l/l 64813:      mdev
l/l 64814:      hwdrivers
l/l 64816:      modules
l/l 64817:      sysctl
l/l 64818:      hostname
l/l 64819:      bootmisc
l/l 64820:      syslog
l/l 64821:      hwclock
l/l 64822:      loadkmap
l/l 64823:      networking
l/l 64824:      seedrng
l/l 64825:      swap
l/l 64826:      mount-ro
l/l 64827:      killprocs
l/l 64828:      savecache
l/l 64829:      crond
l/l 64830:      acpid
l/l 64831:      chronyd
l/l 64832:      sshd
d/d 64776:      keys
r/r 64782:      arch
r/r 64834:      repositories
r/r 64784:      world
r/r 64777:      alpine-devel@lists.alpinelinux.org-4a6a0840.rsa.pub
r/r 64778:      alpine-devel@lists.alpinelinux.org-5243ef4b.rsa.pub
r/r 64779:      alpine-devel@lists.alpinelinux.org-5261cecb.rsa.pub
r/r 64780:      alpine-devel@lists.alpinelinux.org-6165ee59.rsa.pub
r/r 64781:      alpine-devel@lists.alpinelinux.org-61666e3f.rsa.pub
-/- 25873:
-/- 59426:
r/r 64787:      interfaces
r/r 64789:      loadkmap
r/r 64791:      us.bmap.gz
r/r 64794:      UTC
-/- 43586:
-/- 5065:
r/r 64803:      sshd_config
r/r 64804:      ssh_host_rsa_key.pub
r/r 64805:      ssh_host_rsa_key
r/r 64806:      ssh_host_ecdsa_key.pub
r/r 64807:      ssh_host_ecdsa_key
r/r 64808:      ssh_host_ed25519_key.pub
r/r 64809:      ssh_host_ed25519_key
d/d 64835:      features.d
r/r 64836:      mkinitfs.conf
-/- * 0:
-/- 22025:
d/d 32386:      proc
d/d 13: dev
d/d 32387:      tmp
d/d 14: lib
d/d 32388:      var
d/d 21: usr
d/d 32393:      bin
d/d 32395:      sbin
d/d 32513:      home
d/d 32539:      media
d/d 203:        mnt
d/d 32543:      opt
d/d 204:        root
d/d 32544:      run
d/d 205:        srv
d/d 32545:      sys
-/- 3197:       @
^pys
d/d 15: apk
l/l 20: libc.musl-x86_64.so.1
d/d 34: firmware
d/d 199:        mdev
d/d 200:        modules-load.d
d/d 201:        sysctl.d
d/d 229:        rc
d/d 459:        modules
r/r 19: ld-musl-x86_64.so.1
r/r 228:        librc.so.1
r/r 333:        libalpine.sh
r/r 381:        libcrypto.so.3
r/r 390:        libssl.so.3
r/r 332:        dasd-functions.sh
r/r 227:        libeinfo.so.1
r/r 394:        libz.so.1.3
r/r 429:        libblkid.so.1.1.0
l/l 430:        libcom_err.so.2
r/r 395:        libapk.so.2.14.0
l/l 432:        libe2p.so.2
l/l 393:        libz.so.1
r/r 431:        libcom_err.so.2.1
r/r 433:        libe2p.so.2.3
l/l 428:        libblkid.so.1
l/l 434:        libext2fs.so.2
r/r 435:        libext2fs.so.2.4
l/l 436:        libss.so.2
r/r 437:        libss.so.2.0
r/r 439:        libuuid.so.1.3.0
d/d 449:        cryptsetup
l/l 450:        libcryptsetup.so.12
r/r 446:        libdevmapper.so.1.02
l/l 438:        libuuid.so.1
r/r 451:        libcryptsetup.so.12.9.0
r/r 453:        libkmod.so.2.4.1
l/l 452:        libkmod.so.2
d/d 16: db
d/d 33: exec
r/r 17: installed
r/r 18: lock
d/d 32389:      cache
d/d 32396:      lib
d/d 32546:      empty
d/d 32548:      local
d/l 32549:      lock
d/d 32551:      log
d/d 32552:      mail
d/d 32553:      opt
d/d 32555:      spool
d/d 32559:      tmp
l/l 32554:      run
d/d 32390:      apk
d/d 32391:      misc
r/r 32392:      APKINDEX.b2c94760.tar.gz
-/- 43212:
-/r 64867:
r/r 64839:      acct
r/r 64843:      acpid
r/r 64947:      openrc
r/r 64999:      chrony
d/d 22: bin
d/d 25: sbin
d/d 30: share
d/d 206:        lib
d/d 208:        local
d/d 214:        libexec
-/- 36259:
r/r 27: dump-acct
r/r 28: dump-utmp
r/r 29: sa
l/l 37: add-shell
l/l 38: addgroup
l/l 39: adduser
l/l 40: arping
l/l 46: brctl
l/l 51: chpasswd
l/l 52: chroot
l/l 59: crond
l/l 65: delgroup
l/l 66: deluser
l/l 73: ether-wake
l/l 78: fbset
r/r 26: accton
l/l 94: killall5
l/l 97: loadfont
l/l 109:        nanddump
l/l 110:        nandwrite
l/l 111:        nbd-client
l/l 119:        ntpd
l/l 122:        partprobe
l/l 132:        rdate
l/l 133:        rdev
l/l 134:        readahead
l/l 137:        remove-shell
l/l 141:        rfkill
l/l 142:        sendmail
l/l 144:        setfont
l/l 146:        setlogcons
r/r 427:        chronyd
r/r 1645:       sshd
r/r 64842:      hostname
l/l 64846:      mtab
r/r 64853:      shells
r/r 64854:      sysctl.conf
d/d 64865:      init.d
d/d 64866:      modprobe.d
r/r 64952:      mdev.conf
d/d 64954:      lbu
r/r 64957:      issue
d/d 64961:      ssl
d/d 64874:      periodic
d/d 64884:      sysctl.d
r/r 64958:      os-release
d/d 64965:      ssl1.1
d/d 64978:      acpi
d/d 65116:      update-extlinux.d
r/r 65002:      e2scrub.conf
r/r 64845:      modules
r/r 64847:      nsswitch.conf
r/r 64849:      profile
d/d 64838:      logrotate.d
r/r 64850:      protocols
r/r 64851:      services
d/d 64840:      busybox-paths.d
r/r 64862:      udhcpd.conf
d/d 64863:      crontabs
d/d 64871:      modules-load.d
d/d 64860:      udhcpc
r/r 64859:      securetty
d/d 64873:      opt
r/r 64872:      motd
d/d 64880:      profile.d
d/d 64945:      local.d
d/d 64983:      pkcs11
d/d 64997:      chrony
r/r 65003:      mke2fs.conf
r/r 64948:      rc.conf
d/d 65058:      terminfo
d/d 64959:      secfixes.d
r/r 64956:      alpine-release
-/- 13045:      @
r/r 64841:      busybox
d/d 64844:      if-down.d
d/d 64848:      if-post-down.d
d/d 64852:      if-post-up.d
d/d 64855:      if-pre-down.d
d/d 64856:      if-pre-up.d
d/d 64857:      if-up.d
r/r 64885:      ifupdown-ng.conf.example
r/r 64858:      dad
r/r 64861:      udhcpc.conf
-/- 42637:      @
-/- 30391:      @
d/d 31: udhcpc
d/d 212:        man
d/d 213:        misc
d/d 303:        openrc
d/d 334:        apk
d/d 454:        mkinitfs
d/d 1626:       kernel
d/d 1693:       syslinux
r/r 32: default.script
d/d 32397:      udhcpd
d/d 32547:      misc
d/d 32606:      apk
d/d 32609:      chrony
r/r 1834:       kmod-31-r2.trigger
-/- 39304:      @
pyse
-/- 41069:      @
-/- 24019:      @
-/- 36760:
pyse
-/- 41629:
pyse
-/- 35485:
-/- 51925:
-/- 31203:
pyse
-/- 25271:
pyse
-/- 51391:
pyse
-/- 22249:
-/- 59858:
-/- 39687:      x
-/- 50831:
pyse
-/r 64986:
pyse
l/l 41: awk
l/l 48: bzcat
l/l 49: bzip2
l/l 60: crontab
l/l 61: cryptpw
l/l 64: deallocvt
l/l 72: env
l/l 82: free
l/l 83: fuser
l/l 86: head
l/l 87: hexdump
l/l 89: id
l/l 93: killall
l/l 98: logger
l/l 107:        mkfifo
l/l 117:        nsenter
l/l 120:        od
l/l 130:        pstree
l/l 138:        renice
l/l 145:        setkeycodes
l/l 147:        setsid
l/l 148:        sha1sum
l/l 149:        sha256sum
l/l 158:        sum
l/l 170:        truncate
l/l 180:        unshare
l/l 187:        vlock
l/l 195:        xargs
r/r 400:        ldd
r/r 415:        p11-kit
l/l 1657:       mdel
l/l 1660:       mdu
l/l 1662:       minfo
l/l 1665:       mmd
l/l 1666:       mmount
l/l 1667:       mmove
l/l 1669:       mrd
l/l 1670:       mren
l/l 1671:       mshortname
r/r 1679:       uz
l/l 1652:       mcat
l/l 1653:       mcd
r/r 1655:       mcomp
l/l 76: factor
l/l 116:        nproc
l/l 91: ipcrm
l/l 67: diff
l/l 70: du
l/l 103:        lzopcat
l/l 75: expr
l/l 50: cal
l/l 54: cksum
l/l 125:        pgrep
l/l 131:        pwdx
l/l 135:        readlink
l/l 150:        sha3sum
l/l 151:        sha512sum
l/l 156:        split
l/l 163:        time
l/l 165:        top
l/l 171:        tty
l/l 179:        unlzop
l/l 193:        whoami
l/l 194:        whois
r/r 392:        ssl_client
r/r 426:        chronyc
r/r 1647:       openssl
r/r 397:        getconf
l/l 1649:       lz
l/l 1659:       mdir
r/r 1663:       mkmanifest
r/r 1685:       md5pass
r/r 1639:       ssh-copy-id
r/r 1689:       pxelinux-options
-/- 46105:
pyse
-/- 28006:
pyse
-/- 18926:
l/l 32403:      base64
l/l 32407:      cat
l/l 32408:      chattr
l/l 32411:      chown
l/l 32413:      date
l/l 32414:      dd
l/l 32418:      dnsdomainname
l/l 32422:      false
l/l 32423:      fatattr
l/l 32431:      fsync
l/l 32436:      gzip
l/l 32438:      hostname
l/l 32447:      ionice
l/l 32458:      kill
l/l 32460:      link
l/l 32461:      linux32
l/l 32463:      ln
l/l 32468:      ls
l/l 32469:      lsattr
l/l 32474:      mkdir
l/l 32479:      mktemp
l/l 32484:      mountpoint
l/l 32485:      mpstat
l/l 32488:      netstat
l/l 32492:      ping
l/l 32493:      ping6
l/l 32497:      printenv
l/l 32499:      pwd
l/l 32503:      rev
l/l 32504:      rm
l/l 32508:      run-parts
l/l 32538:      sh
l/l 32515:      sleep
l/l 32516:      stat
l/l 32522:      sync
l/l 32525:      tar
l/l 32526:      touch
l/l 32506:      umount
l/l 32531:      uname
l/l 32532:      usleep
l/l 32534:      watch
r/r 32441:      rc-status
r/r 32574:      uniso
r/r 32607:      bbsuid
l/l 32427:      fgrep
l/l 32434:      grep
l/l 32416:      df
l/l 32419:      dumpkmap
l/l 32471:      lzop
l/l 32483:      mount
l/l 32505:      rmdir
l/l 32448:      iostat
l/l 32486:      mv
l/l 32477:      mknod
l/l 32410:      chmod
r/r 32394:      busybox
l/l 32489:      nice
l/l 32402:      ash
l/l 32400:      arch
l/l 32457:      kbd_mode
l/l 32421:      egrep
l/l 32409:      chgrp
l/l 32491:      pidof
l/l 32502:      reformime
l/l 32451:      ipcalc
l/l 32412:      cp
l/l 32404:      bbconfig
l/l 32465:      login
l/l 32462:      linux64
l/l 32472:      makemime
l/l 32498:      ps
l/l 32482:      more
l/l 32435:      gunzip
l/l 32494:      pipe_progress
l/l 32432:      getopt
l/l 32420:      echo
l/l 32417:      dmesg
l/l 32425:      fdflush
l/l 32509:      sed
l/l 32511:      setpriv
l/l 32512:      setserial
l/l 32517:      stty
l/l 32518:      su
l/l 32527:      true
l/l 32536:      zcat
r/r 32620:      kmod
l/l 32621:      lsmod
l/l 32622:      modinfo
-/- 60308:
pyse
-/- 35733:
pyse
-/- 16821:
-/- 37615:
-/- 49766:
-/- 41478:
-/- 41956:
-/- 60639:
-/- 19286:
l/l 47: bunzip2
l/l 172:        ttysize
l/l 45: blkdiscard
l/l 124:        paste
l/l 101:        lzcat
l/l 177:        unlink
l/l 102:        lzma
l/l 56: cmp
l/l 129:        pscan
l/l 95: last
l/l 126:        pkill
l/l 178:        unlzma
l/l 112:        nc
l/l 118:        nslookup
l/l 140:        resize
l/l 44: beep
l/l 168:        traceroute6
l/l 159:        tac
l/l 143:        seq
l/l 80: flock
l/l 106:        microcom
l/l 174:        unexpand
r/r 24: lastcomm
l/l 81: fold
r/r 23: ac
l/l 104:        md5sum
l/l 136:        realpath
l/l 108:        mkpasswd
l/l 92: ipcs
l/l 127:        pmap
l/l 68: dirname
l/l 71: eject
l/l 62: cut
l/l 74: expand
l/l 184:        uudecode
l/l 190:        wget
l/l 192:        who
l/l 197:        xzcat
r/r 399:        iconv
r/r 423:        scmp_sys_resolver
r/r 1636:       sftp
r/r 1637:       ssh-add
l/l 1656:       mcopy
l/l 1668:       mpartition
r/r 1673:       mtools
r/r 1683:       keytab-lilo
r/r 1687:       mkdiskimage
r/r 1691:       syslinux
r/r 1692:       syslinux2ansi
r/r 1648:       amuFormat.sh
r/r 1634:       findssl.sh
-/- 26404:
-/- 50519:
r/r 64864:      root
r/r 64868:      blacklist.conf
r/r 64869:      i386.conf
r/r 64870:      kms.conf
r/r 64867:      aliases.conf
d/d 64875:      15min
d/d 64876:      daily
d/d 64877:      hourly
d/d 64878:      monthly
d/d 64879:      weekly
r/r 64882:      README
r/r 64883:      color_prompt.sh.disabled
r/r 64881:      20locale.sh
r/r 64950:      README
r/r 329:        persistent-storage
r/r 330:        ptpdev
r/r 331:        usbdev
r/r 328:        dvbdev
-/- 18940:
r/r 202:        00-alpine.conf
d/d 32540:      cdrom
d/d 32541:      floppy
d/d 32542:      usb
-/- 59052:
pyse
-/- 20853:
d/d 209:        bin
d/d 210:        lib
d/d 211:        share
d/r 32550:      subsys
d/d 32611:      chrony
-/- 20065:
d/d 32556:      cron
l/l 32558:      mail
l/l 32557:      crontabs
r/- 36649:      ^|
-/- 65124:
l/l 32428:      findfs
l/l 32429:      fsck
l/l 32433:      getty
l/l 32440:      ifconfig
l/l 32561:      ifdown
l/l 32466:      logread
l/l 32627:      modprobe
l/l 32487:      nameif
l/l 32510:      setconsole
l/l 32519:      swapoff
l/l 32520:      swapon
r/r 32572:      start-stop-daemon
r/r 32573:      supervise-daemon
r/r 32443:      mkmntdirs
r/r 32568:      rc-service
r/r 32569:      rc-sstat
r/r 32588:      setup-devd
r/r 32591:      setup-hostname
r/r 32592:      setup-interfaces
r/r 32602:      setup-xorg-base
r/r 32603:      update-conf
l/l 32614:      fsck.ext3
l/l 32615:      fsck.ext4
r/r 32415:      bootchartd
r/r 32470:      nlplug-findfs
r/r 32612:      e2fsck
r/r 32584:      setup-apkcache
r/r * 32585(realloc):   .apk.22e10c7569400e4c8c1e0aeb74cf3e44f4a9d2c1d26d5da2
r/r * 32586(realloc):   .apk.f2c325f8a18152aa16ddc3c218186ded5b89276a1f5d574c
r/r * 32588(realloc):   .apk.9d2af270a1d3bfe493bdb8a868066c6ecd346d900d284fe5
l/l 32455:      iprule
l/l 32507:      route
l/l 32452:      iplink
l/l 32426:      fdisk
l/l 32626:      modinfo
l/l 32501:      reboot
l/l 32401:      arp
l/l 32521:      switch_root
l/l 32437:      halt
l/l 32500:      raidautorun
l/l 32473:      mdev
l/l 32628:      rmmod
l/l 32399:      adjtimex
l/l 32478:      mkswap
l/l 32442:      ifenslave
r/r 32566:      openrc
r/r 32570:      rc-update
l/l 32571:      service
l/l 32581:      lbu_update
r/r 32585:      setup-apkrepos
r/r 32587:      setup-desktop
r/r 32589:      setup-disk
r/r 32593:      setup-keymap
r/r 32597:      setup-proxy
r/r 32604:      update-kernel
r/r 32605:      apk
l/l 32617:      mkfs.ext2
r/r 32481:      update-extlinux
r/r 32575:      copy-modloop
-/- 33261:      y
d/d 215:        ifupdown-ng
d/d 418:        p11-kit
r/r 217:        bridge
r/r 218:        dhcp
r/r 219:        forward
r/r 220:        ipv6-ra
r/r 221:        link
r/r 222:        static
r/r 216:        bond
-/- 13794:      ^|
pyse^|
-/- 42130:
r/r 64886:      networking
r/r 64892:      fsck
r/r 64893:      hwclock
r/r 64894:      killprocs
r/r 64895:      localmount
r/r 64896:      modloop
r/r 64897:      modules
r/r 64898:      mtab
r/r 64899:      net-online
r/r 64900:      netmount
r/r 64901:      seedrng
r/r 64902:      staticroute
r/r 64903:      swap
r/r 64904:      swclock
r/r 64984:      ntpd
r/r 64986:      syslog
r/r 64987:      watchdog
r/r 65112:      sshd
r/r 65000:      chronyd
r/r 64981:      crond
r/r 64985:      rdate
r/r 64982:      klogd
r/r 64890:      devfs
r/r 64891:      dmesg
r/r 64889:      consolefont
r/r 64888:      bootmisc
-/- 18809:
-/- 6249:
r/r 64912:      fsck
l/l 64913:      functions.sh
r/r 64914:      hostname
r/r 64920:      loopback
r/r 64921:      machine-id
r/r 64924:      mount-ro
r/r 64925:      mtab
r/r 64927:      netmount
r/r 64928:      numlock
r/r 64929:      osclock
r/r 64930:      procfs
r/r 64932:      runsvdir
r/r 64933:      s6-svscan
r/r 64936:      savecache
r/r 64944:      termencoding
r/r 64991:      loadkmap
r/r 65001:      chronyd
r/r 64905:      binfmt
r/r * 64927(realloc):   .apk.c8402845a4342b34424710347fb0dc850b66d1427dac6a2a
r/r 64887:      networking
r/r 64915:      hwclock
r/r 64916:      hwdrivers
r/r 64917:      killprocs
r/r 64906:      bootmisc
r/r 64909:      devfs
r/r 64923:      modules
r/r 64926:      net-online
r/r 64937:      seedrng
r/r 64939:      swap
r/r 64940:      swclock
r/r 64951:      acct
-/- 9130:
r/r 64935:      save-termencoding
r/r 64938:      staticroute
r/r 64942:      sysfs
r/r 64918:      local
r/r 64919:      localmount
r/r 64922:      modloop
r/r 64943:      sysfsconf
r/r 64953:      mdev
r/r 64992:      ntpd
r/r 64994:      syslog
r/r 64995:      watchdog
r/r 65004:      kmod-static-nodes
r/r 65114:      sshd
r/r 64989:      crond
r/r 64907:      cgroups
r/r 64911:      firstboot
r/r 64941:      sysctl
r/r 64988:      acpid
r/r 64990:      klogd
r/r 64993:      rdate
r/r 64931:      root
r/r 64934:      save-keymaps
r/r 64908:      consolefont
r/r 64910:      dmesg
-/- 33053:
r/r 64946:      README
-/- 12254:      4
d/d 64949:      nonetwork
d/d 230:        bin
d/d 274:        sbin
d/d 287:        sh
r/r 302:        version
-/- 60518:
-/- 31055:
r/r 238:        einfon
r/r 250:        kill_all
r/r 251:        mountinfo
r/r 266:        shell_var
r/r 237:        einfo
r/r 242:        ewaitfile
r/r 244:        ewarnn
r/r 248:        is_newer_than
r/r 249:        is_older_than
r/r 254:        save_options
r/r 257:        service_hotplugged
r/r 262:        service_starting
r/r 267:        vebegin
r/r 233:        eend
r/r 235:        eerrorn
r/r 263:        service_stopped
r/r 268:        veend
r/r 270:        veinfo
r/r 273:        vewend
r/r 231:        checkpath
r/r * 254(realloc):     .apk.3e0decf8081092dad8c737429f16ca494aff0acefe285e83
-/- 9580:
-/- 2096:
r/r 239:        eoutdent
r/r 243:        ewarn
r/r 245:        ewend
r/r 258:        service_inactive
r/r 264:        service_stopping
r/r 265:        service_wasinactive
r/r 252:        on_ac_power
r/r 255:        service_crashed
r/r 269:        veindent
r/r 271:        veoutdent
r/r 272:        vewarn
r/r 247:        get_options
r/r 236:        eindent
r/r 234:        eerror
-/- 43722:
r/r 246:        fstabinfo
r/r 253:        rc-depend
r/r 256:        service_get_value
r/r 259:        service_set_value
r/r 260:        service_started
r/r 261:        service_started_daemon
r/r 240:        esyslog
r/r 241:        eval_ecolors
r/r 232:        ebegin
-/- 56835:
-/- 39226:
r/r 276:        mark_service_failed
r/r 277:        mark_service_hotplugged
r/r 278:        mark_service_inactive
r/r 279:        mark_service_started
r/r 280:        mark_service_starting
r/r 281:        mark_service_stopped
r/r 282:        mark_service_stopping
r/r 283:        mark_service_wasinactive
r/r 284:        rc-abort
r/r 285:        seedrng
r/r 286:        swclock
r/r 275:        mark_service_crashed
r/r 289:        cgroup-release-agent.sh
r/r 290:        functions.sh
r/r 291:        gendepends.sh
r/r 292:        init-early.sh
r/r 293:        init.sh
r/r 294:        openrc-run.sh
r/r 295:        rc-cgroup.sh
r/r 296:        rc-functions.sh
r/r 297:        rc-mount.sh
r/r 298:        runit.sh
r/r 299:        s6.sh
r/r 300:        start-stop-daemon.sh
r/r 301:        supervise-daemon.sh
r/r 288:        binfmt.sh
-/- 32267:      L
-/- 33630:      L
-/- 33337:
d/d 304:        support
d/d 305:        deptree2dot
d/d 307:        init.d.examples
d/d 320:        openvpn
d/d 324:        sysvinit
r/r 306:        README.md
r/r 309:        avahi-dnsconfd
r/r 310:        avahid
r/r 311:        dbus
r/r 312:        dhcpcd
r/r 313:        hald
r/r 314:        named
r/r 315:        ntpd
r/r 316:        openvpn
r/r 317:        polkitd
r/r 318:        sshd
r/r 319:        wpa_supplicant
r/r 308:        README.md
-/- 12715:      L
-/- 43743:      L
r/r 322:        down.sh
r/r 323:        up.sh
r/r 321:        README.md
r/r 326:        halt.sh
r/r 327:        inittab
r/r 325:        README.md
-/- 33657:
r/r 64955:      lbu.conf
-/- 62035:
l/l 32454:      iproute
r/r 32583:      setup-alpine
r/r 32590:      setup-dns
r/r 32595:      setup-mta
l/l 32439:      hwclock
l/l 32453:      ipneigh
l/l 32533:      vconfig
l/l 32563:      ifquery
l/l 32449:      ip
l/l 32406:      blockdev
l/l 32398:      acpid
l/l 32495:      pivot_root
l/l 32523:      sysctl
l/l 32476:      mkfs.vfat
r/r 32601:      setup-xen-dom0
r/r 32608:      ldconfig
l/l 32618:      mkfs.ext3
l/l 32619:      mkfs.ext4
l/l 32577:      lbu_commit
l/l 32580:      lbu_status
r/r * 32584(realloc):   .apk.740ceaab5bd243aa1a7974670987bdb75577641b8b6385d1
r/r * 32593(realloc):   .apk.e2b2478f58e0020ac86359dc0e616fb7f23c052584e9e921
r/r * 32594(realloc):   .apk.b55f52d6d50c4d3b3308783c421b4f836b24585f35b4c8bc
r/r * 32599(realloc):   .apk.e51089dea093c807957c0cad87a2e4eebec7381596cfc8bf
-/- 22350:
l/l 32578:      lbu_exclude
l/l 32579:      lbu_include
r/r 32598:      setup-sshd
l/l 32450:      ipaddr
l/l 32430:      fstrim
l/l 32496:      poweroff
r/r 32599:      setup-timezone
r/r 32600:      setup-user
l/l 32613:      fsck.ext2
l/l 32537:      zcip
l/l 32464:      loadkmap
l/l 32490:      nologin
l/l 32456:      iptunnel
l/l 32529:      udhcpc
l/l 32444:      init
l/l 32424:      fbsplash
l/l 32564:      ifup
l/l 32528:      tunctl
r/r 32446:      mkinitfs
r/r 32405:      extlinux
l/l 32475:      mkdosfs
l/l 32535:      watchdog
r/r 32565:      ifupdown
l/l 32623:      depmod
l/l 32445:      inotifyd
r/r 32576:      lbu
-/- 46389:
r/r 32594:      setup-lbu
r/r 32596:      setup-ntp
r/r 32616:      mke2fs
r/r 32480:      blkid
r/r 32567:      openrc-run
l/l 32514:      slattach
l/l 32467:      losetup
r/r 32586:      setup-bootable
l/l 32560:      ifctrstat
l/l 32562:      ifparse
l/l 32624:      insmod
l/l 32459:      klogd
l/l 32625:      lsmod
l/l 32524:      syslogd
r/r 32582:      setup-acf
d/d 335:        keys
l/l 338:        alpine-devel@lists.alpinelinux.org-616ae350.rsa.pub
l/l 337:        alpine-devel@lists.alpinelinux.org-58199dcc.rsa.pub
-/r 32599:
pyse
-/- 60498:
-/- 58413:
r/r 341:        alpine-devel@lists.alpinelinux.org-524d27bb.rsa.pub
r/r 351:        alpine-devel@lists.alpinelinux.org-616abc23.rsa.pub
r/r 352:        alpine-devel@lists.alpinelinux.org-616ac3bc.rsa.pub
r/r 353:        alpine-devel@lists.alpinelinux.org-616adfeb.rsa.pub
d/d 356:        armhf
d/d 364:        ppc64le
d/d 377:        x86_64
r/r 339:        alpine-devel@lists.alpinelinux.org-4a6a0840.rsa.pub
r/r 343:        alpine-devel@lists.alpinelinux.org-58199dcc.rsa.pub
r/r * 353(realloc):     .apk.34eeb8b41e72fa60dbea44d6e811f61bf0650c00802d656a
r/r 344:        alpine-devel@lists.alpinelinux.org-58cbb476.rsa.pub
d/d 336:        aarch64
r/r 354:        alpine-devel@lists.alpinelinux.org-616ae350.rsa.pub
r/r 350:        alpine-devel@lists.alpinelinux.org-616a9724.rsa.pub
r/r 348:        alpine-devel@lists.alpinelinux.org-6165ee59.rsa.pub
r/r 340:        alpine-devel@lists.alpinelinux.org-5243ef4b.rsa.pub
r/r 342:        alpine-devel@lists.alpinelinux.org-5261cecb.rsa.pub
r/r 355:        alpine-devel@lists.alpinelinux.org-616db30d.rsa.pub
d/d 359:        armv7
d/d 362:        mips64
d/d 367:        riscv64
d/d 370:        s390x
d/d 373:        x86
r/r 345:        alpine-devel@lists.alpinelinux.org-58e4f17d.rsa.pub
r/r 346:        alpine-devel@lists.alpinelinux.org-5e69ca50.rsa.pub
r/r 347:        alpine-devel@lists.alpinelinux.org-60ac2099.rsa.pub
r/r 349:        alpine-devel@lists.alpinelinux.org-61666e3f.rsa.pub
l/l 358:        alpine-devel@lists.alpinelinux.org-616a9724.rsa.pub
l/l 357:        alpine-devel@lists.alpinelinux.org-524d27bb.rsa.pub
-/- 39726:
l/l 361:        alpine-devel@lists.alpinelinux.org-616adfeb.rsa.pub
l/l 360:        alpine-devel@lists.alpinelinux.org-524d27bb.rsa.pub
-/- 7605:
pyse
l/l 363:        alpine-devel@lists.alpinelinux.org-5e69ca50.rsa.pub
l/l 366:        alpine-devel@lists.alpinelinux.org-616abc23.rsa.pub
l/l 365:        alpine-devel@lists.alpinelinux.org-58cbb476.rsa.pub
-/- 25969:
l/l 369:        alpine-devel@lists.alpinelinux.org-616db30d.rsa.pub
l/l 368:        alpine-devel@lists.alpinelinux.org-60ac2099.rsa.pub
l/l 372:        alpine-devel@lists.alpinelinux.org-616ac3bc.rsa.pub
l/l 371:        alpine-devel@lists.alpinelinux.org-58e4f17d.rsa.pub
l/l 375:        alpine-devel@lists.alpinelinux.org-5243ef4b.rsa.pub
l/l 376:        alpine-devel@lists.alpinelinux.org-61666e3f.rsa.pub
l/l 374:        alpine-devel@lists.alpinelinux.org-4a6a0840.rsa.pub
l/l 379:        alpine-devel@lists.alpinelinux.org-5261cecb.rsa.pub
l/l 380:        alpine-devel@lists.alpinelinux.org-6165ee59.rsa.pub
l/l 378:        alpine-devel@lists.alpinelinux.org-4a6a0840.rsa.pub
r/r 64960:      alpine
r/r 64969:      ct_log_list.cnf.dist
r/r 64974:      openssl.cnf
d/d 64963:      certs
l/l 64962:      cert.pem
r/r 64975:      openssl.cnf.dist
d/d 64970:      misc
d/d 64976:      private
r/r 64968:      ct_log_list.cnf
r/r 64964:      ca-certificates.crt
l/l 64967:      certs
l/l 64966:      cert.pem
-/- 36487:
pyse
l/l 64972:      tsget
r/r 64973:      tsget.pl
r/r 64971:      CA.pl
-/r 906:
r/r 384:        capi.so
r/r 385:        loader_attic.so
r/r 386:        padlock.so
r/r 383:        afalg.so
-/- 8348:
v^qyse
r/r 389:        legacy.so
-/- 63411:      ^/
d/d 64977:      protected_paths.d
d/d 64979:      PWRF
r/r 64980:      00000080
l/l 90: install
l/l 57: comm
r/r 1643:       ssh
l/l 99: lsof
l/l 77: fallocate
l/l 114:        nmeter
l/l 79: find
l/l 173:        udhcpc6
l/l 43: bc
l/l 100:        lsusb
l/l 113:        nl
l/l 153:        shred
l/l 161:        tee
l/l 186:        vi
l/l 96: less
l/l 154:        shuf
l/l 1658:       mdeltree
r/r 1678:       tgz
r/r 1681:       isohybrid
r/r 1684:       lss16toppm
l/l 1651:       mbadblocks
r/r * 1654(realloc):    .apk.ca0a547b234bf83532fee1936ce852e0eb166e49c0f4a3db
l/l * 1658(realloc):    .apk.bbbd92866999075b22cd01cf313b4a40f03ebb7c6846ff84
l/l * 1666(realloc):    .apk.b2a6b7e95a9aca87356fea56ef2c025999059e4f62e6be19
r/r * 1678(realloc):    .apk.556e7470e27dba6f16a91ee8c3cc173e977419dc7e4b90dd
-/- 8990:
c/- 57430:
-/- 40445:
r/r 64996:      pkcs11.conf.example
r/r 420:        trust-extract-compat
r/r 419:        p11-kit-remote
s/- 39628:      T^
r/r 64998:      chrony.conf
-/- 33663:      (
r/r 32610:      chrony.drift
-/- 62541:
eN^qyse
-/- 25354:      (
-/- 20982:      (
-/- 15674:      (
^qyse(
-/- 44405:
-/- 51630:
r/r 224:        libcap.so.2.69
l/l 225:        libpsx.so.2
r/r 226:        libpsx.so.2.69
d/d 388:        ossl-modules
l/l 387:        libcrypto.so.3
l/l 391:        libssl.so.3
l/l 409:        libidn2.so.0
l/l 405:        libnettle.so.8
r/r 410:        libidn2.so.0.3.8
l/l 413:        libtasn1.so.6
r/r 422:        libgnutls.so.30.36.0
l/l 440:        liblzma.so.5
l/l 424:        libseccomp.so.2
l/l 421:        libgnutls.so.30
r/r 441:        liblzma.so.5.4.5
r/r 443:        libzstd.so.1.5.5
r/r 448:        libjson-c.so.5.3.0
l/l 1630:       libncursesw.so.6
d/d 1642:       ssh
r/r 445:        libargon2.so.1
r/r 1633:       libedit.so.0.0.72
l/l 447:        libjson-c.so.5
r/r 1631:       libncursesw.so.6.4
l/l 1632:       libedit.so.0
l/l * 447(realloc):     .apk.a0eff43c8d8f18875eb80b954f29ced96e6bf7b71a5fc16b
l/l 411:        libffi.so.8
r/r 408:        libunistring.so.5.0.0
l/l 403:        libhogweed.so.6
l/l 442:        libzstd.so.1
r/r 425:        libseccomp.so.2.5.5
d/d 382:        engines-3
l/l 407:        libunistring.so.5
r/r 412:        libffi.so.8.1.2
d/d 207:        modules-load.d
l/l 416:        libp11-kit.so.0
l/l 223:        libcap.so.2
r/r 404:        libhogweed.so.6.8
l/l 401:        libgmp.so.10
r/r 417:        libp11-kit.so.0.3.1
r/r 406:        libnettle.so.8.8
r/r 402:        libgmp.so.10.5.0
r/r 414:        libtasn1.so.6.6.3
-/- 20483:
-/- 8064:
-/- 34191:
c/- 41235:
r/r 65015:      cryptsetup.files
r/r 65016:      cryptsetup.modules
r/r 65020:      ena.modules
r/r 65024:      f2fs.modules
r/r 65025:      floppy.modules
r/r 65029:      keymap.files
r/r 65030:      kms.modules
r/r 65032:      lvm.modules
r/r 65033:      mmc.modules
r/r 65035:      nbd.modules
r/r 65037:      network.modules
r/r 65040:      ocfs2.modules
r/r 65049:      virtio.modules
r/r 65052:      xenpci.modules
r/r 65053:      xfs.files
r/r 65057:      zfs.modules
r/r 65008:      base.modules
r/r 65034:      nbd.files
r/r 65044:      reiserfs.modules
r/r 65047:      ubifs.modules
-/- 12012:
r/r 65039:      nvme.modules
r/r 65042:      raid.files
r/r 65046:      squashfs.modules
r/r 65022:      ext3.modules
r/r 65050:      wireguard.files
r/r 65056:      zfs.files
r/r 65005:      aoe.modules
r/r 65007:      base.files
-/- 16140:
r/r 65010:      btrfs.files
r/r 65012:      cdrom.modules
r/r 65026:      gfs2.modules
r/r 65043:      raid.modules
r/r 65048:      usb.modules
r/r 65038:      nfit.modules
r/r 65013:      cramfs.modules
-/- 10904:
r/r 65045:      scsi.modules
r/r 65051:      wireguard.modules
r/r 65036:      network.files
r/r 65041:      qeth.modules
r/r 65054:      xfs.modules
r/r 65055:      zfcp.modules
r/r 65014:      cryptkey.files
r/r 65017:      dasd_mod.modules
r/r 65028:      jfs.modules
r/r 65031:      lvm.files
r/r 65027:      https.files
r/r 65006:      ata.modules
r/r 65009:      bootchart.files
r/r 65011:      btrfs.modules
r/r 65018:      dhcp.files
r/r 65019:      dhcp.modules
r/r 65021:      ext2.modules
r/r 65023:      ext4.modules
-/- 29274:      X
r/r 456:        group
r/r 457:        initramfs-init
r/r 458:        passwd
r/r 455:        fstab
d/d 460:        6.6.5-0-virt
d/d 461:        kernel
r/r 1620:       modules.alias
r/r 1613:       modules.alias.bin
r/r 1615:       modules.builtin
r/r 1616:       modules.builtin.alias.bin
r/r 1617:       modules.builtin.bin
r/r 1618:       modules.builtin.modinfo
r/r 1835:       modules.dep
r/r 1619:       modules.dep.bin
r/r 1621:       modules.devname
r/r 1622:       modules.order
r/r 1614:       modules.softdep
r/r 1623:       modules.symbols
r/r 1625:       modules.symbols.bin
r/r 1624:       modules.symbols.bin.4637.741698.1702066548
r/r 462:        kernel-suffix
-/- 57718:
-/- 28553:
^^\4Z
ryse0L
d/d 463:        arch
d/d 501:        block
d/d 503:        crypto
d/d 582:        drivers
d/d 958:        fs
d/d 1129:       kernel
d/d 1131:       lib
d/d 1162:       net
d/d 1589:       security
d/d 1593:       sound
d/d 1610:       virt
d/d 464:        x86
d/d 465:        crypto
d/d 492:        kernel
d/d 495:        kvm
d/d 499:        video
-/- 63818:
-/- 31885:
-/- 9920:
r/r 474:        chacha-x86_64.ko.gz
r/r 476:        crc32c-intel.ko.gz
r/r 481:        serpent-avx-x86_64.ko.gz
r/r 485:        sha256-ssse3.ko.gz
r/r 487:        sm4-aesni-avx-x86_64.ko.gz
r/r 488:        sm4-aesni-avx2-x86_64.ko.gz
r/r 489:        twofish-avx-x86_64.ko.gz
r/r 490:        twofish-x86_64-3way.ko.gz
r/r 466:        aegis128-aesni.ko.gz
r/r 469:        camellia-aesni-avx-x86_64.ko.gz
r/r 470:        camellia-aesni-avx2.ko.gz
r/r * 483(realloc):     .apk.f98c1dfa258b6875f5a25c34bb835fb9e96ba39816232d76
r/r * 484(realloc):     .apk.b7d80d97f4f0947e72a870e87aafc8ee04d12d7e73c0296b
r/r * 485(realloc):     .apk.4fdb1981267ae3d20edc53d01447946a4a0fd4bd6d8385cd
r/r * 487(realloc):     .apk.583c8295a647f0df6ce713d6bd110f30be7808466896aa3a
r/r 472:        cast5-avx-x86_64.ko.gz
r/r 475:        crc32-pclmul.ko.gz
r/r 477:        crct10dif-pclmul.ko.gz
r/r 478:        curve25519-x86_64.ko.gz
r/r 480:        poly1305-x86_64.ko.gz
r/r 483:        serpent-sse2-x86_64.ko.gz
r/r 484:        sha1-ssse3.ko.gz
r/r 486:        sha512-ssse3.ko.gz
r/r 491:        twofish-x86_64.ko.gz
r/r 482:        serpent-avx2.ko.gz
r/r 473:        cast6-avx-x86_64.ko.gz
r/r 471:        camellia-x86_64.ko.gz
r/r 468:        blowfish-x86_64.ko.gz
r/r 479:        ghash-clmulni-intel.ko.gz
r/r 467:        aesni-intel.ko.gz
r/r 494:        msr.ko.gz
r/r 493:        cpuid.ko.gz
r/r 497:        kvm-intel.ko.gz
r/r 498:        kvm.ko.gz
r/r 496:        kvm-amd.ko.gz
-/- 2336:
r/r 500:        fbdev.ko.gz
r/r 502:        t10-pi.ko.gz
-/- 9895:
r/r 514:        async_pq.ko.gz
r/r 515:        async_raid6_recov.ko.gz
r/r 516:        async_tx.ko.gz
r/r 517:        async_xor.ko.gz
r/r 513:        async_memcpy.ko.gz
r/r 525:        cast6_generic.ko.gz
r/r 538:        crypto_simd.ko.gz
r/r 542:        des_generic.ko.gz
r/r 545:        ecdh_generic.ko.gz
r/r 552:        ghash-generic.ko.gz
r/r 555:        keywrap.ko.gz
r/r 560:        michael_mic.ko.gz
r/r 561:        nhpoly1305.ko.gz
r/r 579:        xctr.ko.gz
r/r 519:        authencesn.ko.gz
r/r 522:        blowfish_generic.ko.gz
r/r 526:        cast_common.ko.gz
r/r 528:        cfb.ko.gz
r/r 567:        seqiv.ko.gz
d/d 512:        async_tx
r/r 554:        jitterentropy_rng.ko.gz
r/r 580:        xor.ko.gz
r/r 504:        adiantum.ko.gz
-/- 62015:
r/r 530:        chacha_generic.ko.gz
r/r 533:        crc32c_generic.ko.gz
r/r 536:        crypto_engine.ko.gz
r/r 539:        crypto_user.ko.gz
r/r 543:        drbg.ko.gz
r/r 548:        essiv.ko.gz
r/r 550:        gcm.ko.gz
r/r 571:        sm3.ko.gz
r/r 520:        blake2b_generic.ko.gz
r/r 572:        sm4.ko.gz
r/r 507:        algif_aead.ko.gz
r/r 509:        algif_rng.ko.gz
r/r 511:        ansi_cprng.ko.gz
r/r 518:        authenc.ko.gz
r/r * 556(realloc):     .apk.06398fc83bf1dd7d1eb0a45a4c9843758c76445a63a18078
r/r * 575(realloc):     .apk.f50fa88afc9e64ae22dcda1032fed53bc5adbedd9de8793e
-/- 18219:
r/r 524:        cast5_generic.ko.gz
r/r 527:        ccm.ko.gz
r/r 535:        cryptd.ko.gz
r/r 537:        crypto_null.ko.gz
r/r 544:        ecc.ko.gz
r/r 532:        crc32_generic.ko.gz
r/r 553:        hctr2.ko.gz
r/r 506:        af_alg.ko.gz
r/r 529:        chacha20poly1305.ko.gz
r/r 557:        lz4.ko.gz
r/r 569:        sha3_generic.ko.gz
r/r 575:        twofish_generic.ko.gz
r/r 576:        vmac.ko.gz
r/r 578:        xcbc.ko.gz
r/r 505:        aegis128.ko.gz
-/- 41030:
-/- 26777:
-/- 50884:
-/- 15585:
r/r 547:        echainiv.ko.gz
r/r 551:        geniv.ko.gz
r/r 558:        lz4hc.ko.gz
r/r 563:        pcrypt.ko.gz
r/r 564:        poly1305_generic.ko.gz
r/r 568:        serpent_generic.ko.gz
r/r 581:        xxhash_generic.ko.gz
r/r 531:        cmac.ko.gz
r/r 540:        ctr.ko.gz
r/r 521:        blowfish_common.ko.gz
r/r 541:        curve25519-generic.ko.gz
r/r 565:        polyval-generic.ko.gz
r/r 566:        rmd160.ko.gz
r/r 562:        pcbc.ko.gz
r/r 573:        tcrypt.ko.gz
r/r 508:        algif_hash.ko.gz
r/r 523:        camellia_generic.ko.gz
r/r 559:        md4.ko.gz
-/- 10165:
r/r 546:        ecdsa_generic.ko.gz
r/r 549:        fcrypt.ko.gz
r/r 510:        algif_skcipher.ko.gz
r/r 534:        crc64_rocksoft_generic.ko.gz
r/r 574:        twofish_common.ko.gz
r/r 577:        wp512.ko.gz
r/r 570:        sm2_generic.ko.gz
r/r 556:        lrw.ko.gz
d/d 583:        acpi
d/d 596:        ata
d/d 598:        base
d/d 601:        block
d/d 613:        cdrom
d/d 615:        char
d/d 621:        crypto
d/d 637:        dca
d/d 639:        dma
d/d 644:        firmware
d/d 648:        gpu
d/d 674:        hid
d/d 684:        hv
d/d 688:        hwmon
d/d 691:        i2c
d/d 700:        input
d/d 708:        iommu
d/d 710:        md
d/d 749:        message
d/d 757:        misc
d/d 765:        net
d/d 841:        nvdimm
d/d 844:        nvme
d/d 852:        pci
d/d 857:        ptp
d/d 860:        rpmsg
d/d 864:        rtc
d/d 866:        scsi
d/d 884:        target
d/d 886:        tty
d/d 892:        usb
d/d 913:        vdpa
d/d 919:        vhost
d/d 924:        video
d/d 932:        virt
d/d 940:        virtio
d/d 945:        watchdog
d/d 948:        xen
r/r 585:        acpi_pad.ko.gz
r/r 586:        battery.ko.gz
r/r 587:        button.ko.gz
r/r 588:        fan.ko.gz
r/r 589:        hed.ko.gz
r/r 592:        sbs.ko.gz
r/r 593:        sbshc.ko.gz
r/r 594:        thermal.ko.gz
r/r 595:        tiny-power-button.ko.gz
d/d 590:        nfit
r/r 584:        ac.ko.gz
r/r 591:        nfit.ko.gz
-/- 47325:
r/r 597:        ata_generic.ko.gz
d/d 599:        firmware_loader
r/r 600:        firmware_class.ko.gz
d/d 602:        drbd
r/r 605:        loop.ko.gz
r/r 606:        nbd.ko.gz
r/r 607:        rbd.ko.gz
r/r 608:        virtio_blk.ko.gz
d/d 609:        xen-blkback
d/d 611:        zram
r/r 604:        floppy.ko.gz
r/r 603:        drbd.ko.gz
-/- 15893:
r/r 610:        xen-blkback.ko.gz
r/r 612:        zram.ko.gz
r/r 614:        cdrom.ko.gz
r/r 620:        nvram.ko.gz
d/d 617:        hw_random
r/r 616:        hangcheck-timer.ko.gz
r/r 619:        virtio-rng.ko.gz
r/r 618:        rng-core.ko.gz
d/d 622:        ccp
d/d 625:        intel
r/r 634:        padlock-sha.ko.gz
d/d 635:        virtio
r/r 633:        padlock-aes.ko.gz
r/r 624:        ccp.ko.gz
r/r 623:        ccp-crypto.ko.gz
d/d 626:        qat
d/d 627:        qat_4xxx
d/d 629:        qat_common
d/d 631:        qat_dh895xccvf
r/r 628:        qat_4xxx.ko.gz
r/r 630:        intel_qat.ko.gz
r/r 632:        qat_dh895xccvf.ko.gz
-/- 13421:
r/r 636:        virtio_crypto.ko.gz
-/- 42742:
r/r 638:        dca.ko.gz
d/d 640:        ioat
d/d 642:        qcom
r/r 641:        ioatdma.ko.gz
r/r 643:        hdma.ko.gz
d/d 645:        efi
r/r 647:        qemu_fw_cfg.ko.gz
-/- 53505:
r/r 646:        efi-pstore.ko.gz
d/d 649:        drm
-/- 33745:
r/r 651:        drm_kms_helper.ko.gz
r/r 652:        drm_panel_orientation_quirks.ko.gz
r/r 653:        drm_shmem_helper.ko.gz
r/r 654:        drm_ttm_helper.ko.gz
r/r 655:        drm_vram_helper.ko.gz
d/d 656:        hyperv
d/d 658:        qxl
d/d 660:        tiny
d/d 664:        ttm
d/d 666:        vboxvideo
d/d 668:        virtio
d/d 670:        vmwgfx
d/d 672:        xen
r/r 650:        drm.ko.gz
r/r 657:        hyperv_drm.ko.gz
-/- 44599:
r/r 659:        qxl.ko.gz
r/r 662:        cirrus.ko.gz
r/r 663:        simpledrm.ko.gz
r/r 661:        bochs.ko.gz
-/- 24135:
r/r 665:        ttm.ko.gz
-/- 11263:
r/r 667:        vboxvideo.ko.gz
r/r 669:        virtio-gpu.ko.gz
r/r 671:        vmwgfx.ko.gz
r/r 673:        drm_xen_front.ko.gz
r/r 676:        hid-generic.ko.gz
r/r 677:        hid-hyperv.ko.gz
r/r 678:        hid.ko.gz
r/r 679:        uhid.ko.gz
d/d 680:        usbhid
r/r 675:        hid-cherry.ko.gz
-/- 24099:
-/r 245:
r/r 682:        usbkbd.ko.gz
r/r 683:        usbmouse.ko.gz
r/r 681:        usbhid.ko.gz
r/r 686:        hv_utils.ko.gz
r/r 687:        hv_vmbus.ko.gz
r/r 685:        hv_balloon.ko.gz
-/- 3110:
-/- 50023:
r/r 690:        hwmon.ko.gz
r/r 689:        acpi_power_meter.ko.gz
d/d 692:        busses
r/r 696:        i2c-dev.ko.gz
r/r 697:        i2c-mux.ko.gz
d/d 698:        muxes
r/r 695:        i2c-core.ko.gz
r/r 694:        i2c-virtio.ko.gz
r/r 693:        i2c-piix4.ko.gz
r/r 699:        i2c-mux-pca9541.ko.gz
r/r 704:        mousedev.ko.gz
d/d 702:        mouse
d/d 705:        serio
r/r 701:        evdev.ko.gz
r/r 703:        psmouse.ko.gz
r/r 707:        pcips2.ko.gz
r/r 706:        hyperv-keyboard.ko.gz
r/r 709:        virtio-iommu.ko.gz
-/- 57871:
r/r 712:        bcache.ko.gz
r/r 716:        dm-cache.ko.gz
r/r 718:        dm-delay.ko.gz
r/r 719:        dm-flakey.ko.gz
r/r 720:        dm-integrity.ko.gz
r/r 721:        dm-io-affinity.ko.gz
r/r 722:        dm-log-userspace.ko.gz
r/r 723:        dm-log-writes.ko.gz
r/r 724:        dm-log.ko.gz
r/r 725:        dm-mirror.ko.gz
r/r 726:        dm-mod.ko.gz
r/r 729:        dm-raid.ko.gz
r/r 730:        dm-region-hash.ko.gz
r/r 732:        dm-service-time.ko.gz
r/r 736:        dm-unstripe.ko.gz
r/r 740:        faulty.ko.gz
r/r 741:        linear.ko.gz
r/r 745:        raid0.ko.gz
r/r 748:        raid456.ko.gz
r/r 714:        dm-bufio.ko.gz
r/r 727:        dm-multipath.ko.gz
r/r 731:        dm-round-robin.ko.gz
r/r 733:        dm-snapshot.ko.gz
r/r 737:        dm-verity.ko.gz
r/r 738:        dm-writecache.ko.gz
r/r 739:        dm-zero.ko.gz
r/r 747:        raid10.ko.gz
-/- 49532:
-/- 42545:
r/r 728:        dm-queue-length.ko.gz
r/r 734:        dm-switch.ko.gz
r/r 742:        multipath.ko.gz
r/r 746:        raid1.ko.gz
r/r 735:        dm-thin-pool.ko.gz
d/d 711:        bcache
d/d 743:        persistent-data
r/r 713:        dm-bio-prison.ko.gz
r/r 715:        dm-cache-smq.ko.gz
r/r 717:        dm-crypt.ko.gz
r/r 744:        dm-persistent-data.ko.gz
-/- 52238:
-/- 59713:
$\4Z
d/d 750:        fusion
r/r 752:        mptctl.ko.gz
r/r 753:        mptfc.ko.gz
r/r 754:        mptsas.ko.gz
r/r 755:        mptscsih.ko.gz
r/r 756:        mptspi.ko.gz
r/r 751:        mptbase.ko.gz
-/- 41450:
d/d 758:        pvpanic
d/d 763:        vmw_vmci
r/r 762:        vmw_balloon.ko.gz
r/r 760:        pvpanic-pci.ko.gz
r/r 761:        pvpanic.ko.gz
r/r 759:        pvpanic-mmio.ko.gz
r/r 764:        vmw_vmci.ko.gz
r/r 768:        bonding.ko.gz
-/- 53600:      \H;'\H;'
d/d 771:        amazon
d/d 774:        google
d/d 777:        intel
d/d 786:        mellanox
d/d 772:        ena
r/r 773:        ena.ko.gz
d/d 775:        gve
r/r 776:        gve.ko.gz
d/d 778:        e1000
d/d 780:        e1000e
d/d 782:        iavf
d/d 784:        ixgbevf
r/r 779:        e1000.ko.gz
r/r 781:        e1000e.ko.gz
r/r 783:        iavf.ko.gz
r/r 785:        ixgbevf.ko.gz
d/d 787:        mlx4
r/r 789:        mlx4_en.ko.gz
r/r 788:        mlx4_core.ko.gz
r/r 792:        hv_netvsc.ko.gz
r/r 795:        ipvlan.ko.gz
-/- 14738:
r/r 801:        fwnode_mdio.ko.gz
r/r 800:        acpi_mdio.ko.gz
-/- 3387:
r/r 807:        libphy.ko.gz
r/r 808:        mdio_devres.ko.gz
r/r 806:        fixed_phy.ko.gz
-/- 34806:
-/- 24511:
r/r 811:        ppp_async.ko.gz
r/r 812:        ppp_deflate.ko.gz
r/r 813:        ppp_generic.ko.gz
r/r 814:        ppp_mppe.ko.gz
r/r 815:        ppp_synctty.ko.gz
r/r 816:        pppox.ko.gz
r/r 817:        pptp.ko.gz
r/r 810:        bsd_comp.ko.gz
r/r 820:        slip.ko.gz
r/r 819:        slhc.ko.gz
r/r 824:        team_mode_activebackup.ko.gz
r/r 825:        team_mode_broadcast.ko.gz
r/r 826:        team_mode_loadbalance.ko.gz
r/r 827:        team_mode_random.ko.gz
r/r 828:        team_mode_roundrobin.ko.gz
r/r 823:        team.ko.gz
r/r 790:        geneve.ko.gz
r/r 798:        macvtap.ko.gz
r/r 829:        tun.ko.gz
d/d 767:        bonding
r/r 802:        net_failover.ko.gz
r/r 830:        veth.ko.gz
r/r 831:        virtio_net.ko.gz
d/d 794:        ipvlan
d/d 799:        mdio
d/d 818:        slip
d/d 837:        wireguard
r/r * 821(realloc):     .apk.3b78d3a7de4085121c9670f2aae7b2871441895246cc2df9
r/r * 830(realloc):     .apk.acefc30e44f64424d80119efd6a46368c12b04aebae888bd
r/r 834:        vrf.ko.gz
r/r 804:        nlmon.ko.gz
r/r 821:        tap.ko.gz
d/d 770:        ethernet
d/d 809:        ppp
d/d 791:        hyperv
r/r 797:        macvlan.ko.gz
r/r 803:        netconsole.ko.gz
d/d 805:        phy
r/r 793:        ifb.ko.gz
r/r 796:        macsec.ko.gz
d/d 822:        team
d/d 832:        vmxnet3
d/d 835:        vxlan
d/d 839:        xen-netback
r/r 766:        bareudp.ko.gz
r/r 769:        dummy.ko.gz
r/r 833:        vmxnet3.ko.gz
r/r 836:        vxlan.ko.gz
-/- 20710:
r/r 838:        wireguard.ko.gz
r/r 840:        xen-netback.ko.gz
r/r 843:        nd_pmem.ko.gz
r/r 842:        nd_btt.ko.gz
d/d 845:        host
d/d 849:        target
r/r 847:        nvme-fabrics.ko.gz
r/r 848:        nvme.ko.gz
r/r 846:        nvme-core.ko.gz
r/r 851:        nvmet.ko.gz
r/r 850:        nvme-loop.ko.gz
d/d 853:        controller
r/r 856:        pci-stub.ko.gz
r/r 855:        pci-hyperv.ko.gz
r/r 854:        pci-hyperv-intf.ko.gz
r/r 859:        ptp_vmw.ko.gz
r/r 858:        ptp_kvm.ko.gz
r/r 862:        rpmsg_ns.ko.gz
r/r 863:        virtio_rpmsg_bus.ko.gz
r/r 861:        rpmsg_core.ko.gz
-/r 1613:
r/r 865:        rtc-test.ko.gz
-/- 50714:
r/r 872:        libsas.ko.gz
-/- 16002:
r/r 885:        target_core_mod.ko.gz
-/- 36238:
d/d 887:        serial
r/r 889:        altera_uart.ko.gz
d/d 890:        jsm
r/r 888:        altera_jtaguart.ko.gz
r/r 891:        jsm.ko.gz
d/d 893:        common
d/d 895:        core
d/d 897:        host
d/d 908:        mon
d/d 910:        storage
-/- 23347:
r/r 894:        usb-common.ko.gz
r/r 896:        usbcore.ko.gz
r/r 899:        ehci-pci.ko.gz
r/r 900:        ehci-platform.ko.gz
r/r 901:        ohci-hcd.ko.gz
r/r 902:        ohci-pci.ko.gz
r/r 903:        ohci-platform.ko.gz
r/r 904:        uhci-hcd.ko.gz
r/r 905:        xen-hcd.ko.gz
r/r 906:        xhci-hcd.ko.gz
r/r 907:        xhci-pci.ko.gz
r/r 898:        ehci-hcd.ko.gz
r/r 909:        usbmon.ko.gz
r/r 912:        usb-storage.ko.gz
r/r 911:        uas.ko.gz
d/d 914:        ifcvf
d/d 917:        virtio_pci
r/r 916:        vdpa.ko.gz
r/r 915:        ifcvf.ko.gz
r/r 918:        vp_vdpa.ko.gz
r/r 921:        vhost_iotlb.ko.gz
r/r 922:        vhost_net.ko.gz
r/r 923:        vhost_vdpa.ko.gz
r/r 920:        vhost.ko.gz
d/d 925:        fbdev
-/- 43970:
-/- 3667:
d/d 926:        core
r/r 928:        fb_sys_fops.ko.gz
r/r 929:        syscopyarea.ko.gz
r/r 930:        sysfillrect.ko.gz
r/r 931:        sysimgblt.ko.gz
r/r 927:        fb.ko.gz
d/d 933:        coco
d/d 936:        nitro_enclaves
d/d 938:        vboxguest
d/d 934:        efi_secret
r/r 935:        efi_secret.ko.gz
r/r 937:        nitro_enclaves.ko.gz
-/- 58021:
r/r 939:        vboxguest.ko.gz
r/r 942:        virtio_dma_buf.ko.gz
r/r 943:        virtio_input.ko.gz
r/r 944:        virtio_vdpa.ko.gz
r/r 941:        virtio_balloon.ko.gz
-/- 55416:
r/r 947:        xen_wdt.ko.gz
r/r 946:        i6300esb.ko.gz
r/r 950:        xen-acpi-processor.ko.gz
r/r 951:        xen-evtchn.ko.gz
r/r 952:        xen-front-pgdir-shbuf.ko.gz
r/r 953:        xen-gntalloc.ko.gz
r/r 954:        xen-gntdev.ko.gz
r/r 957:        xen-scsiback.ko.gz
d/d 955:        xen-pciback
r/r 949:        pvcalls-front.ko.gz
-/- 31957:
-/- 8612:
r/r 956:        xen-pciback.ko.gz
-/- 63989:
d/d 959:        9p
d/d 961:        autofs
r/r 1009:       mbcache.ko.gz
d/d 964:        btrfs
d/d 966:        cachefiles
d/d 968:        ceph
d/d 970:        configfs
d/d 972:        cramfs
d/d 974:        dlm
d/d 976:        ecryptfs
d/d 978:        efivarfs
d/d 980:        efs
d/d 982:        exfat
d/d 984:        ext2
d/d 986:        ext4
d/d 988:        f2fs
d/d 990:        fat
d/d 994:        fscache
d/d 996:        fuse
d/d 999:        gfs2
d/d 1001:       isofs
d/d 1003:       jbd2
d/d 1005:       jfs
d/d 1007:       lockd
d/d 1010:       netfs
d/d 1012:       nfs
d/d 1023:       nfs_common
d/d 1025:       nfsd
d/d 1027:       nilfs2
d/d 1029:       nls
d/d 1082:       ntfs
d/d 1084:       ntfs3
d/d 1086:       ocfs2
d/d 1097:       overlayfs
d/d 1099:       pstore
d/d 1101:       quota
d/d 1105:       reiserfs
d/d 1107:       romfs
d/d 1109:       smb
d/d 1117:       squashfs
d/d 1119:       sysv
d/d 1121:       udf
d/d 1123:       ufs
d/d 1125:       vboxsf
d/d 1127:       xfs
r/r 963:        binfmt_misc.ko.gz
r/r 960:        9p.ko.gz
-/- 57747:
r/r 962:        autofs4.ko.gz
r/r 965:        btrfs.ko.gz
r/r 967:        cachefiles.ko.gz
r/r 969:        ceph.ko.gz
-/- 8324:
syset
r/r 971:        configfs.ko.gz
r/r 973:        cramfs.ko.gz
r/r 975:        dlm.ko.gz
r/r 977:        ecryptfs.ko.gz
r/r 979:        efivarfs.ko.gz
r/r 981:        efs.ko.gz
r/r 983:        exfat.ko.gz
r/r 985:        ext2.ko.gz
r/r 987:        ext4.ko.gz
r/r 989:        f2fs.ko.gz
r/r 992:        msdos.ko.gz
r/r 993:        vfat.ko.gz
r/r 991:        fat.ko.gz
r/r 995:        fscache.ko.gz
r/r 998:        virtiofs.ko.gz
r/r 997:        fuse.ko.gz
r/r 1000:       gfs2.ko.gz
r/r 1002:       isofs.ko.gz
r/r 1004:       jbd2.ko.gz
r/r 1006:       jfs.ko.gz
r/r 1008:       lockd.ko.gz
r/r 1011:       netfs.ko.gz
d/d 1013:       blocklayout
d/d 1015:       filelayout
d/d 1017:       flexfilelayout
r/r 1020:       nfsv2.ko.gz
r/r 1021:       nfsv3.ko.gz
r/r 1022:       nfsv4.ko.gz
r/r 1019:       nfs.ko.gz
r/r 1014:       blocklayoutdriver.ko.gz
r/r 1016:       nfs_layout_nfsv41_files.ko.gz
r/r 1018:       nfs_layout_flexfiles.ko.gz
-/- 59595:
r/r 1024:       grace.ko.gz
r/r 1026:       nfsd.ko.gz
r/r 1028:       nilfs2.ko.gz
r/r 1043:       nls_cp1251.ko.gz
r/r 1056:       nls_cp864.ko.gz
r/r 1069:       nls_iso8859-15.ko.gz
r/r 1071:       nls_iso8859-3.ko.gz
r/r 1076:       nls_iso8859-9.ko.gz
r/r 1078:       nls_koi8-ru.ko.gz
r/r 1040:       mac-turkish.ko.gz
r/r 1061:       nls_cp932.ko.gz
r/r 1070:       nls_iso8859-2.ko.gz
-/- 36530:
r/r 1053:       nls_cp861.ko.gz
r/r 1065:       nls_euc-jp.ko.gz
r/r 1047:       nls_cp775.ko.gz
r/r 1050:       nls_cp855.ko.gz
r/r 1032:       mac-croatian.ko.gz
r/r 1041:       nls_ascii.ko.gz
r/r 1080:       nls_ucs2_utils.ko.gz
r/r 1031:       mac-centeuro.ko.gz
r/r 1036:       mac-iceland.ko.gz
r/r 1039:       mac-romanian.ko.gz
r/r * 1063(realloc):    .apk.9a295221d4138941a47f5ce8906c8d72f55209c4a3c5eb48
r/r * 1064(realloc):    .apk.7b48a32ea6cdbc6922e4aeac0edb7aa2fd1f8cec311a70ff
r/r * 1070(realloc):    .apk.7d98615db65a18bf065331d568e522452b36b76e1b32a1cc
-/- 61527:
r/r 1037:       mac-inuit.ko.gz
r/r 1038:       mac-roman.ko.gz
r/r 1049:       nls_cp852.ko.gz
r/r 1052:       nls_cp860.ko.gz
r/r 1055:       nls_cp863.ko.gz
r/r 1057:       nls_cp865.ko.gz
r/r 1059:       nls_cp869.ko.gz
r/r 1062:       nls_cp936.ko.gz
r/r 1034:       mac-gaelic.ko.gz
r/r 1042:       nls_cp1250.ko.gz
r/r 1063:       nls_cp949.ko.gz
r/r 1064:       nls_cp950.ko.gz
r/r 1068:       nls_iso8859-14.ko.gz
r/r 1074:       nls_iso8859-6.ko.gz
r/r 1077:       nls_koi8-r.ko.gz
r/r 1079:       nls_koi8-u.ko.gz
r/r 1030:       mac-celtic.ko.gz
r/r 1033:       mac-cyrillic.ko.gz
-/- 37949:
r/r 1067:       nls_iso8859-13.ko.gz
r/r 1075:       nls_iso8859-7.ko.gz
r/r 1060:       nls_cp874.ko.gz
r/r 1046:       nls_cp737.ko.gz
r/r 1048:       nls_cp850.ko.gz
r/r 1083:       ntfs.ko.gz
r/r 1085:       ntfs3.ko.gz
-/- 61488:
d/d 1087:       cluster
d/d 1089:       dlm
d/d 1091:       dlmfs
r/r 1094:       ocfs2_stack_o2cb.ko.gz
r/r 1095:       ocfs2_stack_user.ko.gz
r/r 1096:       ocfs2_stackglue.ko.gz
r/r 1093:       ocfs2.ko.gz
r/r 1088:       ocfs2_nodemanager.ko.gz
r/r 1090:       ocfs2_dlm.ko.gz
r/r 1092:       ocfs2_dlmfs.ko.gz
r/r 1098:       overlay.ko.gz
r/r 1100:       ramoops.ko.gz
-/- 57524:
-/- 48496:
r/r 1103:       quota_v1.ko.gz
r/r 1104:       quota_v2.ko.gz
r/r 1102:       quota_tree.ko.gz
r/r 1106:       reiserfs.ko.gz
r/r 1108:       romfs.ko.gz
d/d 1110:       client
d/d 1112:       common
d/d 1115:       server
r/r 1111:       cifs.ko.gz
r/r 1114:       cifs_md4.ko.gz
r/r 1113:       cifs_arc4.ko.gz
-/- 31711:
r/r 1116:       ksmbd.ko.gz
r/r 1118:       squashfs.ko.gz
r/r 1120:       sysv.ko.gz
r/r 1122:       udf.ko.gz
r/r 1124:       ufs.ko.gz
-/- 24627:
r/r 1126:       vboxsf.ko.gz
r/r 1128:       xfs.ko.gz
r/r 1130:       configs.ko.gz
r/r 1133:       crc-itu-t.ko.gz
r/r 1134:       crc16.ko.gz
r/r 1135:       crc64-rocksoft.ko.gz
r/r 1136:       crc64.ko.gz
r/r 1137:       crc7.ko.gz
r/r 1138:       crc8.ko.gz
r/r 1148:       libcrc32c.ko.gz
r/r 1149:       lru_cache.ko.gz
r/r 1159:       ts_bm.ko.gz
r/r 1160:       ts_fsm.ko.gz
r/r 1161:       ts_kmp.ko.gz
d/d 1139:       crypto
d/d 1150:       lz4
d/d 1153:       math
d/d 1155:       raid6
d/d 1157:       reed_solomon
r/r 1132:       crc-ccitt.ko.gz
r/r 1141:       libarc4.ko.gz
r/r 1142:       libchacha.ko.gz
r/r 1143:       libchacha20poly1305.ko.gz
r/r 1144:       libcurve25519-generic.ko.gz
r/r 1145:       libcurve25519.ko.gz
r/r 1146:       libdes.ko.gz
r/r 1147:       libpoly1305.ko.gz
r/r 1140:       gf128mul.ko.gz
-/- 3227:
-/- 38374:
r/r 1152:       lz4hc_compress.ko.gz
r/r 1151:       lz4_compress.ko.gz
r/r 1154:       cordic.ko.gz
r/r 1156:       raid6_pq.ko.gz
r/r 1158:       reed_solomon.ko.gz
d/d 1163:       802
d/d 1168:       8021q
d/d 1170:       9p
d/d 1175:       bridge
d/d 1202:       ceph
d/d 1204:       core
d/d 1208:       dccp
d/d 1213:       ife
d/d 1215:       ipv4
d/d 1270:       ipv6
d/d 1312:       key
d/d 1314:       l2tp
d/d 1321:       llc
d/d 1324:       mpls
d/d 1328:       netfilter
d/d 1494:       nsh
d/d 1496:       openvswitch
d/d 1501:       packet
d/d 1504:       sched
d/d 1565:       sctp
d/d 1568:       sunrpc
d/d 1573:       tls
d/d 1575:       unix
d/d 1577:       vmw_vsock
d/d 1584:       xfrm
r/r 1165:       p8022.ko.gz
r/r 1166:       psnap.ko.gz
r/r 1167:       stp.ko.gz
r/r 1164:       mrp.ko.gz
r/r 1169:       8021q.ko.gz
-/- 8181:
r/r 1172:       9pnet_fd.ko.gz
r/r 1173:       9pnet_virtio.ko.gz
r/r 1174:       9pnet_xen.ko.gz
r/r 1171:       9pnet.ko.gz
-/- 42436:
r/r 1177:       bridge.ko.gz
d/d 1178:       netfilter
r/r 1176:       br_netfilter.ko.gz
-/- 55211:
r/r 1180:       ebt_among.ko.gz
r/r 1183:       ebt_dnat.ko.gz
r/r 1184:       ebt_ip.ko.gz
r/r 1185:       ebt_ip6.ko.gz
r/r 1186:       ebt_limit.ko.gz
r/r 1187:       ebt_log.ko.gz
r/r 1188:       ebt_mark.ko.gz
r/r 1189:       ebt_mark_m.ko.gz
r/r 1191:       ebt_pkttype.ko.gz
r/r 1192:       ebt_redirect.ko.gz
r/r 1193:       ebt_snat.ko.gz
r/r 1195:       ebt_vlan.ko.gz
r/r 1197:       ebtable_filter.ko.gz
r/r 1199:       ebtables.ko.gz
r/r 1194:       ebt_stp.ko.gz
r/r 1196:       ebtable_broute.ko.gz
r/r 1198:       ebtable_nat.ko.gz
r/r 1200:       nf_conntrack_bridge.ko.gz
r/r 1190:       ebt_nflog.ko.gz
r/r 1201:       nft_reject_bridge.ko.gz
r/r 1182:       ebt_arpreply.ko.gz
r/r 1179:       ebt_802_3.ko.gz
r/r 1181:       ebt_arp.ko.gz
r/r 1203:       libceph.ko.gz
r/r 1206:       pktgen.ko.gz
r/r 1207:       selftests.ko.gz
r/r 1205:       failover.ko.gz
-/- 34332:
r/r 1210:       dccp_diag.ko.gz
r/r 1211:       dccp_ipv4.ko.gz
r/r 1212:       dccp_ipv6.ko.gz
r/r 1209:       dccp.ko.gz
-/- 45809:
r/r 1214:       ife.ko.gz
-/r 278:
-/- 25371:
r/r 1227:       arpt_mangle.ko.gz
r/r 1228:       arptable_filter.ko.gz
r/r 1231:       ipt_REJECT.ko.gz
r/r 1234:       ipt_rpfilter.ko.gz
r/r 1235:       iptable_filter.ko.gz
r/r 1236:       iptable_mangle.ko.gz
r/r 1237:       iptable_nat.ko.gz
r/r 1238:       iptable_raw.ko.gz
r/r 1239:       nf_defrag_ipv4.ko.gz
r/r 1241:       nf_nat_h323.ko.gz
r/r 1242:       nf_nat_pptp.ko.gz
r/r 1243:       nf_nat_snmp_basic.ko.gz
r/r 1248:       nft_fib_ipv4.ko.gz
r/r 1226:       arp_tables.ko.gz
r/r 1229:       ip_tables.ko.gz
r/r * 1238(realloc):    .apk.fd22f25e23770299c80c93689eca347b7b2148eeeaa0a767
r/r * 1239(realloc):    .apk.11eeabd753bc921b90c32384b6ca7085ce1f64c8137eae93
r/r * 1240(realloc):    .apk.0c561abdcab6fb111567767a04c94851cfab98a71cb3c82b
r/r 1240:       nf_dup_ipv4.ko.gz
r/r 1244:       nf_reject_ipv4.ko.gz
r/r 1245:       nf_socket_ipv4.ko.gz
r/r 1246:       nf_tproxy_ipv4.ko.gz
r/r 1247:       nft_dup_ipv4.ko.gz
r/r 1249:       nft_reject_ipv4.ko.gz
r/r 1230:       ipt_ECN.ko.gz
r/r 1232:       ipt_SYNPROXY.ko.gz
r/r 1233:       ipt_ah.ko.gz
r/r 1219:       inet_diag.ko.gz
r/r 1220:       ip_gre.ko.gz
r/r 1221:       ip_tunnel.ko.gz
r/r 1222:       ip_vti.ko.gz
r/r 1250:       tcp_bbr.ko.gz
r/r 1258:       tcp_illinois.ko.gz
r/r 1259:       tcp_lp.ko.gz
r/r 1264:       tcp_westwood.ko.gz
r/r 1268:       udp_tunnel.ko.gz
r/r 1269:       xfrm4_tunnel.ko.gz
r/r 1223:       ipcomp.ko.gz
r/r 1256:       tcp_htcp.ko.gz
r/r 1257:       tcp_hybla.ko.gz
r/r 1260:       tcp_nv.ko.gz
r/r 1262:       tcp_vegas.ko.gz
r/r 1267:       udp_diag.ko.gz
d/d 1225:       netfilter
r/r 1217:       esp4.ko.gz
r/r * 1265(realloc):    .apk.992ee6e33110a28914fd49d181945278418023d70784aa33
-/- 44111:
-/- 64283:
-/- 4193:
r/r 1255:       tcp_highspeed.ko.gz
r/r 1261:       tcp_scalable.ko.gz
r/r 1224:       ipip.ko.gz
r/r 1251:       tcp_bic.ko.gz
r/r 1265:       tcp_yeah.ko.gz
r/r 1266:       tunnel4.ko.gz
r/r 1263:       tcp_veno.ko.gz
r/r 1216:       ah4.ko.gz
r/r 1218:       fou.ko.gz
r/r 1252:       tcp_cdg.ko.gz
r/r 1253:       tcp_dctcp.ko.gz
r/r 1254:       tcp_diag.ko.gz
-/- 46567:
r/r 1272:       esp6.ko.gz
r/r 1273:       fou6.ko.gz
r/r 1276:       ip6_gre.ko.gz
r/r 1277:       ip6_tunnel.ko.gz
r/r 1278:       ip6_udp_tunnel.ko.gz
r/r 1279:       ip6_vti.ko.gz
r/r 1280:       ipcomp6.ko.gz
r/r 1281:       ipv6.ko.gz
d/d 1274:       ila
r/r 1282:       mip6.ko.gz
r/r 1309:       sit.ko.gz
r/r 1310:       tunnel6.ko.gz
r/r 1311:       xfrm6_tunnel.ko.gz
d/d 1283:       netfilter
r/r 1271:       ah6.ko.gz
r/r 1275:       ila.ko.gz
-/- 20433:
-/- 24863:
r/r 1285:       ip6t_NPT.ko.gz
r/r 1288:       ip6t_ah.ko.gz
r/r 1290:       ip6t_frag.ko.gz
r/r 1291:       ip6t_hbh.ko.gz
r/r 1292:       ip6t_ipv6header.ko.gz
r/r 1293:       ip6t_mh.ko.gz
r/r 1294:       ip6t_rpfilter.ko.gz
r/r 1295:       ip6t_rt.ko.gz
r/r 1296:       ip6t_srh.ko.gz
r/r 1297:       ip6table_filter.ko.gz
r/r 1298:       ip6table_mangle.ko.gz
r/r 1299:       ip6table_nat.ko.gz
r/r 1300:       ip6table_raw.ko.gz
r/r 1301:       nf_defrag_ipv6.ko.gz
r/r 1302:       nf_dup_ipv6.ko.gz
r/r 1303:       nf_reject_ipv6.ko.gz
r/r 1304:       nf_socket_ipv6.ko.gz
r/r 1306:       nft_dup_ipv6.ko.gz
r/r 1307:       nft_fib_ipv6.ko.gz
r/r 1305:       nf_tproxy_ipv6.ko.gz
r/r 1308:       nft_reject_ipv6.ko.gz
r/r 1286:       ip6t_REJECT.ko.gz
r/r 1287:       ip6t_SYNPROXY.ko.gz
r/r 1284:       ip6_tables.ko.gz
r/r 1289:       ip6t_eui64.ko.gz
-/- 49371:
-/- 46045:
-/- 14095:
-/- 51556:
-/- 3763:
r/r 1313:       af_key.ko.gz
-/- 30878:
-/- 28350:
r/r 1316:       l2tp_eth.ko.gz
r/r 1317:       l2tp_ip.ko.gz
r/r 1318:       l2tp_ip6.ko.gz
r/r 1319:       l2tp_netlink.ko.gz
r/r 1320:       l2tp_ppp.ko.gz
r/r 1315:       l2tp_core.ko.gz
-/- 10252:
r/r 1323:       llc2.ko.gz
r/r 1322:       llc.ko.gz
r/r 1326:       mpls_iptunnel.ko.gz
r/r 1327:       mpls_router.ko.gz
r/r 1325:       mpls_gso.ko.gz
-/r 1845:
-/- 37918:
r/r 1332:       ip_set_bitmap_ipmac.ko.gz
r/r 1333:       ip_set_bitmap_port.ko.gz
r/r 1335:       ip_set_hash_ipmac.ko.gz
r/r 1336:       ip_set_hash_ipmark.ko.gz
r/r 1337:       ip_set_hash_ipport.ko.gz
r/r 1339:       ip_set_hash_ipportnet.ko.gz
r/r 1340:       ip_set_hash_mac.ko.gz
r/r 1341:       ip_set_hash_net.ko.gz
r/r 1344:       ip_set_hash_netport.ko.gz
r/r 1345:       ip_set_hash_netportnet.ko.gz
r/r 1330:       ip_set.ko.gz
r/r 1338:       ip_set_hash_ipportip.ko.gz
r/r * 1339(realloc):    .apk.4b9a38a38d695e063acfa1cdc18abe8154644c6659d4c1f5
r/r * 1342(realloc):    .apk.e9e01f5f668d185a1116cb76da76c7e9f491a9e856e84c13
r/r * 1344(realloc):    .apk.d8c4a0615c5b17466df555eed4b37426f6d423fc612307ff
r/r 1342:       ip_set_hash_netiface.ko.gz
r/r 1343:       ip_set_hash_netnet.ko.gz
r/r 1346:       ip_set_list_set.ko.gz
r/r 1334:       ip_set_hash_ip.ko.gz
r/r 1331:       ip_set_bitmap_ip.ko.gz
-/- 51373:
r/r 1349:       ip_vs_dh.ko.gz
r/r 1352:       ip_vs_lblc.ko.gz
r/r 1355:       ip_vs_mh.ko.gz
r/r 1357:       ip_vs_ovf.ko.gz
r/r 1359:       ip_vs_rr.ko.gz
r/r 1361:       ip_vs_sh.ko.gz
r/r 1362:       ip_vs_wlc.ko.gz
r/r 1363:       ip_vs_wrr.ko.gz
r/r 1358:       ip_vs_pe_sip.ko.gz
r/r 1360:       ip_vs_sed.ko.gz
r/r 1354:       ip_vs_lc.ko.gz
r/r 1356:       ip_vs_nq.ko.gz
r/r 1348:       ip_vs.ko.gz
r/r 1350:       ip_vs_fo.ko.gz
r/r 1351:       ip_vs_ftp.ko.gz
r/r 1353:       ip_vs_lblcr.ko.gz
-/- 40182:
-/- 51762:
-/- 41161:
r/r 1375:       nf_conntrack_sip.ko.gz
r/r 1387:       nf_nat_tftp.ko.gz
r/r 1391:       nfnetlink_acct.ko.gz
r/r 1394:       nfnetlink_log.ko.gz
r/r 1415:       nft_quota.ko.gz
r/r 1417:       nft_reject.ko.gz
r/r 1419:       nft_socket.ko.gz
r/r 1426:       xt_CONNSECMARK.ko.gz
r/r 1438:       xt_REDIRECT.ko.gz
r/r 1441:       xt_TCPOPTSTRIP.ko.gz
r/r 1446:       xt_bpf.ko.gz
r/r 1451:       xt_connlabel.ko.gz
r/r 1452:       xt_connlimit.ko.gz
r/r 1455:       xt_cpu.ko.gz
r/r 1462:       xt_helper.ko.gz
r/r 1480:       xt_quota.ko.gz
r/r 1484:       xt_sctp.ko.gz
r/r 1400:       nft_ct.ko.gz
r/r 1406:       nft_fwd_netdev.ko.gz
r/r 1412:       nft_numgen.ko.gz
r/r 1422:       x_tables.ko.gz
r/r 1380:       nf_flow_table_inet.ko.gz
r/r 1392:       nfnetlink_cthelper.ko.gz
r/r 1405:       nft_flow_offload.ko.gz
r/r 1443:       xt_TPROXY.ko.gz
r/r 1373:       nf_conntrack_pptp.ko.gz
r/r 1374:       nf_conntrack_sane.ko.gz
r/r 1395:       nfnetlink_osf.ko.gz
r/r 1408:       nft_limit.ko.gz
r/r 1430:       xt_HMARK.ko.gz
r/r 1465:       xt_iprange.ko.gz
r/r 1475:       xt_osf.ko.gz
r/r 1393:       nfnetlink_cttimeout.ko.gz
r/r 1407:       nft_hash.ko.gz
r/r 1377:       nf_conntrack_tftp.ko.gz
r/r 1381:       nf_log_syslog.ko.gz
r/r 1437:       xt_RATEEST.ko.gz
r/r 1440:       xt_TCPMSS.ko.gz
r/r 1488:       xt_statistic.ko.gz
-/- 64287:
-/- 10327:
-/- 6033:
-/- 35756:
-/- 22161:
r/r 1418:       nft_reject_inet.ko.gz
r/r 1421:       nft_tunnel.ko.gz
d/d 1347:       ipvs
r/r 1382:       nf_nat.ko.gz
r/r 1386:       nf_nat_sip.ko.gz
r/r 1473:       xt_nat.ko.gz
r/r 1368:       nf_conntrack_ftp.ko.gz
d/d 1329:       ipset
r/r 1423:       xt_AUDIT.ko.gz
r/r 1425:       xt_CLASSIFY.ko.gz
r/r 1410:       nft_masq.ko.gz
r/r 1431:       xt_IDLETIMER.ko.gz
r/r 1399:       nft_connlimit.ko.gz
r/r 1444:       xt_TRACE.ko.gz
r/r 1447:       xt_cgroup.ko.gz
r/r 1448:       xt_cluster.ko.gz
r/r 1460:       xt_esp.ko.gz
r/r 1467:       xt_l2tp.ko.gz
r/r 1469:       xt_limit.ko.gz
r/r 1479:       xt_policy.ko.gz
r/r 1486:       xt_socket.ko.gz
r/r 1489:       xt_string.ko.gz
r/r 1493:       xt_u32.ko.gz
r/r 1466:       xt_ipvs.ko.gz
r/r 1472:       xt_multiport.ko.gz
r/r 1477:       xt_physdev.ko.gz
r/r 1478:       xt_pkttype.ko.gz
r/r 1485:       xt_set.ko.gz
r/r 1369:       nf_conntrack_h323.ko.gz
r/r 1366:       nf_conntrack_amanda.ko.gz
r/r 1491:       xt_tcpudp.ko.gz
r/r 1383:       nf_nat_amanda.ko.gz
r/r 1385:       nf_nat_irc.ko.gz
-/- 48341:
-/- 64456:
-/- 5224:
-/- 44003:
r/r 1453:       xt_connmark.ko.gz
r/r 1490:       xt_tcpmss.ko.gz
r/r 1414:       nft_queue.ko.gz
r/r 1428:       xt_DSCP.ko.gz
r/r 1372:       nf_conntrack_netlink.ko.gz
r/r 1378:       nf_dup_netdev.ko.gz
-/- 50175:
-/- 63217:
r/r 1390:       nfnetlink.ko.gz
r/r 1397:       nft_chain_nat.ko.gz
r/r 1435:       xt_NFLOG.ko.gz
r/r 1481:       xt_rateest.ko.gz
r/r 1376:       nf_conntrack_snmp.ko.gz
r/r 1384:       nf_nat_ftp.ko.gz
r/r 1409:       nft_log.ko.gz
r/r 1411:       nft_nat.ko.gz
r/r 1365:       nf_conntrack.ko.gz
r/r 1396:       nfnetlink_queue.ko.gz
r/r 1398:       nft_compat.ko.gz
r/r 1450:       xt_connbytes.ko.gz
r/r 1454:       xt_conntrack.ko.gz
r/r 1433:       xt_MASQUERADE.ko.gz
r/r 1436:       xt_NFQUEUE.ko.gz
r/r 1457:       xt_devgroup.ko.gz
r/r 1482:       xt_realm.ko.gz
r/r 1487:       xt_state.ko.gz
r/r 1364:       nf_conncount.ko.gz
r/r 1367:       nf_conntrack_broadcast.ko.gz
r/r 1459:       xt_ecn.ko.gz
r/r 1470:       xt_mac.ko.gz
r/r 1474:       xt_nfacct.ko.gz
r/r * 1479(realloc):    .apk.4fb1098e5ee1bf463cf34d73a05c390983b02ad8c5b6ea6b
r/r * 1483(realloc):    .apk.06c3b0af886f338065abe611865e5dd4cd5ca4857404acbd
r/r * 1493(realloc):    .apk.5050bbbc83cc3abebaa8f0dd0f3d10416d99ef6cf1603ce2
r/r 1461:       xt_hashlimit.ko.gz
r/r 1468:       xt_length.ko.gz
r/r 1413:       nft_osf.ko.gz
r/r 1424:       xt_CHECKSUM.ko.gz
r/r 1401:       nft_dup_netdev.ko.gz
r/r 1434:       xt_NETMAP.ko.gz
r/r 1389:       nf_tables.ko.gz
r/r 1449:       xt_comment.ko.gz
r/r 1370:       nf_conntrack_irc.ko.gz
r/r 1371:       nf_conntrack_netbios_ns.ko.gz
-/- 4694:
r/r 1495:       nsh.ko.gz
r/r 1498:       vport-geneve.ko.gz
r/r 1499:       vport-gre.ko.gz
r/r 1500:       vport-vxlan.ko.gz
r/r 1497:       openvswitch.ko.gz
-/- 29689:
r/r 1503:       af_packet_diag.ko.gz
r/r 1502:       af_packet.ko.gz
-/- 56485:
-/- 7240:
r/r 1514:       act_mirred.ko.gz
r/r 1515:       act_nat.ko.gz
r/r 1517:       act_police.ko.gz
r/r 1526:       cls_flow.ko.gz
r/r 1536:       em_nbyte.ko.gz
r/r 1541:       sch_choke.ko.gz
r/r 1548:       sch_hfsc.ko.gz
r/r 1558:       sch_prio.ko.gz
r/r 1562:       sch_sfq.ko.gz
r/r 1522:       act_vlan.ko.gz
r/r 1525:       cls_cgroup.ko.gz
r/r 1513:       act_meta_skbtcindex.ko.gz
r/r 1516:       act_pedit.ko.gz
r/r 1507:       act_csum.ko.gz
r/r 1508:       act_gact.ko.gz
r/r 1529:       cls_matchall.ko.gz
r/r 1532:       em_cmp.ko.gz
r/r 1552:       sch_mqprio.ko.gz
r/r 1555:       sch_netem.ko.gz
r/r 1556:       sch_pie.ko.gz
r/r 1560:       sch_red.ko.gz
r/r 1510:       act_ipt.ko.gz
-/- 57345:
-/- 18818:
-/- 43775:
-/- 57242:
-/- 63290:
r/r 1537:       em_text.ko.gz
r/r 1551:       sch_ingress.ko.gz
r/r 1512:       act_meta_skbprio.ko.gz
r/r 1518:       act_simple.ko.gz
r/r 1553:       sch_mqprio_lib.ko.gz
r/r 1524:       cls_bpf.ko.gz
r/r 1527:       cls_flower.ko.gz
r/r 1520:       act_skbmod.ko.gz
r/r 1528:       cls_fw.ko.gz
r/r 1534:       em_ipt.ko.gz
r/r 1535:       em_meta.ko.gz
r/r 1538:       em_u32.ko.gz
r/r 1544:       sch_fq.ko.gz
r/r 1533:       em_ipset.ko.gz
r/r 1539:       sch_cake.ko.gz
r/r 1540:       sch_cbs.ko.gz
r/r 1543:       sch_drr.ko.gz
r/r 1546:       sch_fq_pie.ko.gz
r/r 1554:       sch_multiq.ko.gz
r/r 1557:       sch_plug.ko.gz
-/- 47031:
-/r 1140:
-/- 26567:
-/- 37772:
r/r 1542:       sch_codel.ko.gz
r/r 1545:       sch_fq_codel.ko.gz
r/r 1521:       act_tunnel_key.ko.gz
r/r 1523:       cls_basic.ko.gz
r/r 1547:       sch_gred.ko.gz
r/r 1549:       sch_hhf.ko.gz
r/r 1559:       sch_qfq.ko.gz
r/r 1561:       sch_sfb.ko.gz
r/r 1563:       sch_tbf.ko.gz
r/r 1530:       cls_route.ko.gz
r/r 1531:       cls_u32.ko.gz
r/r 1505:       act_bpf.ko.gz
r/r 1506:       act_connmark.ko.gz
r/r 1511:       act_meta_mark.ko.gz
r/r 1564:       sch_teql.ko.gz
r/r 1550:       sch_htb.ko.gz
r/r 1519:       act_skbedit.ko.gz
r/r 1509:       act_ife.ko.gz
-/- 30528:
-/- 61005:
syse
-/- 35308:
r/r 1567:       sctp_diag.ko.gz
r/r 1566:       sctp.ko.gz
d/d 1569:       auth_gss
r/r 1572:       sunrpc.ko.gz
r/r 1571:       rpcsec_gss_krb5.ko.gz
r/r 1570:       auth_rpcgss.ko.gz
r/r 1574:       tls.ko.gz
r/r 1576:       unix_diag.ko.gz
r/r 1579:       vmw_vsock_virtio_transport_common.ko.gz
r/r 1580:       vmw_vsock_vmci_transport.ko.gz
r/r 1581:       vsock.ko.gz
r/r 1582:       vsock_diag.ko.gz
r/r 1583:       vsock_loopback.ko.gz
r/r 1578:       vmw_vsock_virtio_transport.ko.gz
-/- 37937:
r/r 1586:       xfrm_interface.ko.gz
r/r 1587:       xfrm_ipcomp.ko.gz
r/r 1588:       xfrm_user.ko.gz
r/r 1585:       xfrm_algo.ko.gz
-/- 50246:
-/- 24701:
d/d 1590:       keys
d/d 1591:       encrypted-keys
r/r 1592:       encrypted-keys.ko.gz
d/d 1594:       core
d/d 1599:       hda
d/d 1603:       pci
d/d 1608:       virtio
r/r 1596:       snd-pcm.ko.gz
r/r 1597:       snd-timer.ko.gz
r/r 1598:       snd.ko.gz
r/r 1595:       snd-hwdep.ko.gz
r/r 1601:       snd-intel-dspcfg.ko.gz
r/r 1602:       snd-intel-sdw-acpi.ko.gz
r/r 1600:       snd-hda-core.ko.gz
-/- 63992:
syse
d/d 1604:       hda
r/r 1606:       snd-hda-codec.ko.gz
r/r 1607:       snd-hda-intel.ko.gz
r/r 1605:       snd-hda-codec-generic.ko.gz
r/r 1609:       virtio_snd.ko.gz
-/- 18400:      $~
d/d 1611:       lib
r/r 1612:       irqbypass.ko.gz
-/r 876:         
-/- 6363:
s/- 31087:
r/- 10409:
d/d 1627:       virt
r/r 1628:       kernel.release
r/r 869:        libiscsi.ko.gz
r/r 874:        scsi_transport_fc.ko.gz
r/r 875:        scsi_transport_iscsi.ko.gz
r/r 876:        scsi_transport_sas.ko.gz
r/r 877:        scsi_transport_spi.ko.gz
r/r 880:        sg.ko.gz
r/r 881:        sr_mod.ko.gz
d/d 871:        libsas
r/r 878:        scsi_transport_srp.ko.gz
r/r 879:        sd_mod.ko.gz
r/r 882:        virtio_scsi.ko.gz
r/r 883:        xen-scsifront.ko.gz
r/r 870:        libiscsi_tcp.ko.gz
r/r 873:        raid_class.ko.gz
r/r 867:        hv_storvsc.ko.gz
r/r 868:        iscsi_tcp.ko.gz
r/r 1066:       nls_iso8859-1.ko.gz
r/r 1072:       nls_iso8859-4.ko.gz
r/r 1073:       nls_iso8859-5.ko.gz
r/r 1081:       nls_utf8.ko.gz
r/r 1035:       mac-greek.ko.gz
r/r 1044:       nls_cp1255.ko.gz
r/r 1045:       nls_cp437.ko.gz
r/r 1058:       nls_cp866.ko.gz
r/r 1051:       nls_cp857.ko.gz
r/r 1054:       nls_cp862.ko.gz
r/r 1456:       xt_dccp.ko.gz
r/r 1429:       xt_HL.ko.gz
r/r 1388:       nf_synproxy_core.ko.gz
r/r 1420:       nft_tproxy.ko.gz
r/r 1403:       nft_fib_inet.ko.gz
r/r 1404:       nft_fib_netdev.ko.gz
r/r 1483:       xt_recent.ko.gz
r/r 1492:       xt_time.ko.gz
r/r 1379:       nf_flow_table.ko.gz
r/r 1416:       nft_redir.ko.gz
r/r 1439:       xt_SECMARK.ko.gz
r/r 1463:       xt_hl.ko.gz
r/r 1458:       xt_dscp.ko.gz
r/r 1442:       xt_TEE.ko.gz
r/r 1445:       xt_addrtype.ko.gz
r/r 1427:       xt_CT.ko.gz
r/r 1432:       xt_LOG.ko.gz
r/r 1402:       nft_fib.ko.gz
r/r 1464:       xt_ipcomp.ko.gz
r/r 1471:       xt_mark.ko.gz
r/r 1476:       xt_owner.ko.gz
d/d 65059:      a
d/d 65062:      d
d/d 65064:      g
d/d 65067:      k
d/d 65071:      l
d/d 65073:      p
d/d 65076:      r
d/d 65079:      s
d/d 65089:      t
d/d 65097:      v
d/d 65104:      x
r/r 65061:      ansi
r/r 65060:      alacritty
r/r 65063:      dumb
r/r 65066:      gnome-256color
r/r 65065:      gnome
r/r 65069:      konsole-256color
r/r 65070:      konsole-linux
r/r 65068:      konsole
r/r 65072:      linux
r/r 65075:      putty-256color
r/r 65074:      putty
r/r 65078:      rxvt-256color
r/r 65077:      rxvt
-/- 10025:      X
-/- 13337:      X
r/r 65081:      screen-256color
r/r 65082:      st-0.6
r/r 65083:      st-0.7
r/r 65084:      st-0.8
r/r 65085:      st-16color
r/r 65086:      st-256color
r/r 65087:      st-direct
r/r 65088:      sun
r/r 65080:      screen
-/- 59602:      X
-/- 35868:      X
r/r 65091:      terminology
r/r 65092:      terminology-0.6.1
r/r 65093:      terminology-1.0.0
r/r 65094:      terminology-1.8.1
r/r 65095:      tmux
r/r 65096:      tmux-256color
r/r 65090:      terminator
-/- 23267:      X
-/- 32321:      X
r/r 65099:      vt102
r/r 65100:      vt200
r/r 65100:      vt220
r/r 65101:      vt52
r/r 65102:      vte
r/r 65103:      vte-256color
r/r 65098:      vt100
r/r 65106:      xterm-256color
r/r 65107:      xterm-color
r/r 65108:      xterm-xfree86
r/r 65105:      xterm
-/- 55373:
r/r 65110:      ssh_config
d/d 65113:      sshd_config.d
d/d 65111:      ssh_config.d
r/r 65109:      moduli
-/l 187:
r/r 1644:       sftp-server
r/r 1646:       ssh-pkcs11-helper
-/- 64533:      dY
l/l 181:        unxz
l/l 166:        tr
l/l 182:        unzip
l/l 164:        timeout
l/l 55: clear
l/l 175:        uniq
l/l 85: hd
l/l 160:        tail
r/r 1629:       ssh-keygen
r/r 1638:       ssh-agent
r/r 1635:       scp
l/l 139:        reset
l/l 58: cpio
l/l 88: hostid
r/r 398:        getent
l/l 198:        yes
l/l 42: basename
r/r 1654:       mcheck
l/l 1661:       mformat
l/l 1664:       mlabel
l/l 1675:       mtype
l/l 185:        uuencode
r/r 1641:       ssh-pkcs11-helper
l/l 115:        nohup
l/l 157:        strings
l/l 123:        passwd
l/l 191:        which
l/l 36: [[
l/l 169:        tree
l/l 121:        openvt
l/l 162:        test
l/l 189:        wc
r/r 1676:       mxtar
l/l 1677:       mzip
r/r 1682:       isohybrid.pl
r/r 1686:       memdiskfind
r/r 1688:       ppmtolss16
r/r 1690:       sha1pass
r/r 1680:       gethostip
l/l 1650:       mattrib
-/- 7513:       @
syse@
-/- 14434:      @
syse@
-/r 65105:      @
syse@
l/l 183:        uptime
l/l 63: dc
r/r 444:        lddtree
r/r 396:        scanelf
l/l 196:        xxd
l/l 69: dos2unix
l/l 1672:       mshowfat
l/l 1674:       mtoolstest
l/l 167:        traceroute
l/l 152:        showkey
l/l 176:        unix2dos
l/l 155:        sort
l/l 105:        mesg
l/l 53: chvt
r/r 1640:       ssh-keyscan
l/l 35: [
l/l 188:        volname
l/l 84: groups
l/l 128:        printf
-/- 27116:
r/r 1703:       libgpl.c32
r/r 1702:       com32.ld
r/r 1713:       geodspms.img.xz
r/r 1714:       handoff.bin
r/r 1712:       geodsp1s.img.xz
-/- 18656:
r/r 1716:       disk.c32
r/r 1775:       gpxecmd.c32
r/r 1789:       isolinux-debug.bin
r/r 1791:       kbdmap.c32
r/r 1796:       libgpl.c32
r/r 1814:       poweroff.c32
r/r 1818:       pxelinux.0
r/r 1820:       rosh.c32
r/r 1821:       sanboot.c32
r/r 1832:       whichsys.c32
r/r 1694:       altmbr.bin
r/r 1706:       cpu.c32
r/r * 1814(realloc):    .apk.cf1166da1df18223641aafae9f8634aff02eeec2fb7466fe
r/r * 1818(realloc):    .apk.4ef6dd4b66fa957ccc972d298e7edb3336b1d91671535315
r/r 1778:       host.c32
r/r 1783:       isohdpfx.bin
r/r 1793:       ldlinux.c32
r/r 1708:       cpuidtest.c32
r/r 1794:       lfs.c32
r/r 1802:       ls.c32
r/r 1705:       cptime.c32
r/r 1806:       mbr_c.bin
r/r 1809:       meminfo.c32
r/r 1819:       reboot.c32
d/d 1723:       efi64
r/r 1721:       eltorito.sys
r/r 1722:       mdiskchk.com
r/r 1720:       copybs.com
-/- 24539:
r/r 1727:       cmenu.c32
r/r 1730:       cpu.c32
r/r 1733:       debug.c32
r/r 1744:       ldlinux.e64
r/r 1747:       libgpl.c32
r/r 1760:       rosh.c32
r/r 1767:       whichsys.c32
r/r 1743:       ifcpu64.c32
r/r * 1753(realloc):    .apk.95fbca37b8524e6f6194783868879ce72c2983f7b4cb452b
r/r * 1755(realloc):    .apk.3103a9f17c314844e953b96ce665554d950418d45c8de9c0
r/r * 1758(realloc):    .apk.31c419e3dceaf9eb2a34e36cf3350927095a721bdcbc4e51
r/r * 1761(realloc):    .apk.cb0df11e1e2b3d629fbb3adada0cea3e2e5b1b8fb8f6ddbf
r/r 1734:       dhcp.c32
r/r 1735:       dir.c32
r/r 1736:       dmi.c32
r/r 1737:       dmitest.c32
r/r 1738:       gfxboot.c32
r/r 1753:       lua.c32
r/r 1754:       mboot.c32
r/r 1757:       pci.c32
r/r 1725:       chain.c32
r/r * 1756(realloc):    .apk.d0cf2e4b0e73f11e9cba3490658296a1d13673cc9529f8c2
r/r * 1759(realloc):    .apk.7655b67c66d5eebd53e95a50e6d4c882eec8e67996c313bf
r/r * 1764(realloc):    .apk.295b3f9a175dadaef1cc02b5ee3b358f3055615772ec2fd2
-/- 10704:
r/r 1745:       lfs.c32
r/r 1748:       liblua.c32
r/r 1749:       libmenu.c32
r/r 1740:       hexdump.c32
r/r 1741:       host.c32
r/r 1759:       reboot.c32
r/r 1765:       vesamenu.c32
r/r 1732:       cpuidtest.c32
r/r 1724:       cat.c32
r/r 1729:       cptime.c32
-/- 11456:
r/r 1739:       hdt.c32
r/r 1750:       libutil.c32
r/r 1751:       linux.c32
r/r 1752:       ls.c32
r/r 1755:       meminfo.c32
r/r 1728:       config.c32
r/r 1731:       cpuid.c32
r/r 1742:       ifcpu.c32
r/r 1766:       vpdtest.c32
r/r 1768:       zzjson.c32
r/r 1756:       menu.c32
r/r 1758:       pwd.c32
r/r 1761:       sysdump.c32
r/r 1746:       libcom32.c32
r/r 1762:       syslinux.c32
r/r 1763:       syslinux.efi
r/r 1764:       vesa.c32
r/r 1726:       cmd.c32
-/- 49981:
-/- 59455:
r/r 1710:       dhcp.c32
r/r 1715:       dir.c32
r/r 1717:       dmi.c32
r/r 1781:       ifmemdsk.c32
r/r 1785:       isohdpfx_f.bin
r/r 1803:       lua.c32
r/r 1811:       pci.c32
r/r 1817:       pxechn.c32
d/d 1701:       com32
d/d 1719:       dosutil
r/r 1695:       altmbr_c.bin
r/r * 1793(realloc):    .apk.363b6b6e589207a93188b85061761eea2b7d1090f3032dc7
-/- 28399:
-/- 21455:
r/r 1776:       hdt.c32
r/r 1792:       kontron_wdt.c32
r/r 1800:       linux.c32
r/r 1813:       pmload.c32
r/r 1826:       syslinux.exe
r/r 1827:       syslinux64.exe
r/r 1829:       vesainfo.c32
-/- 34018:
r/r 1697:       cat.c32
r/r 1698:       chain.c32
r/r 1718:       dmitest.c32
r/r 1777:       hexdump.c32
r/r 1782:       ifplop.c32
r/r 1784:       isohdpfx_c.bin
r/r 1797:       liblua.c32
r/r 1798:       libmenu.c32
r/r 1804:       mboot.c32
r/r 1815:       prdhcp.c32
r/r 1825:       syslinux.com
r/r 1830:       vesamenu.c32
r/r 1771:       gfxboot.c32
r/r 1801:       lpxelinux.0
r/r 1808:       memdisk
r/r 1810:       menu.c32
r/r 1779:       ifcpu.c32
r/r 1786:       isohdppx.bin
r/r 1795:       libcom32.c32
r/r 1772:       gptmbr.bin
r/r 1773:       gptmbr_c.bin
r/r 1812:       pcitest.c32
r/r 1816:       pwd.c32
r/r 1822:       sdi.c32
r/r 1823:       sysdump.c32
r/r 1824:       syslinux.c32
r/r 1828:       vesa.c32
r/r 1831:       vpdtest.c32
r/r 1833:       zzjson.c32
r/r 1696:       altmbr_f.bin
r/r 1699:       cmd.c32
r/r 1704:       config.c32
r/r 1707:       cpuid.c32
r/r 1769:       elf.c32
s/r 1740:
-/- 36176:
-/- 47770:
-/- 10435:
-/- 47062:
r/r 1700:       cmenu.c32
r/r 1709:       debug.c32
r/r 1770:       ethersel.c32
r/r 1799:       libutil.c32
r/r 1805:       mbr.bin
r/r 1807:       mbr_f.bin
r/r 1774:       gptmbr_f.bin
r/r 1780:       ifcpu64.c32
r/r 1787:       isohdppx_c.bin
r/r 1788:       isohdppx_f.bin
r/r 1790:       isolinux.bin
d/d 1711:       diag
l/- 43112:
l/r 800:
r/r 1617:       modules.builtin.alias.bin
r/r 1625:       modules.builtin.bin
r/r 1616:       modules.devname
r/r 1624:       modules.symbols.bin
r/r 1834:       initramfs-suffix
-/- 57634:
-/- 42156:
r/r 1621:       syslinux-6.04_pre1-r15.trigger
-/r 556:
-/- 57965:
pyse
-/- 56307:
Vtysed
-/- 37884:
Vtysed
-/- 21980:
-/- 7503:       ^/
-/- 4689:
-/- 59473:      4
-/- 5847:
-/- 9095:
-/- 61433:
-/- 57524:
-/- 45151:
-/- 60444:
-/- 25344:
^^pyse
-/- 56212:
uyse
-/- 46011:
-/r 466:
^tc.
-/- 40901:
uyse
-/- 9950:
-/- 29559:
^^,uyse
-/- 22859:
)uyse
-/- 62103:
-/- 59156:
-/- 21120:
uyse
-/- 2337:
-/- 29277:
-/- 53439:
-/- 56457:
-/- 50221:
-/- 25318:
P^uyse\t^^
-/- 25279:
P^uyse\t^^
-/- 47329:
-/- 58611:
uyse
-/- 35941:
uyse
-/- 7312:
-/- 54457:
-/- 16624:
-/- 18064:
-/- 9509:
-/- 8392:
-/- 52844:
-/- 24875:
-/- 56235:
-/- 58452:
-/- 9155:
-/d 660:
-/- 34854:
-/- 31288:
s/- 39968:
-/- 19743:
-/- 52419:
-/- 29177:
-/- 62508:
-/- 3489:
-/- 45250:
-/- 42040:
-/- 31955:
-/- 42777:
-/- 29559:
-/- 54034:
-/- 33922:
-/- 30220:
-/- 59526:
-/- 29391:
-/- 61092:
-/- 52155:
-/- 41749:
-/- 60757:
-/- 54947:
-/- 34151:
-/- 18601:
-/- 38694:
-/- 5364:
-/- 65502:
-/- 30055:
-/- 37952:
-/- 27632:
-/- 24591:
-/- 59830:
-/- 26865:
-/- 46541:
-/- 62990:
-/- 18385:
-/- 56164:      X
-/- 60640:      X
-/- 7014:       X
-/r 330:        X
-/- 41477:      X
-/- 7691:
-/- 58144:
-/- 5634:
-/- 44675:
-/- 20417:      @
-/- 4587:
-/- 29229:
-/- 22938:
-/- 18449:
-/- 64646:
-/- 8290:
-/- 10246:
-/- 48854:
-/- 43916:
-/- 14806:
-/- 12654:
-/r 1558:
-/- 34921:
-/- 12061:
r/r 65115:      world
r/r 1621:       installed
r/r 17: scripts.tar
r/r 1836:       triggers
-/- 40270:
-/- 33261:
-/- * 56496:    ^|
-/- 36324:
d/d 32530:      swap
-/- 44367:      @
-/- 46545:      ^|
-/- 50367:
-/- 48428:
L-pyse
-/- 6545:
/pyse
r/r 32550:      wtmp
r/r 32629:      dmesg
-/- 60774:
-/- 52057:
r/r 64784:      resolv.conf
r/r 32631:      seed.no-credit
d/d 32630:      seedrng
r/r 32631:      seed.credit
-/- 43563:      ^|
r/r 32632:      messages
r/r 32633:      acpid.log
-/- 15239:
-/- 45284:
-/- 54056:      ^/
-/- 15882:
-/- 52167:
-/- 50246:
r/r 1837:       .ash_history
-/- 23032:
r/r 32634:      chrony.drift
-/- 57528:
-/- 37943:
r/r 1839:       depconfig
r/r 1840:       deptree
r/r 1841:       softlevel
-/- 12845:      X8
pyse|
d/d 1838:       cache
-/- 48055:
-/- 4295:
-/- 17302:      \
-/r 1149:       pyse^~qe
-/- 33261:
-/r 633:        pyse^~qe
-/- 59213:      @
Gpyse@
-/- 56279:
/pys
-/- 43820:
-/- 61744:      ^|
-/- 16406:      @
-/- 22416:      pyse^~qe
-/r 32:
r/r 32610:      seed.no-credit
r/r 32610:      seed.credit
-/r 292:        qyse
-/l 20: oyseoyse
-/r 18: qyse
-/r 1226:       oyse
-/r 17: oyseoyse
-/l 114:        oyse
-/- * 38824:    pyse^~qe
-/r 1024:       oyseoyse
-/d 16: oyseoyse
-/d * 21(realloc):      oyseoyse
-/- 56328:
-/r 12: pysepyse
-/r 879:        qyseA^pe
-/l 129:        qyseA^pe
-/- 108328:     qyse6
-/d 16: qyseqyse
-/l 20: qyseqyse
-/d 11: qyseqyse
-/- * 100208:   qyseX^;e
-/r 17: qyseqyse
-/- * 67448:    qyse%
-/l 42:
-/d 204:        qyse
-/l 54: qyse
-/r 1024:       sysesyse
l/- 59795:
-/- 2602:       oyse+yse
-/- * 0:        oyse
-/l 411:        oyse+yse
-/- 50788:      4
-/l 54: pysex
-/- 38950:
d/d 1842:       secret-secrets
-/- 38975:
r/r 1843:       force-wait.sh
r/r 1844:       innocuous-file.txt
-/- * 0:
r/r 1845:       original-filename
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

