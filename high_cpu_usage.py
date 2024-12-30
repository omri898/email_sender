import streamlit as st
import time

st.title("Simulate Application Crashes")

if st.button("Simulate Missing DLL"):
    st.write("Simulating missing DLL file...")
    time.sleep(1)
    st.error("The application failed to start because a DLL is missing! (Simulation)")
    st.write("Suggested solution: Reinstall the application or restore the missing DLL.")

if st.button("Simulate High RAM Usage"):
    st.write("Simulating high RAM usage...")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)  # Simulate high RAM usage delay
        progress_bar.progress(i + 1)
    st.warning("RAM usage is critically high! (Simulation)")
    st.write("Suggested solution: Close unnecessary applications.")

if st.button("Simulate Corrupt Config File"):
    st.write("Simulating corrupt configuration file...")
    time.sleep(1)
    st.error("The application configuration file is corrupted! (Simulation)")
    st.write("Suggested solution: Reset or delete the configuration file and restart the application.")
