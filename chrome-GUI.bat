call .\myenv\Scripts\activate
start python GUI-Server.py
timeout /nobreak 3
start chrome.exe http://localhost:53535