# 🚩Riddle Registry - picoMini by CMU-Afirca 

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `confidential.pdf`
- **Key Skills And Tools:** base64, exiftool, pdf, reading images and extracting data.
----

## 🔍 Challenge 

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.
Find the PDF file here Hidden Confidential Document and uncover the flag within the metadata.


### 🧪 Logic Extraction:

To test this, I realized it was a PDF file. I used the `xxd` command to check if the file was actually a PDF or if it was a different file converted to PDF. It turned out to be a PDF because the first few bytes were `25 50 44 46`In the ASCII character set, these hexadecimal values ​​correspond to: `25 = %, 50 = P, 44 = D, 46 = F`

<div align="center">
  <img width="704" height="358" alt="image" src="https://github.com/user-attachments/assets/ae3edee2-8b3f-40d4-827c-e793e54699f5" />

</div> 

#
Next, I used the `exiftool` command to extract the data and found a piece of code with signs of `base64`, which I changed to get the flag.

<div align="center"> 

  <img width="809" height="287" alt="image" src="https://github.com/user-attachments/assets/5f2aa5c5-af25-48b2-bf4d-b2743d351e53" />

</div> 

## Run 
.flag picoCTF{puzzl3d_m3tadata_f0und!_c8f91d68}
