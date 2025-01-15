"""
🚦Traffic Light Simulator
 Simulate a traffic light that changes colors after a set time.
"""
import tkinter as tk

class TrafficLightSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulator")

        # Canvas for the traffic light
        self.canvas = tk.Canvas(root, width=200, height=400, bg="white")
        self.canvas.pack(pady=20)

        # Draw the traffic light structure
        self.canvas.create_rectangle(50, 50, 150, 350, fill="black")
        self.red_light = self.canvas.create_oval(70, 70, 130, 130, fill="gray")
        self.yellow_light = self.canvas.create_oval(70, 160, 130, 220, fill="gray")
        self.green_light = self.canvas.create_oval(70, 250, 130, 310, fill="gray")

        # Traffic light state and controls
        self.state = "Red"  # Initial state
        self.running = False

        # Start and Stop Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=10)

    def start(self):
        """Start the traffic light simulation."""
        if not self.running:
            self.running = True
            self.update_light()

    def stop(self):
        """Stop the traffic light simulation."""
        self.running = False

    def reset(self):
        """Reset the traffic light to its initial state."""
        self.running = False
        self.state = "Red"
        self.update_display()

    def update_light(self):
        """Update the light state and schedule the next update."""
        if not self.running:
            return

        # Cycle through states
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

        self.update_display()

        # Schedule the next update based on the state
        delay = 3000 if self.state == "Red" else 2000  # Red lasts 3s, others 2s
        self.root.after(delay, self.update_light)

    def update_display(self):
        """Update the visual display of the traffic light."""
        # Reset all lights to gray
        self.canvas.itemconfig(self.red_light, fill="gray")
        self.canvas.itemconfig(self.yellow_light, fill="gray")
        self.canvas.itemconfig(self.green_light, fill="gray")

        # Light up the current state
        if self.state == "Red":
            self.canvas.itemconfig(self.red_light, fill="red")
        elif self.state == "Yellow":
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
        elif self.state == "Green":
            self.canvas.itemconfig(self.green_light, fill="green")


# Create the GUI application
root = tk.Tk()
app = TrafficLightSimulator(root)
root.mainloop()
