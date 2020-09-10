SHELL := /bin/bash
PYTHONPATH = .
DEFAULT_GOAL = client

.PHONY: client
client:
	@docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i https://raw.githubusercontent.com/mailhog/MailHog/master/docs/APIv2/swagger-2.0.json \
		-g python \
		-o /local