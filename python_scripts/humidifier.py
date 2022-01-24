setpoint = data.get('setpoint', 30)
forecastTemp = data.get('forecast_temp', -20)
actualTemp = data.get('actual_temp', -20)
actual = data.get('actual', 45)
offset = data.get('offset', 0)
status = True if data.get('status', 'off') == 'on' else False

#logger.info("Setpoint: %s", setpoint)
#logger.info("ForecastTemp: %s", forecastTemp)
#logger.info("ActualTemp: %s", actualTemp)
#logger.info("Actual: %s", actual)
#logger.info("Offset: %s", offset)
#logger.info("Status: %s", status)

def turn_on():
    global status
    if not status:
        status = True
        hass.states.set('input_boolean.humidifier_on', 'on')
        hass.services.call('homeassistant', 'turn_on', {'entity_id': 'switch.humidifier'})

def turn_off():
    global status
    if status:
        status = False
        hass.states.set('input_boolean.humidifier_on', 'off')
        hass.services.call('homeassistant', 'turn_off', {'entity_id': 'switch.humidifier'})

def get_humidity_from_temp(temp):
    if temp <= -20:
        return 30
    if temp > 0:
        return 45
    return 0.5*temp + 45

minTemp = min(forecastTemp, actualTemp)
#logger.info("Min Temp: %s", minTemp)

humidity = get_humidity_from_temp(minTemp)
#logger.info("Calculated Humidity: %s", humidity)

hass.states.set('input_number.humidity_setpoint', humidity + offset)

if actual < (humidity + offset - 0.5):
    turn_on()
elif actual > (humidity + offset + 0.5):
    turn_off()
