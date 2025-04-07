from pathlib import Path

def print_directory_structure():
    # Base paths
    base_dir = Path("dataset_leetcode/dataset_20241126_193530")
    claude_dir = Path("claude_generated_testcases")
    chatgpt_dir = Path("chatgpt_generated_testcases")
    
    print("\nDirectory Structure:\n")
    
    # Print baseline dataset
    print("1. Baseline Dataset")
    print("==================")
    if base_dir.exists():
        for problem_dir in sorted(base_dir.iterdir()):
            if problem_dir.is_dir():
                print(f"\n+--- {problem_dir.name}/")
                for file in sorted(problem_dir.glob("*.*")):
                    print(f"|    +--- {file.name}")
    
    # Print Claude dataset
    print("\n2. Claude Generated Tests")
    print("=======================")
    if claude_dir.exists():
        print(f"\n+--- {claude_dir.name}/")
        if (claude_dir / "problem_outputs").exists():
            print("|    +--- problem_outputs/")
            for problem_dir in sorted((claude_dir / "problem_outputs").iterdir()):
                if problem_dir.is_dir():
                    print(f"|         +--- {problem_dir.name}/")
                    
                    # Print zero-shot and few-shot directories
                    zero_shot = problem_dir / "zero_shot"
                    few_shot = problem_dir / "few_shot"
                    
                    if zero_shot.exists():
                        print(f"|              +--- zero_shot/")
                        for file in sorted(zero_shot.glob("*.*")):
                            print(f"|              |    +--- {file.name}")
                    
                    if few_shot.exists():
                        print(f"|              +--- few_shot/")
                        for file in sorted(few_shot.glob("*.*")):
                            print(f"|              |    +--- {file.name}")
    
    # Print ChatGPT dataset
    print("\n3. ChatGPT Generated Tests")
    print("=========================")
    if chatgpt_dir.exists():
        print(f"\n+--- {chatgpt_dir.name}/")
        if (chatgpt_dir / "problem_outputs").exists():
            print("|    +--- problem_outputs/")
            for problem_dir in sorted((chatgpt_dir / "problem_outputs").iterdir()):
                if problem_dir.is_dir():
                    print(f"|         +--- {problem_dir.name}/")
                    
                    # Print zero-shot and few-shot directories
                    zero_shot = problem_dir / "zero_shot"
                    few_shot = problem_dir / "few_shot"
                    
                    if zero_shot.exists():
                        print(f"|              +--- zero_shot/")
                        for file in sorted(zero_shot.glob("*.*")):
                            print(f"|              |    +--- {file.name}")
                    
                    if few_shot.exists():
                        print(f"|              +--- few_shot/")
                        for file in sorted(few_shot.glob("*.*")):
                            print(f"|              |    +--- {file.name}")

    print("\nNote:")
    print("* Directory paths are shown with trailing /")
    print("* Files are shown with their exact names")
    print("* Each LLM problem has zero-shot and few-shot subdirectories")

def main():
    print_directory_structure()

if __name__ == "__main__":
    main()