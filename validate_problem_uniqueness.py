import os
import yaml
from pathlib import Path

def check_uniqueness():
    problem_dirs = [d for d in os.listdir('problems') if os.path.isdir(os.path.join('problems', d))]
    seen = set()
    
    for dir_name in problem_dirs:
        if dir_name in seen:
            raise ValueError(f"Duplicate problem directory: {dir_name}")
        seen.add(dir_name)
        
        problem_file = Path(f"problems/{dir_name}/problem.md")
        if not problem_file.exists():
            raise ValueError(f"Missing problem.md in {dir_name}")
            
    print("All problems are unique and valid!")

if __name__ == "__main__":
    check_uniqueness()