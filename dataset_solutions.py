import json
from pathlib import Path
from leetscrape import GetSolution

class LeetCodeSolutionCollector:
    def __init__(self):
        self.base_path = Path("C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530")
        self.solution_path = Path("leetcode_solutions")
        self.solution_path.mkdir(parents=True, exist_ok=True)

    def collect_solutions(self):
        with open(self.base_path / "baseline_report.json", "r") as f:
            report = json.load(f)
        problems = report.get("problems", [])

        for problem in problems:
            problem_id = problem["problem_id"]
            title_slug = problem["title"].lower().replace(" ", "-")
            solution_file_name = f"{problem_id}_{title_slug}_solution.py"
            solution_file_path = self.solution_path / solution_file_name

            try:
                solution = GetSolution(titleSlug=title_slug).scrape()
                solution_code = solution.code

                if solution_code:
                    with open(solution_file_path, "w", encoding="utf-8") as f:
                        f.write(solution_code)
                    print(f"Solution retrieved for problem: {problem['title']}")
                else:
                    print(f"No solution code found for problem: {problem['title']}")
            except Exception as e:
                print(f"Error retrieving solution for problem: {problem['title']}")
                print(f"Error message: {str(e)}")

        print("\nSolution retrieval completed.")
        print(f"Solutions saved in: {self.solution_path}")

def main():
    collector = LeetCodeSolutionCollector()
    collector.collect_solutions()

if __name__ == "__main__":
    main()