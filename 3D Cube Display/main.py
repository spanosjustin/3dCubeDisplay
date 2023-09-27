## 3D Display
import tkinter as tk
    
# Create the main application window
root = tk.Tk()

# Set the window title
root.title("3D Cube Display")

# Add widget and functionality
canvas = tk.Canvas(root, width=800, height=700, bg="black")
canvas.pack()

# Add 3D 'Background'
canvas.create_polygon(0, 710, 0, 0,  400, 350, 400, 350, fill="#09a800", outline="")
canvas.create_polygon(810,0,810,710, 400, 350, 400, 350, fill="#09a800", outline="")

# Control Box
canvas.create_rectangle(50,590,750,690, fill="darkblue", outline="")



# Main Cube          Mid Point   Right     Back Mid
canvas.create_polygon(400,300,  294,275,   400,255,   506,275, fill="#1048bc", outline="")




# Load Image
rArrow_Img = tk.PhotoImage(file="right.png")
lArrow_Img = tk.PhotoImage(file="left.png")
scalingFactor = 8;

# Resize Photos
rArrow_Sized = rArrow_Img.subsample(scalingFactor, scalingFactor)
lArrow_Sized = lArrow_Img.subsample(scalingFactor, scalingFactor)

# Create labels and widgets to display the images
rArrow = tk.Label(root, image=rArrow_Sized)
lArrow = tk.Label(root, image=lArrow_Sized)

# Add the Label to the Widget to the canvas
canvas.create_window(315, 640, anchor=tk.W, window=lArrow)
canvas.create_window(415, 640, anchor=tk.W, window=rArrow)

# Start the Tkinter main loop
root.mainloop()
