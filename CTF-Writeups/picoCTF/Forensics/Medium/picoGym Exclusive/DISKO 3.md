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

#
Another way to do it is to search using the tools command in Kali Linux.
I used the `strings` command to check for any abnormalities, and I found that the picoctf file showed very unusual activity from the drive.
<div align="center">
  <img width="683" height="380" alt="image" src="https://github.com/user-attachments/assets/15ecd15e-b185-4ca7-a10f-fc3044841ba9" />

</div>

#
I used the command `fly -r -q disko-3.dd` to perform the operation. `fly` can be understood as listing partitions, similar to the `ls` command, but it lists the partitions in the disk image. `-r` lists the files in the root directory and goes deeper into the directory. `-p` displays the full path, showing not just the file name but also the root directory path. I found a file named `flag.gz`.

<div align="center">
 <img width="463" height="650" alt="image" src="https://github.com/user-attachments/assets/27afbd85-e607-4103-a1cf-8c6b4a8671c0" />

</div>
#

<div align="center">
  <img width="544" height="296" alt="image" src="https://github.com/user-attachments/assets/789c0634-114b-4d52-a09b-b429af26a52a" />

</div>

<div align="center">

</div>



## Run 
.flag ppicoCTF{n3v3r_z1p_2_h1d3_26d4f233}

