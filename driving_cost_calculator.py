# CS1400 Assignment 3: Driving Cost Calculator by Brian Yang

# Add the functions for the assignment below here and above the main function.

# Calculates the cost of a trip for a gas vehicle.
def calculate_gas_vehicle_trip_cost(Miles, Mpg, Gascost):
    gallons = Miles / Mpg
    cost = gallons * Gascost
    return cost

# Calculates the cost of a trip for an electric vehicle.
def calculate_electric_vehicle_trip_cost(Miles, Whpm, Kwhcost):
    kwh = (Whpm / 1000) * Miles
    cost = kwh * Kwhcost
    return cost

# Keep this main function

# calculates trip costs for different distances, and prints results.
def main():

    price_of_gasoline = float(input("What price of gasoline (in dollars per gallon): "))
    price_of_electricity = float(input("What price of electricity (in dollars per kWh): "))


    car_mpg = 24.4
    truck_mpg = 14.2
    ev_whpm = 229

    print()

    for distance in range (50, 501, 50):

        truck_cost = calculate_gas_vehicle_trip_cost(distance, truck_mpg, price_of_gasoline)
        car_cost = calculate_gas_vehicle_trip_cost(distance, car_mpg, price_of_gasoline)
        ev_car_cost = calculate_electric_vehicle_trip_cost(distance, ev_whpm, price_of_electricity)

        print("For a trip of", distance, "miles, the costs are: truck $" + str(round(truck_cost)) + ", car $" + str(round(car_cost)) + ", electric $" + str(round(ev_car_cost)) + ".")

# Keep these lines. It helps Python run the program correctly by calling main when the program is run.
if __name__ == "__main__":
    main()