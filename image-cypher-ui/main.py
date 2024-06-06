import sys
import random
import string
import numpy as np
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QLineEdit, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('XOR Image Encryption')
        self.setGeometry(200, 200, 900, 600)
        
        # Set up the main layout
        main_layout = QHBoxLayout()
        
        # Left side layout for image upload and display
        left_layout = QVBoxLayout()
        
        self.image_label = QLabel('Image will be displayed here')
        self.image_label.setFixedSize(400, 400)
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        left_layout.addWidget(self.image_label)
        
        self.upload_button = QPushButton('Upload Image')
        left_layout.addWidget(self.upload_button)
        self.upload_button.clicked.connect(self.upload_image)
        
        left_layout.addStretch(1)
        
        # Center layout for encryption process
        center_layout = QVBoxLayout()
        
        self.encrypt_label = QLabel('encrypt')
        self.encrypt_label.setFixedSize(100, 40)
        self.encrypt_label.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(self.encrypt_label)
        
        self.arrow_label = QLabel('→')
        self.arrow_label.setFixedSize(100, 40)
        self.arrow_label.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(self.arrow_label)
        
        center_layout.addStretch(1)
        
        # Right side layout for password entry and encryption
        right_layout = QVBoxLayout()
        
        self.encrypted_image_label = QLabel('Encrypted image will be displayed here')
        self.encrypted_image_label.setFixedSize(400, 400)
        self.encrypted_image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        right_layout.addWidget(self.encrypted_image_label)
        
        self.password_entry = QLineEdit(self)
        self.password_entry.setFixedSize(400, 30)
        self.password_entry.setPlaceholderText('Enter password or press generate!')
        right_layout.addWidget(self.password_entry)
        
        self.generate_button = QPushButton('Generate Password')
        self.generate_button.setFixedSize(400, 30)
        self.generate_button.clicked.connect(self.generate_password)
        right_layout.addWidget(self.generate_button)
        
        self.encrypt_button = QPushButton('Encrypt')
        self.encrypt_button.setFixedSize(400, 30)
        self.encrypt_button.clicked.connect(self.encrypt_image)
        right_layout.addWidget(self.encrypt_button)
        
        right_layout.addStretch(1)
        
        # Combine layouts
        main_layout.addLayout(left_layout)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)
        
        # Set main widget and layout
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        self.image_path = None
    
    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg *.bmp)')
        if file_name:
            self.image_label.setPixmap(QPixmap(file_name).scaled(400, 400))
            self.image_path = file_name
    
    def generate_password(self):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        self.password_entry.setText(password)
    
    def encrypt_image(self):
        if self.image_path and self.password_entry.text():
            from xor_encrypt import xor_encrypt  # Import the function from xor-encrypt.py
            password = self.password_entry.text()
            xor_encrypt(self.image_path, password)
            self.encrypted_image_label.setPixmap(QPixmap('encrypted_image.png').scaled(400, 400))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
