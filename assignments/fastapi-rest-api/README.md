# 📘 Tarefa: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST para gerenciar tarefas usando FastAPI e modelos Pydantic. Pratique rotas HTTP, validação de dados, operações CRUD e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Consultar Tarefas pela API

#### Descrição
Complete os endpoints de leitura no código inicial para listar tarefas e consultar uma tarefa pelo identificador. Os dados podem permanecer em memória durante a execução do servidor.

#### Requisitos
O programa concluído deve:

- Definir um modelo de tarefa com `id`, `title` e `completed`.
- Implementar `GET /tasks` para retornar todas as tarefas em formato JSON; inicialmente, a lista pode estar vazia.
- Implementar `GET /tasks/{task_id}` para retornar a tarefa correspondente.
- Retornar o código HTTP `404` quando o identificador solicitado não existir.

### 🛠️ Criar, Atualizar e Remover Tarefas

#### Descrição
Complete os endpoints restantes para permitir que clientes criem tarefas, atualizem seus dados e removam tarefas existentes.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa com identificador único e retornar o código HTTP `201`.
- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente e retornar o código HTTP `204`.
- Retornar `404` ao tentar atualizar ou remover uma tarefa inexistente.
- Usar modelos Pydantic para validar os dados recebidos.
- Permitir testar e consultar a documentação interativa da API em `/docs`.

Para executar a API, instale as dependências e inicie o servidor:

```bash
python -m pip install fastapi uvicorn
python -m uvicorn starter-code:app --reload
```