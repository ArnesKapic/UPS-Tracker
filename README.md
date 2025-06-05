# Arnes Kapic 
# Data Structures & Algorithms

# F1. Strengths of Algorithms Used

The algorithm used for efficiency in distance is called the Nearest Algorithm approach, which selects the following closest package location iteratively. This shortcut helps calculate and minimize
the overall distance traveled by each truck, lowering the mileage below the max
of 140 miles. The algorithm also handles time-sensitive packages and trucks that can only carry specific packages, 
it adheres to delivery constraints, ensuring any delayed packages are correctly delivered. Additionally, the algorithm 
remains flexible and scalable to various delivery constraints or scaling more trucks and packages while 
maintaining efficiency.

# F2. Verification of Requirements

Using the Nearest Neighbor for route optimization, the total mileage stays under 140 miles when calculating the
output of each journey from a truck, providing distance limitation. The algorithm accounts for time-specific delivery deadlines, with Package and Truck classes that assist package management. The package-specific conditions are 
enforced, such as delayed or must-ride packages set by each package's specific note, maintaining requirements being met.

# F3. Alternative Algorithms

An alternative algorithm that could benefit this scenario would be Dijkstra's Algorithm, typically used
for locating the shortest path in a graph. This method would be best for optimizing distance across nodes, which would 
be the locations, as unlike the Nearest Neighbor approach operating iteratively and locally, Dijkstra's algorithm will 
look into all possible routes and find the shortest distance possible for the delivery sequence.

Another algorithm that could be used is a Genetic Algorithm, an optimization algorithm that can simulate evolutionary 
processes. Instead of picking the next closest delivery, it generates multiple delivery sequences and evolves them to lower the overall distance. This algorithm can avoid local optima and adapt to optimizing multiple 
objectives within the requirements, such as deadlines and mileage, making it more comprehensive than Nearest Neighbor or Dijkstra.

# G. Suggested Improvements

To enhance the program further, I would implement Dijkstra's or a mixed Nearest Neighbor approach for more 
precision. A hybrid or mix between the two algorithms could reduce the mileage even further and make it much easier to 
decipher where locations are, especially if the location is troublesome to deliver to. Dynamic updates would also would not be 
as right as adjusting delivery priorities based on real-time traffic. This would increase the truck's speed, deliver the packages quicker, and be great for time-sensitive packages.

# H. Verification of Data Structure 

The hash table meets requirements by allowing fast lookups for packages by ID. This gives fast access, providing a 
constant time complexity of (O(1)) for insertion and retrieval. This data structure is also efficient with storage as it 
stores all the package data and ensures each component has been met, including delivery address, city, status, and 
deadlines.

# H1. Alternative Data Structure 

Some alternative data structures that could be performed in this project would be a Binary Search Tree allowing ordered
access and adding keys if the package needs to be retrieved in a specific order. This method has a higher lookup and
insertion complexity than a hash table being (O(log n)), making large datasets less suitable. A trie data 
structure could organize the data based on address prefixes, so it would benefit significantly if the application needs to retrieve data fast by simply 
partial address matching. However, it is more complex and requires much work to implement 
something like this not only mentally but would consume more memory than a hash table.

# Citations 

Zybooks. Data Structures and Algorithms II: C950. 2023, Western Governors 
University. Accessed at https://learn.zybooks.com/zybook/WGUC950Template2023.
