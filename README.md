# 📁 Mobile to Laptop File Uploader (Flask)

- This is a simple Flask web application that lets you upload files (e.g., from your mobile device) directly to your laptop/PC via local network.

- No internet required. Just connect your mobile and PC to the same Wi-Fi hotspot.

---

## 🚀 Features

- Upload files from mobile browser to your PC/laptop.

- Saves uploaded files with a timestamp.

### Displays:

- ✅ File name

- 🗂️ File size in MB

- ⏱️ Upload time

- 🚀 Upload speed in MB/s

- Max file size: 2GB

---

### 📦 Requirements
    Python 3.x

    Flask

Install Flask (if not installed):

    pip install flask

---

### 🛠️ How to Use

Save the script (e.g., upload_app.py)

Run the server:

    python upload_app.py
- Connect your mobile and laptop to the same Wi-Fi

- Find your laptop's IP address (e.g., 192.168.1.5)

- On your mobile browser, visit:

http://<your-laptop-ip>:5000
Select a file and upload.

---

### 📁 Uploaded Files Location

All files are saved in the uploads/ folder inside the script's directory. The filename will be prefixed with the current timestamp for uniqueness.

Example:

    uploads/20250802_154020_example.jpg

---

### ⚙️ Configuration

You can modify:

UPLOAD_FOLDER = "uploads" → to change save path

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024 → to change max size (currently 2GB)

---

### 🔒 Note
This server is meant for local/offline use only. Do not expose it to the public internet without adding proper authentication and security.

---

### 📸 Screenshot

### 📃 License
MIT License

