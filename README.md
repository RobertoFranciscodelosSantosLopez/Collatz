# Bit-Dynamics Analysis of the 3n+1 Problem: Stochastic Decay and the Intrinsic Ratio

This repository contains the computational framework and source code used in the manuscript submitted to the *Journal of Number Theory*. The study provides a formalization of the Collatz Conjecture through the lens of 2-adic valuation dynamics and bit-parity entropy.

## 1. Theoretical Framework

This research introduces a state-space classification for odd integers $n$ based on their 2-adic valuation of $3n+1$:

* **Weak Expansive State ($\Omega_w$):** Defined by $v_2(3n+1) = 1$. These states drive local magnitude growth.
* **Strong Reductive State ($\Omega_s$):** Defined by $v_2(3n+1) \ge 2$. These states act as kinetic brakes, liquidating "bit-debt."
* **The Law of Suicidal Expansion:** Postulates that the growth of bit-length increases the statistical probability of encountering high-order Strong States, making collapse inevitable.

### Key Theorem: The Intrinsic Ratio
We demonstrate that the expected ratio of reductive bit-extractions ($k_r$) to expansive multiplications ($k_e$) converges to:
$$E[k_r / k_e] = 2.0$$
Since this exceeds the divergence threshold of $\log_2(3) \approx 1.585$, every trajectory possesses a deterministic negative drift in logarithmic space.

## 2. Contents

* `collatz_simulation.py`: The primary Python script for analyzing high-entropy trajectories.
* `state_transition_map_for_n.png`: A visual mapping of bit-length entropy vs. iteration steps, highlighting the transition between $\Omega_w$ (Red) and $\Omega_s$ (Green).

## 3. Installation & Usage

### Prerequisites
* Python 3.8+
* Libraries: `numpy`, `matplotlib`

### Execution
To reproduce the experimental results for $n \approx 2^{1024}$, run:
```bash
python collatz_simulation.py---
