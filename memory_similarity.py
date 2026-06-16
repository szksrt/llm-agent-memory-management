from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class MemorySimilarity:
    def __init__(self):

        self.memories = []

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.threshold = 0.8

    def add(self, text):

        if len(self.memories) == 0:
            self.memories.append(text)
            return

        text_embedding = self.model.encode(
            text,
            convert_to_tensor=True
        )

        memory_embeddings = self.model.encode(
            self.memories,
            convert_to_tensor=True
        )

        similarities = cos_sim(
            text_embedding,
            memory_embeddings
        )[0]

        if similarities.max() < self.threshold:
            self.memories.append(text)

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