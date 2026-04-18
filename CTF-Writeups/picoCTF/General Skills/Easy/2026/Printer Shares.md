# 🚩 Printer Shares - picoCTF 2026

- **Category:**General Skills ⚙️
- **Difficulty:** Easy
- **Target File:** `nc -vz mysterious-sea.picoctf.net 51352`
- **Key Skills And Tools:** smbclient, Enumeration, Identifying Misconfigurations, Information Gathering

---

## 🔍 Challenge 

Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?
The printer is on `51352`. you can try $ `nc -vz mysterious-sea.picoctf.net 51352`

### 🧪 Logic Extraction:

We connect to the server and list the lists to perform checks and the shared folder path is `shares` and log in anonymously with the command `smbclient -L //mysterious-sea.picoctf.net -p 51872 -N`

<div align="center">
    <img width="763" height="128" alt="image" src="https://github.com/user-attachments/assets/a405a024-0e5a-4ee7-b648-05754f60fad8" />

</div> 

#
After using the command `smbclient //mysterious-sea.picoctf.net/shares -p 51872 -N`, we have a shared directory. We access the directory address to log into the server and check for flags. A flag file appears, so we download the flag file and exit. Once the file is downloaded, we open it to find the flags.
<div align="center">

   <img width="786" height="271" alt="image" src="https://github.com/user-attachments/assets/800a33d2-3f37-489c-b3bd-51ad97f62b02" />

</div>

## Run 
.flag picoCTF{5mb_pr1nter_5h4re5_8eb6dd5d} 
