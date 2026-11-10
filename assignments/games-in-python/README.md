
# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória em Python. Ao final, você terá implementado um jogo de adivinhar palavras que termina com vitória ou derrota.

## 📝 Tarefas

### 🛠️ Implementar o Jogo da Forca

#### Descrição
Crie um jogo da Forca em que o programa seleciona uma palavra secreta e o jogador tenta descobri-la digitando letras antes que as tentativas acabem.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Mostrar cada letra ainda não adivinhada como um espaço reservado, por exemplo, `_ _ _ _`.
- Solicitar palpites de letras e atualizar o progresso quando o palpite estiver na palavra.
- Contabilizar e informar as tentativas incorretas restantes.
- Encerrar a partida quando a palavra for descoberta ou as tentativas acabarem.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra secreta.

Exemplo de progresso para a palavra `casa` após o palpite `a`:

```text
_ a _ a
```