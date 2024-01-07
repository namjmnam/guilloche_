import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting
from tkinter import filedialog, colorchooser, ttk, Tk, Scale, Toplevel, StringVar


def generate_guilloche(a, b, c, frequency, phase, step, t_max, m, n):
    t = np.linspace(0, t_max, step)
    x = (a + b) * np.cos(m * t + phase) - c * np.cos((a/b + frequency) * t)
    y = (a + b) * np.sin(n * t + phase) - c * np.sin((a/b + frequency) * t)
    return x, y

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

# Function for plotting mirrored patterns
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

    x, y = generate_guilloche(a, b, c, frequency, phase, step, t_max, m, n)

    ax.clear()
    ax.plot(x, y, color=color_var.get())
    ax.plot(-x, y, color=color_var.get())
    ax.plot(x, -y, color=color_var.get())
    ax.plot(-x, -y, color=color_var.get())
    ax.set_aspect('equal', adjustable='box')
    canvas.draw()

# Function to save the plot with the graph

def plot_3d_pattern():
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
    z = np.linspace(0, t_max, step)  # Example z-axis values

    fig_3d = plt.figure()
    ax_3d = fig_3d.add_subplot(111, projection='3d')
    ax_3d.plot(x, y, z, color=color_var.get())
    plt.show()

def save_plot_with_graph():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if file_path:
        dpi = 320
        fig.set_size_inches(12, 6.75)
        fig.savefig(file_path, dpi=dpi)

# Function to save the pattern only
def save_pattern_only():
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png')])
    if file_path:
        dpi = 320
        fig.set_size_inches(12, 6.75)
        ax.axis('off')
        fig.savefig(file_path, transparent=True, bbox_inches='tight', pad_inches=0, dpi=dpi)
        ax.axis('on')
        canvas.draw()

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    color_var.set(color_code[1])

root = Tk()
root.title("Guilloché Pattern Generator")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

plot_window = Toplevel(root)
plot_window.title("Guilloché Pattern")
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=plot_window)
canvas.get_tk_widget().pack(fill='both', expand=True)

# Sliders for adjusting guilloche parameters
slider_a = Scale(frame, from_=1, to=50, resolution=0.001, orient='horizontal', label="a", command=update_plot)
slider_a.grid(row=0, column=0, sticky="ew")
slider_b = Scale(frame, from_=1, to=50, resolution=0.001, orient='horizontal', label="b", command=update_plot)
slider_b.grid(row=1, column=0, sticky="ew")
slider_c = Scale(frame, from_=1, to=100, resolution=0.001, orient='horizontal', label="c", command=update_plot)
slider_c.grid(row=2, column=0, sticky="ew")
slider_frequency = Scale(frame, from_=0.1, to=10, resolution=0.0001, orient='horizontal', label="Frequency", command=update_plot)
slider_frequency.grid(row=3, column=0, sticky="ew")
slider_phase = Scale(frame, from_=0, to=2 * np.pi, resolution=0.0001, orient='horizontal', label="Phase", command=update_plot)
slider_phase.grid(row=4, column=0, sticky="ew")
slider_step = Scale(frame, from_=100, to=10000, resolution=1, orient='horizontal', label="Steps", command=update_plot)
slider_step.set(10000)
slider_step.grid(row=5, column=0, sticky="ew")
slider_t_max = Scale(frame, from_=2, to=50, resolution=0.01, orient='horizontal', label="t_max (π)", command=update_plot)
slider_t_max.set(24)
slider_t_max.grid(row=6, column=0, sticky="ew")
slider_m = Scale(frame, from_=1, to=2, resolution=0.0001, orient='horizontal', label="m", command=update_plot)
slider_m.grid(row=7, column=0, sticky="ew")
slider_n = Scale(frame, from_=1, to=2, resolution=0.0001, orient='horizontal', label="n", command=update_plot)
slider_n.grid(row=8, column=0, sticky="ew")

# Buttons
color_var = StringVar(value='#000000')
color_button = ttk.Button(frame, text="Choose Color", command=choose_color)
color_button.grid(row=9, column=0, sticky="ew")
save_with_graph_button = ttk.Button(frame, text="Save with Graph", command=save_plot_with_graph)
save_with_graph_button.grid(row=10, column=0, sticky="ew")
save_pattern_only_button = ttk.Button(frame, text="Save Pattern Only", command=save_pattern_only)
save_pattern_only_button.grid(row=11, column=0, sticky="ew")
plot_mirrored_button = ttk.Button(frame, text="Plot Mirrored Pattern", command=plot_mirrored_pattern)
plot_mirrored_button.grid(row=12, column=0, sticky="ew")
plot_3d_button = ttk.Button(frame, text="Plot 3D Pattern", command=plot_3d_pattern)
plot_3d_button.grid(row=13, column=0, sticky="ew")

root.mainloop()