# LLM Agent Memory Management

A simple LLM agent with long-term memory management and forgetting strategies.

## Overview

This project explores memory management methods for LLM agents operating under limited memory capacity.

The agent stores user information as long-term memories, retrieves relevant memories using semantic search, and injects them into prompts during conversation.

To investigate effective memory retention under memory constraints, two memory management strategies are compared:

* FIFO (First-In First-Out)
* Similarity-Based Memory Management

The retrieval performance of each strategy is evaluated in a noisy environment containing both important user information and irrelevant memories.

## Features

* Long-term memory storage
* Semantic memory retrieval using Sentence Transformers
* Integration with Gemini API
* FIFO-based forgetting strategy
* Similarity-based memory management
* Memory capacity constraints
* Retrieval performance evaluation

## Project Structure

```text
.
├── main.py
├── memory.py
├── memory_fifo.py
├── memory_similarity.py
├── generate_dataset.py
├── experiment.py
├── experiment_retrieval.py
├── experiment_evaluation.py
├── README.md
├── pyproject.toml
└── uv.lock
```

## Method

### Memory Storage

User utterances are stored as long-term memories.

Example:

```text
私の名前は鈴木です
私は機械学習が好きです
私は鳥を飼っています
```

### Memory Retrieval

Each memory is converted into an embedding using Sentence Transformers (`all-MiniLM-L6-v2`).

When a query arrives, cosine similarity is calculated between the query embedding and stored memory embeddings.

The most relevant memories are retrieved and provided to the language model.

### Forgetting Strategies

#### 1. FIFO (First-In First-Out)

When memory capacity is exceeded, the oldest memory is removed.

Example:

```text
Memory Limit = 5

Before:
[A, B, C, D, E]

Add F

After:
[B, C, D, E, F]
```

#### 2. Similarity-Based Memory Management

When memory capacity is exceeded, the system identifies highly similar memories and removes redundant information.

This strategy attempts to preserve diverse and informative memories while discarding repetitive content.

## Experimental Setup

Memory Capacity:

```text
5 memories
```

Important Memories:

```text
私の名前は鈴木です
私は埼玉に住んでいます
私は化学を専攻しています
私は機械学習が好きです
私は鳥を飼っています
```

Noise Memories:

```text
今日は0回目の研究をしました
...
今日は19回目の研究をしました
```

Total Memories:

```text
25 memories
```

### Evaluation Queries

```text
私の名前を覚えていますか？
どこに住んでいますか？
専攻は何ですか？
何が好きですか？
ペットを飼っていますか？
```

## Results

| Strategy         | Recall |
| ---------------- | ------ |
| FIFO             | 0/5    |
| Similarity-Based | 4/5    |

### Example Retrieval

Query:

```text
私の名前を覚えていますか？
```

FIFO:

```text
今日は17回目の研究をしました
今日は19回目の研究をしました
今日は18回目の研究をしました
```

Similarity-Based:

```text
私の名前は鈴木です
私は物理学を専攻しています
私はハムスターを飼っています
```

## Discussion

FIFO forgetting removes memories solely based on age.

As a result, important user information can be lost when many irrelevant memories are added later.

The similarity-based strategy preserves diverse information by removing redundant memories instead of simply removing the oldest entries.

In the experiment, the similarity-based approach achieved significantly better retrieval performance than FIFO under the same memory capacity constraint.

## Technologies

* Python
* Sentence Transformers
* all-MiniLM-L6-v2
* Gemini API
* NumPy
* PyTorch

## Future Work

* Importance-aware memory retention
* Top-k retrieval evaluation
* Evaluation on larger conversation datasets
* LLM-based memory summarization
* Integration with more advanced LLM agents

## Motivation

Large Language Models are limited by context length and cannot remember all previous interactions indefinitely.

This project investigates simple memory management techniques that allow LLM agents to retain useful long-term information while operating under memory constraints.