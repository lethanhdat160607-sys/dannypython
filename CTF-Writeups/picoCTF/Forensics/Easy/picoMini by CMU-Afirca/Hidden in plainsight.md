# 🚩Hidden in plainsight - picoMini by CMU-Afirca 

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `img.jpg`
- **Key Skills And Tools:** base64, exiftool, jpg, steghide, reading images and extracting data.
---

## 🔍 Challenge 

You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.
Download the jpg image here.

### 🧪 Logic Extraction:
This is an article about images, and I used the `exiftool` command to explore what data the images contain.

<div align="center">
    <img width="552" height="338" alt="image" src="https://github.com/user-attachments/assets/1f4376c7-0c53-4810-b9dc-c87813ef3f14" />

</div>

#
I noticed the presence of `base64` code in the image data, so I encoded it twice because the `base64` code was still present. This created some kind of cipher that might help me extract the flag from this image.

<div align="center">
    <img width="540" height="101" alt="image" src="https://github.com/user-attachments/assets/f39f3c5b-524e-4d83-be69-f1dbff2f0a4a" />

</div>

#
From the previous step, we deciphered something that could be a password, and I used the `steghide` command to extract the data. For the hidden data, we used the `extract -sf` command; this helped me extract the hidden data into the `flag.txt` file.

<div align="center"> 
    <img width="430" height="163" alt="image" src="https://github.com/user-attachments/assets/b6aaebf9-a99a-4516-b70f-e1572729897f" />

</div> 

## Run 
.flag picoCTF{h1dd3n_1n_1m4g3_92f08d7c}

