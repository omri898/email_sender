import os
import psutil
import streamlit as st

st.title("Simulate Slow PC Performance")

if st.button("Simulate High CPU Usage"):
    for _ in range(4):  # Run 4 processes to mimic heavy CPU usage
        os.system("python -c \"while True: pass\" &")

# if st.button("Simulate Low Disk Space"):
#     os.makedirs("dummy_files", exist_ok=True)
#     for i in range(100):
#         with open(f"dummy_files/dummy_file_{i}.txt", "w") as f:
#             f.write("x" * 10**6)  # 1 MB per file

# if st.button("Simulate Excess Startup Programs"):
#     os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v DummyApp /t REG_SZ /d "C:\\DummyApp.exe"')