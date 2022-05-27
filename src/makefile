.PHONY: clean

NAME 	   	:= Protocolo de Codificación Superdensa
VERSION	:= 1.0
DEVELOPERS	:= Carlos Arrieta, Reinaldo Barrera, Ariel Plasencia
COPYRIGHT  	:= Copyright © 2022: $(DEVELOPERS)

run: ## Run the project ;)
	python3 main.py

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

install: ## Install the project dependencies
	pip3 install qiskit

clean: ## Remove temporary files
	rm -rf printer/__pycache__/
	rm -rf superdense_coding/__pycache__/

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
