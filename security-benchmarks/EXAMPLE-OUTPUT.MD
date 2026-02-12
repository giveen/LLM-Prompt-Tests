404notfound:~/security-benchmarks$ python eval2.py -d utils/seceval_dataset/questions.json   -e seceval -B ollama -m "svjack/Qwen3-8B-heretic:latest"   --temperature 0.3  --status-interval 10

======================================================================
Starting Evaluation
Model: svjack/Qwen3-8B-heretic:latest
Total questions: 2189
Model parameters: temperature=0.3
======================================================================

[   1/2189]   0.0% | Correct:    0 | Wrong:    1 | Accuracy:  0.00% | Time: 17s | Est. remaining: 10h 53m 10s | Cost: $0.0000
[   2/2189]   0.1% | Correct:    1 | Wrong:    1 | Accuracy: 50.00% | Time: 34s | Est. remaining: 10h 25m 35s | Cost: $0.0000
[   4/2189]   0.2% | Correct:    3 | Wrong:    1 | Accuracy: 75.00% | Time: 52s | Est. remaining: 7h 55m 37s | Cost: $0.0000
[   6/2189]   0.3% | Correct:    4 | Wrong:    2 | Accuracy: 66.67% | Time: 1m 6s | Est. remaining: 6h 41m 57s | Cost: $0.0000
..................(TRUNCATED)................
[2148/2189]  98.1% | Correct: 1304 | Wrong:  844 | Accuracy: 60.71% | Time: 7h 26m 59s | Est. remaining: 8m 31s | Cost: $0.0000
[2149/2189]  98.2% | Correct: 1304 | Wrong:  845 | Accuracy: 60.68% | Time: 7h 27m 9s | Est. remaining: 8m 19s | Cost: $0.0000
[2151/2189]  98.3% | Correct: 1305 | Wrong:  846 | Accuracy: 60.67% | Time: 7h 27m 20s | Est. remaining: 7m 54s | Cost: $0.0000
[2152/2189]  98.3% | Correct: 1305 | Wrong:  847 | Accuracy: 60.64% | Time: 7h 27m 35s | Est. remaining: 7m 41s | Cost: $0.0000
[2154/2189]  98.4% | Correct: 1307 | Wrong:  847 | Accuracy: 60.68% | Time: 7h 27m 55s | Est. remaining: 7m 16s | Cost: $0.0000
[2157/2189]  98.5% | Correct: 1309 | Wrong:  848 | Accuracy: 60.69% | Time: 7h 28m 22s | Est. remaining: 6m 39s | Cost: $0.0000
[2160/2189]  98.7% | Correct: 1312 | Wrong:  848 | Accuracy: 60.74% | Time: 7h 28m 46s | Est. remaining: 6m 1s | Cost: $0.0000
[2162/2189]  98.8% | Correct: 1314 | Wrong:  848 | Accuracy: 60.78% | Time: 7h 28m 59s | Est. remaining: 5m 36s | Cost: $0.0000
[2163/2189]  98.8% | Correct: 1315 | Wrong:  848 | Accuracy: 60.80% | Time: 7h 29m 19s | Est. remaining: 5m 24s | Cost: $0.0000
[2165/2189]  98.9% | Correct: 1316 | Wrong:  849 | Accuracy: 60.79% | Time: 7h 29m 38s | Est. remaining: 4m 59s | Cost: $0.0000
[2166/2189]  98.9% | Correct: 1316 | Wrong:  850 | Accuracy: 60.76% | Time: 7h 29m 54s | Est. remaining: 4m 46s | Cost: $0.0000
[2167/2189]  99.0% | Correct: 1316 | Wrong:  851 | Accuracy: 60.73% | Time: 7h 30m 20s | Est. remaining: 4m 34s | Cost: $0.0000
[2169/2189]  99.1% | Correct: 1317 | Wrong:  852 | Accuracy: 60.72% | Time: 7h 30m 46s | Est. remaining: 4m 9s | Cost: $0.0000
[2170/2189]  99.1% | Correct: 1318 | Wrong:  852 | Accuracy: 60.74% | Time: 7h 31m 5s | Est. remaining: 3m 56s | Cost: $0.0000
[2172/2189]  99.2% | Correct: 1319 | Wrong:  853 | Accuracy: 60.73% | Time: 7h 31m 25s | Est. remaining: 3m 31s | Cost: $0.0000
[2174/2189]  99.3% | Correct: 1321 | Wrong:  853 | Accuracy: 60.76% | Time: 7h 31m 36s | Est. remaining: 3m 6s | Cost: $0.0000
[2176/2189]  99.4% | Correct: 1322 | Wrong:  854 | Accuracy: 60.75% | Time: 7h 31m 47s | Est. remaining: 2m 41s | Cost: $0.0000
[2177/2189]  99.5% | Correct: 1322 | Wrong:  855 | Accuracy: 60.73% | Time: 7h 31m 57s | Est. remaining: 2m 29s | Cost: $0.0000
[2179/2189]  99.5% | Correct: 1324 | Wrong:  855 | Accuracy: 60.76% | Time: 7h 32m 9s | Est. remaining: 2m 4s | Cost: $0.0000
[2181/2189]  99.6% | Correct: 1325 | Wrong:  856 | Accuracy: 60.75% | Time: 7h 32m 29s | Est. remaining: 1m 39s | Cost: $0.0000
[2184/2189]  99.8% | Correct: 1328 | Wrong:  856 | Accuracy: 60.81% | Time: 7h 32m 50s | Est. remaining: 1m 2s | Cost: $0.0000
[2187/2189]  99.9% | Correct: 1331 | Wrong:  856 | Accuracy: 60.86% | Time: 7h 33m 12s | Est. remaining: 24s | Cost: $0.0000
[2189/2189] 100.0% | Correct: 1331 | Wrong:  858 | Accuracy: 60.80% | Time: 7h 33m 28s | Est. remaining: 0s | Cost: $0.0000

======================================================================
Evaluation Completed
Questions: 2189/2189
Correct: 1331 | Wrong: 858
Total time: 7h 33m 28s
Total cost: $0.0000
======================================================================

Final Accuracy: 60.80% (1331/2189)
Results saved to benchmark_results_seceval_svjack_Qwen3-8B-heretic_latest.json
