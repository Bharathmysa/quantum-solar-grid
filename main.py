import random

# ==========================================
# Quantum Optimized Energy Grid Simulator
# ==========================================

print("\n⚡ QUANTUM OPTIMIZED ENERGY GRID ⚡")

# ------------------------------------------
# Generate random energy demand for cities
# ------------------------------------------

cities = {
    "Hyderabad": random.randint(50, 100),
    "Mumbai": random.randint(50, 100),
    "Delhi": random.randint(50, 100),
    "Bangalore": random.randint(50, 100)
}

# ------------------------------------------
# Total solar energy available
# ------------------------------------------

solar_energy = 250

print(f"\n🌞 Total Solar Energy Available: {solar_energy} units")

# ------------------------------------------
# Display city demands
# ------------------------------------------

print("\n🏙️ City Energy Demands")

for city, demand in cities.items():
    print(f"{city}: {demand} units")

# ------------------------------------------
# Smart Energy Distribution
# ------------------------------------------

allocation = {}

total_demand = sum(cities.values())

print("\n📡 Energy Distribution")

for city, demand in cities.items():

    # Proportional allocation
    share = (demand / total_demand) * solar_energy

    # Final allocation
    allocation[city] = min(demand, share)

    print(f"{city} receives {allocation[city]:.2f} units")

# ------------------------------------------
# Efficiency Calculation
# ------------------------------------------

used_energy = sum(allocation.values())

wasted_energy = solar_energy - used_energy

efficiency = (used_energy / solar_energy) * 100

print("\n🔋 Energy Statistics")
print(f"Total Used Energy: {used_energy:.2f} units")
print(f"Wasted Energy: {wasted_energy:.2f} units")
print(f"Grid Efficiency: {efficiency:.2f}%")

# ------------------------------------------
# Future Quantum Optimization Note
# ------------------------------------------

print("\n🧠 Future Scope")
print("Quantum optimization algorithms can improve")
print("energy routing and reduce transmission loss.")
