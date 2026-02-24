import streamlit as st
import requests
import time

# স্ট্রীমলিট পেজ কনফিগারেশন
st.set_page_config(page_title="Wingo Hack VIP", page_icon="💀", layout="centered")

# CSS দিয়ে টার্মিনাল লুক দেওয়া
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ff0000; font-family: 'Courier New', Courier, monospace; }
    .stTextInput>div>div>input { background-color: #111; color: #ff0000; border: 1px solid #ff0000; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    pre { background-color: #000 !important; color: #ff0000 !important; border: 1px solid #ff0000; }
    </style>
    """, unsafe_allow_html=True)

# পাসওয়ার্ড প্রটেকশন
if "auth" not in st.session_state:
    st.session_state.auth = False

def login():
    st.markdown("### 🛡️ SECURITY AUTHENTICATION")
    pwd = st.text_input("Enter Access Password:", type="password")
    if st.button("UNLOCK SYSTEM"):
        if pwd == "robin1235":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Incorrect Password!")

if not st.session_state.auth:
    login()
else:
    # হ্যাকার ব্যানার (তোমার দেওয়া ডিজাইন)
    banner = """
    ██╗    ██╗██╗███╗   ██╗ ██████╗  ██████╗ 
    ██║    ██║██║████╗  ██║██╔════╝ ██╔═══██╗
    ██║ █╗ ██║██║██╔██╗ ██║██║  ███╗██║   ██║
    ██║███╗██║██║██║╚██╗██║██║   ██║██║   ██║
    ╚███╔███╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝
     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
    """
    st.code(banner, language=None)
    st.markdown("<h3 style='color:red; text-align:center;'>💀 SYSTEM BREACHED: WINGO SERVER HACKED 💀</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:red; text-align:center;'>⚡ HACKED BY : MD ROBIN ISLAM<br>⚡ STATUS : ADMIN ACCESS GRANTED</p>", unsafe_allow_html=True)
    st.write("---")

    placeholder = st.empty()

    # মেইন লজিক লুপ
    while True:
        try:
            api_url = "https://draw.ar-lottery01.com/WinGo/WinGo_30S/GetHistoryIssuePage.json"
            params = {"pageNo": 1, "pageSize": 20, "typeId": 1, "language": 0, "random": "4f3d7f7a8a3d4f3d"}
            res = requests.get(api_url, params=params, timeout=10)
            data = res.json()

            if data.get('code') == 0:
                history = data['data']['list']
                last_1 = "BIG" if int(history[0]['number']) >= 5 else "SMALL"
                last_2 = "BIG" if int(history[1]['number']) >= 5 else "SMALL"
                next_period = int(history[0]['issueNumber']) + 1

                # তোমার দেওয়া হুবহু ২টা লজিক
                if last_1 == last_2:
                    prediction = last_1
                    hack_type = "TREND DETECTED (DRAGON) 🐉"
                else:
                    prediction = "SMALL" if last_1 == "BIG" else "BIG"
                    hack_type = "ZIGZAG DETECTED (FLIP) ⚡"

                with placeholder.container():
                    st.write(f"🟢 [Injecting Payload...] SUCCESS")
                    st.write(f"🟢 [Bypassing Firewall...] SUCCESS")
                    st.write("---")
                    st.error(f"😈 TARGET PERIOD : {next_period}")
                    st.warning(f"🦠 HACK TYPE : {hack_type}")
                    st.info(f"🎯 PREDICTION : {prediction}")
                    st.write("---")
                    st.success("💰 INVESTMENT PLAN: USE 7-STEP STRATEGY")
                    
                    # ডেটা স্ট্রিম (হিস্ট্রি)
                    stream = " ".join(["B" if int(x['number']) >= 5 else "S" for x in history[:8]])
                    st.text(f"DATA STREAM: {stream}")

            time.sleep(10) # ১০ সেকেন্ড পর পর আপডেট হবে
            st.rerun()

        except Exception as e:
            st.error("Connecting to Server...")
            time.sleep(5)
            st.rerun()
