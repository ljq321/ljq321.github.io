import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QFont

class AppleDesktopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("苹果桌面应用")
        self.setGeometry(100, 100, 500, 400)
        
        # 设置背景
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 加载背景图片
        self.background_label = QLabel(central_widget)
        self.background_label.setGeometry(0, 0, 500, 400)
        self.background_label.setScaledContents(True)
        background_pixmap = QPixmap("主机ID介绍.png")
        if not background_pixmap.isNull():
            # 缩放背景图片以适应窗口
            scaled_pixmap = background_pixmap.scaled(500, 400, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.lower()  # 将背景置于底层
        
        # 标题
        title_label = QLabel("苹果桌面控制器")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # 按钮容器
        button_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        
        # 开始按钮
        self.start_button = QPushButton("开始")
        self.start_button.setFixedSize(120, 50)
        self.start_button.setFont(QFont("Arial", 12))
        self.start_button.clicked.connect(self.on_start)
        button_layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        
        # 暂停按钮
        self.pause_button = QPushButton("暂停")
        self.pause_button.setFixedSize(120, 50)
        self.pause_button.setFont(QFont("Arial", 12))
        self.pause_button.clicked.connect(self.on_pause)
        button_layout.addWidget(self.pause_button, alignment=Qt.AlignCenter)
        
        # 重置按钮
        self.reset_button = QPushButton("重置")
        self.reset_button.setFixedSize(120, 50)
        self.reset_button.setFont(QFont("Arial", 12))
        self.reset_button.clicked.connect(self.on_reset)
        button_layout.addWidget(self.reset_button, alignment=Qt.AlignCenter)
        
        # 状态显示
        self.status_label = QLabel("就绪")
        self.status_label.setFont(QFont("Arial", 14))
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)
    
    def on_start(self):
        print("开始按钮被点击")
        self.status_label.setText("运行中")
        self.status_label.setStyleSheet("color: green")
    
    def on_pause(self):
        print("暂停按钮被点击")
        self.status_label.setText("已暂停")
        self.status_label.setStyleSheet("color: orange")
    
    def on_reset(self):
        print("重置按钮被点击")
        self.status_label.setText("就绪")
        self.status_label.setStyleSheet("color: black")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppleDesktopApp()
    window.show()
    sys.exit(app.exec())

'''
图标生成提示词：
为PySide6桌面应用设计三个简约风格的按钮图标，分别是：
1. 开始按钮图标：绿色圆形，内部有一个白色的播放符号
2. 暂停按钮图标：黄色圆形，内部有两个白色的竖线
3. 重置按钮图标：红色圆形，内部有一个白色的逆时针箭头
图标风格要统一，简约现代，适合桌面应用使用，尺寸建议为24x24像素。
'''
