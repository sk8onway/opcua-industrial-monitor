# OPC-UA Telemetry Monitoring System

## Overview

This project is a real-time industrial telemetry monitoring prototype built using Python, OPC-UA, SQLite, and PySide6.

The system simulates an industrial PLC/server environment using an OPC-UA server and continuously acquires telemetry data through an asynchronous OPC-UA client. The acquired telemetry is stored in an SQLite database and visualized through a live monitoring desktop UI.

The architecture is modular and designed to demonstrate:

- Industrial communication using OPC-UA
- Asynchronous telemetry acquisition
- Persistent telemetry logging
- Automatic reconnect handling
- Real-time GUI monitoring

---

## Features

### OPC-UA Server Simulation

- Simulates an industrial OPC-UA server
- Dynamically generates 50 telemetry variables
- Continuously updates variable values

### OPC-UA Client

- Asynchronously reads telemetry variables
- Handles communication failures gracefully
- Automatically reconnects if server connection is lost
- Logs telemetry into SQLite database

### SQLite Telemetry Logging

Stores:

- Variable ID
- Timestamp
- Current Value

Maintains persistent telemetry history.

### PySide6 Monitoring UI

- Live telemetry table
- Displays Variable ID, Latest Value, and Last Updated Timestamp
- Periodically refreshes data from SQLite
- Displays connection status

---

## System Architecture

```
OPC-UA Server
      ↓
Async OPC-UA Client
      ↓
SQLite Database
      ↓
PySide6 Monitoring UI
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Core language |
| asyncua | OPC-UA server & client |
| SQLite | Telemetry persistence |
| PySide6 | Desktop monitoring UI |

---

## Project Structure

```
project/
│
├── server.py          # OPC-UA server simulation
├── client.py          # OPC-UA telemetry client
├── database.py        # SQLite database functions
├── ui.py              # PySide6 monitoring UI
├── telemetry.db       # SQLite telemetry database
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the System

### Step 1 — Start OPC-UA Server

```bash
python server.py
```

### Step 2 — Start OPC-UA Client

```bash
python client.py
```

### Step 3 — Launch Monitoring UI

```bash
python ui.py
```

---

## Reliability Features

- Node-level exception handling
- Automatic OPC-UA reconnect logic
- Graceful failure recovery
- Decoupled UI/database architecture

---

## Future Improvements

Potential future enhancements:

- Alarm system
- Historical trend visualization
- CSV export
- Multi-device monitoring
- Real Siemens S7-1500 PLC integration
- Authentication/security support

---

## Notes

This project currently uses a simulated OPC-UA server for development and testing purposes. The client architecture is designed such that the simulated server can later be replaced with a real industrial PLC exposing OPC-UA endpoints.

---

## Author

**Saket Sagar**