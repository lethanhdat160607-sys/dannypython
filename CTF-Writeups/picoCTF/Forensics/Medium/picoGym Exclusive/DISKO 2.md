# 🚩DISKO 2 - picoGym Exclusive

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `disko-2.dd`
- **Key Skills And Tools:** Sleuthkit, Enumeration, Identifying Misconfigurations, Identifying Misconfigurations
---

## 🔍 Challenge 
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!
Download the disk image here.

### 🧪 Logic Extraction:

I use the `mmls` command to retrieve a disk map and raw image files like `.dd` and `.img`. This helps display the partitions and how many partitions are inside (Linux, FAT32, NTFS, etc.), and is considered as sectors, slots, start, end, length, and description units.

```
┌──(kali㉿kali)-[~/Tools]
└─$ mmls disko-2.dd           
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000053247   0000051200   Linux (0x83)
003:  000:001   0000053248   0000118783   0000065536   Win95 FAT32 (0x0b)
004:  -------   0000118784   0000204799   0000086016   Unallocated

```
#
Then I used the strings command to check the file and look up keywords, but it had too many false flags.

```
┌──(kali㉿kali)-[~/Tools]
└─$ strings disko-2.dd | grep "picoCTF"

picoCTF{4_P4Rt_1t_i5_5d70d515}
picoCTF{4_P4Rt_1t_i5_17d555d0}
picoCTF{4_P4Rt_1t_i5_157d50d5}
picoCTF{4_P4Rt_1t_i5_5dd07515}
picoCTF{4_P4Rt_1t_i5_d055d175}
picoCTF{4_P4Rt_1t_i5_dd150575}
picoCTF{4_P4Rt_1t_i5_5d570d51}
picoCTF{4_P4Rt_1t_i5_55175dd0}
picoCTF{4_P4Rt_1t_i5_75505d1d}
picoCTF{4_P4Rt_1t_i5_70d1555d}
picoCTF{4_P4Rt_1t_i5_1507dd55}
picoCTF{4_P4Rt_1t_i5_05dd1755}
picoCTF{4_P4Rt_1t_i5_51705dd5}
picoCTF{4_P4Rt_1t_i5_01d755d5}
picoCTF{4_P4Rt_1t_i5_10d55d75}
picoCTF{4_P4Rt_1t_i5_d05d5751}
picoCTF{4_P4Rt_1t_i5_755015dd}
picoCTF{4_P4Rt_1t_i5_d057515d}
picoCTF{4_P4Rt_1t_i5_55517dd0}
picoCTF{4_P4Rt_1t_i5_517dd550}
picoCTF{4_P4Rt_1t_i5_7d55501d}
picoCTF{4_P4Rt_1t_i5_510d5d57}
picoCTF{4_P4Rt_1t_i5_d5057d51}
picoCTF{4_P4Rt_1t_i5_05d7d551}
picoCTF{4_P4Rt_1t_i5_5155d7d0}
picoCTF{4_P4Rt_1t_i5_055dd175}
picoCTF{4_P4Rt_1t_i5_5dd15750}se: 
Description-id.UTF-8: Tidak ada medpicoCTF{4_P4Rt_1t_i5_1d5055d7}
Description-nl.UTF-8: Uw ethernetpicoCTF{4_P4Rt_1t_i5_5710d55d}d_description-nl.UTF-8: Er is op dit systeem geen ethernetkaart gevonden.
Extended_description-pt.UTF-8: NecessitpicoCTF{4_P4Rt_1t_i5_d50d5751}
r din computer starter, vipicoCTF{4_P4Rt_1t_i5_570d5d15}l
picoCTF{4_P4Rt_1t_i5_5d01755d}
Choices-ja.UTF-8: AfghpicoCTF{4_P4Rt_1t_i5_d7055d15}Bhutan, Brunei Darussalam, Cambodia, China, Hong Kong, India, Indonesia, Iran\, Islamic Republic of, Iraq, Israel, Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Lao People's Democratic Republic, Lebanon, Macao, Malaysia, Mongolia, Myanmar, Nepal, North Korea, Oman, Pakistan, Palestine\, State of, Philippines, Qatar, Saudi Arabia, Singapore, South Korea, Sri Lanka, Syrian Arab Republic, Taiwan, Tajikistan, Thailand, Timor-Leste, Turkey, Turkmenistan, United Arab Emirates, Uzbekistan, Vietnam, Yemen
 vybrapicoCTF{4_P4Rt_1t_i5_d5501d57}.UTF-8: Dodatne krajevne nastavitve:
Extended_picoCTF{4_P4Rt_1t_i5_d5d50517}tt csatol
picoCTF{4_P4Rt_1t_i5_dd015575}ded_description-ar.UTF-8: 
Description-zh_picoCTF{4_P4Rt_1t_i5_51dd0557}
DescriptipicoCTF{4_P4Rt_1t_i5_150575dd}
picoCTF{4_P4Rt_1t_i5_51d755d0}
 picoCTF{4_P4Rt_1t_i5_5dd57015}
se vazhpicoCTF{4_P4Rt_1t_i5_10d7555d}m
picoCTF{4_P4Rt_1t_i5_5d7055d1}
DescrippicoCTF{4_P4Rt_1t_i5_d715055d}s iSCSI-Initiators f
nih nosilcev (LVMpicoCTF{4_P4Rt_1t_i5_175dd055}tion-sl.UTF-8: Trenutno jedro ne podpira Upravljalnika logi
 possibile selezipicoCTF{4_P4Rt_1t_i5_55dd0517}iption-ja.UTF-8: 
picoCTF{4_P4Rt_1t_i5_515d5d70}
 minden adat epicoCTF{4_P4Rt_1t_i5_d5d01755}rt
Description-picoCTF{4_P4Rt_1t_i5_0d5557d1}iption-ml.UTF-8: 
, picoCTF{4_P4Rt_1t_i5_5dd70155} Godthab, Danmarkshavn, Scoresbysund, Thule
Aug 30 02:00:42 in-target:  picoCTF{4_P4Rt_1t_i5_d17550d5}-perl libdrm-amdgpu1 libdrm-common
Aug 30 02:00:43 in-target:   ruby-ethon ruby-fpicoCTF{4_P4Rt_1t_i5_501557dd}ssapi ruby-gyoku
Aug picoCTF{4_P4Rt_1t_i5_1505d5d7}8 cdrom://[Kali GNU/Linux 2022.3rc2 _Kali-last-snapshot_ - Official amd64 BD Binary-1 with firmware 20220804-16:57] kali-rolling/main amd64 librttopo1 amd64 1.1.0-2 [180 kB]
Aug 30 02:0picoCTF{4_P4Rt_1t_i5_05557d1d}iously unselected package tcl8.6.^M
Aug 30 02:04:34 in-target: Preparing topicoCTF{4_P4Rt_1t_i5_5d05175d}_2.1.2-1_amd64.deb ...^M
Aug 30 02:05:10 in-target: Preparing to unpack .../1440-pythpicoCTF{4_P4Rt_1t_i5_5d150d57}Aug 30 02:05:10 in-target: Unpacking python3-fs (2.4.16-1) ...^M
Aug 29 22:14:39 kali kernel: [    0.214601] ACpicoCTF{4_P4Rt_1t_i5_75015dd5}onfigured for IRQ 11
picoCTF{4_P4Rt_1t_i5_07d5d551}
picoCTF{4_P4Rt_1t_i5_7d501d55}
picoCTF{4_P4Rt_1t_i5_5d155d70}
picoCTF{4_P4Rt_1t_i5_d50751d5}
picoCTF{4_P4Rt_1t_i5_d0755d51}
picoCTF{4_P4Rt_1t_i5_d15d0575}
picoCTF{4_P4Rt_1t_i5_57d105d5}
picoCTF{4_P4Rt_1t_i5_d15550d7}
picoCTF{4_P4Rt_1t_i5_5dd01755}
picoCTF{4_P4Rt_1t_i5_15575d0d}
picoCTF{4_P4Rt_1t_i5_d5d71055}
picoCTF{4_P4Rt_1t_i5_750d1d55}
picoCTF{4_P4Rt_1t_i5_7dd50551}
picoCTF{4_P4Rt_1t_i5_517d0d55}
picoCTF{4_P4Rt_1t_i5_50715d5d}
MESSAGE=picoCTF{4_P4Rt_1t_i5_0d75d155}o  0x0d00-0xfeff window]
picoCTF{4_P4Rt_1t_i5_075dd155}8
picoCTF{4_P4Rt_1t_i5_1d570d55}
picoCTF{4_P4Rt_1t_i5_0d5155d7}
MESSAGE=pci 0000:00:15.0:   bridge window [io  0picoCTF{4_P4Rt_1t_i5_550571dd}
picoCTF{4_P4Rt_1t_i5_7d055d15}
picoCTF{4_P4Rt_1t_i5_d051755d}
picoCTF{4_P4Rt_1t_i5_55d7510d}
picoCTF{4_P4Rt_1t_i5_505d5d71}
picoCTF{4_P4Rt_1t_i5_71055dd5}
picoCTF{4_P4Rt_1t_i5_15d7d550}
picoCTF{4_P4Rt_1t_i5_515dd705}
picoCTF{4_P4Rt_1t_i5_d5550d17}
picoCTF{4_P4Rt_1t_i5_1d5d0575}
picoCTF{4_P4Rt_1t_i5_01575d5d}
picoCTF{4_P4Rt_1t_i5_057d515d}
picoCTF{4_P4Rt_1t_i5_5157d05d}
picoCTF{4_P4Rt_1t_i5_d1557d05}
picoCTF{4_P4Rt_1t_i5_505d15d7}
picoCTF{4_P4Rt_1t_i5_d51d5750}
picoCTF{4_P4Rt_1t_i5_05d5715d}
picoCTF{4_P4Rt_1t_i5_5751d5d0}
picoCTF{4_P4Rt_1t_i5_10d575d5}
picoCTF{4_P4Rt_1t_i5_550d75d1}
picoCTF{4_P4Rt_1t_i5_d505751d}
picoCTF{4_P4Rt_1t_i5_57d10d55}
picoCTF{4_P4Rt_1t_i5_501d557d}
picoCTF{4_P4Rt_1t_i5_51d70d55}
picoCTF{4_P4Rt_1t_i5_d555017d}
picoCTF{4_P4Rt_1t_i5_05d155d7}
picoCTF{4_P4Rt_1t_i5_d5175d05}
picoCTF{4_P4Rt_1t_i5_15055d7d}
picoCTF{4_P4Rt_1t_i5_5d5107d5}
picoCTF{4_P4Rt_1t_i5_1d0d5557}
picoCTF{4_P4Rt_1t_i5_755d15d0}
picoCTF{4_P4Rt_1t_i5_01d57d55}
picoCTF{4_P4Rt_1t_i5_5170d55d}
picoCTF{4_P4Rt_1t_i5_d57d0551}
picoCTF{4_P4Rt_1t_i5_7015dd55}
picoCTF{4_P4Rt_1t_i5_d5d75501}
picoCTF{4_P4Rt_1t_i5_5d7d5015}
picoCTF{4_P4Rt_1t_i5_5d75051d}
picoCTF{4_P4Rt_1t_i5_d1575d50}
picoCTF{4_P4Rt_1t_i5_5715d5d0}
picoCTF{4_P4Rt_1t_i5_55d75d10}
picoCTF{4_P4Rt_1t_i5_5751dd50}
picoCTF{4_P4Rt_1t_i5_d5d57510}
picoCTF{4_P4Rt_1t_i5_d505d571}
picoCTF{4_P4Rt_1t_i5_d7150d55}
picoCTF{4_P4Rt_1t_i5_07d55d15}
picoCTF{4_P4Rt_1t_i5_15d50d57}
picoCTF{4_P4Rt_1t_i5_575d0d15}
picoCTF{4_P4Rt_1t_i5_d1d07555}
picoCTF{4_P4Rt_1t_i5_155d507d}
picoCTF{4_P4Rt_1t_i5_55d5d071}

```
#
`dd` is the command to copy data. `if=` is the input, and the input is the file `díko-2.dd`, which retrieves data from the image file. `of=` is the output, where the data is written. `of=LinuxPartition.img` creates a new file containing that data. `bs=` is the byte, and `skip=` simply means to drag the tape and remove the first segment. For example, `skip=2048` will remove the 2048 segment, and `count=` will only take the exact number of blocks; otherwise, it will use a false flag.
```
┌──(kali㉿kali)-[~/Tools]
└─$ dd if=disko-2.dd of=LinuxPartition.img bs=512 skip=2048 count=51200
51200+0 records in
51200+0 records out
26675200 bytes (27 MB, 25 MiB) copied, 0.807706 s, 33.0 MB/s

```
#
Then, call the newly copied file that retrieved the data, call the keyword `picoCTF`, and it produced the flag.
```
┌──(kali㉿kali)-[~/Tools]
└─$ strings LinuxPartition.img | grep "picoCTF"
picoCTF{4_P4Rt_1t_i5_055dd175}

```



## Run 
.flag picoCTF{4_P4Rt_1t_i5_055dd175}
