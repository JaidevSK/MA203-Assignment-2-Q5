# MA203 Assignment 2, Q5: von Karman Equation Solver

This Streamlit web application calculates the Fanning friction factor ($f$) for turbulent flow by solving the von Karman equation. It uses a numerical approach to find the root of the equation based on user-defined Reynolds numbers ($Re$).

## Mathematical Background

The application finds the root of the following von Karman equation:

$$f(f) = \frac{1}{\sqrt{f}} - 4\log_{10}(Re\sqrt{f}) + 0.4 = 0$$

To solve this, the script implements the **Fixed-Point Iteration** method. The equation is rearranged into the form $f = g(f)$, where:

$$g(f) = \frac{1}{(4\log_{10}(Re\sqrt{f}) - 0.4)^2}$$

The iteration runs until the approximate relative error falls below the threshold of $10^{-8}$.

## Features

* **Interactive Input:** A slider to select the Reynolds number ($Re$) between 2,500 and 1,000,000.
* **Numerical Solver:** Calculates the Fanning friction factor ($f$) using Fixed-Point Iteration with an initial guess of $1$.
* **Verification Plot:** Automatically generates a Matplotlib graph of $f(f)$ against $f$ to visually verify the calculated root.

## Requirements

Ensure you have Python installed along with the following dependencies:

```bash
pip install streamlit numpy matplotlib

```

## How to Run

1. Save the code in a Python file (e.g., `app.py`).
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file and run the following command:

```bash
streamlit run app.py

```

This will launch the application in your default web browser.

---

**Author:** Jaidev S. K. (Roll No. 103)

**Course:** MA 203 (Numerical Methods)
