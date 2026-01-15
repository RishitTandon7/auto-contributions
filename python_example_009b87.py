# Simple Star Tracker Simulation: Estimating Latitude Using Polaris

# Learning Objective:
# This tutorial demonstrates how to simulate a simplified star tracker
# to estimate your latitude on Earth. We will focus on a fundamental
# astronomical principle: the altitude of Polaris (the North Star) above
# the horizon directly corresponds to your latitude in the Northern Hemisphere.

# Imports needed for mathematical operations and date/time handling.
import math
import datetime

# --- Constants ---
# We'll use some approximate values for celestial bodies and Earth.
# In a real star tracker, these would be precise and dynamic.

# Approximate Right Ascension (RA) and Declination (Dec) for Polaris.
# RA and Dec are celestial coordinates, similar to longitude and latitude on Earth.
# Polaris's Declination is very close to the celestial North Pole.
# For simplicity, we'll use a constant value.
POLARIS_DECLINATION_DEGREES = 89.2  # Degrees

# Earth's radius in kilometers. Not directly used in this latitude calculation,
# but useful for context in broader geodetic calculations.
EARTH_RADIUS_KM = 6371

# --- Core Functionality ---

def degrees_to_radians(degrees):
    # Converts degrees to radians. Many trigonometric functions in Python's
    # math module expect angles in radians.
    return degrees * math.pi / 180

def radians_to_degrees(radians):
    # Converts radians to degrees. Useful for interpreting results.
    return radians * 180 / math.pi

def calculate_latitude_from_polaris_altitude(polaris_altitude_degrees):
    # This is the core logic of our simplified star tracker.
    # In the Northern Hemisphere, the altitude of Polaris above the horizon
    # is approximately equal to the observer's latitude.
    # This works because Polaris is very close to the celestial North Pole.
    # As you move north, Polaris appears higher in the sky.

    # Input validation: Latitude cannot be less than 0 for this simplified model.
    if polaris_altitude_degrees < 0:
        print("Warning: Polaris altitude cannot be negative. Assuming 0 degrees.")
        return 0

    # In a real star tracker, we'd measure Polaris's altitude using star sensors.
    # Here, we're directly using the altitude as input.
    # For the Northern Hemisphere, latitude = Polaris altitude.
    # This is a simplification; for Southern Hemisphere users, Polaris isn't visible.
    estimated_latitude = polaris_altitude_degrees

    # We return the estimated latitude in degrees.
    return estimated_latitude

# --- Simulation and Usage ---

def simulate_star_tracker_observation(observer_latitude_degrees):
    # This function simulates what a star tracker might "observe"
    # and then uses our calculation function to estimate the latitude.

    print(f"--- Simulating Observation for Observer at {observer_latitude_degrees:.2f} degrees North ---")

    # In a real scenario, the star tracker would measure the angle of Polaris.
    # For this simulation, we'll assume the measured altitude is equal to the
    # actual latitude (which is the principle we're demonstrating).
    # This is the "measurement" our simulated star tracker makes.
    simulated_polaris_altitude_degrees = observer_latitude_degrees

    print(f"Simulated Polaris altitude measured: {simulated_polaris_altitude_degrees:.2f} degrees")

    # Now, we use our calculation function to estimate the latitude based on this measurement.
    estimated_latitude = calculate_latitude_from_polaris_altitude(simulated_polaris_altitude_degrees)

    print(f"Estimated Latitude: {estimated_latitude:.2f} degrees North")
    print("-" * 40)

# --- Example Usage ---
if __name__ == "__main__":
    # This block of code runs only when the script is executed directly.

    print("Welcome to the Simple Star Tracker Simulation!")
    print("We'll estimate your latitude using the North Star (Polaris).\n")

    # --- Scenario 1: Simulating a location in New York City ---
    # Latitude of New York City is approximately 40.7 degrees North.
    simulate_star_tracker_observation(40.7)

    # --- Scenario 2: Simulating a location near the equator ---
    # Latitude of Quito, Ecuador is approximately 0 degrees.
    simulate_star_tracker_observation(0.2)

    # --- Scenario 3: Simulating a location further north ---
    # Latitude of Anchorage, Alaska is approximately 61.2 degrees North.
    simulate_star_tracker_observation(61.2)

    # --- Scenario 4: Demonstrating the limitation of negative input ---
    simulate_star_tracker_observation(-10)