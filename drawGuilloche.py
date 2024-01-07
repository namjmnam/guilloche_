import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, colorchooser
import tkinter as tk
from tkinter import ttk


# ... [Other parts of the script remain unchanged] ...

def save_plot_with_graph():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if file_path:
        dpi = 320  # This value will give you 4K resolution for a 12x6.75 inches figure
        fig.set_size_inches(12, 6.75)  # Set the figure size
        fig.savefig(file_path, dpi=dpi)

def save_pattern_only():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if file_path:
        dpi = 320  # This value will give you 4K resolution for a 12x6.75 inches figure
        fig.set_size_inches(12, 6.75)  # Set the figure size
        ax.axis('off')  # Turn off the axis
        fig.savefig(file_path, transparent=True, bbox_inches='tight', pad_inches=0, dpi=dpi)
        ax.axis('on')  # Turn the axis back on
        canvas.draw()

# ... [Rest of the script remains unchanged] ...

def generate_guilloche(a, b, c, frequency, phase, step, t_max, m, n):
    t = np.linspace(0, t_max, step)
    # More complex formula
    x = (a + b) * np.cos(m * t + phase) - c * np.cos((a/b + frequency) * t)
    y = (a + b) * np.sin(n * t + phase) - c * np.sin((a/b + frequency) * t)
    return x, y
    # ... [Previous parts of the script] ...

def plot_mirrored_pattern():
    a = slider_a.get()
    b = slider_b.get()
    c = slider_c.get()
    frequency = slider_frequency.get()
    phase = slider_phase.get()
    step = slider_step.get()
    t_max = slider_t_max.get() * np.pi
    m = slider_m.get()
    n = slider_n.get()

    # Generate the original pattern
    x, y = generate_guilloche(a, b, c, frequency, phase, step, t_max, m, n)

    ax.clear()
    # Plot the original and mirrored patterns
    ax.plot(x, y, color=color_var.get())
    ax.plot(-(x+1), y, color=color_var.get())  # Mirrored horizontally
    ax.plot(x, -(y+1), color=color_var.get())  # Mirrored vertically
    ax.plot(-(x+1), -(y+1), color=color_var.get())  # Mirrored both horizontally and vertically
    ax.set_aspect('equal', adjustable='box')
    canvas.draw()

def update_plot(event=None):
    a = slider_a.get()
    b = slider_b.get()
    c = slider_c.get()
    frequency = slider_frequency.get()
    phase = slider_phase.get()
    step = slider_step.get()
    t_max = slider_t_max.get() * np.pi
    m = slider_m.get()
    n = slider_n.get()
    x, y = generate_guilloche(a, b, c, frequency, phase, step, t_max, m, n)

    
    ax.clear()
    ax.plot(x, y, color=color_var.get())
    ax.set_aspect('equal', adjustable='box')
    canvas.draw()

def save_plot_with_graph():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if file_path:
        # Calculate the figure size for a 4K resolution
        dpi = 100
        fig.set_size_inches(3840 / dpi, 2160 / dpi)
        fig.savefig(file_path, dpi=dpi)

def save_pattern_only():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if file_path:
        # Calculate the figure size for a 4K resolution
        dpi = 100
        fig.set_size_inches(3840 / dpi, 2160 / dpi)
        ax.axis('off')  # Turn off the axis
        fig.savefig(file_path, transparent=True, bbox_inches='tight', pad_inches=0, dpi=dpi)
        ax.axis('on')  # Turn the axis back on
        canvas.draw()
def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    color_var.set(color_code[1])

root = tk.Tk()
root.title("Guilloché Pattern Generator")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Creating a separate window for the plot
plot_window = tk.Toplevel(root)
plot_window.title("Guilloché Pattern")
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=plot_window)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

slider_length = 400  # Length of sliders in pixels

# Sliders for a, b, c, frequency, phase, step, t_max
slider_a = tk.Scale(frame, from_=1, to=50, resolution=0.001, orient=tk.HORIZONTAL, length=slider_length, label="a", command=update_plot)
slider_a.grid(row=0, column=0, sticky="ew")

slider_b = tk.Scale(frame, from_=1, to=50, resolution=0.001, orient=tk.HORIZONTAL, length=slider_length, label="b", command=update_plot)
slider_b.grid(row=1, column=0, sticky="ew")

slider_c = tk.Scale(frame, from_=1, to=100, resolution=0.001, orient=tk.HORIZONTAL, length=slider_length, label="c", command=update_plot)
slider_c.grid(row=2, column=0, sticky="ew")

slider_frequency = tk.Scale(frame, from_=0.1, to=10, resolution=0.0001, orient=tk.HORIZONTAL, length=slider_length, label="Frequency", command=update_plot)
slider_frequency.grid(row=3, column=0, sticky="ew")

slider_phase = tk.Scale(frame, from_=0, to=2*np.pi, resolution=0.0001, orient=tk.HORIZONTAL, length=slider_length, label="Phase", command=update_plot)
slider_phase.grid(row=4, column=0, sticky="ew")

slider_step = tk.Scale(frame, from_=100, to=10000, resolution=1, orient=tk.HORIZONTAL, length=slider_length, label="Steps", command=update_plot)
slider_step.set(10000)  # Default value
slider_step.grid(row=5, column=0, sticky="ew")

slider_t_max = tk.Scale(frame, from_=2, to=50, resolution=0.01, orient=tk.HORIZONTAL, length=slider_length, label="t_max (π)", command=update_plot)
slider_t_max.set(24)  # Default value
slider_t_max.grid(row=6, column=0, sticky="ew")

slider_m = tk.Scale(frame, from_=1, to=2, resolution=0.0001, orient=tk.HORIZONTAL, length=slider_length, label="m", command=update_plot)
slider_m.grid(row=7, column=0, sticky="ew")

slider_n = tk.Scale(frame, from_=1, to=2, resolution=0.0001, orient=tk.HORIZONTAL, length=slider_length, label="n", command=update_plot)
slider_n.grid(row=8, column=0, sticky="ew")


# Color selection and Save buttons
color_var = tk.StringVar(value='#000000')  # Default color: black
color_button = ttk.Button(frame, text="Choose Color", command=choose_color)
color_button.grid(row=9, column=0, sticky="ew")

save_with_graph_button = ttk.Button(frame, text="Save with Graph", command=save_plot_with_graph)
save_with_graph_button.grid(row=10, column=0, sticky="ew")

save_pattern_only_button = ttk.Button(frame, text="Save Pattern Only", command=save_pattern_only)
save_pattern_only_button.grid(row=11, column=0, sticky="ew")

plot_mirrored_button = ttk.Button(frame, text="Plot Mirrored Pattern", command=plot_mirrored_pattern)
plot_mirrored_button.grid(row=12, column=0, sticky="ew")


root.mainloop()
