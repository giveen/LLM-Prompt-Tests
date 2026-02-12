# Test: Recursive Fractal Tree

This test evaluates an agent's ability to handle complex mathematical visualizations, recursive logic, and real-time user input.

## 🎯 Objective
To generate a tree structure using recursion that dynamically reacts to mouse movement. This tests the agent's understanding of trigonometry, coordinate systems, and performance-heavy recursive calls.

## 🧠 Why this is a difficult test
1. **Coordinate Inversion:** Pygame uses an inverted Y-axis (0 is top). Agents often draw the tree growing downward into the floor.
2. **Recursive Logic:** The agent must implement a base case (`depth == 0`) to prevent infinite loops and stack overflows.
3. **Parameter Mapping:** Mapping Mouse X and Y to specific mathematical variables (angle and depth) requires precise scaling.
4. **Inverted Visuals:** Agents often struggle to map "thickness" and "color" correctly to the depth, frequently making the trunk thin/green and the leaves thick/brown.

## 📊 Evaluation Results
- **Logic:** ✅ Passed. The agent correctly implemented `math.sin` and `math.cos`.
- **Physics:** ✅ Passed. The Y-axis inversion was handled correctly.
- **Visuals:** ⚠️ Partial. While the tree grows correctly, the thickness and color gradients were inverted (twigs thicker than the trunk).




https://github.com/user-attachments/assets/b4b9da65-86fc-4e29-8a8d-66556d68b464

