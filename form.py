import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QFormLayout, QVBoxLayout,
    QPushButton, QMessageBox, QComboBox, QTextEdit, QHBoxLayout, QShortcut
)
from PyQt5.QtGui import QKeySequence

class FormValidationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation")
        self.setFixedSize(400, 450)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        # Name
        self.name_input = QLineEdit()
        form_layout.addRow("Name:", self.name_input)

        # Email
        self.email_input = QLineEdit()
        form_layout.addRow("Email:", self.email_input)

        # Age
        self.age_input = QLineEdit()
        form_layout.addRow("Age:", self.age_input)

        # Phone Number
        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62 000 0000 0000;")
        form_layout.addRow("Phone Number:", self.phone_input)

        # Address
        self.address_input = QTextEdit()
        self.address_input.setFixedHeight(70)
        form_layout.addRow("Address:", self.address_input)

        # Gender
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["", "Male", "Female", "Other"])
        form_layout.addRow("Gender:", self.gender_combo)

        # Education
        self.education_combo = QComboBox()
        self.education_combo.addItems(["", "High School", "Diploma", "Bachelor", "Master", "Doctor"])
        form_layout.addRow("Education:", self.education_combo)

        layout.addLayout(form_layout)

        # Save & Clear buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.validate_form)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)

        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)

        # Name & NIM Info (as footer)
        self.footer_label = QLabel("Nama: Rafli | NIM: F1D022022")
        layout.addWidget(self.footer_label)

        # Shortcut 'Q' to quit
        quit_shortcut = QShortcut(QKeySequence("Q"), self)
        quit_shortcut.activated.connect(self.close)

        self.setLayout(layout)

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_combo.currentText()
        education = self.education_combo.currentText()

        # Validasi
        if not name or len(name) < 3:
            self.show_warning("Name is required and must be at least 3 characters.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_warning("Invalid email format.")
        elif not age.isdigit():
            self.show_warning("Age must be a number.")
        elif len(re.sub(r'\D', '', phone)) != 13:
            self.show_warning("Phone number must be 13 digits.")
        elif not address:
            self.show_warning("Address is required.")
        elif not gender:
            self.show_warning("Please select a gender.")
        elif not education:
            self.show_warning("Please select your education.")
        else:
            QMessageBox.information(self, "Success", "Data saved successfully!")
            self.clear_fields()

    def show_warning(self, message):
        QMessageBox.warning(self, "Validation Error", message)

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_combo.setCurrentIndex(0)
        self.education_combo.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
