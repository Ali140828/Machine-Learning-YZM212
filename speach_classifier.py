from hmmlearn import hmm
import numpy as np

# Model 1 : EV
model_ev = hmm.MultinomialHMM(n_components=2, n_trials=1)
model_ev.startprob_ = np.array([1.0, 0.0])
model_ev.transmat_ = np.array([
    [0.6, 0.4],
    [0.2, 0.8]
])
model_ev.emissionprob_ = np.array([
    [0.7, 0.3], # E
    [0.1, 0.9]  # V
])

# Model 2 : OKUL
model_okul = hmm.MultinomialHMM(n_components=4, n_trials=1) 
model_okul.startprob_ = np.array([1.0, 0.0, 0.0, 0.0])
model_okul.transmat_ = np.array([
    [0.6, 0.4, 0.0, 0.0],
    [0.0, 0.6, 0.4, 0.0],
    [0.0, 0.0, 0.6, 0.4],
    [0.0, 0.0, 0.0, 1.0]
])
model_okul.emissionprob_ = np.array([
    [0.6, 0.4], # O
    [0.5, 0.5], # K
    [0.4, 0.6], # U
    [0.3, 0.7]  # L
])


# Test verisi (yeni ses)
test_sequences = [
    np.array([[1,0],[0,1],[0,1]]),   # test 1
    np.array([[1,0],[1,0],[0,1]]),   # test 2
    np.array([[0,1],[0,1],[1,0]])    # test 3
]

for i, seq in enumerate(test_sequences):
    score_ev = model_ev.score(seq) / len(seq)
    score_okul = model_okul.score(seq) / len(seq)
    print(f"Test {i+1}: EV={score_ev:.3f}, OKUL={score_okul:.3f}")
    
    if score_ev > score_okul:
        print("  Predicted word: EV")
    else:
        print("  Predicted word: OKUL")