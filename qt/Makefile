compile:
	poetry run pyside6-uic \
		   src/views/main.ui \
		-o src/views/main_ui.py

	poetry run pyside6-uic \
		   src/views/loginForm.ui \
		-o src/views/loginForm_ui.py

	poetry run pyside6-uic \
		   src/views/ingrediente_group.ui \
		-o src/views/ingrediente_group_ui.py

lines:
	poetry run python scripts/lines.py

dev:
	make compile
	poetry run python app.py

build:
	rm -rf dist
	rm -rf build

	# poetry run pyinstaller --name="Chiquitos" --windowed app.py
	poetry run cxfreeze -c app.py --target-dir dist/Chiquitos
	mv ./dist/Chiquitos/app ./dist/Chiquitos/Chiquitos

run:
	./dist/Chiquitos/Chiquitos

