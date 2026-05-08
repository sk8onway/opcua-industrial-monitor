import sqlite3
import sys
from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QHeaderView, QLabel, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OPC-UA Telemetry Monitor")
        self.setGeometry(100, 100, 800, 600)

        title_label = QLabel("OPC-UA Telemetry Monitor")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)

        self.status_label = QLabel("Status: Waiting for telemetry...")
        self.status_label.setStyleSheet("color: #333333; margin-bottom: 8px;")

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(["Variable ID", "Latest Value", "Last Updated Timestamp"])
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        for row in range(50):
            variable_id = str(row + 2)
            self.table.setItem(row, 0, QTableWidgetItem(variable_id))
            self.table.setItem(row, 1, QTableWidgetItem("0"))
            self.table.setItem(row, 2, QTableWidgetItem("-"))

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(title_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.table)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        self.setCentralWidget(container)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_table)
        self.timer.start(1000)

    def refresh_table(self):
        connection = sqlite3.connect('telemetry.db')
        cursor = connection.cursor()

        telemetry_available = False

        for row in range(50):
            variable_id = str(row + 2)
            cursor.execute(
                "SELECT value, timestamp FROM telemetry WHERE variable_id = ? ORDER BY id DESC LIMIT 1",
                (variable_id,),
            )
            result = cursor.fetchone()

            if result is not None:
                telemetry_available = True
                current_value = str(result[0])
                last_update = str(result[1])
            else:
                current_value = "N/A"
                last_update = "-"

            self.table.setItem(row, 1, QTableWidgetItem(current_value))
            self.table.setItem(row, 2, QTableWidgetItem(last_update))

        connection.close()

        if telemetry_available:
            self.status_label.setText("Status: Connected")
        else:
            self.status_label.setText("Status: Waiting for telemetry...")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())