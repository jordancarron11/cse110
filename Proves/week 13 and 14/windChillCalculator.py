def compute_wind_chill(T, V):
    return (35.74 + (0.6215 * T) - 35.75 * (V ** 0.16) + ((0.4275 * T) * (V ** 0.16)))

def convert_temperature(celsius):
    return (celsius *(9 / 5)) + 32

again = 'y'

while again == 'y':
    
    T = float(input('What is the temperature? '))
    V = 0
    scale = input('Fahrenheit or Celsius (F/C)? ').lower()

    if scale == 'f':
        while V < 60:
            V += + 5
            wind_chill = compute_wind_chill(T, V)    
    
            print(f'At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F')
    
    elif scale == 'C':
        T = convert_temperature(T)
        while V < 60:
            V += + 5
            wind_chill = compute_wind_chill(T, V)    
    
            print(f'At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F')

    again = input('Calculate again? (Y/N) ').lower()

print('Thank you, good bye!')