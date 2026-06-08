# 🚩Blast from the past - picoCTF 2024

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `original.jpg`
- **Key Skills And Tools:** exiftool, ghex, reading data
---

## 🔍 Challenge 

The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?

Set the timestamps on this picture to 1970:01:01 00:00:00.001+00:00 with as much precision as possible for each timestamp. In this example, +00:00 is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: 1969:12:31 19:00:00.001-05:00. For timestamps without a timezone adjustment, put them in GMT time (+00:00). The checker program provides the timestamp needed for each.

Use this picture.

Submit your modified picture here:

`nc -w 2 mimas.picoctf.net 55901 < original_modified.jpg`

Check your modified picture here:

`nc mimas.picoctf.net 49425`

### 🧪 Logic Extraction:

I used the `exiftool` command to probe the file.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ exiftool original.jpg

ExifTool Version Number         : 13.50
File Name                       : original.jpg
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2024:03:13 13:44:58-04:00
File Access Date/Time           : 2026:06:03 09:24:44-04:00
File Inode Change Date/Time     : 2026:06:03 09:24:44-04:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Little-endian (Intel, II)
Image Description               : 
Make                            : samsung
Camera Model Name               : SM-A326U
Orientation                     : Rotate 90 CW
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : MediaTek Camera Application
Modify Date                     : 2023:11:20 15:46:23
Y Cb Cr Positioning             : Co-sited
Exposure Time                   : 1/24
F Number                        : 1.8
Exposure Program                : Program AE
ISO                             : 500
Sensitivity Type                : Unknown
Recommended Exposure Index      : 0
Exif Version                    : 0220
Date/Time Original              : 2023:11:20 15:46:23
Create Date                     : 2023:11:20 15:46:23
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/24
Aperture Value                  : 1.9
Brightness Value                : 3
Exposure Compensation           : 0
Max Aperture Value              : 1.8
Metering Mode                   : Center-weighted average
Light Source                    : Other
Flash                           : On, Fired
Focal Length                    : 4.6 mm
Sub Sec Time                    : 703
Sub Sec Time Original           : 703
Sub Sec Time Digitized          : 703
Flashpix Version                : 0100
Color Space                     : sRGB
Exif Image Width                : 4000
Exif Image Height               : 3000
Interoperability Index          : R98 - DCF basic file (sRGB)
Interoperability Version        : 0100
Exposure Mode                   : Auto
White Balance                   : Auto
Digital Zoom Ratio              : 1
Focal Length In 35mm Format     : 25 mm
Scene Capture Type              : Standard
Compression                     : JPEG (old-style)
Thumbnail Offset                : 1408
Thumbnail Length                : 64000
Image Width                     : 4000
Image Height                    : 3000
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Time Stamp                      : 2023:11:20 15:46:21.420-05:00
MCC Data                        : United States / Guam (310)
Aperture                        : 1.8
Image Size                      : 4000x3000
Megapixels                      : 12.0
Scale Factor To 35 mm Equivalent: 5.4
Shutter Speed                   : 1/24
Create Date                     : 2023:11:20 15:46:23.703
Date/Time Original              : 2023:11:20 15:46:23.703
Modify Date                     : 2023:11:20 15:46:23.703
Thumbnail Image                 : (Binary data 64000 bytes, use -b option to extract)
Circle Of Confusion             : 0.006 mm
Field Of View                   : 71.5 deg
Focal Length 35mm Equiv         : 4.6 mm (35 mm equivalent: 25.0 mm)
Hyperfocal Distance             : 2.13 m
Light Value                     : 4.0

```
Change the date.

 - `-AllDates=1970:01:01 00:00:00.001`: This is a shortcut in the `exiftool` command that automatically finds and modifies the three most important timestamps of an image simultaneously: `DateTimeOriginal`, `CreateDate`, and `ModifyDate`.

 - `-DateTimeOriginal=1970:01:01 00:00:00.001`: Specifies the time the capture button was pressed to ensure that the data on this card is overwritten correctly.

 - `-CreateDate=1970:01:01 00:00:00.001`: Is the time the image was captured and recorded as a digital data file in memory.

Convert to fractions of a second.

- `-SubSecTimeOriginal=001`: Adds 001 milliseconds to the time the shutter button is pressed.

- `-SubSecTimeDigitized=001`: Adds 001 milliseconds to the time the file is created.

- `-SubSecTime=001`: Adds 001 milliseconds to the time the file is edited.

Set time zone

- `-OffsetTime=+00:00`: Specifies the time zone for the above time as GMT/UTC (time zone 0). This helps the scoring system accurately identify this time as the standard international time, avoiding time discrepancies when transferred to computers in other countries.

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$  exiftool "-AllDates=1970:01:01 00:00:00.001" "-DateTimeOriginal=1970:01:01 00:00:00.001" "-CreateDate=1970:01:01 00:00:00.001" "-ModifyDate=1970:01:01 00:00:00.001" "-OffsetTime=+00:00" "-SubSecTimeOriginal=001" "-SubSecTimeDigitized=001" "-SubSecTime=001" original.jpg
    1 image files updated

```

Image_UTC_Data0000000000001

<div align="center">
 <img width="1350" height="588" alt="image" src="https://github.com/user-attachments/assets/ab15551a-4a50-4f5a-b317-609d67535b4c" />

</div>

#

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ nc -w 2 mimas.picoctf.net 64125 < original.jpg
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ nc mimas.picoctf.net 56060                    


MD5 of your picture:
6bc3fc93ab60e34d0284e37ee2066f2c  test.out

Checking tag 1/7
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 2/7
Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 3/7
Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 4/7
Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 5/7
Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 6/7
Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 1970:01:01 00:00:00.001+00:00
Great job, you got that one!

You did it!
picoCTF{71m3_7r4v311ng_p1c7ur3_a4f2b526}

```

## Run 
.flag picoCTF{71m3_7r4v311ng_p1c7ur3_a4f2b526}

