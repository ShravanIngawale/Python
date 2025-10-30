weather = []

with open("weather data.csv", 'r') as f:
    lines = f.readlines()[1:]

    for line in lines:
        date, temp, humidity = line.strip().split(',')
        weather.append({
            "date": date,
            "temperature": float(temp),
            "humidity": float(humidity)
        })

total_temp = 0
max_temp = weather[0]["temperature"]
min_temp = weather[0]["temperature"]
hottest_day = weather[0]["date"]

for day in weather:
    total_temp += day["temperature"]

    if day["temperature"] > max_temp:
        max_temp = day["temperature"]
        hottest_day = day["date"]

    if day["temperature"] < min_temp:
        min_temp = day["temperature"]

average_temp = total_temp / len(weather)

file = [
    "WEATHER DATA SUMMARY\n"
    "=====================\n"
    f"Average Temperature: {average_temp:.2f}°C\n"
    f"Higher Temperature: {max_temp}°C ({hottest_day})\n"
    f"Lowest Temperature: {min_temp}°C\n"
    f"Total Days Analyzed: {len(weather)}\n"
]
with open("Weather Summary.txt", 'w') as f:
    f.writelines(file)

print("Weather summary saved as 'Weather Summary.txt'")