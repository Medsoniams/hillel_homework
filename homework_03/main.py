from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

results: list = []

with open(
    ROOT_DIR / "rockyou.txt", encoding="utf-8", errors="replace"
) as file:
    for line in file:
        if "user" in line:
            print("Line:", line.strip())
            user_input = input(
                "Do you want to add this line to results? (yes/no): "
            ).lower()

            if user_input == "yes":
                results.append(line.strip())

print("\nAmount of added lines:", len(results))
