install:
	poetry install

uninstall:
	pip uninstall hexlet-code


build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


do:
	make uninstall
	make build
	make publish
	make package-install
	poetry update
