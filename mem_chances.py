import random
import os

MEMES_RARITY = {
    "bobr.png": 1,
    "ananas.png": 88,
}

def mem_gen():
    memes = os.listdir('p')
    valid_memes = [m for m in memes if m in MEMES_RARITY]
    if not valid_memes:
        raise FileNotFoundError("Нет подходящих мемов в папке 'p'")
    weights = [MEMES_RARITY[m] for m in valid_memes]
    chosen_meme = random.choices(valid_memes, weights=weights, k=1)[0]
    with open(f'p/{chosen_meme}', 'rb') as f:
        return chosen_meme

# Пример использования
print(mem_gen())
