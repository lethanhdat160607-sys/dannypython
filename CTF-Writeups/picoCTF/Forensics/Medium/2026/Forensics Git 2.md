# 🚩Forensics Git 2 - picoCTF 2026

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** ``
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

The agents interrupted the perpetrator's disk deletion routine. Can you recover this git repo?

Download the disk image here.
### 🧪 Logic Extraction:


```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file disk.img                               
disk.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x2,0,33), end-CHS (0x263,8,56), startsector 2048, 614400 sectors; partition 2 : ID=0x82, start-CHS (0x263,8,57), end-CHS (0x3ff,15,63), startsector 616448, 524288 sectors; partition 3 : ID=0x83, start-CHS (0x3ff,15,63), end-CHS (0x3ff,15,63), startsector 1140736, 956416 sectors
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fdisk -l disk.img
Disk disk.img: 1 GiB, 1073741824 bytes, 2097152 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x610b63c2

Device     Boot   Start     End Sectors  Size Id Type
disk.img1  *       2048  616447  614400  300M 83 Linux
disk.img2        616448 1140735  524288  256M 82 Linux swap / Solaris
disk.img3       1140736 2097151  956416  467M 83 Linux
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ sudo mkdir -p /mnt/git2                                                               
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ sudo mount -o loop,offset=$((1140736 * 512)) disk.img /mnt/git2
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ find /mnt/git2 -name ".git" -type d 2>/dev/null
/mnt/git2/home/ctf-player/Code/killer-chat-app/.git
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ 
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ cd /mnt/git2/home/ctf-player/Code/killer-chat-app/.git
                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/ctf-player/Code/killer-chat-app/.git]
└─$ git log  --oneline 
fatal: your current branch 'master' does not have any commits yet
                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/ctf-player/Code/killer-chat-app/.git]
└─$ git status         
fatal: this operation must be run in a work tree
                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/ctf-player/Code/killer-chat-app/.git]
└─$ git status 
fatal: this operation must be run in a work tree
                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/ctf-player/Code/killer-chat-app/.git]
└─$ cd ..                                                 
                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/home/ctf-player/Code/killer-chat-app]
└─$ git status 
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   client
        new file:   logs/1.txt
        new file:   logs/2.txt
        new file:   logs/4.txt
        new file:   server

                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/home/ctf-player/Code/killer-chat-app]
└─$ ls .git/objects  
01  20  21  22  26  2c  58  5e  66  6b  71  a0  aa  c9  d4  d7  e8  ea  f1  info  pack
                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/home/ctf-player/Code/killer-chat-app]
└─$ git cat-file -batch-all-objects --batch-check
error: did you mean `--batch-all-objects` (with two dashes)?
                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/home/ctf-player/Code/killer-chat-app]
└─$ git cat-file --batch-all-objects --batch-check
01533f718556a0e59f1467dae4fa462eed82c2a1 commit 238
201c707b43219a63c1d3499b29c7d539af079861 tree 99
2151ef0ccc15aed1ab88e1afdc7484aaeff211c4 commit 244
22f7d0c9bd045563ae33bfacfbe46fe406a5b318 tree 99
26b809e0c41d8421f1126ed3a4eb06ad66e6d90a commit 242
2c0a9b2b15dce92f800393d5030c7454efc278ae commit 189
5827632e046a80a1e0d7b4fc5c7800dd539baeaf commit 239
5eb896e3ccd51175f66480cdb247fc45f3e8ac2d tree 68
66273877d2ff3f51a14473b7200aae5a798ff64f blob 140
6b1ebe10826d5c1efc58ae475c0a0af10f580b77 tree 33
6bf83de540f7d12cc3b683a83d69432e03d84509 tree 99
7178644433e7cb6da3adf028f1c80d382a18e7b6 blob 188
71fd2fafcd5ebd62fbf857769c92a91225ab3954 blob 25
a0c13fe974d95661f24e32bc0d79f54f05ea13c5 tree 99
aa1cc01687b4ec94faf9916c3fc6efd83f23b816 blob 134
c931ae0868411e5f23656a2436e78a4c4699e18c tree 99
d4666b9472fad7cd75d05b641e402347d9aac605 tree 66
d7b4a371ebd23e682ffebc7ec355690fdc94fbd1 blob 25
e80b38b3322a5ba32ac07076ef5eeb4a59449875 commit 246
ead27e2bd5a0fc22868ffb629a768f82dfcda11c tree 99
f150f0b963ab3ee95ba5656212abd76d7f2fed2e blob 142
                                                                                                                                                           

                                                                                                                                                           
┌──(kali㉿kali)-[/mnt/…/home/ctf-player/Code/killer-chat-app]
└─$ git cat-file --batch-all-objects --batch | strings | grep -i "picoCTF\|3.txt"
.100644 3.txt
Jay: Ask Rusty at the door and use password picoCTF{g17_r35cu3_16ac6bf3}.

```

## Run 
.flag 

