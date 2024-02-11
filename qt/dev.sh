#!/bin/bash

cd /home/antonio/Development/Chickie/qt

./.venv/bin/pyside6-uic \
	   src/views/main.ui \
	-o src/views/main_ui.py

./.venv/bin/pyside6-uic \
	   src/views/loginForm.ui \
	-o src/views/loginForm_ui.py

./.venv/bin/pyside6-uic \
	   src/views/ingrediente_group.ui \
	-o src/views/ingrediente_group_ui.py

./.venv/bin/python3.10 app.py
