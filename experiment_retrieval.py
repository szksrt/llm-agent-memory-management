from memory_fifo import MemoryFIFO
from memory_similarity import MemorySimilarity


fifo = MemoryFIFO()
sim = MemorySimilarity()

data = [
    "私の名前は鈴木です",
    "私は量子コンピュータが好きです",
    "私は量子計算に興味があります",
    "私は量子情報を勉強しています",
    "私は犬を飼っています",
    "私は猫も好きです",
]

for text in data:
    fifo.add(text)
    sim.add(text)


query = "私の名前を覚えていますか？"

print("=== FIFO ===")
print(fifo.retrieve(query))

print()

print("=== SIMILARITY ===")
print(sim.retrieve(query))