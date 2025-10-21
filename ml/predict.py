import random

def predict_availability(slot_id):
    # Dummy ML output
    confidence = random.randint(70, 99)
    return {"slot_id": slot_id, "confidence": confidence}

if __name__ == "__main__":
    print(predict_availability("A12"))
