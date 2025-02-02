import json
import os
import re

DATASET_FILE = "dataset.json"
PROBLEMS_DIR = "problems/"

dataset = []

# Function to extract title from problem.md
def extract_title_from_problem(problem_path):
    try:
        with open(os.path.join(problem_path, "problem.md"), "r") as problem_file:
            first_line = problem_file.readline().strip()
            # Look for a line starting with '# Problem:' and clean it up
            match = re.match(r"#\s*Problem:\s*(.*)", first_line)
            if match:
                return match.group(1).strip()
            else:
                return "Unknown Title"
    except Exception as e:
        print(f"Error extracting title from {problem_path}: {e}")
        return "Unknown Title"

# Loop through all problem directories
for problem_dir in os.listdir(PROBLEMS_DIR):
    problem_path = os.path.join(PROBLEMS_DIR, problem_dir)
    
    if os.path.isdir(problem_path) and not problem_dir.startswith('.'):  # Skip non-directories and hidden dirs like .pytest_cache
        try:
            # Open metadata file and read it
            metadata_path = os.path.join(problem_path, "metadata.json")
            if os.path.exists(metadata_path):
                with open(metadata_path, "r") as meta_file:
                    metadata = json.load(meta_file)

                # Retrieve metadata fields with default values
                difficulty = metadata.get("difficulty", "Unknown Difficulty").lower()  # Standardize difficulty value
                tags = metadata.get("tags", [])
                author = metadata.get("author", "Unknown Author")

                # Get the title from metadata, or extract from problem.md if missing
                title = metadata.get("title", extract_title_from_problem(problem_path))

                # Read problem text
                problem_text_path = os.path.join(problem_path, "problem.md")
                with open(problem_text_path, "r") as problem_file:
                    problem_text = problem_file.read()

                # Read solution code
                solution_code_path = os.path.join(problem_path, "solution.py")
                with open(solution_code_path, "r") as solution_file:
                    solution_code = solution_file.read()

                # Append the problem data to the dataset
                dataset.append({
                    "id": problem_dir, 
                    "title": title, 
                    "difficulty": difficulty, 
                    "tags": tags,
                    "author": author,
                    "problem_text": problem_text,
                    "solution_code": solution_code
                })
            else:
                print(f"Warning: {problem_dir}/metadata.json not found.")
        
        except Exception as e:
            print(f"Error processing {problem_dir}: {e}")

# Save dataset as JSON
with open(DATASET_FILE, "w") as outfile:
    json.dump(dataset, outfile, indent=4)

print(f"Dataset generated: {DATASET_FILE}")
