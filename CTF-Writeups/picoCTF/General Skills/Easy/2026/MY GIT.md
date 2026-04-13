# 🚩 MY GIT - picoCTF 2026

- **Category:** General Skills ⚙️
- **Difficulty:** Easy 
- **Target File:** `git clone ssh://git@foggy-cliff.picoctf.net:54460/git/challenge.git`
- **Key Skills:** Impersonation Attack Git 

---

## 🔍 Challenge 
I have built my own Git server with my own rules! You can clone the challenge repo using the command below.

 `git clone ssh://git@foggy-cliff.picoctf.net:54460/git/challenge.git` Here's the password: d9df7038
Check the README to get your flag!


### 🧪 Logic Extraction:

### Command Explanation Table

| Command | Technical Meaning | Purpose in CTF |
| :--- | :--- | :--- |
| `git config user.name root` | Sets the local author name to "root". | **Impersonation:** Wearing a "mask" so the server believes you are the admin. |
| `git config user.email root@picoctf` | Sets the local author email to "root@picoctf". | **Authentication:** Completing the fake profile to match the challenge requirements. |
| `echo "give meflag" > flag.txt` | Creates a file named `flag.txt` with a string. | **Trigger:** Creating a physical change for Git to track and commit. |
| `git add flag.txt` | Moves the file to the Staging Area. | **Staging:** Preparing the specific file to be included in the next "package". |
| `git commit -m "flagggg"` | Records the changes in the local repository. | **Finalizing:** Sealing the package with the (fake) `root` fingerprint. |
| `git push origin master` | Uploads local commits to the remote server. | **Delivery:** Sending the "spoofed package" to the server to trigger the flag. |


I connected to the Git system, checked it, and it showed the system configuration. This is probably the map we need to pay attention to.

<div align="center">

  <img width="669" height="356" alt="image" src="https://github.com/user-attachments/assets/1b7301b0-9b31-48d8-9a25-c0d55f498795" />

  <img width="624" height="41" alt="image" src="https://github.com/user-attachments/assets/a4f625f7-df90-47cf-bed5-b3472137e1fc" />

</div> 



## Run 

.flag picoCTF{1mp3rs0n4t4_g17_345y_e522152d}
