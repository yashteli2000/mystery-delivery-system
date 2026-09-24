import json
import math

# Calculate the Euclidean distance between two points
def euclidean_distance(point1,point2):
    ans=(point2[0]-point1[0])**2+(point2[1]-point1[1])**2
    ans=math.sqrt(ans)
    return ans


# Find the agent with the minimum distance
def minimum_distance(distances):
    min_distance=float('inf')
    nearest_agent=''
    for distance,values in distances.items():
        if min_distance > values:
            min_distance=values
            nearest_agent=distance
    return nearest_agent,min_distance


# Find the agent with the lowest efficiency value
def find_best_agent(agent_report):
    min_efficiency=float('inf')
    best_agent_name=''
    for agent,details in agent_report.items():
        
        if details['packages_delivered'] > 0 and min_efficiency > details['efficiency']:
            min_efficiency = details['efficiency']
            best_agent_name=agent

    return best_agent_name           


# Path of the input JSON file
file_path="../Python Assignment -2026/Python Assignment(Delivery System Test Cases)/test_case_4.json"
with open(file_path,"r",encoding='utf-8') as file:

    # Read and parse the JSON data
    data=file.read()
    data=json.loads(data)
    warehouses=data["warehouses"]
    agents=data["agents"]
    packages = data["packages"]

    agent_report = {}
    for agent in agents:
                agent_report[agent] = {
                    "packages_delivered": 0,
                    "total_distance": 0
            }
    assignments = {}
    # Process each package one by one
    for package in packages:

        warehouse = package["warehouse"]
        points2 = warehouses[warehouse]

        agent_distances={}
        
        # Calculate distance from each agent to the package warehouse
        for agent, points1 in agents.items():
            ans = euclidean_distance(points1, points2)
            agent_distances[agent] = ans

        # Select the nearest agent    
        nearest_agent, min_distance = minimum_distance(agent_distances)

        destination = package["destination"]


        # Calculate distance from warehouse to package destination
        delivery_distance = euclidean_distance(points2, destination)

        # Total distance for delivering the package
        total_distance = min_distance + delivery_distance

        # Store package assignment details
        assignments[package["id"]] = {
            "agent": nearest_agent,
            "distance": min_distance,
            "total_distance": total_distance
        }


        # Create report entry for the assigned agent if it does not exist
        if nearest_agent not in agent_report:
            agent_report[nearest_agent] = {
            "packages_delivered": 0,
            "total_distance": 0
        }
            
        # Update the agent's delivery information
        agent_report[nearest_agent]["packages_delivered"] += 1
        agent_report[nearest_agent]["total_distance"] += total_distance

    # Calculate efficiency for each agent
    for agent, details in agent_report.items():
        details["total_distance"] = round(details["total_distance"], 2)
        if details["packages_delivered"] > 0:
            efficiency = details["total_distance"] / details["packages_delivered"]
        else:
            efficiency = 0
        details["efficiency"] = round(efficiency, 2)
    
    # Find the most efficient agent
    best = find_best_agent(agent_report)

    # Add the best agent to the final report
    report = agent_report
    report["best_agent"] = best

    # Save the final report as a JSON file
    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)
