help: ## Écran d'aide
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-10s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
build: ## Construction de l'image
	docker build -t agentcobra/blockshell .
run: build ## Lance la compilation et l'image docker (garde le conteneur à l'arret)
	docker run -d --name blockshell -p 5000:5000 -v app:/var/www/html/app agentcobra/blockshell
shell: ## Lance bash dans le conteneur
	docker exec -it blockshell bash
test: build ## Lance la compilation et l'image docker (supprime le conteneur à l'arret)
	docker run --rm --name blockshell -p 5000:5000 agentcobra/blockshell
