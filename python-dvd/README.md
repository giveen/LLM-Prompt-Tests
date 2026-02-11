# Test: Bouncing DVD Physics

This test evaluates the agent's ability to handle high-frequency updates (60 FPS) and coordinate-based collision logic.

## Why this is a good test:
Many models fail this by:
1. Hardcoding a square instead of measuring the text dimensions.
2. Forgetting to handle the right/bottom boundaries (using only 0,0).
3. Causing memory leaks by loading the font file inside the `while` loop.

## Evaluation
- **Success:** The code runs, the text color changes only on impact, and the 'DVD' stays strictly within the window boundaries.
- **Bonus:** Implementation of random starting vectors to ensure the path isn't identical every run.



https://github.com/user-attachments/assets/5a1ae089-0abb-4269-b94b-3b48e688e621

