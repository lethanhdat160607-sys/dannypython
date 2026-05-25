# 🚩Mob psycho - picoCTF 2024

- **Category:** Forensics ⚙️
- **Difficulty:** Medium 
- **Target File:** `mobpsycho.apk`
- **Key Skills And Tools:** xxd, tree, file, python, reading data
---

## 🔍 Challenge 

Can you handle APKs?

Download the android apk here.

### 🧪 Logic Extraction:

```        
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ mv mobpsycho.apk mobpsycho.zip

┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ ls
AndroidManifest.xml  classes2.dex  classes3.dex  classes.dex  META-INF  mobpsycho.zip  res  resources.arsc

```

<div align="center">
 <img width="1301" height="413" alt="image" src="https://github.com/user-attachments/assets/caa503ad-4f9c-4a6e-9785-4cc503bb44f7" />

</div>

#
```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tree META-INF 
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tree META-INF | grep flag

```

```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tree res | grep flag
│   ├── flag.txt


```


```
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ tree -f -a res | grep flag
│   ├── res/color/flag.txt
                                                                                                                                                            
┌──(kali㉿kali)-[~/Tools/CTF1]
└─$ cat res/color/flag.txt 

7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f62313132616535377d

```



## Run 
.flag picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57}

