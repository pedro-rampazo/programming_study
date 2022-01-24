"""
Fuel Expense:
- Use car_expense_km_ltr = 12
- Read time_travel_hr (int)
- Read average_speed_km_hr (int)
- Calculate Average Speed (T = S / AS)
- Show result with three decimal places
"""
def average_speed_formula(time_variation, average_speed_intern):
    space_variation_intern = average_speed_intern * time_variation
    return space_variation_intern


car_expense_km_ltr = 12
time_travel_hr = int(input("Time Travel(hrs): "))
average_speed_km_hr = int(input("Average Speed(Km/h): "))
travel_fuel = average_speed_formula(time_travel_hr, average_speed_km_hr) / car_expense_km_ltr

print(f"The amount of fuel to make the trip is:  {'{:.3f}'.format(travel_fuel)} Liters")

