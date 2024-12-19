from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ImageWindow(QDialog):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Просмотр изображения")
        layout = QVBoxLayout()

        # Отображение изображения
        label = QLabel(self)
        pixmap = QPixmap(image_path)

        # Масштабирование изображения
        scaled_pixmap = pixmap.scaled(
            800, 600,  # Заданные размеры
            Qt.AspectRatioMode.KeepAspectRatio,  # Сохранение пропорций
            Qt.TransformationMode.SmoothTransformation  # Плавное масштабирование
        )
        label.setPixmap(scaled_pixmap)

        # Выравнивание изображения по центру
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)

        # Установка минимального размера окна
        self.setMinimumSize(800, 600)
