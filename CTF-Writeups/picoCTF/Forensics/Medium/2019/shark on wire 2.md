# 🚩shark on wire 2 - picoCTF 2019

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `pico_img.png`
- **Key Skills And Tools:** wireshark, tshark, 
---

## 🔍 Challenge 

We found this packet capture. Recover the flag.


### 🧪 Logic Extraction:

I opened the `pcap` file using the `Wireshark` command, started filtering the `udp` and `tcp` protocols, viewed the streams and searched within the packet contents (as I did in “shark on wire 1”) and I read the ports, but checking only showed `udp.port == 22` had data.

<div align="center">
   <img width="1306" height="694" alt="image" src="https://github.com/user-attachments/assets/cd0fbcf6-66f4-4d27-a335-9bf1f128df62" />
</div>

#
The tshark command structure typically follows this pattern: `[Action]` + `[Source File]` + `[Output Format]` + `[Filter]`.

tshark: Calls the TShark program (the command-line version of Wireshark).

-r ./capture.pcap:

-r stands for Read.

./capture.pcap is the path to the file you need to analyze in the current directory.

-t fields:

Instructs TShark to display the results in specific data fields, instead of printing the entire cumbersome packet content.

-e udp.srcport:

-e stands for Extract.

udp.srcport specifies that you only want to retrieve the Source Port value. These are the numbers (like 5112, 5105...) that you would use to subtract 5000 and convert to ASCII code.

-Y "udp.dstport == 22":

-Y is the Display Filter.

The quotation marks surrounding the condition indicate: Only packets with Destination Port 22 should be retrieved.
```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -r ./capture.pcap -T fields -e udp.srcport -Y "udp.dstport == 22"
5000
5112
5105
5099
5111
5067
5084
5070
5123
5112
5049
5076
5076
5102
5051
5114
5051
5100
5095
5100
5097
5116
5097
5095
5118
5049
5097
5095
5115
5116
5051
5103
5048
5125
5000
```
#

<div align="center"> 
   <img width="856" height="423" alt="image" src="https://github.com/user-attachments/assets/f813ddf4-2de8-4896-8b88-96cbf6aa0948" />

</div>

## Run 
.flag picoCTF{p1LLf3r3d_data_v1a_st3g0}
