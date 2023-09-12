import tkinter as tk
from tkinter import ttk
import random
import time
import sys
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if left:
        result += left
    if right:
        result += right
    return result

def generate_array():
    global unsorted_array
    array_size = size_entry.get()
    if array_size.isdigit():
        array_size = int(array_size)
        unsorted_array = [random.randint(1, 1000) for _ in range(array_size)]
        result_label.config(text="Array generated with size: " + str(array_size))
        array_label.config(text="Generated Array: " + ', '.join(map(str, unsorted_array)))
    else:
        result_label.config(text="Invalid input for array size")

def analyze_algorithms():
    selected_algorithms = [algorithm.get() for algorithm in algorithm_vars]
    results_text.delete(1.0, tk.END)
    
    for algo in selected_algorithms:
        arr_copy = unsorted_array.copy()
        start_time = time.time()
        if algo == "Bubble Sort":
            bubble_sort(arr_copy)
        elif algo == "Selection Sort":
            selection_sort(arr_copy)
        elif algo == "Insertion Sort":
            insertion_sort(arr_copy)
        elif algo == "Quick Sort":
            quick_sort(arr_copy)
        elif algo == "Merge Sort":
            arr_copy = merge_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        space_complexity = sys.getsizeof(arr_copy)
        
        results_text.insert(tk.END, f"Algorithm: {algo}\n")
        results_text.insert(tk.END, f"Execution Time: {execution_time:.6f} seconds\n")
        results_text.insert(tk.END, f"Space Complexity: {space_complexity} bytes\n\n")
        
# Create the main window
root = tk.Tk()
root.title("Algorithm Efficiency Analyzer Tool")

# header image for the main app  
header_frame = customtkinter.CTkFrame(root, corner_radius= 30)
header_frame.pack(padx=20, pady=20)

header_image = ImageTk.PhotoImage(Image.open("img/header_image.jpg").resize((700,70)))
header_button = customtkinter.CTkButton(header_frame, image=header_image, fg_color='transparent',text="")
header_button.grid(row=0)

# Create and configure the input frame
input_frame = ttk.Frame(root)
input_frame.pack(padx=20, pady=20)

# Create and configure the array label
array_label = ttk.Label(root, text="")
array_label.pack(pady=10)

size_label = ttk.Label(input_frame, text="Enter array size (or leave empty):")
size_label.grid(row=0, column=0, sticky=tk.W)

size_entry = ttk.Entry(input_frame, width=10)
size_entry.grid(row=0, column=1)

generate_button = ttk.Button(input_frame, text="Generate Array", command=generate_array)
generate_button.grid(row=0, column=2)

# Create and configure the algorithm selection frame
algorithm_frame = ttk.Frame(root)
algorithm_frame.pack(padx=20, pady=10)

algorithm_vars = [tk.StringVar() for _ in range(5)]

algorithm_labels = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Quick Sort", "Merge Sort"]

algorithm_checkboxes = [ttk.Checkbutton(algorithm_frame, text=algorithm_labels[i], variable=algorithm_vars[i]) for i in range(5)]

for i, checkbox in enumerate(algorithm_checkboxes):
    checkbox.grid(row=i, column=0, sticky=tk.W)

analyze_button = ttk.Button(algorithm_frame, text="Analyze Algorithms", command=analyze_algorithms)
analyze_button.grid(row=5, column=0)

# Create and configure the result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Create and configure the results text box
results_text = tk.Text(root, height=10, width=50)
results_text.pack(pady=10)

# Initialize the unsorted array
unsorted_array = []

# Start the Tkinter main loop
root.mainloop()
