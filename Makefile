setup:
	conda env create -f env.yml
	echo "Verify if the pip and python are in the required enviroment"
	which pip
	which python

pip-tools: req/req.in
	pip-compile req/req.in
	pip-sync req/req.txt

run: app.py
	python app.pppy
