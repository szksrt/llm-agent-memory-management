from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

MAX_MEMORY = 5


class MemorySimilarity:
    def __init__(self):

        self.memories = []

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def add(self, text):

        if len(self.memories) < MAX_MEMORY:
            self.memories.append(text)
            return

        all_memories = self.memories + [text]

        embeddings = self.model.encode(
            all_memories,
            convert_to_tensor=True
        )

        sim_matrix = cos_sim(
            embeddings,
            embeddings
        )

        n = len(all_memories)

        max_sim = -1
        remove_idx = -1

        for i in range(n):
            for j in range(i + 1, n):

                if sim_matrix[i][j] > max_sim:
                    max_sim = sim_matrix[i][j]

                    remove_idx = j

        all_memories.pop(remove_idx)

        self.memories = all_memories

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