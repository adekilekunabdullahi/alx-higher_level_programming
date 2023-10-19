-- import database
-- code
SELECT city, AVG(temperature * 9/5 + 32) AS avg_temp
FROM weather_data
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;

