# 🚩Event-Viewing - picoCTF 2025

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `Windows_Logs.evtx`
- **Key Skills And Tools:** strings, reading data
---

## 🔍 Challenge 

One of the employees at your company has their computer infected by malware! Turns out every time they try to switch on the computer, it shuts down right after they log in. The story given by the employee is as follows:.

1 They installed software using an installer they downloaded online.

2 They ran the installed software but it seemed to do nothing.

3 Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.

See if you can find evidence for the each of these events and retrieve the flag (split into 3 pieces) from the correct logs!
Download the Windows Log file here

### 🧪 Logic Extraction:

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ file Windows_Logs.evtx
Windows_Logs.evtx: MS Windows 10-11 Event Log, version  3.2, 99 chunks (no. 98 in use), next record no. 8620

```

<a href="https://github.com/omerbenamram/evtx/releases/download/v0.9.0/evtx_dump-v0.9.0-x86_64-unknown-linux-gnu">download tools evtx_dump</a>
```

┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ./evtx_dump Windows_Logs.evtx > output.xml
```

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ grep -i "==" output.xml
    <Data>Totally_Legit_Software,1.3.3.7,0,0,cGljb0NURntFdjNudF92aTN3djNyXw==,(NULL),</Data>
    <Data Name="ObjectValueName">Immediate Shutdown (MXNfYV9wcjN0dHlfdXMzZnVsXw==)</Data>
```
```                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ grep -i -C 5 "shutdown.exe" output.xml
    <Data Name="HandleId">0x208</Data>
    <Data Name="OperationType">%%1904</Data>
    <Data Name="OldValueType">-</Data>
    <Data Name="OldValue">-</Data>
    <Data Name="NewValueType">%%1873</Data>
    <Data Name="NewValue">C:\Program Files (x86)\Totally_Legit_Software\custom_shutdown.exe</Data>
    <Data Name="ProcessId">0x1bd0</Data>
    <Data Name="ProcessName">C:\Program Files (x86)\Totally_Legit_Software\Totally_Legit_Software.exe</Data>
  </EventData>
</Event>
Record 187
--
    <Computer>DESKTOP-EKVR84B</Computer>
    <Security UserID="S-1-5-21-3576963320-1344788273-4164204335-1001">
    </Security>
  </System>
  <EventData>
    <Data Name="param1">C:\Windows\system32\shutdown.exe (DESKTOP-EKVR84B)</Data>
    <Data Name="param2">DESKTOP-EKVR84B</Data>
    <Data Name="param3">No title for this reason could be found</Data>
    <Data Name="param4">0x800000ff</Data>
    <Data Name="param5">shutdown</Data>
    <Data Name="param6">dDAwbF84MWJhM2ZlOX0=</Data>
--
    <Computer>DESKTOP-EKVR84B</Computer>
    <Security UserID="S-1-5-21-3576963320-1344788273-4164204335-1001">
    </Security>
  </System>
  <EventData>
    <Data Name="param1">C:\Windows\system32\shutdown.exe (DESKTOP-EKVR84B)</Data>
    <Data Name="param2">DESKTOP-EKVR84B</Data>
    <Data Name="param3">No title for this reason could be found</Data>
    <Data Name="param4">0x800000ff</Data>
    <Data Name="param5">shutdown</Data>
    <Data Name="param6">dDAwbF84MWJhM2ZlOX0=</Data>

```

<div align="center">
    <img width="888" height="425" alt="image" src="https://github.com/user-attachments/assets/af320003-5273-4984-8e00-a5901e6a7c9d" />

</div>


## Run 
.flag picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}

