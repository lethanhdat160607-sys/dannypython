# 🚩Milkslap - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `concat_v.png`
- **Key Skills And Tools:** python3, zsteg, bash,
---

## 🔍 Challenge 

🥛
http://wily-courier.picoctf.net:59045/


### 🧪 Logic Extraction:

I use the `zsteg` command to extract hidden data (steganography) from PNG and BMP image files. It's used for LSB analysis, checking the least significant bits in the color channels (Red, Green, Blue, Alpha), and for testing bit reading by row or column, scanning for unusual data areas, and searching for filename signatures.

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ zsteg concat_v.png

/var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:369:in `prev_scanline_byte': stack level too deep (SystemStackError)
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:319:in `block in decoded_bytes'
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:318:in `upto'
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:318:in `decoded_bytes'
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line/mixins.rb:17:in `prev_scanline_byte'
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:377:in `prev_scanline_byte'
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:319:in `block in decoded_bytes'
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:318:in `upto'
        from /var/lib/gems/3.3.0/gems/zpng-0.4.6/lib/zpng/scan_line.rb:318:in `decoded_bytes'
         ... 10225 levels...
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.14/lib/zsteg.rb:26:in `run'
        from /var/lib/gems/3.3.0/gems/zsteg-0.2.14/bin/zsteg:8:in `<top (required)>'
        from /usr/local/bin/zsteg:25:in `load'
        from /usr/local/bin/zsteg:25:in `<main>'
```


# Code Python

Simply put, this code helps us crop a large image into a smaller one for analysis, and it also overlays and hides other images, making the data clearer.

```
#usage:
# need to place in one directory with *.png
# chmod +x cut_frames.py
# python3 cut_frames.py
from PIL import Image
 
def extract_frames():
    print('Start frame extraction')
 
    img = Image.open('concat_v.png')
    print(f'Sprite sheet size (pix): {img.size}')
 
    frame_height = 720
    frame_width = 1280
 
    for i in range(66): #0-65
        frame_num = i + 1
 
        y_start = i * frame_height
        y_end = y_start + frame_height
 
        print(f'==Extracting frame {frame_num} (y: {y_start}-{y_end})==')
 
        # Cutting the frame (left, top, right, bottom)
        frame = img.crop((0, y_start, frame_width, y_end))
 
        frame_name = f"frame_{frame_num}.png"
        frame.save(frame_name)
        print(f'==Saved frame {frame_num}.png==')
 
    print('Extraction completed')
 
if __name__ == "__main__":
    extract_frames()
```

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ python3 solve.py                      
Start frame extraction
Sprite sheet size (pix): (1280, 47520)
==Extracting frame 1 (y: 0-720)==
==Saved frame 1.png==
==Extracting frame 2 (y: 720-1440)==
==Saved frame 2.png==
==Extracting frame 3 (y: 1440-2160)==
==Saved frame 3.png==
==Extracting frame 4 (y: 2160-2880)==
==Saved frame 4.png==
==Extracting frame 5 (y: 2880-3600)==
==Saved frame 5.png==
==Extracting frame 6 (y: 3600-4320)==
==Saved frame 6.png==
==Extracting frame 7 (y: 4320-5040)==
==Saved frame 7.png==
==Extracting frame 8 (y: 5040-5760)==
==Saved frame 8.png==
==Extracting frame 9 (y: 5760-6480)==
==Saved frame 9.png==
==Extracting frame 10 (y: 6480-7200)==
==Saved frame 10.png==
==Extracting frame 11 (y: 7200-7920)==
==Saved frame 11.png==
==Extracting frame 12 (y: 7920-8640)==
==Saved frame 12.png==
==Extracting frame 13 (y: 8640-9360)==
==Saved frame 13.png==
==Extracting frame 14 (y: 9360-10080)==
==Saved frame 14.png==
==Extracting frame 15 (y: 10080-10800)==
==Saved frame 15.png==
==Extracting frame 16 (y: 10800-11520)==
==Saved frame 16.png==
==Extracting frame 17 (y: 11520-12240)==
==Saved frame 17.png==
==Extracting frame 18 (y: 12240-12960)==
==Saved frame 18.png==
==Extracting frame 19 (y: 12960-13680)==
==Saved frame 19.png==
==Extracting frame 20 (y: 13680-14400)==
==Saved frame 20.png==
==Extracting frame 21 (y: 14400-15120)==
==Saved frame 21.png==
==Extracting frame 22 (y: 15120-15840)==
==Saved frame 22.png==
==Extracting frame 23 (y: 15840-16560)==
==Saved frame 23.png==
==Extracting frame 24 (y: 16560-17280)==
==Saved frame 24.png==
==Extracting frame 25 (y: 17280-18000)==
==Saved frame 25.png==
==Extracting frame 26 (y: 18000-18720)==
==Saved frame 26.png==
==Extracting frame 27 (y: 18720-19440)==
==Saved frame 27.png==
==Extracting frame 28 (y: 19440-20160)==
==Saved frame 28.png==
==Extracting frame 29 (y: 20160-20880)==
==Saved frame 29.png==
==Extracting frame 30 (y: 20880-21600)==
==Saved frame 30.png==
==Extracting frame 31 (y: 21600-22320)==
==Saved frame 31.png==
==Extracting frame 32 (y: 22320-23040)==
==Saved frame 32.png==
==Extracting frame 33 (y: 23040-23760)==
==Saved frame 33.png==
==Extracting frame 34 (y: 23760-24480)==
==Saved frame 34.png==
==Extracting frame 35 (y: 24480-25200)==
==Saved frame 35.png==
==Extracting frame 36 (y: 25200-25920)==
==Saved frame 36.png==
==Extracting frame 37 (y: 25920-26640)==
==Saved frame 37.png==
==Extracting frame 38 (y: 26640-27360)==
==Saved frame 38.png==
==Extracting frame 39 (y: 27360-28080)==
==Saved frame 39.png==
==Extracting frame 40 (y: 28080-28800)==
==Saved frame 40.png==
==Extracting frame 41 (y: 28800-29520)==
==Saved frame 41.png==
==Extracting frame 42 (y: 29520-30240)==
==Saved frame 42.png==
==Extracting frame 43 (y: 30240-30960)==
==Saved frame 43.png==
==Extracting frame 44 (y: 30960-31680)==
==Saved frame 44.png==
==Extracting frame 45 (y: 31680-32400)==
==Saved frame 45.png==
==Extracting frame 46 (y: 32400-33120)==
==Saved frame 46.png==
==Extracting frame 47 (y: 33120-33840)==
==Saved frame 47.png==
==Extracting frame 48 (y: 33840-34560)==
==Saved frame 48.png==
==Extracting frame 49 (y: 34560-35280)==
==Saved frame 49.png==
==Extracting frame 50 (y: 35280-36000)==
==Saved frame 50.png==
==Extracting frame 51 (y: 36000-36720)==
==Saved frame 51.png==
==Extracting frame 52 (y: 36720-37440)==
==Saved frame 52.png==
==Extracting frame 53 (y: 37440-38160)==
==Saved frame 53.png==
==Extracting frame 54 (y: 38160-38880)==
==Saved frame 54.png==
==Extracting frame 55 (y: 38880-39600)==
==Saved frame 55.png==
==Extracting frame 56 (y: 39600-40320)==
==Saved frame 56.png==
==Extracting frame 57 (y: 40320-41040)==
==Saved frame 57.png==
==Extracting frame 58 (y: 41040-41760)==
==Saved frame 58.png==
==Extracting frame 59 (y: 41760-42480)==
==Saved frame 59.png==
==Extracting frame 60 (y: 42480-43200)==
==Saved frame 60.png==
==Extracting frame 61 (y: 43200-43920)==
==Saved frame 61.png==
==Extracting frame 62 (y: 43920-44640)==
==Saved frame 62.png==
==Extracting frame 63 (y: 44640-45360)==
==Saved frame 63.png==
==Extracting frame 64 (y: 45360-46080)==
==Saved frame 64.png==
==Extracting frame 65 (y: 46080-46800)==
==Saved frame 65.png==
==Extracting frame 66 (y: 46800-47520)==
==Saved frame 66.png==
Extraction completed
                                                                                                                                                           
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ ls
concat_v.png  frame_16.png  frame_22.png  frame_29.png  frame_35.png  frame_41.png  frame_48.png  frame_54.png  frame_60.png  frame_6.png
frame_10.png  frame_17.png  frame_23.png  frame_2.png   frame_36.png  frame_42.png  frame_49.png  frame_55.png  frame_61.png  frame_7.png
frame_11.png  frame_18.png  frame_24.png  frame_30.png  frame_37.png  frame_43.png  frame_4.png   frame_56.png  frame_62.png  frame_8.png
frame_12.png  frame_19.png  frame_25.png  frame_31.png  frame_38.png  frame_44.png  frame_50.png  frame_57.png  frame_63.png  frame_9.png
frame_13.png  frame_1.png   frame_26.png  frame_32.png  frame_39.png  frame_45.png  frame_51.png  frame_58.png  frame_64.png  solve.py
frame_14.png  frame_20.png  frame_27.png  frame_33.png  frame_3.png   frame_46.png  frame_52.png  frame_59.png  frame_65.png  zteg_to_each_frame.sh
frame_15.png  frame_21.png  frame_28.png  frame_34.png  frame_40.png  frame_47.png  frame_53.png  frame_5.png   frame_66.png

```


# Code Bash

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ chmod +x zteg_to_each_frame.sh 
```

```
#!/bin/bash
 
echo "==zsteg scan=="
 
for frame in frame_*.png; do 
  if zsteg $frame 2>/dev/null | grep -iE "pico|ctf|flag"; then
  	echo "FOUND FLAG"
  	zsteg $frame 2>/dev/null | grep -iE "pico|ctf|flag"
  else
  	echo "NOTHING YET"
  fi
done
```

```
┌──(kali㉿kali)-[~/Tools/CTF]
└─$ ./zteg_to_each_frame.sh
==zsteg scan==
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"
FOUND FLAG
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
NOTHING YET
```
## Run 
.flag picoCTF{imag3_m4n1pul4t10n_sl4p5}
