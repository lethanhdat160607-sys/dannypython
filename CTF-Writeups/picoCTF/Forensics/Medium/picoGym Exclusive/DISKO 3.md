# 🚩WPA-ing Out - picoGym Exclusive

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `pcap file`
- **Key Skills And Tools:** Aotupys, 

## 🔍 Challenge 

Can you find the flag in this disk image? This time, its not as plain as you think it is!

Download the disk image here.


### 🧪 Logic Extraction:
I use a tool called Autopys to open hidden files and hidden packets to view them.


<div align="center">

  <img width="842" height="315" alt="image" src="https://github.com/user-attachments/assets/45793ab6-740d-485e-a6b9-34f55f5b5270" />
  <p> Autopys open file</p>
</div>

#
Try opening the log file because most basic systems usually have many hidden files inside.
<div align="center">
  <img width="850" height="462" alt="image" src="https://github.com/user-attachments/assets/dbdb98a0-28af-4a48-8cc9-be5e87283e69" />
  <p> Autopys open file</p>
</div>

#
I found a file named `flag.gz`, so I opened it and checked it out.
<div align="center">
<img width="841" height="405" alt="image" src="https://github.com/user-attachments/assets/e9601ef1-1323-40c9-96b1-9262986bafe4" />


</div>

#
And inside there's a half-flag file, and I've already seen the flag displayed.
<div align="center">

  <img width="854" height="505" alt="image" src="https://github.com/user-attachments/assets/e8cbcdb6-3448-4caa-8e61-16bfff765a4b" />
  <p> Autopys open file</p>


</div>

#
This is a disk hiding technique I'm showing you so you can see which files are hidden here.
<div align="center">
  <img width="345" height="462" alt="image" src="https://github.com/user-attachments/assets/db9b0d0d-11c0-4e83-b0dc-dcfe581072ff" />
  <p> Autopys I opened the file and saw the flag. </p>


</div>


## Run 
.flag picoCTF{}
