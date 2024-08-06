# Async Comprehension Project

## Description

This project contains a series of Python scripts that demonstrate the use of asynchronous programming in Python using `async` and `await`.

## Tasks

### Task 0: Async Generator

- **File:** `0-async_generator.py`
- **Description:** A coroutine called `async_generator` that loops 10 times, each time asynchronously waits 1 second, then yields a random number between 0 and 10.

### Task 1: Async Comprehensions

- **File:** `1-async_comprehension.py`
- **Description:** A coroutine called `async_comprehension` that collects 10 random numbers using async comprehension over `async_generator`.

### Task 2: Run time for four parallel comprehensions

- **File:** `2-measure_runtime.py`
- **Description:** A coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`, and measures the total runtime.

## Usage

1. **Run Task 0:**
   ```bash
   ./0-main.py
   ```
2. **Run Task 0:**
   ```bash
   ./1-main.py
   ```
3. **Run Task 0:**
   ```bash
   ./2-main.py
   ```
