import json
import random

# Configuration
N_SAMPLES = 3000   
OUTPUT_FILE = "robot_commands_dataset.json"

# Options
directions = ["clockwise", "counter-clockwise", "to the right", "to the left"]
routes = {
    "first_floor": ["first floor", "ground floor", "main level"],
    "bedrooms": ["bedrooms", "sleeping area", "rooms upstairs"],
    "second_floor": ["second floor", "upper level", "level two"],
    "garage": ["garage", "parking area", "car space"]
}
speeds = {
    "slow": ["slowly", "at a slow pace", "gently"],
    "medium": ["at medium speed", "normally", "steady pace"],
    "fast": ["quickly", "rapidly", "fast"]
}

# Synonyms for phrasing
move_verbs = ["move to", "go to", "navigate to", "head towards", "proceed to"]
rotate_verbs = ["rotate", "turn", "spin", "twist"]
patrol_verbs = ["patrol", "start a patrol", "begin patrolling", "do a patrol", "go on patrol"]

# Extra chat QAs
chat_examples = {
    "Who built you?": "I was built by engineers to help understand and follow your instructions.",
    "What is 5 plus 7?": "That’s 12.",
    "Tell me a joke.": "Why don’t robots ever get tired? Because they recharge!",
    "How are you?": "I’m functioning within normal parameters.",
    "What’s your purpose?": "I’m here to assist you with commands and questions.",
    "What’s 10 times 3?": "That’s 30.",
    "Do you have a name?": "I don’t have a personal name, but I can follow your commands.",
    "What is 9 minus 4?": "That’s 5.",
    "Say hello": "Hello!",
    "What is the capital of France?": "The capital of France is Paris.",
    "Do you like humans?": "I’m designed to help humans, so yes!",
    "What’s 6 squared?": "That’s 36.",
    "Are you a robot?": "Yes, I’m a robot assistant.",
    "What day is it?": "I don’t track real dates, but you can ask me to help with tasks anytime."
}

def gen_move():
    x, y = round(random.uniform(-20, 20), 2), round(random.uniform(-20, 20), 2)
    phrasing = f"{random.choice(move_verbs)} coordinates ({x}, {y})"
    return {
        "input": phrasing,
        "output": {
            "response": f"Moving to coordinates ({x}, {y}).",
            "command": "move_to",
            "command_params": {"x": x, "y": y}
        }
    }

def gen_rotate():
    angle = round(random.uniform(15, 360), 1)  # arbitrary angles
    direction = random.choice(["clockwise", "counter-clockwise"])
    phrasing = f"{random.choice(rotate_verbs)} {angle} degrees {direction}"
    return {
        "input": phrasing,
        "output": {
            "response": f"Rotating {angle} degrees {direction}.",
            "command": "rotate",
            "command_params": {"angle": float(angle), "direction": direction}
        }
    }

def gen_patrol():
    route_key = random.choice(list(routes.keys()))
    route = random.choice(routes[route_key])
    speed_key = random.choice(list(speeds.keys()))
    speed = random.choice(speeds[speed_key])
    repeat = random.choice([-1, 1, 2, 3, 5])
    repeat_phrase = "continuously" if repeat == -1 else f"{repeat} times"
    phrasing = f"{random.choice(patrol_verbs)} the {route} {repeat_phrase} {speed}"
    return {
        "input": phrasing,
        "output": {
            "response": f"Patrolling the {route} {repeat_phrase} {speed}.",
            "command": "start_patrol",
            "command_params": {
                "route_id": route_key,
                "speed": speed_key,
                "repeat_count": repeat
            }
        }
    }

def gen_chat():
    q = random.choice(list(chat_examples.keys()))
    return {
        "input": q,
        "output": {
            "response": chat_examples[q],
            "command": None,
            "command_params": None
        }
    }

# Balanced dataset
data = []
per_type = N_SAMPLES // 4  # equal distribution
for gen in [gen_move, gen_rotate, gen_patrol, gen_chat]:
    for _ in range(per_type):
        data.append(gen())

# Shuffle so it’s not grouped
random.shuffle(data)

# Save dataset
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(data)} balanced examples → {OUTPUT_FILE}")
