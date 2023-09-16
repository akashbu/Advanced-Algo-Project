import tkinter as tk
from tkinter import ttk
import random
import time
from input_handling import validate_input
from IntSort import SortInteger 
import matplotlib.pyplot as plt

# Define global variables for user input and sorting results
unsorted_array = []
user_input = ""
flag = False

# Function to handle user input and validation
def handle_user_input():
    global user_input, data_type, flag
    user_input = input_field.get()
#     data_type = data_type_var.get()
    selected_data_label.config(text=f"Selected Option: {user_input}")
    if validate_input(user_input, "number"):
        error_label.config(text="Valid input", foreground="green")
        flag = False
    else:
        error_label.config(text="Invalid input. Please check your data type selection.", foreground="red")


# Function to generate a random array
def generate_array():
    global unsorted_array, flag
    array_size = array_size_entry.get()
    if array_size.isdigit():
        array_size = int(array_size)
        unsorted_array = [random.randint(1, 1000) for _ in range(array_size)]
        array_size_label.config(text="Array generated with size: " + str(array_size))
        flag = True
        # Update the generated_array_text widget with the new array
        generated_array_text.delete(1.0, tk.END)  # Clear previous content
        generated_array_text.insert(tk.END, ', '.join(map(str, unsorted_array)))
    else:
        array_size_label.config(text="Invalid input for array size")

# Function to toggle all checkboxes
def toggle_all_checkboxes():
    checkbox_state = select_all_var.get()
    for var in algorithm_vars:
        var.set(checkbox_state)
# Function to run selected sorting algorithms and plot results
def run_algorithms():
    time_list = {}
    global flag
    selected_algorithms = [algo_var.get() for algo_var in algorithm_vars]
    execution_times = []
    
    for algo_index, selected in enumerate(selected_algorithms):
        if selected == "1":
                 
            if(flag):
                arr_new1 = unsorted_array
            else:
                arr_input = [int(x) for x in user_input.split(",")] 
                arr_new1 = arr_input
            print(arr_new1)
            arr_new = arr_new1.copy()  # Make a copy of the input array
            start_time = time.time()
            if algo_index == 0:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "BubbleSort")
                time_list["Bubble Sort"] = time_consumed*1000000
            elif algo_index == 1:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "InsertionSort")
                time_list["Insertion Sort"] = time_consumed*1000000
            elif algo_index == 2:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "MergeSort")
                time_list["Merge Sort"] = time_consumed*1000000
            elif algo_index == 3:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "QuickSort")
                time_list["Quick Sort"] = time_consumed*1000000
            elif algo_index == 4:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "HeapSort")
                time_list["Heap Sort"] = time_consumed*1000000
            elif algo_index == 5:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "BucketSort")
                time_list["Bucket Sort"] = time_consumed*1000000
            elif algo_index == 6:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "CountingSort")
                time_list["Counting Sort"] = time_consumed*1000000
            elif algo_index == 7:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "RadixSort")
                time_list["Radix Sort"] = time_consumed*1000000
            elif algo_index == 8:
                sorted_array,time_consumed = SortInteger.SortInteger(arr_new, "SelectionSort")
                time_list["Selection Sort"] = time_consumed*1000000
            
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)
        
    # Plot the comparison graph
    print("Selected List:", time_list)
    print("Selected Algorithms:", selected_algorithms)

    plt.figure(figsize=(10, 6))
    plt.bar(time_list.keys(), time_list.values(), color='skyblue')
    plt.ylabel('Execution Time (micro seconds)')
    plt.title('Execution Time of Sorting Algorithms on a Sorted Array')

        # Display the graph
    plt.xticks(rotation=15, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

    # plot_comparison(selected_algorithms, execution_times)


# Create the main window
root = tk.Tk()
root.title("Sorting Algorithm Efficiency Analyzer")

# Create and configure the input frame
input_frame = ttk.Frame(root)
input_frame.pack(padx=20, pady=20)

# Create and configure the input field
input_label = ttk.Label(input_frame, text="Enter comma-separated input:")
input_label.grid(row=1, column=0, sticky=tk.W)

input_field = ttk.Entry(input_frame, width=40)
input_field.grid(row=1, column=1)

validate_button = ttk.Button(input_frame, text="Validate Input", command=handle_user_input)
validate_button.grid(row=1, column=2, padx=10)

error_label = ttk.Label(input_frame, text="", foreground="red")
error_label.grid(row=2, columnspan=3)

# Create and configure the array size field
array_size_label = ttk.Label(input_frame, text="Enter array size:")
array_size_label.grid(row=3, column=0, sticky=tk.W)

array_size_entry = ttk.Entry(input_frame, width=10)
array_size_entry.grid(row=3, column=1)

generate_button = ttk.Button(input_frame, text="Generate Array", command=generate_array)
generate_button.grid(row=3, column=2, padx=10)

# Create a label to display the selected data
selected_data_label = ttk.Label(root, text="")
selected_data_label.pack(padx=20, pady=10)

# Create a label to display the generated array
generated_array_label = ttk.Label(root, text="Generated Array:")
generated_array_label.pack(pady=10)

generated_array_text = tk.Text(root, height=5, width=50)
generated_array_text.pack(pady=10)

# Create and configure the sorting algorithm checkboxes
algorithm_frame = ttk.Frame(root)
algorithm_frame.pack(padx=20, pady=10)

algorithm_labels = [
    "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Bucket Sort", "Counting Sort", "Radix Sort", "Selection Sort"
]

algorithm_vars = [tk.StringVar() for _ in algorithm_labels]

algorithm_checkboxes = [ttk.Checkbutton(algorithm_frame, text=label, variable=var) for label, var in zip(algorithm_labels, algorithm_vars)]


for i, checkbox in enumerate(algorithm_checkboxes):
    checkbox.grid(row=i, column=0, sticky=tk.W)
    

# Create a "Select All" checkbox
select_all_var = tk.IntVar()
select_all_checkbox = ttk.Checkbutton(algorithm_frame, text="Select All", variable=select_all_var)

select_all_checkbox.configure(command=toggle_all_checkboxes)
select_all_checkbox.grid(row=len(algorithm_labels), column=0, sticky=tk.W)

# Create and configure the run button
run_button = ttk.Button(root, text="Run Algorithms & Plot Comparison", command=run_algorithms)
run_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()