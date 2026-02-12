**Role:** You are a Python developer specializing in computer graphics and mathematical visualizations.

**Task:** Create a Python script using Pygame that generates an interactive "Recursive Fractal Tree." 
**Constraint:** This task must be performed with no additional input from the user.

**Technical Constraints:**
1. **Mathematics & Spatial Logic:**
    * Use recursion to draw branches. Each branch must split into two sub-branches.
    * Use `math.sin` and `math.cos` for coordinate calculation.
    * **CRITICAL:** Account for Pygame's inverted Y-axis (0 is top). The tree must grow UPWARD starting from the bottom-center of the window.
2. **Dynamic Interaction:**
    * The simulation must respond to real-time mouse movement.
    * **Mouse X:** Map to the "spread angle" between branches (0 to 120 degrees).
    * **Mouse Y:** Map to the recursion depth (Limit: 2 to 12 levels to ensure performance).
3. **Visual Fidelity & Gradients:**
    * **Thickness:** The trunk (base level) must be the thickest, with branches becoming progressively thinner as recursion depth increases (minimum 1px).
    * **Color Gradient:** Implement a "Life Cycle" color shift. The base trunk must be Brown `(139, 69, 19)`, transitioning dynamically to Leaf Green `(34, 139, 34)` at the thinnest, final tips.
4. **Performance & Structure:**
    * Use a clear functional or class-based structure.
    * Redraw the background and the tree every frame to allow for smooth animation at 60 FPS.
    * Ensure the base branch (the trunk) is always visible even at low recursion depths.

**Output:** Provide the complete, copy-pasteable Python code.
