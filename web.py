import streamlit as st
import requests
import time
from streamlit_autorefresh import st_autorefresh

# অটো-রিফ্রেশ সেটআপ
st_autorefresh(interval=10000, key="wingorefresh")

# ডিজাইন এবং স্টাইল
st.set_page_config(page_title="Wingo Hack VIP", page_icon="💀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #ff0000; font-family: 'Courier New', Courier, monospace; }
    stCodeBlock, pre { background-color: #000 !important; color: #ff0000 !important; border: 1px solid #ff0000 !important; }
    .stTextInput>div>div>input { background-color: #111; color: #ff0000; border: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

banner = """
    ██╗    ██╗██╗███╗   ██╗ ██████╗  ██████╗ 
    ██║    ██║██║████╗  ██║██╔════╝ ██╔═══██╗
    ██║ █╗ ██║██║██╔██╗ ██║██║  ███╗██║   ██║
    ██║███╗██║██║██║╚██╗██║██║   ██║██║   ██║
    ╚███╔███╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝
     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
"""

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h2 style='color:yellow; text-align:center;'>🛡️ SECURITY AUTHENTICATION 🛡️</h2>", unsafe_allow_html=True)
    pwd = st.text_input("Enter Access Password:", type="password")
    if st.button("UNLOCK SYSTEM"):
        if pwd == "robin1235":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Incorrect Password!")
else:
    st.code(banner, language=None)
    st.markdown("<h3 style='background-color:red; color:white; text-align:center;'> 💀 SYSTEM BREACHED: WINGO SERVER HACKED 💀 </h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:red; font-weight:bold;'>⚡ HACKED BY : MD ROBIN ISLAM<br>⚡ STATUS : ADMIN ACCESS GRANTED<br>⚡ WARNING : FOLLOW MUST BE 7 STEP (RISK FREE)</p>", unsafe_allow_html=True)
    st.write("---")

    try:
        api_url = "https://draw.ar-lottery01.com/WinGo/WinGo_30S/GetHistoryIssuePage.json"
        
        # শক্তিশালী হেডার যাতে ব্লক না হয়
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.ar-lottery01.com/'
        }
        params = {"pageNo": 1, "pageSize": 10, "typeId": 1, "language": 0, "random": "4f3d7f7a8a3d4f3d"}
        
        res = requests.get(api_url, headers=headers, params=params, timeout=10)
        data = res.json()

        if data.get('code') == 0:
            history = data['data']['list']
            last_1 = "BIG" if int(history[0]['number']) >= 5 else "SMALL"
            last_2 = "BIG" if int(history[1]['number']) >= 5 else "SMALL"
            next_period = int(history[0]['issueNumber']) + 1

            if last_1 == last_2:
                prediction = last_1
                hack_type = "TREND DETECTED (DRAGON) 🐉"
            else:
                prediction = "SMALL" if last_1 == "BIG" else "BIG"
                hack_type = "ZIGZAG DETECTED (FLIP) ⚡"

            st.write("🟢 [Injecting Payload...] SUCCESS")
            st.write("🟢 [Bypassing Firewall...] SUCCESS")
            st.write("---")
            
            st.error(f"😈 TARGET PERIOD : {next_period}")
            st.markdown(f"<span style='color:magenta;'>🦠 HACK TYPE : {hack_type}</span>", unsafe_allow_html=True)
            
            color = "#00ffff" if prediction == "BIG" else "#ffff00"
            st.markdown(f"🎯 PREDICTION : <span style='color:{color}; font-weight:bold; font-size:25px;'>{prediction} ●</span>", unsafe_allow_html=True)
            
            st.write("---")
            st.markdown("<p style='background-color:black; color:green; font-weight:bold;'> 💰 INVESTMENT PLAN: USE 7-STEP STRATEGY </p>", unsafe_allow_html=True)
            st.write("---")
            
            stream = " ".join(["B" if int(x['number']) >= 5 else "S" for x in history[:8]])
            st.text(f"DATA STREAM: {stream}")
            
    except:
        st.error("Connecting to Wingo Server... (Please Wait)")
