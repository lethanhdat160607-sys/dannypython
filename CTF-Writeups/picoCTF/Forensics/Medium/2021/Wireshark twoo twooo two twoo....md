# 🚩Wireshark twoo twooo two twoo... - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `shark2.pcapng`
- **Key Skills And Tools:**  wireshark, tshark, 
---

## 🔍 Challenge 


Can you find the flag?
shark2.pcapng

### 🧪 Logic Extraction:


<div align="center"> 
  <img width="1361" height="575" alt="image" src="https://github.com/user-attachments/assets/98c29adb-0192-4c38-b301-4b0023db066c" />
</div>
#

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -nr shark2.pcapng -Y 'dns'
```

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' 
```

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response
```

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local
```

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk '{print $12}'
```

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk  '{print $12}' | sed  's/\..*//' 
```

```
┌──(kali㉿kali)-[~/Tools]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk  '{print $12}' | sed  's/\..*//' | base64 -d
picoCTF{dns_3xf1l_ftw_deadbeef}}
```
## Run 
.flag picoCTF{dns_3xf1l_ftw_deadbeef}}                                                                                                                                                           
