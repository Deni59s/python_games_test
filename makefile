install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8 brain_games
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
again:
	poetry build
	python3 -m pip install --user dist/*.whl
	pip install --user dist/*.whl --force-reinstall