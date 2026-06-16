# LLM Agent Memory Management

A simple LLM agent with long-term memory management and forgetting strategies.

## Overview

This project explores memory management methods for LLM agents.

The agent stores user information as long-term memories, retrieves relevant memories using semantic search, and injects them into the prompt during conversation.

In addition, different memory management strategies are compared to investigate how forgetting affects memory retrieval performance.

## Features

- Long-term memory storage
- Semantic memory retrieval using Sentence Transformers
- Integration with Gemini API
- FIFO-based forgetting strategy
- Similarity-based memory management
- Retrieval performance evaluation

## Project Structure

```text
.
├── main.py
├── memory.py
├── memory_fifo.py
├── memory_similarity.py
├── experiment.py
├── experiment_retrieval.py
├── experiment_evaluation.py
├── README.md
├── pyproject.toml
└── uv.lock
```

## Method

### Memory Storage

User utterances are stored as text memories.

Example:

```text
私の名前は鈴木です
私は量子コンピュータが好きです
私は犬を飼っています
```

### Memory Retrieval

Each memory is converted into an embedding using Sentence Transformers.

When a new query arrives, cosine similarity is used to retrieve the most relevant memories.

### Forgetting Strategies

#### 1. FIFO (First-In First-Out)

When memory capacity is exceeded, the oldest memory is removed.

Example:

```text
Memory limit = 5

Before:
[A, B, C, D, E]

Add F

After:
[B, C, D, E, F]
```

#### 2. Similarity-Based Memory Management

If a newly added memory is highly similar to an existing memory, it is not stored.

This reduces redundant memories while preserving diverse information.

## Experiments

### Experimental Data

```text
私の名前は鈴木です
私は量子コンピュータが好きです
私は量子計算に興味があります
私は量子情報を勉強しています
私は犬を飼っています
私は猫も好きです
```

### Evaluation Queries

```text
私の名前を覚えていますか？
量子コンピュータについて覚えていますか？
ペットを飼っていますか？
```

### Results

| Strategy | Recall |
|-----------|-----------|
| FIFO | 2/3 |
| Similarity-Based | 3/3 |

### Example

Query:

```text
私の名前を覚えていますか？
```

FIFO:

```text
私は犬を飼っています
```

Similarity-Based:

```text
私の名前は鈴木です
```

### Observation

FIFO forgetting may remove important information simply because it is old.

In contrast, similarity-based memory management preserved important user information such as names while reducing redundancy.

## Technologies

- Python
- Sentence Transformers
- all-MiniLM-L6-v2
- Gemini API
- NumPy
- PyTorch

## Future Work

- Fair comparison under the same memory budget
- Importance-aware memory retention
- Top-k retrieval evaluation
- Evaluation on larger conversation datasets
- Integration with more advanced LLM agents

## Motivation

Large Language Models are limited by context length and cannot remember all previous interactions indefinitely.

This project investigates simple memory management techniques that enable LLM agents to maintain useful long-term memories while operating under memory constraints.

## Author

Physics M.S. student interested in:

- Quantum Computing
- Information Theory
- Artificial Intelligence
- LLM Agents
- Memory Systems