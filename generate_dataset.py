import random

names = [
    "鈴木",
    "佐藤",
    "高橋",
    "田中",
    "渡辺"
]

cities = [
    "東京",
    "埼玉",
    "千葉",
    "横浜",
    "大阪"
]

majors = [
    "物理学",
    "情報科学",
    "数学",
    "化学",
    "電気工学"
]

hobbies = [
    "量子コンピュータ",
    "機械学習",
    "数学",
    "読書",
    "ゲーム"
]

pets = [
    "犬",
    "猫",
    "鳥",
    "ハムスター",
    "うさぎ"
]

memories = []

person = {
    "name": random.choice(names),
    "city": random.choice(cities),
    "major": random.choice(majors),
    "hobby": random.choice(hobbies),
    "pet": random.choice(pets),
}

memories.append(
    f"私の名前は{person['name']}です"
)

memories.append(
    f"私は{person['city']}に住んでいます"
)

memories.append(
    f"私は{person['major']}を専攻しています"
)

memories.append(
    f"私は{person['hobby']}が好きです"
)

memories.append(
    f"私は{person['pet']}を飼っています"
)

for i in range(20):

    memories.append(
        f"今日は{i}回目の研究をしました"
    )


test_cases = [
    (
        "私の名前を覚えていますか？",
        [f"私の名前は{person['name']}です"]
    ),
    (
        "どこに住んでいますか？",
        [f"私は{person['city']}に住んでいます"]
    ),
    (
        "専攻は何ですか？",
        [f"私は{person['major']}を専攻しています"]
    ),
    (
        "何が好きですか？",
        [f"私は{person['hobby']}が好きです"]
    ),
    (
        "ペットを飼っていますか？",
        [f"私は{person['pet']}を飼っています"]
    )
]

if __name__ == "__main__":

    print("=== MEMORIES ===")

    for memory in memories:
        print(memory)

    print()

    print("=== TEST CASES ===")

    for query, answers in test_cases:
        print(query)
        print(answers)
        print()