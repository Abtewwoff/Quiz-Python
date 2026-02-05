# PLANEAMENTO.md — Criado por Enzo e Domingos

### 1. Modelo de Dados

Utilizaremos listas de dicionários para gerir as informações em memória. Esta estrutura permite aceder facilmente aos dados e convertê-los para o formato JSON.

**Exemplo 1: Estrutura de uma pergunta**

```python
pergunta_exemplo = {
    "id": 1,
    "pergunta": "Qual é a capital de Portugal?",
    "opcoes": ["Porto", "Lisboa", "Coimbra", "Braga"],
    "resposta": 1, 
    "categoria": "Geografia",
    "dificuldade": "fácil",
    "explicacao": "Lisboa é a capital e a maior cidade de Portugal."
}

```

**Exemplo 2: Estrutura da pontuação do ranking**

```python
score_exemplo = {
    "nome": "Enzo",
    "pontos": 8,
    "total_perguntas": 10,
    "data": "2024-05-20"
}

```

#

### 2. Entradas / Processamento / Saídas

| Fase | Descrição |
| --- | --- |
| **Entradas** | Opções do menu, nome do jogador, respostas (índices 1-4), ficheiro `perguntas.json`. |
| **Processamento** | Validação de tipos, cálculo da pontuação, filtragem por dificuldade, ordenação do Top 10 para a recuperação de pontuações. |
| **Saídas** | Menus formatados, feedback das respostas, resumo final, escrita no ficheiro `pontuacoes.json`. |

#

### 3. Lista de Funções e Responsabilidades

| Função | Descrição | Responsabilidade |
| --- | --- | --- |
| `carregar_json` | Lê os ficheiros JSON e gere erros de ficheiro inexistente. | Estudante A |
| `guardar_score` | Adiciona e regista os novos resultados no histórico. | Estudante A |
| `validar_input` | Garante que o utilizador insere um número válido dentro do intervalo. | Estudante B |
| `exibir_pergunta` | Gere a exibição da pergunta e verifica se a resposta corresponde ao índice correto. | Estudante B |
| `gerar_quiz` | Filtra as perguntas pela dificuldade escolhida e baralha-as. | Estudante C |
| `mostrar_ranking` | Lê o ficheiro de pontuações e exibe os 10 melhores resultados. | Estudante C |

#

### 4. Fluxo do Programa

* **Iniciar o programa** e carregar os dados do ficheiro `perguntas.json`.
* **Exibir o menu principal** com as opções: Jogar, Ranking e Sair.
* **Ler a escolha do utilizador:** se a entrada for inválida, repetir o pedido até obter um número válido.
* **Se a escolha for "Jogar":**
1. Pedir o nome e a dificuldade.
2. Carregar as perguntas correspondentes.
3. Iniciar o **ciclo de jogo**: exibir o enunciado, validar se a resposta está entre 1 e 4, atualizar a pontuação e exibir a explicação.
4. No final, exibir o **resumo de pontos**, guardar a pontuação e propor jogar novamente ou voltar ao menu.


* **Se a escolha for "Ver o ranking":** Ler o ficheiro `pontuacoes.json` e exibir o Top 10 das melhores pontuações, regressando depois ao menu.
* **Se a escolha for "Sair":** Exibir uma mensagem de despedida e encerrar a execução do código.

#

### 5. Estrutura de Ficheiros

* **`main.py`**: Ficheiro principal do jogo. Contém o ciclo principal e o menu.
* **`logica_jogo.py`**: Ficheiro que contém as funções específicas do quiz (perguntas, verificação de respostas, exibição de resultados).
* **`utils.py`**: Ficheiro que contém funções utilitárias (validação de entradas no terminal, etc.).
* **`perguntas.json`**: Ficheiro que contém a base de dados das perguntas.
* **`pontuacoes.json`**: Ficheiro que contém o histórico de classificações.

#

### 6. Plano de Testes (Manual)

1. **Erro de entrada:** Inserir, por exemplo, **"abc"** no menu em vez de um número. (**Esperado: Erro e repetição do pedido**).
2. **Fora do limite:** Inserir "5" quando existem apenas 4 opções. (**Esperado: Mensagem de opção inválida**), via `utils.py`.
3. **Ficheiro inexistente:** Renomear `perguntas.json` e iniciar o jogo. (**Esperado: Mensagem de erro "Ficheiro não encontrado"**), via `utils.py`.
4. **Entrada vazia:** Pressionar `Enter` sem escrever nada. (**Esperado: Sem crash, repetição do pedido**).
5. **Dificuldade:** Escolher "fácil" e verificar se não aparece nenhuma pergunta "difícil".
6. **Ranking:** Verificar se o nome e a pontuação são exibidos corretamente após o fim de uma partida através de um print básico.
7. **Repetição:** Jogar 2 vezes seguidas sem fechar o programa e verificar se os pontos reiniciam corretamente.
8. **Sair:** Sair do programa e verificar se o ficheiro `pontuacoes.json` guardou corretamente as pontuações.
9. **Erro de ficheiro:** Renomear `pontuacoes.json` ou outros ficheiros e testar a robustez do código via `utils.py`.

link para ajudar a criar este ficheiro .md (Documentação em FR) : [Clique aqui](https://datascientist.fr/blog/guide-ultime-creer-fichiers-readme-md-efficaces-markdown)