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

	poetry run pyside6-uic \
	       src/views/pedidos.ui \
		-o src/views/pedidos_ui.py

lines:
	poetry run python scripts/lines.py

dev:
	./dev.sh

b:
	rm -rf dist
	rm -rf build

	# poetry run pyinstaller --name="Chiquitos" --windowed app.py
	# poetry run cxfreeze -c app.py --target-dir dist/Chiquitos
	# mv ./dist/Chiquitos/app ./dist/Chiquitos/Chiquitos

	poetry run python setup.py build

run:
	./dist/Chiquitos/Chiquitos

