import random


def analyze_image(image_id: str) -> dict:
    skin_types = ["Oily", "Dry", "Combination", "Normal"]
    issues = ["Acne", "Hyperpigmentation", "Wrinkles", "Dark spots"]

    return {
        "image_id": image_id,
        "skin_type": random.choice(skin_types),
        "issues": random.sample(issues, k=1),
        "confidence": round(random.uniform(0.75, 0.95), 2),
    }
