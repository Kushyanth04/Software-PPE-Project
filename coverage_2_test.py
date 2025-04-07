import os
import sys
import json
import pytest
import coverage
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, List
import warnings
warnings.filterwarnings('ignore')

class CoverageAnalyzer:
    # ... [previous __init__ and run_coverage_for_test methods remain same] ...

    def get_overall_statistics(self) -> Dict:
        """Calculate overall statistics for each test type"""
        stats = {
            'baseline': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'problems': 0},
            'chatgpt': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'problems': 0},
            'claude': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'problems': 0}
        }
        
        for problem, results in self.results.items():
            # Baseline stats
            if results['baseline']['status'] == 'pass':
                stats['baseline']['passed'] += 1
            else:
                stats['baseline']['failed'] += 1
            stats['baseline']['total_coverage'] += results['baseline']['coverage']
            stats['baseline']['problems'] += 1

            # ChatGPT stats (average of zero-shot and few-shot)
            chatgpt_coverage = (results['chatgpt_zero']['coverage'] + results['chatgpt_few']['coverage']) / 2
            if results['chatgpt_zero']['status'] == 'pass' and results['chatgpt_few']['status'] == 'pass':
                stats['chatgpt']['passed'] += 1
            else:
                stats['chatgpt']['failed'] += 1
            stats['chatgpt']['total_coverage'] += chatgpt_coverage
            stats['chatgpt']['problems'] += 1

            # Claude stats (average of zero-shot and few-shot)
            claude_coverage = (results['claude_zero']['coverage'] + results['claude_few']['coverage']) / 2
            if results['claude_zero']['status'] == 'pass' and results['claude_few']['status'] == 'pass':
                stats['claude']['passed'] += 1
            else:
                stats['claude']['failed'] += 1
            stats['claude']['total_coverage'] += claude_coverage
            stats['claude']['problems'] += 1

        # Calculate averages
        for test_type in stats:
            if stats[test_type]['problems'] > 0:
                stats[test_type]['avg_coverage'] = stats[test_type]['total_coverage'] / stats[test_type]['problems']
            else:
                stats[test_type]['avg_coverage'] = 0

        return stats

    def generate_comparison_report(self):
        """Generate comprehensive comparison report"""
        stats = self.get_overall_statistics()
        
        print("\n" + "="*50)
        print("COMPARATIVE ANALYSIS REPORT")
        print("="*50)
        
        # Overall Performance Table
        print("\nOverall Performance:")
        df_overall = pd.DataFrame({
            'Metric': ['Total Problems', 'Tests Passed', 'Tests Failed', 'Avg Coverage (%)'],
            'Baseline': [
                stats['baseline']['problems'],
                stats['baseline']['passed'],
                stats['baseline']['failed'],
                round(stats['baseline']['avg_coverage'], 2)
            ],
            'ChatGPT': [
                stats['chatgpt']['problems'],
                stats['chatgpt']['passed'],
                stats['chatgpt']['failed'],
                round(stats['chatgpt']['avg_coverage'], 2)
            ],
            'Claude': [
                stats['claude']['problems'],
                stats['claude']['passed'],
                stats['claude']['failed'],
                round(stats['claude']['avg_coverage'], 2)
            ]
        }).set_index('Metric')
        
        print(df_overall)
        
        # Difficulty-wise Analysis
        print("\nDifficulty-wise Coverage Analysis:")
        difficulty_stats = {'Easy': {}, 'Medium': {}, 'Hard': {}}
        
        for problem, results in self.results.items():
            difficulty = problem.split('_')[0]
            if difficulty not in difficulty_stats:
                difficulty_stats[difficulty] = {
                    'baseline': [], 'chatgpt': [], 'claude': []
                }
            
            difficulty_stats[difficulty]['baseline'].append(results['baseline']['coverage'])
            difficulty_stats[difficulty]['chatgpt'].append(
                (results['chatgpt_zero']['coverage'] + results['chatgpt_few']['coverage']) / 2
            )
            difficulty_stats[difficulty]['claude'].append(
                (results['claude_zero']['coverage'] + results['claude_few']['coverage']) / 2
            )

        df_difficulty = pd.DataFrame({
            'Difficulty': [],
            'Test Type': [],
            'Avg Coverage (%)': []
        })

        for difficulty in difficulty_stats:
            for test_type in ['baseline', 'chatgpt', 'claude']:
                avg_coverage = sum(difficulty_stats[difficulty][test_type]) / len(difficulty_stats[difficulty][test_type])
                df_difficulty = df_difficulty.append({
                    'Difficulty': difficulty,
                    'Test Type': test_type.capitalize(),
                    'Avg Coverage (%)': round(avg_coverage, 2)
                }, ignore_index=True)

        print(df_difficulty.pivot(index='Difficulty', columns='Test Type', values='Avg Coverage (%)'))

        # Create visualizations
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Overall Coverage Comparison
        plt.subplot(2, 1, 1)
        overall_coverage = [
            stats['baseline']['avg_coverage'],
            stats['chatgpt']['avg_coverage'],
            stats['claude']['avg_coverage']
        ]
        plt.bar(['Baseline', 'ChatGPT', 'Claude'], overall_coverage)
        plt.title('Overall Coverage Comparison')
        plt.ylabel('Average Coverage (%)')

        # Plot 2: Difficulty-wise Coverage
        plt.subplot(2, 1, 2)
        df_difficulty_pivot = df_difficulty.pivot(
            index='Difficulty', 
            columns='Test Type', 
            values='Avg Coverage (%)'
        )
        df_difficulty_pivot.plot(kind='bar')
        plt.title('Coverage by Difficulty Level')
        plt.ylabel('Average Coverage (%)')
        
        plt.tight_layout()
        plt.savefig('coverage_analysis.png')

        # Save detailed results
        with open('coverage_analysis.json', 'w') as f:
            json.dump({
                'overall_stats': stats,
                'difficulty_stats': difficulty_stats
            }, f, indent=2)

def main():
    base_dir = r"C:\Users\kushy\Desktop\SE_PROJECT - Main"
    analyzer = CoverageAnalyzer(base_dir)
    analyzer.analyze_all_problems()
    analyzer.generate_comparison_report()

if __name__ == "__main__":
    main()