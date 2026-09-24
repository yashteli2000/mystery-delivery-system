Mystery Delivery System
Overview

Mystery Delivery System is a Python-based logistics simulation developed as part of a Python programming assignment.

The system simulates package deliveries between warehouses and destinations. Each package is assigned to the nearest delivery agent based on Euclidean distance. The system then calculates the delivery distance, total distance traveled by each agent, and their delivery efficiency.

Features
Reads and parses JSON input data
Calculates Euclidean distance between two points
Assigns each package to the nearest delivery agent
Calculates warehouse-to-destination delivery distance
Tracks packages delivered by each agent
Calculates total distance traveled
Calculates agent efficiency
Identifies the most efficient agent
Generates a JSON report
Supports multiple test cases
How It Works

The system follows these steps:

Read the input JSON file.
Load warehouses, delivery agents, and packages.
Calculate the distance between each agent and the package warehouse.
Assign the package to the nearest agent.
Calculate the distance from the warehouse to the package destination.
Add the distances to calculate the total delivery distance.
Generate an agent-wise delivery report.
Calculate efficiency for each agent.
Identify the best agent based on the efficiency value.
Save the final report as report.json.
Distance Formula

The system uses the Euclidean distance formula:

distance = √((x2 - x1)² + (y2 - y1)²)

Efficiency

efficiency = total distance / packages delivered
For an agent who delivers zero packages, efficiency is reported as 0 and the agent is not considered when selecting the best agent.

Design Decisions

* All agents are included in the final report, even if they are not assigned any package.
* For an agent with zero delivered packages, efficiency is reported as `0` to avoid division by zero.
* Agents with zero delivered packages are not considered when selecting the best agent.
* The best agent is selected based on the lowest efficiency value among agents who delivered at least one package.

Project Structure
mystery-delivery-system/
│
├── main.py
├── base_case.json
├── report.json
├── Python Assignment(Delivery System).pdf
│
└── Python Assignment(Delivery System Test Cases)/
    ├── test_case_1.json
    ├── test_case_2.json
    ├── test_case_3.json
    ├── test_case_4.json
    ├── test_case_5.json
    ├── test_case_6.json
    ├── test_case_7.json
    ├── test_case_8.json
    ├── test_case_9.json
    └── test_case_10.json
How to Run
Requirements
Python 3
No external Python packages are required.
Run the program

Clone the repository and navigate to the project directory:

git clone https://github.com/yashteli2000/mystery-delivery-system.git
cd mystery-delivery-system

Run the Python program:

python3 main.py

The program generates the delivery report in:

report.json
Input

The input JSON contains:

Warehouse locations
Delivery agent locations
Package information
Package warehouse
Package destination

Example:

{
    "warehouses": {
        "W1": [0, 0],
        "W2": [50, 75]
    },
    "agents": {
        "A1": [5, 5],
        "A2": [60, 60]
    },
    "packages": [
        {
            "id": "P1",
            "warehouse": "W1",
            "destination": [30, 40]
        }
    ]
}
Output

The system generates an agent-wise report containing:

Number of packages delivered
Total distance traveled
Efficiency
Best agent based on the lowest efficiency among agents who delivered at least one package

The output is saved to report.json.

Technologies Used
Python
JSON
json module
math module
Testing

The program was tested using 10 different JSON test cases to verify the delivery assignment and distance calculation logic with different input data.

Assignment

This project was developed as a Python programming assignment based on the Mystery Delivery System scenario.
