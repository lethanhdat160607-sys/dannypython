# Challenges

<div align="center">

  <img width="1049" height="449" alt="image" src="https://github.com/user-attachments/assets/7fabbb48-343e-4f6e-a902-dcfd9e993714" />


</div>
#

I used the `gunzip` command to extract the files.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ gunzip ch39.gz
```

I then used the `file` command to probe the file data, and it showed `POSIX tar archive (GNU)`, indicating that it was closed and contained an additional file.

```                                                                                                                               
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file ch39    
ch39: POSIX tar archive (GNU)
```
Next, I used the `tar -xvf` command to extract data from the file being packaged, and it gave us an image file.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tar -xvf ch39    
usb.image
```

I used the `file` command again to view the image file data.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file usb.image
usb.image: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, reserved sectors 4, root entries 512, sectors 63488 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 64, sectors/track 62, heads 124, hidden sectors 2048, reserved 0x1, serial number 0xc7ecde5b, label: "USB        ", FAT (16 bit)
```


```
         
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ fls usb.image    
r/r 3:  USB         (Volume Label Entry)
r/r * 5:        anonyme.png
v/v 1013699:    $MBR
v/v 1013700:    $FAT1
v/v 1013701:    $FAT2
V/V 1013702:    $OrphanFiles
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ icat usb.image 5 > flag.png
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
ch39  flag.png  usb.image

```


```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ exiftool flag.png
ExifTool Version Number         : 13.50
File Name                       : flag.png
Directory                       : .
File Size                       : 246 kB
File Modification Date/Time     : 2026:05:08 18:46:06-04:00
File Access Date/Time           : 2026:05:08 18:46:06-04:00
File Inode Change Date/Time     : 2026:05:08 18:46:06-04:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 400
Image Height                    : 300
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Gamma                           : 2.2
White Point X                   : 0.3127
White Point Y                   : 0.329
Red X                           : 0.64
Red Y                           : 0.33
Green X                         : 0.3
Green Y                         : 0.6
Blue X                          : 0.15
Blue Y                          : 0.06
Background Color                : 255 255 255
XMP Toolkit                     : Image::ExifTool 11.88
Creator                         : Javier Turcot
Image Size                      : 400x300
Megapixels                      : 0.120

```


# flag 

. key javier_turcot 
