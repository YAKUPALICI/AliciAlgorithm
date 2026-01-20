# Alıcı Algorithm: Discrete Computation Method

This repository contains the official Python implementation and performance benchmarks for the **Alıcı Algorithm**, as presented in the technical paper *"The Alıcı Algorithm: An Optimized Discrete Computation Method for Bounded Arithmetic Series"*.

## 📄 Overview

The Alıcı Algorithm is a computational method designed to calculate the sum of bounded arithmetic progressions in **O(1) Constant Time**, eliminating the need for iterative loops (O(n)). This approach is optimized for resource-constrained systems such as:
- Aerospace Fuel Optimization
- Quantum Energy Summation
- Cloud Budget Capping

## 🚀 Performance Test

The file `performance_test.py` compares the Alıcı Algorithm against a traditional brute-force iterative loop.

**Test Scenario:**
- **Goal:** Sum an arithmetic series up to a limit of 1000 with a micro-increment of 0.000001.
- **Complexity:** ~1 Billion Steps.

### Results (Typical):
| Method | Execution Time | Complexity |
| :--- | :--- | :--- |
| **Traditional Loop** | ~5.2 Seconds | O(n) |
| **Alıcı Algorithm** | ~0.000001 Seconds | O(1) |

## 💻 How to Run

Ensure you have Python installed. Run the script directly in your terminal:

```bash
python performance_test.py
