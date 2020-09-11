SHELL := /bin/bash
PYTHONPATH = .
DEFAULT_GOAL = client

.PHONY: client
client:
	@docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i https://raw.githubusercontent.com/mailhog/MailHog/master/docs/APIv2/swagger-2.0.json \
		-g python \
		-o /local

.PHONY: venv
venv:
	@if [ ! -d .venv ]; then \
		python3 -m venv .venv; \
		source .venv/bin/activate && python3 -m pip install -r requirements.txt; \
		source .venv/bin/activate && python3 -m pip install -r test-requirements.txt; \
	fi

.PHONY: test
test: venv
	source .venv/bin/activate && python3 -m pytest --cov=openapi_client