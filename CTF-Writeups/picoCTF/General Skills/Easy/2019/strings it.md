# 🚩 strings it - picoCTF 2019

- **Category:** General Skills ⚙️
- **Difficulty:** Easy
- **Target File:** `strings`
- **Key Skills:** strings and grep  
---

## 🔍 Challenge 
Can you find the flag in `file` without running it?

### 🧪 Logic Extraction:
- strings: Filters out binary "junk," keeping only readable characters.
- Uses: Searches for hidden text, error messages, function names, or URLs in non-text files (such as .exe, .bin, .png images, etc.).
- | (Pipe): The funnel. Pushes results from the previous command to the next.
- grep: The crawler. Only picks out lines containing the keyword you want.
```
~ strings file
~ strings strings | grep pico
```
## Run 
.flag picoCTF{5tRIng5_1T_60eA8fdA}
