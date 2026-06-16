from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

MAX_MEMORY = 5


class MemoryFIFO:
    def __init__(self):
        self.memories = []

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def add(self, text):

        self.memories.append(text)

        if len(self.memories) > MAX_MEMORY:
            self.memories.pop(0)

    def get_all(self):
        return self.memories

    def retrieve(self, query, k=3):

        if not self.memories:
                return []

        query_embedding = self.model.encode(
            query,
            convert_to_tensor=True
        )

        memory_embeddings = self.model.encode(
            self.memories,
            convert_to_tensor=True
        )   

        similarities = cos_sim(
            query_embedding,
            memory_embeddings
        )[0]

        top_indices = similarities.argsort(
            descending=True
        )[:k]

        return [
            self.memories[idx]
            for idx in top_indices
        ]