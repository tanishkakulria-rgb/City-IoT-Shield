# City-IoT-Shield
Smart-city IoT cybersecurity dashboard prototype
# City IoT Shield

## Smart-City IoT Cybersecurity Dashboard

### Project Overview
City IoT Shield is a Python and Streamlit-based prototype that demonstrates how a cybersecurity dashboard can display smart-city device information, simulated security alerts, risk indicators, analytics, and reports.

### Features
- Overview dashboard with device risk indicators
- Device inventory for example IoT devices
- Simulated security alerts
- Risk analytics and visualisation
- Device security verification demo
- Device isolation simulator
- Downloadable CSV security report

### Technologies Used
- Python
- Streamlit
- Pandas
- JSON and CSV

### How to Run
1. Install Python 3.10 or newer.
2. Open the project folder in VS Code.
3. Open the terminal and install dependencies:

   `python -m pip install streamlit pandas`

4. Run the application:

   `python -m streamlit run app.py`

5. Open the local URL shown in the terminal.

### Demo Scenarios
- Normal Activity
- Suspicious Traffic
- Outdated Firmware

### Current Limitations
This prototype uses simulated scenarios. It does not currently monitor real IoT devices, analyse live network traffic, or isolate actual devices.

### Future Improvements
- Integrate authorised live IoT network data
- Implement and test traffic-detection rules
- Improve device risk assessment
- Develop validated alerting and response mechanisms

### Project Goal
To demonstrate how a centralised dashboard could help present cybersecurity information for smart-city IoT devices.
