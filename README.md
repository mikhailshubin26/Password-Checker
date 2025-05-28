# Password Checker

Простой и удобный десктопный инструмент для проверки надежности паролей, написанный на Python с использованием PySide6.

---

## Особенности

- Ввод пароля с возможностью показать/скрыть символы
- Проверка сложности пароля с подсветкой результата цветом (белый, красный, зелёный)
- Красивый современный интерфейс в синих тонах
- Использование моноширинного шрифта для отображения пароля при показе
- Кроссплатформенный (Windows, Linux, macOS)

---

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/mikhailshubin26/Password-Checker.git
cd Password-Checker
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv venv # Windows
venv\Scripts\activate # Linux/macOS
source venv/bin/activate
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

Запуск

```
python main.py
```

## Компиляция в .exe
Используйте PyInstaller:
```
pyinstaller --onefile --windowed --icon=icon.ico --add-data "img/logo.png;img" --add-data "img/hide_password.png;img" --add-data "img/show_password.png;img" main.py
```

## Лицензия
Этот проект распространяется под лицензией MIT. Подробнее в файле LICENSE.

## Контакты
Автор: Михаил Шубин
GitHub: mikhailshubin26
Email: mishaelshubin@gmail.com

## Поддержать
BTC: ```bc1qllfd0zxmk45j3x53d5dnu9y0ls7vdx60yyk3u4```
ETH: ```0x480468BbB77ef4a4abed20e81656e4CFBcc1C055```
USDT TRC-20: ```TVrv9eQp4cvQ71NhE2uypCksjR9qQZBHcZ```

Ваша поддержка очень ценна ❤️