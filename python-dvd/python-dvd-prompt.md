The Agent Test Prompt

Role: You are a Python developer specializing in physics-based animations and the Pygame library.

Task: Create a standalone Python script that replicates the classic "DVD Player" bouncing screensaver.

Technical Constraints:

    Visuals: Instead of a rectangle, render the text "DVD" using a bold system font. The background must be black.

    Physics: * The simulation must run at 60 FPS for smooth motion.

        Use vector-based movement (Velocity_X and Velocity_Y).

        Implement Elastic Collisions: The text must bounce perfectly off the edges of the window without "bleeding" off-screen or getting stuck in the walls.

    Behavioral Logic:

        Color Cycling: Every time the text hits a boundary, its color must change to a new, random bright RGB color.

        Corner Detection: The hitboxes must be pixel-perfect relative to the text size so that the "golden moment" (hitting a corner perfectly) is mathematically possible.

    Code Quality:

        Use a class-based structure (e.g., a DVDLogo class).

        Avoid re-rendering the font inside the main loop for performance; only re-render the surface when the color changes.

        Include a simple "event loop" that allows the user to close the window gracefully.

Output: Provide the complete, copy-pasteable Python code.
