# Arnes Kapic 
# Data Structures & Algorithms

# 📦 Delivery Route Optimization Program  
**Author:** Arnes Kapic  
**Course:** Data Structures & Algorithms – C950 (WGU)

## 🔍 Overview

This project demonstrates the application of efficient algorithms and data structures to solve a real-world logistics problem: optimizing delivery routes for a fleet of trucks, while considering time-sensitive constraints and mileage limits.

The program simulates a delivery system that:
- Prioritizes time-sensitive and grouped packages.
- Adheres to delivery restrictions (e.g., delayed packages, grouped delivery requirements).
- Keeps the total mileage under a strict limit (140 miles).
- Scales well with more trucks and packages.

---

## 🧠 F1. Strengths of the Algorithm Used

The program utilizes the **Nearest Neighbor Algorithm** to optimize delivery routes. This algorithm:
- Iteratively selects the next closest location, reducing overall travel time and mileage.
- Ensures time-sensitive packages are prioritized.
- Handles conditional package assignments (e.g., certain packages must be delivered together or on specific trucks).
- Remains flexible and scalable, making it suitable for larger and more complex delivery operations.

---

## ✅ F2. Verification of Requirements

The system meets the project’s requirements in the following ways:
- **Mileage Constraint:** Each truck's total mileage remains under 140 miles.
- **Deadline Awareness:** Packages with deadlines are delivered on time using prioritized routing.
- **Delivery Restrictions:** Delayed, grouped, and truck-specific packages are enforced using metadata in each package’s notes.
- **Efficient Tracking:** Packages and trucks are managed through custom Python classes that facilitate clean data handling and routing logic.

---

## 🔄 F3. Alternative Algorithms Considered

While the Nearest Neighbor approach works well, other algorithms could further enhance performance:

### 1. **Dijkstra’s Algorithm**  
- Finds the absolute shortest path in a graph.
- Could improve precision over Nearest Neighbor by evaluating all paths rather than local optima.
- Ideal for dense networks or highly dynamic routes.

### 2. **Genetic Algorithm**  
- Simulates evolutionary optimization.
- Creates and evolves multiple route sequences to find the most optimal delivery solution.
- Capable of balancing multiple constraints (distance, time, delivery pairing) more robustly than greedy approaches.

---

## 🚀 G. Suggested Improvements

To improve the system further, the following enhancements are suggested:
- **Hybrid Algorithms:** Combining Nearest Neighbor with Dijkstra’s for more accurate routing.
- **Dynamic Updates:** Integrate real-time traffic data to adapt delivery priorities on the fly.
- **Improved UI/UX:** A visual representation of delivery routes and statuses could enhance usability.

---

## 🗃️ H. Verification of Data Structure

The project uses a **Hash Table** to store and manage packages.  
- **Time Complexity:** Constant-time (`O(1)`) lookups by Package ID.
- **Efficiency:** Each package's delivery details (address, city, deadline, status) are easily accessible and updatable.

---

## 🌲 H1. Alternative Data Structures

While the hash table is optimal for this use case, other options were considered:

### 1. **Binary Search Tree (BST)**
- Allows ordered traversal and retrieval.
- Better suited for sorted access but comes with `O(log n)` performance and more overhead.

### 2. **Trie**
- Useful for partial address matching (prefix lookups).
- More complex to implement and memory-intensive, but valuable in large-scale delivery applications.

---

## 📚 Citation

Zybooks. *Data Structures and Algorithms II: C950*. 2023, Western Governors University.  
Accessed at: https://learn.zybooks.com/zybook/WGUC950Template2023


