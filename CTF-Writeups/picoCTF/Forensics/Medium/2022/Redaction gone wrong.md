# 🚩Redaction gone wrong - picoCTF 2022

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `Financial_Report_for_ABC_Labs.pdf`
- **Key Skills And Tools:** file, pdftotext, reading data
---

## 🔍 Challenge 

Now you DON’T see me.

This report has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

### 🧪 Logic Extraction:
I highlighted it and a hidden flag appeared in the PDF file.

<div align="center">
  <img width="1133" height="605" alt="image" src="https://github.com/user-attachments/assets/b373eed8-dca5-487e-8ffe-7a6d7c5ccfe5" />

</div>

#
Your friend can use the `pdftotext` command to convert the PDF file into a note file to get the flag.
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ pdftotext Financial_Report_for_ABC_Labs.pdf
                                                                                             
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ cat Financial_Report_for_ABC_Labs.txt
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.

Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.

```
## Run 
.flag picoCTF{C4n_Y0u_S33_m3_fully}

                                                                                                                                                     

