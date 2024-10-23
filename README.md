# Pseudorandom Number Generator

This project generates and analyzes sequences from three pseudorandom number generators (PRNGs): the Linear Congruential Generator (LCG), IBM's RANDU, and Python's built-in PRNG. The goal is to generate sequences, visualize them, and compare their randomness properties.

## Project Structure
## LCG (Linear Congruential Generator)

The Linear Congruential Generator (LCG) is a simple PRNG that uses a basic mathematical rule to generate sequences. The sequences are saved in files following the naming format:  
`LCG1-N{N}U{U0}.txt`, where `N` is the number of values and `U0` is the starting seed.

## RANDU

RANDU is an older PRNG introduced by IBM in the 1960s. Despite its historical importance, RANDU is known for producing poor-quality random numbers, especially in certain situations.

## Python Core PRNG

Python uses the **Mersenne Twister** as its default PRNG. This modern generator is more reliable, offering better randomness and a much longer sequence before repeating. We compare its results with LCG and RANDU.

## Plots & Analysis

The project generates several types of plots based on the sequences:
- **Trajectory plots**: Show how the generated numbers change over time.
- **2D scatter plots**: Compare consecutive numbers in the sequence.
- **3D plots**: Visualize relationships between three consecutive numbers.
