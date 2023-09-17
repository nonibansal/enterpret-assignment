SHELL := /bin/bash

# Get directory of repo
CWD := $(shell cd -P -- '$(shell dirname -- "$0")' && pwd -P)

ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

install:
	(\
		python3 -m pip install poetry ;\
		poetry env use python3.11.5 ;\
		poetry install --all-extras;\
	)

model_hoster-run:
	poetry run model_hoster

model_management-run:
	poetry run model_management

model_executor-run:
	poetry run model_executor