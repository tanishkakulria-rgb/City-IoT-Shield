import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="City IoT Shield | Security Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    [data-testid="stMetric"] {
        background-color: #eaf2ff;
        border: 2px solid #2563eb;
        padding: 22px;
        border-radius: 14px;
        color: #172554;
    }

    [data-testid="stSidebar"] {
        background-color: #f1f5f9;
        border-right: 2px solid #cbd5e1;
    }

    h1 {
        color: #1d4ed8;
        font-size: 2.4rem;
        font-weight: 800;
    }

    div.stButton > button,
    div.stDownloadButton > button {
        border-radius: 8px;
        font-weight: 700;
        min-height: 45px;
    }
</style>
""", unsafe_allow_html=True)

LOG_FILE = "security_history.json"

if "event_history" not in st.session_state:
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as file:
                st.session_state.event_history = json.load(file)
        except (json.JSONDecodeError, OSError):
            st.session_state.event_history = []
    else:
        st.session_state.event_history = []

def save_security_event(device, event, severity, action):
    record = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Device": device,
        "Event": event,
        "Severity": severity,
        "Recommended Action": action
    }

    st.session_state.event_history.append(record)

    with open(LOG_FILE, "w") as file:
        json.dump(st.session_state.event_history, file, indent=4)

st.title("🛡️ City IoT Shield")
st.subheader("Smart City Cybersecurity Monitoring Dashboard")

st.sidebar.title("🛡️ City IoT Shield")
st.sidebar.caption("Security Operations Center")
st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Device Inventory",
        "Security Alerts",
        "Analytics",
        "Reports"
    ]
)



if page == "Overview":
    st.info("Demo mode: Using simulated IoT device data.")
    st.subheader("City IoT Shield Overview")
    st.write(
        "Monitor connected devices, review security risks, "
        "and track simulated cybersecurity alerts from one dashboard."
    )
    st.success("System initialized — monitoring 4 simulated IoT devices.")

st.sidebar.header("Control Panel")
scenario = st.sidebar.selectbox(
    "Simulate device activity",
    ["Normal Activity", "Suspicious Traffic", "Outdated Firmware"]
)

if scenario == "Normal Activity":
    online = 4
    suspicious = 0
    risk = "LOW"
elif scenario == "Suspicious Traffic":
    online = 4
    suspicious = 1
    risk = "HIGH"
else:
    online = 4
    suspicious = 1
    risk = "MEDIUM"

c1, c2, c3 = st.columns(3)
c1.metric("Registered Devices", 4)
c2.metric("Online Devices", online)
c3.metric("Devices Requiring Attention", suspicious)

st.divider()
if page=="Overview":
    st.divider()
    st.subheader("📊 Device Risk Scores")

if scenario == "Normal Activity":
    risk_scores = {
        "Traffic Camera 01": 15,
        "Smart Meter 02": 10,
        "Air Sensor 03": 8,
        "Traffic Signal 04": 12
    }
elif scenario == "Suspicious Traffic":
    risk_scores = {
        "Traffic Camera 01": 90,
        "Smart Meter 02": 10,
        "Air Sensor 03": 8,
        "Traffic Signal 04": 12
    }
else:
    risk_scores = {
        "Traffic Camera 01": 15,
        "Smart Meter 02": 70,
        "Air Sensor 03": 8,
        "Traffic Signal 04": 12
    }


if page == "Overview":
    st.subheader("📊 Device Risk Scores")

    for device, score in risk_scores.items():
        st.write(f"**{device}** — Risk Score: {score}/100")
        st.progress(score)

if page == "Device Inventory":
    st.subheader("📡 Connected Device Inventory")
    devices = [
        {
            "Device": "Traffic Camera 01",
            "Type": "CCTV",
            "Status": "Online",
            "Risk": "High" if scenario == "Suspicious Traffic" else "Low"
        },
        {
            "Device": "Smart Meter 02",
            "Type": "Electricity",
            "Status": "Online",
            "Risk": "Medium" if scenario == "Outdated Firmware" else "Low"
        },
        {
            "Device": "Air Sensor 03",
            "Type": "Environment",
            "Status": "Online",
            "Risk": "Low"
        },
        {
            "Device": "Traffic Signal 04",
            "Type": "Traffic",
            "Status": "Online",
            "Risk": "Low"
        }
    ]

    st.dataframe(devices, use_container_width=True)

    st.divider()

if page == "Security Alerts":
    st.subheader("🚨 Security Alerts")

    if scenario == "Normal Activity":
        st.success("All simulated devices are behaving normally.")
    elif scenario == "Suspicious Traffic":
        st.error(
            "HIGH RISK: Traffic Camera 01 shows unusual network activity."
        )
        st.write("Recommended action: Investigate the device and review its network logs.")
    elif scenario == "Outdated Firmware":
        st.warning(
            "MEDIUM RISK: Smart Meter 02 requires a firmware review."
        )
        st.write("Recommended action: Verify the firmware version and apply approved updates.")

    st.caption(
        "City IoT Shield | Prototype v1.0 | "
        + datetime.now().strftime("%d-%m-%Y %H:%M")
    )

    st.divider()
    st.subheader("🛠️ Security Response Center")
    st.info("City IoT Shield — Security Monitoring")

col1, col2 = st.columns(2)

with col1:
    st.metric("Monitoring Status", "ACTIVE")

with col2:
    if scenario == "Suspicious Traffic":
        st.error("Threat Detected")
    elif scenario == "Outdated Firmware":
        st.warning("Firmware Update Required")
    else:
        st.success("All Systems Normal")

    if scenario == "Suspicious Traffic":
        st.error("Active Alert: Traffic Camera 01 — HIGH RISK")

        if st.button("Mark as Investigated"):
            st.success(
                "Investigation marked complete. "
                "Review the device network logs before taking further action."
            )

    elif scenario == "Outdated Firmware":
        st.warning("Active Alert: Smart Meter 02 — MEDIUM RISK")

        if st.button("Acknowledge Firmware Alert"):
            st.success(
                "Alert acknowledged. "
                "Verify the firmware version and plan an approved update."
            )

    else:
        st.success("No active security alerts to investigate.")

    if scenario == "Normal Activity":
        logs = [
            {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Device": "All Devices",
                "Event": "Normal activity detected",
                "Severity": "INFO",
                "Action": "No action required"
            }
        ]
    elif scenario == "Suspicious Traffic":
        logs = [
            {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Device": "Traffic Camera 01",
                "Event": "Unusual network traffic detected",
                "Severity": "HIGH",
                "Action": "Investigate network logs"
            }
        ]
    else:
        logs = [
            {
                "Time": datetime.now().strftime("%H:%M:%S"),
                "Device": "Smart Meter 02",
                "Event": "Firmware review required",
                "Severity": "MEDIUM",
                "Action": "Verify firmware version"
            }
        ]

    st.dataframe(logs, use_container_width=True)

st.subheader("🕒 Recent Security Events")

if scenario == "Suspicious Traffic":
    st.error("HIGH — Unusual traffic detected from Traffic Camera 01")
elif scenario == "Outdated Firmware":
    st.warning("MEDIUM — Smart Meter 02 requires a firmware update")
else:
    st.success("LOW — No suspicious activity in the current simulation")

st.divider()
st.subheader("🗂️ Saved Security Event History")

if st.button("Save Current Security Alert"):
    if scenario == "Suspicious Traffic":
        save_security_event(
            "Traffic Camera 01",
            "Unusual network traffic detected",
            "HIGH",
            "Investigate network logs"
        )
        st.success("Security event saved!")

    elif scenario == "Outdated Firmware":
        save_security_event(
            "Smart Meter 02",
            "Firmware review required",
            "MEDIUM",
            "Verify firmware version"
        )
        st.success("Security event saved!")

    else:
        st.info("No security alert to save in Normal Activity.")

if st.session_state.event_history:
    st.dataframe(
        st.session_state.event_history,
        use_container_width=True
    )
else:
    st.info("No saved events yet. Select an alert scenario and save it.")

st.divider()


st.divider()
st.header("📈 Security Analytics")

if scenario == "Normal Activity":
    risk_counts = {"High": 0, "Medium": 0, "Low": 4}
elif scenario == "Suspicious Traffic":
    risk_counts = {"High": 1, "Medium": 0, "Low": 3}
else:
    risk_counts = {"High": 0, "Medium": 1, "Low": 3}

col1, col2, col3 = st.columns(3)
col1.metric("High Risk", risk_counts["High"])
col2.metric("Medium Risk", risk_counts["Medium"])
col3.metric("Low Risk", risk_counts["Low"])

if page == "Analytics":
   st.subheader("Device Risk Distribution")
   st.bar_chart(risk_counts)

st.caption(
    "Analytics are based on simulated device data."
)

st.divider()
st.header("📥 Download Security Report")

report_rows = [
    {
        "Device": "Traffic Camera 01",
        "Type": "CCTV",
        "Status": "Online",
        "Risk": "High" if scenario == "Suspicious Traffic" else "Low"
    },
    {
        "Device": "Smart Meter 02",
        "Type": "Electricity",
        "Status": "Online",
        "Risk": "Medium" if scenario == "Outdated Firmware" else "Low"
    },
    {
        "Device": "Air Sensor 03",
        "Type": "Environment",
        "Status": "Online",
        "Risk": "Low"
    },
    {
        "Device": "Traffic Signal 04",
        "Type": "Traffic",
        "Status": "Online",
        "Risk": "Low"
    }
]

import pandas as pd

report_df = pd.DataFrame(report_rows)

csv_data = report_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Device Security Report (CSV)",
    data=csv_data,
    file_name="city_iot_security_report.csv",
    mime="text/csv"
)

st.divider()
st.header("🖥️ IoT Device Technical Details")

device_details = [
    {
        "Device": "Traffic Camera 01",
        "IP Address": "192.168.1.101",
        "Firmware": "v2.1.0",
        "Last Seen": "Just now"
    },
    {
        "Device": "Smart Meter 02",
        "IP Address": "192.168.1.102",
        "Firmware": "v1.4.2",
        "Last Seen": "Just now"
    },
    {
        "Device": "Air Sensor 03",
        "IP Address": "192.168.1.103",
        "Firmware": "v3.0.1",
        "Last Seen": "Just now"
    },
    {
        "Device": "Traffic Signal 04",
        "IP Address": "192.168.1.104",
        "Firmware": "v2.0.5",
        "Last Seen": "Just now"
    }
]

st.divider()
st.subheader("📊 Report Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Devices", 3)

with col2:
    st.metric(
        "Online Devices",
        3 if scenario == "Normal Activity" else 2
    )

with col3:
    st.metric(
        "Security Status",
        "High Risk" if scenario == "Suspicious Traffic"
        else "Medium Risk" if scenario == "Outdated Firmware"
        else "Normal"
    )

st.write("Current simulation:", scenario)

if scenario == "Suspicious Traffic":
    st.error("Overall Status: HIGH RISK")
elif scenario == "Outdated Firmware":
    st.warning("Overall Status: MEDIUM RISK")
else:
    st.success("Overall Status: NORMAL")

st.dataframe(
    device_details,
    use_container_width=True,
    hide_index=True
)

st.caption("Prototype data — IP addresses and firmware versions are simulated.")

st.divider()
st.header("🛡️ Security Threat Summary")

if scenario == "Normal Activity":
    st.success("SYSTEM STATUS: NORMAL")
    st.write("All simulated devices are operating normally.")
    st.write("Recommended action: Continue monitoring.")

elif scenario == "Suspicious Traffic":
    st.error("SYSTEM STATUS: HIGH RISK")
    st.write("Traffic Camera 01 has unusual simulated network activity.")
    st.write("Recommended action: Investigate traffic logs and review device access.")

else:
    st.warning("SYSTEM STATUS: MEDIUM RISK")
    st.write("Smart Meter 02 requires a firmware review.")
    st.write("Recommended action: Verify firmware and plan an approved update.")

st.caption(
    "This threat summary uses simulated scenarios and is not a live security detection system."
)
