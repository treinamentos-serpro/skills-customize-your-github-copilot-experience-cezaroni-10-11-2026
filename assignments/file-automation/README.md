# 📘 Atividade: Automação de Arquivos com Python

## 🎯 Objetivo

Use `pathlib`, loops e condicionais para automatizar a organização de arquivos por extensão. Você vai começar listando arquivos e terminar movendo arquivos de uma pasta de teste para subpastas organizadas.

## 📝 Tarefas

### 🛠️ Listar Arquivos da Pasta de Teste

#### Descrição
Complete a função `list_files()` no código inicial para encontrar os arquivos diretamente dentro da pasta `sample_files`.

#### Requisitos
O programa concluído deve:

- Listar apenas arquivos, sem incluir subpastas.
- Mostrar o nome de cada arquivo encontrado.
- Retornar uma lista vazia quando a pasta não contiver arquivos.

### 🛠️ Agrupar Arquivos por Extensão

#### Descrição
Complete a função `group_files_by_extension()` para agrupar os arquivos encontrados de acordo com suas extensões.

#### Requisitos
O programa concluído deve:

- Agrupar extensões sem diferenciar letras maiúsculas de minúsculas.
- Usar o nome `sem-extensao` para arquivos sem extensão.
- Exibir a quantidade de arquivos em cada grupo.

### 🛠️ Organizar os Arquivos em Subpastas

#### Descrição
Complete a função `organize_files()` para criar uma subpasta para cada grupo e mover para ela os arquivos correspondentes.

#### Requisitos
O programa concluído deve:

- Criar uma subpasta para cada extensão dentro de `sample_files`.
- Mover cada arquivo para a subpasta correspondente, sem processar arquivos dentro de outras subpastas.
- Manter os arquivos dentro de `sample_files`; não altere arquivos fora dessa pasta.
- Exibir uma mensagem informando quando a organização terminar.

Para testar, crie alguns arquivos de exemplo dentro de `sample_files` e execute:

```bash
python starter-code.py
```