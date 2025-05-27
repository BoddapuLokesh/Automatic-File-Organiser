# File Organizer GUI

A simple and user-friendly graphical tool to organize your files into categorized folders based on their file types.

## Features
- Organize files by category (Documents, Images, Videos, Music, Archives, Code, Executables, etc.)
- Preview files before organizing
- Progress bar and results summary
- Safe: No overwriting, files are moved to new folders
- Cross-platform (works on Windows, macOS, Linux)

## How to Use

### 1. Command Line
You can use the command-line version for automation:
```bash
python file_organizer.py /path/to/your/folder
```

### 2. GUI Version
1. Run the GUI:
   ```bash
   python file_organizer_gui.py
   ```
2. Click **Browse** to select a folder
3. Click **Scan Files** to preview what will be organized
4. Click **Organize Files** to move files into categorized folders

## File Categories
- **Documents:** .pdf, .docx, .txt, .xlsx, .pptx, etc.
- **Images:** .jpg, .png, .gif, .bmp, etc.
- **Videos:** .mp4, .avi, .mov, etc.
- **Music:** .mp3, .wav, etc.
- **Code:** .py, .js, .html, .css, etc.
- **Archives:** .zip, .tar.gz, .rar, etc.
- **Executables:** .exe, .msi, etc.
- **MISC:** Files without extensions
- **Xyz:** Unknown file types

## Requirements
- Python 3.6+
- tkinter (comes with most Python installations)

## Project Structure
```
file_organizer.py           # Command-line version
file_organizer_gui.py       # GUI version
README.md                   # This file
demo_files/                 # Demo/test files
```

## License
MIT License

---
**Effortlessly organize your files with a single click!**
