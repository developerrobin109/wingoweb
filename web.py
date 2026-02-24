import streamlit as st
import requests
import time

# স্টাইল এবং হেডার
st.set_page_config(page_title="Wingo Hack VIP", page_icon="💀", layout="centered")
st.markdown("<h1 style='text-align: center; color: red;'>💀 WINGO HACKED SCRIPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Hacked by <b>Md Robin Islam</b></p>", unsafe_allow_html=True)

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
    # মেইন ডিসপ্লে এরিয়া
    placeholder = st.empty()
    
    # এটি প্রতি ১০ সেকেন্ড পর পর অটো-রিফ্রেশ হবে
    while True:
        try:
            api_url = "https://draw.ar-lottery01.com/WinGo/WinGo_30S/GetHistoryIssuePage.json"
            params = {"pageNo": 1, "pageSize": 20, "typeId": 1, "language": 0, "random": "4f3d7f7a8a3d4f3d"}
            res = requests.get(api_url, params=params, timeout=10)
            data = res.json()

            if data.get('code') == 0:
                history = data['data']['list']
                last_num = int(history[0]['number'])
                last_res = "BIG" if last_num >= 5 else "SMALL"
                prev_res = "BIG" if int(history[1]['number']) >= 5 else "SMALL"
                next_period = int(history[0]['issueNumber']) + 1

                # লজিক: ড্রাগন ও জিগজ্যাগ
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
                    
                    # ডাটা স্ট্রিম (হিস্ট্রি)
                    stream = " ".join(["B" if int(x['number']) >= 5 else "S" for x in history[:8]])
                    st.text(f"DATA STREAM: {stream}")
            
            # ১০ সেকেন্ড অপেক্ষা করে পেজটি রিফ্রেশ করবে
            time.sleep(10)
            st.rerun()

        except Exception as e:
            st.error("Connecting to Wingo Server...")
            time.sleep(5)
            st.rerun()
