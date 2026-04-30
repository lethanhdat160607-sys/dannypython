# 🚩Weird File - picoCTF 2021

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `pico_img.png`
- **Key Skills And Tools:** 
---

## 🔍 Challenge 

What could go wrong if we let Word documents run programs? (aka "in-the-clear").
weird.docm

### 🧪 Logic Extraction:

I used the `file` command to view the file's data because it's a Microsoft Word 2007+ file.

```
┌──(kali㉿kali)-[~/Tools]
└─$ file weird.docm
weird.docm: Microsoft Word 2007+

```
I use the `olevba` command to scan and analyze Microsoft Office files (such as .doc, .xls, .ppt, .docm, .xlsm,...) to search for, extract, and analyze VBA macro code snippets. This is because commands like `exiftool` and `xxd` usually cannot find them.

```
┌──(kali㉿kali)-[~/Tools]
└─$ olevba weird.docm                                     
olevba 0.60.2 on Python 3.13.12 - http://decalage.info/python/oletools
===============================================================================
FILE: weird.docm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub AutoOpen()
    MsgBox "Macros can run any program", 0, "Title"
    Signature

End Sub
 
 Sub Signature()
    Selection.TypeText Text:="some text"
    Selection.TypeParagraph
    
 End Sub
 
 Sub runpython()

Dim Ret_Val
Args = """" '"""
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
If Ret_Val = 0 Then
   MsgBox "Couldn't run python script!", vbOKOnly
End If
End Sub
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |AutoOpen            |Runs when the Word document is opened        |
|Suspicious|Shell               |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|vbNormalFocus       |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|run                 |May run an executable file or a system       |
|          |                    |command                                      |
+----------+--------------------+---------------------------------------------+
```

This part is base64, you can convert it and you're done.
```
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)

```
#

Changing the base64 data will give you the flag.
```
                                                                             
┌──(kali㉿kali)-[~/Tools]
└─$ echo "cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9" | base64 -d
picoCTF{m4cr0s_r_d4ng3r0us}    
```


## Run 
.flag picoCTF{m4cr0s_r_d4ng3r0us}                                                                                                                                                            

