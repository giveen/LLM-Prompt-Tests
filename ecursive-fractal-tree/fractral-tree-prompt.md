**Role:** You are a Python developer specializing in computer graphics and mathematical visualizations.

**Task:** Create a Python script using Pygame that generates a "Recursive Fractal Tree."
This TASK IS TO BE PERFORMED WITH NO INPUT FROM THE USER.

**Technical Constraints:**
1. **Mathematics:** * Use recursion to draw branches. 
    * Each branch must split into two smaller branches at a specific angle.
    * Use trigonometry (`math.sin` and `math.cos`) to calculate the end coordinates of each branch based on the angle and length.
2. **Dynamic Interaction:** * The "depth" of the recursion or the "angle" of the branches must be controlled by the user's mouse position. 
    * For example: Moving the mouse left-to-right changes the spread angle; moving it up-and-down changes the recursion depth (limit depth to 10-12 to prevent crashes).
3. **Visuals:** * Draw the tree using lines (`pygame.draw.line`). 
    * Implement a "seasonal" color shift: thicker "trunk" branches should be brown, while the thinnest "leaf" branches at the end of the recursion should be green.
4. **Performance:** The tree should re-render in real-time as the mouse moves, maintaining a smooth frame rate.

**Output:** Provide the complete, copy-pasteable Python code upon completion.
