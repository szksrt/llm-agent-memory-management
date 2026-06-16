from memory_fifo import MemoryFIFO
from memory_similarity import MemorySimilarity
from generate_dataset import memories
from generate_dataset import test_cases



fifo = MemoryFIFO()
sim = MemorySimilarity()

for text in memories:
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