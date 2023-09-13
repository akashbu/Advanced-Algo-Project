import tkinter as tk
from tkinter import ttk
import random
import time
from input_handling import validate_input, generate_random_array
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort
from plotting import plot_comparison
import customtkinter
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Define global variables for user input and sorting results
user_input = ""
data_type = "number"
array_size = 0
selected_algorithms = []

# Function to handle user input and validation
def handle_user_input():
    global user_input, data_type
    user_input = input_field.get()
    data_type = data_type_var.get()
    selected_data_label.config(text=f"Selected Option: {user_input}\nUser Input: {data_type}")
    if data_type == "number":
        if validate_input(user_input, data_type):
            error_label.config(text="Valid input", foreground="green")
        else:
            error_label.config(text="Invalid input. Please check your data type selection.", foreground="red")
    elif data_type == "string":
        # Validation for string data type (customize as needed)
        if validate_string_input(user_input):
            error_label.config(text="Valid input", foreground="green")
        else:
            error_label.config(text="Invalid input. Please check your data type selection.", foreground="red")

# Function to generate a random array
def generate_array():
    global unsorted_array
    array_size = array_size_entry.get()
    if array_size.isdigit():
        array_size = int(array_size)
        unsorted_array = [random.randint(1, 1000) for _ in range(array_size)]
        array_size_label.config(text="Array generated with size: " + str(array_size))
        
        # Update the generated_array_text widget with the new array
        generated_array_text.delete(1.0, tk.END)  # Clear previous content
        generated_array_text.insert(tk.END, ', '.join(map(str, unsorted_array)))
    else:
        array_size_label.config(text="Invalid input for array size")

# Function to run selected sorting algorithms and plot results
def run_algorithms():
    selected_algorithms = [algo_var.get() for algo_var in algorithm_vars]
    execution_times = []
    
    for algo in selected_algorithms:
        arr_copy = generate_random_array(array_size)  # Generate a random array for each algorithm
        #TODO
        start_time = time.time()
        if algo == "Bubble Sort":
            bubble_sort(arr_copy)
        elif algo == "Insertion Sort":
            insertion_sort(arr_copy)
        elif algo == "Merge Sort":
            merge_sort(arr_copy)
        elif algo == "Quick Sort":
            quick_sort(arr_copy)
        # Add other sorting algorithms as needed
        end_time = time.time()
        
        execution_time = end_time - start_time
        execution_times.append(execution_time)

    # Plot the comparison graph
    #plot_comparison(selected_algorithms, execution_times)
    plt.plot(selected_algorithms, execution_times)
    plt.xlabel('Algorithms')
    plt.ylabel('Execution time')
    plt.savefig('bubble_sort_output.png')
    plt.show()
    #output_image = ImageTk.PhotoImage(Image.open("bubble_sort_output.png").resize((700,700)))
    #output_button.configure(image =output_image)
    #update the output frame in the main app 


# Create the main window
root = customtkinter.CTk()
root.title("Sorting Algorithm Efficiency Analyzer")

# header image for the main app  
header_frame = customtkinter.CTkFrame(root, corner_radius= 30)
header_frame.pack(padx=20, pady=20)

header_image = ImageTk.PhotoImage(Image.open("img/header_image.jpg").resize((700,70)))
header_button = customtkinter.CTkButton(header_frame, image=header_image, fg_color='transparent',text="")
header_button.grid(row=0)

# Create and configure the input frame
input_frame = customtkinter.CTkFrame(root, corner_radius= 30)
input_frame.pack(padx=20, pady=20)

# Create and configure the data type dropdown
data_type_label = customtkinter.CTkLabel(input_frame, text="Select Data Type:", corner_radius=10)
data_type_label.grid(row=0, column=0, sticky=tk.W)

data_type_var = tk.StringVar(value="number")
data_type_dropdown = ttk.Combobox(input_frame, textvariable=data_type_var, values=["number", "string"])
data_type_dropdown.grid(row=0, column=1, padx=10)

# Create and configure the input field
input_label = customtkinter.CTkLabel(input_frame, text="Enter comma-separated input:",corner_radius=20)
input_label.grid(row=1, column=0, sticky=tk.W)

input_field = ttk.Entry(input_frame, width=40)
input_field.grid(row=1, column=1)

validate_button = customtkinter.CTkButton(input_frame, text="Validate Input", command=handle_user_input)
validate_button.grid(row=1, column=2, padx=10)

error_label = customtkinter.CTkLabel(input_frame, text="", fg_color="red", corner_radius=20)
error_label.grid(row=2, columnspan=3)

# Create and configure the array size field
array_size_label = customtkinter.CTkLabel(input_frame, text="Enter array size:",corner_radius=20)
array_size_label.grid(row=3, column=0, sticky=tk.W)

array_size_entry = ttk.Entry(input_frame, width=10)
array_size_entry.grid(row=3, column=1)

generate_button = customtkinter.CTkButton(input_frame, text="Generate Array", command=generate_array, hover_color='light blue')
generate_button.grid(row=3, column=2)

# Create a label to display the selected data
selected_data_label = customtkinter.CTkLabel(root, text="",corner_radius=20)
selected_data_label.pack(padx=20, pady=10)

# Create a label to display the generated array
generated_array_label = customtkinter.CTkLabel(root, text="Generated Array:",corner_radius=20)
generated_array_label.pack(pady=10)

generated_array_text = tk.Text(root, height=5, width=50)
generated_array_text.pack(pady=10)

# Create and configure the sorting algorithm checkboxes
algorithm_frame = customtkinter.CTkFrame(root, fg_color='transparent')
algorithm_frame.pack(padx=20, pady=10)

algorithm_labels = [
    "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"
    # Add more sorting algorithms as needed
]

algorithm_vars = [tk.StringVar() for _ in algorithm_labels]

algorithm_checkboxes = [ttk.Checkbutton(algorithm_frame, text=label, variable=var) for label, var in zip(algorithm_labels, algorithm_vars)]

for i, checkbox in enumerate(algorithm_checkboxes):
    checkbox.grid(row=i, column=0, sticky=tk.W)

# Create a "Select All" checkbox
select_all_var = tk.IntVar()
select_all_checkbox = ttk.Checkbutton(algorithm_frame, text="Select All", variable=select_all_var)

# Function to toggle all checkboxes
def toggle_all_checkboxes():
    checkbox_state = select_all_var.get()
    for var in algorithm_vars:
        var.set(checkbox_state)

# Function to validate string input (customize as needed)
def validate_string_input(input_str):
    # Example: Check if input contains only letters and commas
    return all(c.isalpha() or c == ',' for c in input_str)

select_all_checkbox.configure(command=toggle_all_checkboxes)
select_all_checkbox.grid(row=len(algorithm_labels), column=0, sticky=tk.W)

# Create and configure the run button
run_button = customtkinter.CTkButton(root, text="Run Algorithms & Plot Comparison", command=run_algorithms)
run_button.pack(pady=10)

# Create and configure the output frame
output_frame = customtkinter.CTkFrame(root, corner_radius= 30)
output_frame.pack(padx=20, pady=20)
output_image = ImageTk.PhotoImage(Image.open("img/output.jpg").resize((700,70)))
output_button = customtkinter.CTkButton(output_frame, image=output_image, fg_color='transparent',text="")
output_button.grid(row=0)

# Start the Tkinter main loop
root.mainloop()
