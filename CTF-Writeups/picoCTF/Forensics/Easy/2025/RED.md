# 🚩RED - picoGym Exclusive

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `pcap file`
- **Key Skills And Tools:** 
---

## 🔍 Challenge 

RED, RED, RED, RED  Download the image: red.png

### 🧪 Logic Extraction:

We see this is an image challenge and only that color is available, so I used `Extract LSB` in Cyberchef to convert it to pixels because the challenge says `RED, RED, RED, RED`. Usually, only 4 graphic values ​​(R, G, B, A) make up an image.

<div align="center"> 
  <img width="1049" height="526" alt="image" src="https://github.com/user-attachments/assets/954518c6-26ef-4832-8317-061650c281bd" />

</div>

#
Then I noticed signs of base64 encoding and converted it to a flag.

<div align="center"> 
  <img width="1055" height="551" alt="image" src="https://github.com/user-attachments/assets/2cafa61c-4755-4fc2-9d76-fa61e1619c38" />

</div>

#
Another method I learned from your article is that you can use the command `sudo zsteg red.png` to access the image data and download it like this: `sudo apt install ruby ​​ruby-dev`, `sudo gem install zsteg`
<div align="center"> 
  <img width="1341" height="247" alt="image" src="https://github.com/user-attachments/assets/85ef4644-82dc-4cbe-9296-9d9ccbaac305" />

</div>
#
```
┌──(kali㉿kali)-[~/Tools]
└─$ echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d 
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}                                                                                                                                                            
```

## Run 
.flag picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
