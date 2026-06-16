from memory_fifo import MemoryFIFO
from memory_similarity import MemorySimilarity


data = [
    "私の名前は鈴木です",
    "私は量子コンピュータが好きです",
    "私は量子計算に興味があります",
    "私は量子情報を勉強しています",
    "私は犬を飼っています",
    "私は猫も好きです",
]


test_cases = [
    (
        "私の名前を覚えていますか？",
        ["私の名前は鈴木です"]
    ),
    (
        "量子コンピュータについて覚えていますか？",
        [
            "私は量子コンピュータが好きです",
            "私は量子計算に興味があります",
            "私は量子情報を勉強しています"
        ]
    ),
    (
        "ペットを飼っていますか？",
        [
            "私は犬を飼っています",
            "私は猫も好きです"
        ]
    )
]


fifo = MemoryFIFO()
sim = MemorySimilarity()

for text in data:
    fifo.add(text)
    sim.add(text)


fifo_correct = 0
sim_correct = 0

print("===== FIFO =====")

for query, answer in test_cases:

    retrieved = fifo.retrieve(query)

    print()
    print("Query:", query)
    print("Retrieved:", retrieved)
    print("Expected:", answer)

    if any(r in answer for r in retrieved):
        fifo_correct += 1


print()
print("===== SIMILARITY =====")

for query, answer in test_cases:

    retrieved = sim.retrieve(query)

    print()
    print("Query:", query)
    print("Retrieved:", retrieved)
    print("Expected:", answer)

    if any(r in answer for r in retrieved):
        sim_correct += 1


print()
print("===== RESULT =====")

print(
    f"FIFO Recall: "
    f"{fifo_correct}/{len(test_cases)}"
)

print(
    f"Similarity Recall: "
    f"{sim_correct}/{len(test_cases)}"
)