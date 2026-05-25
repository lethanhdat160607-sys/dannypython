# 🚩Blast from the past - picoCTF 2024

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `trace.pcap`
- **Key Skills And Tools:** strings, reading data
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



## Run 
.flag picoCTF{P64P_4N4L7S1S_SU55355FUL_31010c46}

