# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

O arquivo git_update vai em todos os arquivos que estão no dicionário "repositories"
e faz um pull do repositório no git, esse arquivo deve permanecer no diretório padrão pra tudo funcionar.

O arquivo install_aliases.py irá instalar atalhos do git além da chamada do script que atualiza
os repositórios e alguns outros comandos no arquivo .bash_profile.

### How do I get set up? ###

* Baixar os dois arquivos para a o diretório padrão
* Editar a variável "workspace_directory" no arquivo git_update.py (Trocar pelo caminho que está seu workpace)
* Executar: python install_aliases.py
* Executar: cat .bash_profile e ver se os comandos foram gerados no fim do arquivo
* Fechar o terminal e abrir outro
* Executar: gupdate do novo terminal em qualquer diretório da máquina

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* adrianolucianoribeiro@gmail.com
