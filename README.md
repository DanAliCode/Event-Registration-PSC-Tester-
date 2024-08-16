# Sistema de Cadastro e Notificação de Eventos

## Descrição do Projeto

Este projeto é um sistema de cadastro e notificação de eventos desenvolvido em Python, seguindo o paradigma de Programação Orientada a Objetos (POO). O sistema permite o cadastro de usuários e eventos, além de gerenciar a participação dos usuários nos eventos. Os dados dos eventos e dos usuários são salvos em arquivos de texto para persistência.

## Funcionalidades

- **Cadastro de Usuário:** Permite o cadastro de usuários com nome de usuário e senha.
- **Login de Usuário:** Verifica o login do usuário antes de permitir o acesso às funcionalidades do sistema.
- **Cadastro de Evento:** Permite o cadastro de eventos com nome, endereço, categoria, horário e descrição.
- **Listagem de Eventos:** Lista os eventos cadastrados em ordem de horário.
- **Confirmação de Participação:** Permite que o usuário confirme a participação em um evento.
- **Cancelamento de Participação:** Permite que o usuário cancele a participação em um evento.
- **Persistência de Dados:** Os eventos são salvos em um arquivo `events.data` e os usuários em `users.data`, sendo carregados ao iniciar o programa.

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicializa o sistema e gerencia o fluxo do programa.
- `user.py`: Define a classe `User` e seus métodos.
- `event.py`: Define a classe `Event` e seus métodos.
- `event_manager.py`: Gerencia o cadastro e a notificação de eventos.
- `data_handler.py`: Lida com a leitura e escrita dos dados dos eventos e usuários nos arquivos `events.data` e `users.data`.

## Metodologias de POO

O projeto foi desenvolvido utilizando as seguintes metodologias de Programação Orientada a Objetos:

- **Encapsulamento:** As classes `User` e `Event` encapsulam os atributos e métodos relacionados a usuários e eventos, respectivamente.
- **Abstração:** As classes abstraem os conceitos de usuário e evento, fornecendo uma interface clara para interação.
- **Herança:** Não foi utilizada herança neste projeto, mas poderia ser aplicada para estender funcionalidades.
- **Polimorfismo:** Não foi utilizado polimorfismo neste projeto, mas poderia ser aplicado para métodos que compartilham a mesma assinatura.

## Salvamento por Arquivo de Texto

Os dados dos eventos são salvos em um arquivo de texto chamado `events.data` e os dados dos usuários em `users.data` utilizando a biblioteca `json` do Python para eventos e manipulação de strings para usuários. Toda vez que o programa é iniciado, os eventos e usuários são carregados a partir destes arquivos para garantir a persistência dos dados.

## Como Executar o Projeto

1. Clone o repositório do GitHub:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
