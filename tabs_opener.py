import streamlit as st

# Streamlit app
st.title("Open Multiple Resource-Intensive Tabs")

# List of resource-intensive websites
urls = [
    "https://www.youtube.com",
    "https://www.netflix.com",
    "https://www.twitch.tv",
    "https://www.zoom.us",
    "https://www.vimeo.com",
    "https://www.teams.microsoft.com",
    "https://www.disneyplus.com",
    "https://www.hbo.com",
    "https://www.spotify.com",
    "https://www.apple.com/apple-tv-plus",
    "https://www.adobe.com",
    "https://www.figma.com",
    "https://www.autodesk.com",
    "https://www.unity.com",
    "https://www.epicgames.com",
    "https://www.roblox.com",
    "https://www.photoshop.com",
    "https://www.canva.com",
    "https://www.behance.net",
    "https://www.dribbble.com",
    "https://www.google.com/maps",
    "https://www.washingtonpost.com",
    "https://www.reddit.com",
    "https://www.pinterest.com",
    "https://www.cnn.com",
    "https://www.dropbox.com",
    "https://www.box.com",
    "https://www.amazon.com",
    "https://www.ebay.com",
    "https://www.alibaba.com"
]

if st.button("Open 30 Tabs"):
    # JavaScript to open multiple tabs
    js_code = "<script>\n"
    for url in urls:
        js_code += f'window.open("{url}", "_blank");\n'
    js_code += "</script>"
    st.components.v1.html(js_code, height=0, width=0)
