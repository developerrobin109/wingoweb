import streamlit as st
import requests
import time

# স্টাইল এবং হেডার কনফিগারেশন
st.set_page_config(page_title="Wingo Hack VIP", page_icon="💀", layout="centered")

# ব্যাকগ্রাউন্ড এবং টেক্সট কালার স্টাইল
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ff0000; }
    .stAlert { background-color: #111; border: 1px solid #ff0000; color: #ff0000; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: red;'>💀 WINGO HACKED SCRIPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Hacked by <b>Md Robin Islam</b></p>", unsafe_allow_html=True)

# পাসওয়ার্ড প্রটেকশন
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    pwd = st.text_input("Enter Access Password:", type="password")
    if st.button("UNLOCK SYSTEM"):
        if pwd == "robin1235":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Incorrect Password!")
else:
    placeholder = st.empty()
    
    # মেইন রিকোয়েস্ট লজিক
    try:
        api_url = "https://draw.ar-lottery01.com/WinGo/WinGo_30S/GetHistoryIssuePage.json"
        
        # অ্যাডভান্সড হেডার্স (যাতে সার্ভার ব্লক না করে)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.ar-lottery01.com',
            'Referer': 'https://www.ar-lottery01.com/'
        }
        
        params = {
            "pageNo": 1, 
            "pageSize": 20, 
            "typeId": 1, 
            "language": 0, 
            "random": "4f3d7f7a8a3d4f3d"
        }

        # ডেটা ফেচ করা
        res = requests.get(api_url, headers=headers, params=params, timeout=15)
        
        if res.status_code == 200:
            data = res.json()
            if data.get('code') == 0:
                history = data['data']['list']
                last_num = int(history[0]['number'])
                last_res = "BIG" if last_num >= 5 else "SMALL"
                prev_res = "BIG" if int(history[1]['number']) >= 5 else "SMALL"
                next_period = int(history[0]['issueNumber']) + 1

                # ড্রাগন ও জিগজ্যাগ লজিক
                if last_res == prev_res:
                    prediction = last_res
                    h_type = "TREND DETECTED (DRAGON) 🐉"
                else:
                    prediction = "SMALL" if last_res == "BIG" else "BIG"
                    h_type = "ZIGZAG DETECTED (FLIP) ⚡"

                with placeholder.container():
                    st.write("---")
                    st.error(f"😈 TARGET PERIOD : {next_period}")
                    st.warning(f"🦠 HACK TYPE : {h_type}")
                    st.info(f"🎯 PREDICTION : {prediction}")
                    st.success("💰 INVESTMENT PLAN: USE 7-STEP STRATEGY")
                    st.write("---")
                    
                    # ডাটা স্ট্রিম
                    stream = " ".join(["B" if int(x['number']) >= 5 else "S" for x in history[:8]])
                    st.text(f"DATA STREAM: {stream}")
            else:
                st.error("API Response Error. Check Logic.")
        else:
            st.error(f"Server Connection Blocked! (Error Code: {res.status_code})")

    except Exception as e:
        st.error(f"Connecting to Wingo Server... (Retrying)")
        time.sleep(5)
        st.rerun()

# অটো রিফ্রেশ করার জন্য সাইডবারে একটি বাটন বা অটো লজিক
time.sleep(10)
st.rerun()
