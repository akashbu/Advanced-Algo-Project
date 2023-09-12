import matplotlib.pyplot as plt

def plot_comparison(algorithm_names, execution_times):
    plt.figure(figsize=(10, 6))
    plt.bar(algorithm_names, execution_times, color=['blue', 'green', 'red', 'purple', 'orange', 'pink', 'brown', 'cyan'])
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Comparison')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
