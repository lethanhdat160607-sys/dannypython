# 🚩WPA-ing Out - picoGym Exclusive

- **Category:** Forensics ⚙️
- **Difficulty:** Easy
- **Target File:** `flag2of2-final.pdf`
- **Key Skills And Tools:** 
---

## 🔍 Challenge 
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
Download the suspicious file here.

### 🧪 Logic Extraction:

We downloaded the challenge, and I saw it was a PDF file, so I opened it. It showed what looked like half a flag `1n_pn9&pdf_2a6a1ea8}`, maybe we need to find the other one.

<div align="center">

  <img width="1718" height="920" alt="image" src="https://github.com/user-attachments/assets/557b8daa-f3bf-40be-a2b5-881c8ba6b71e" />

</div>

#
The first method I used was simply to use `convert flag2of2-final.pdf flag2of2-final.png` and open the png file to get the flags.
<div align="center">
  <img width="550" height="114" alt="image" src="https://github.com/user-attachments/assets/fd704458-de6c-4480-8dc2-1c8d2a6f6cbe" />
</div>

#

<div align="center">
  <img width="883" height="623" alt="image" src="https://github.com/user-attachments/assets/c1e8fab9-a391-4a69-b8a8-c16971883c88" />

</div>

#
```
~binwalk flag2of2-final.pdf
~binwalk -e flag2of2-final.pdf
~ls -la _flag2of2-final.pdf.extracted/
~dd if=~/Tools/flag2of2-final.pdf of=extracted.png bs=1 count=914
```

```
# PNG: Starting from byte 0, take 914 bytes (until PDF begins)

dd if=file of=png bs=1 count=914

# PDF: Starting from byte 914, take 235 bytes (1149 - 914 = 235)

dd if=file of=pdf bs=1 skip=914 count=235

# Zlib: Starting from byte 1149 to the end
dd if=file of=zlib bs=1 skip=1149
```
<div align="center">
  <img width="1220" height="685" alt="image" src="https://github.com/user-attachments/assets/691e665c-3af2-45bd-8b90-873ca43b9b3f" />

</div>


## Comparison Table

| Feature | Visual Rendering (`convert`) | Data Carving (`dd` + `strings`) |
| :--- | :--- | :--- |
| **Pros** | Fast, reveals visual content immediately. | Deep dive into file structure; bypasses rendering limits. |
| **Cons** | Misses hidden metadata and non-rendered data. | Requires more steps and knowledge of offsets. |
| **Use Case** | Flag is part of the visible PDF text/images. | Flag is hidden in **Streams**, **Metadata**, or **Polyglot** headers. |

---



## Run 
.flag picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}



