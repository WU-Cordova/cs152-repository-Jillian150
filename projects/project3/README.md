**1️⃣ Menu (`list` of `Drink` objects)**
- **Choice:** I used a list to store menu items since the drink options are hardcoded and limited in size.
- **Complexity:**  
  - **Accessing an item (`O(1)`)** — Direct index-based lookup in a small list is constant time.  
  - **Searching for a drink (`O(n)`)** — When a user enters a drink name, we must iterate over the list (`O(n)`) to find a match, but `n` is small (5 items).  
- **Trade-offs:** Lists are simple and efficient for small fixed menus. If the menu were larger and frequently searched, a dictionary (`dict`) with drink names as keys would be better (`O(1)` lookup).  

**2️⃣ Customer Orders (`list` of `CustomerOrder` objects)**
- **Choice:** I used a list (`open_orders`) to maintain a queue of customer orders.  
- **Complexity:**  
  - **Adding an order (`O(1)`)** — Appending to a list is fast.  
  - **Viewing orders (`O(n)`)** — Iterating over all open orders is linear in the number of customers (`n`).  
  - **Removing the next order (`O(1)`)** — Using `.pop(0)` follows **FIFO (First In, First Out)** behavior like a queue.  
- **Trade-offs:** A `deque` (double-ended queue) from `collections` would offer `O(1)` removals from both ends, but a list is simpler given the problem scope.  

**3️⃣ Order Confirmation (`CustomerOrder` holding a `list` of `OrderItem`)**
- **Choice:** Each order holds a list of order items (drinks + customizations).  
- **Complexity:**  
  - **Adding items (`O(1)`)** — Appending an item to an order is fast.  
  - **Viewing items (`O(n)`)** — The program prints all ordered drinks, iterating through the list (`O(n)`).  
- **Trade-offs:** No need for a dictionary since we only track order details per customer in sequence.  

**4️⃣ Open Orders Queue (`list` of CustomerOrder objects)**
- **Choice:** Open orders are stored in a list, allowing processing in order received.  
- **Complexity:**  
  - **Adding an order (`O(1)`)** — New orders are appended to the queue.  
  - **Processing an order (`O(1)`)** — Using `.pop(0)` quickly removes the oldest order.  
- **Trade-offs:** If order prioritization was required (e.g., urgent orders), a heap-based priority queue (`heapq`) would be preferable (`O(log n)` inserts/removals).  

**5️⃣ Completed Orders (`list` of CustomerOrder objects)**
- **Choice:** Completed orders are stored in another list for record-keeping.  
- **Complexity:**  
  - **Adding an order (`O(1)`)** — Orders are appended.  
  - **Viewing all completed orders (`O(n)`)** — Iterating over completed orders is linear in size.  
- **Trade-offs:** If long-term tracking were needed, saving orders in a database would be better than an in-memory list.  

**6️⃣ Sales Tracking (`dictionary` for drinks sold)**
- **Choice:** The dictionary `{drink_name: quantity_sold}` efficiently tracks sales.  
- **Complexity:**  
  - **Updating sales (`O(1)`)** — Adding values to a dictionary is constant time.  
  - **Retrieving totals (`O(1)`)** — Direct key-based lookups for sales counts are fast.  
- **Trade-offs:** A list would require a full scan (`O(n)`) to count occurrences, whereas a dictionary provides immediate access (`O(1)`).  


You can run project in terminal.

Example of it ran: Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 1

📋 Menu:
Bearcat Mocha - $4.50
Caramel Catpuccino - $4.25
Meowcha Latte - $4.75
Hazelnut Cappuccino - $4.00
Matcha Green Tea - $4.50

Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 2

Enter customer name: Jillian

📋 Menu:
Bearcat Mocha - $4.50
Caramel Catpuccino - $4.25
Meowcha Latte - $4.75
Hazelnut Cappuccino - $4.00
Matcha Green Tea - $4.50
Select a drink by name (or type 'done' to finish): Bearcat Mocha
Enter customization (or press enter for none): 

📋 Menu:
Bearcat Mocha - $4.50
Caramel Catpuccino - $4.25
Meowcha Latte - $4.75
Hazelnut Cappuccino - $4.00
Matcha Green Tea - $4.50
Select a drink by name (or type 'done' to finish): done

Order confirmed!

Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit

Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 4
6. Exit
Enter your choice: 4

Enter your choice: 4

✅ Completed Order for Jillian!

✅ Completed Order for Jillian!

✅ Completed Order for Jillian!


Welcome to the Bearcat Bistro!
1. Display Menu
Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
1. Display Menu
2. Take New Order
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
4. Mark Next Order as Complete
5. View End-of-Day Report
5. View End-of-Day Report
6. Exit
Enter your choice: 5

📋 End-of-Day Report
Enter your choice: 5

📋 End-of-Day Report

📋 End-of-Day Report
📋 End-of-Day Report
----------------------------
Total Revenue: $4.50

Welcome to the Bearcat Bistro!
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 6
Exiting Bearcat Bistro. Have a great day!
PS C:\Users\Pooky\OneDrive\Documents\GitHub\cs152-repository-Jillian150>


There is a lack of ordering and editing choices. 

Future Enhancements
- Implement barista authention
- Add estimated preperation time
- More ordering and editing choices




