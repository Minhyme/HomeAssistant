period = data.get('period', 10)
light = data.get('light', 0)
cycles = data.get('cycles', 0)
setpoint = data.get('setpoint', 24)
threshold = data.get('threshold', 0)
permissive = True if data.get('permissive', 'off') == 'on' else False
status = True if data.get('status', 'off') == 'on' else False
hysteresis = data.get('hysteresis', 50)

#logger.info("Light: %s", light)
#logger.info("Accumulated: %s", accumulated)
#logger.info("Setpoint: %s", setpoint)
#logger.info("Threshold: %s", threshold)
#logger.info("permissive: %s", permissive)
#logger.info("status: %s", status)

def turn_on():
    global status
    if not status:
        status = True
        hass.states.set('input_boolean.growlight_on', 'on')
        hass.services.call('homeassistant', 'turn_on', {'entity_id': 'switch.growlights'})

def turn_off():
    global status
    if status:
        status = False
        hass.states.set('input_boolean.growlight_on', 'off')
        hass.services.call('homeassistant', 'turn_off', {'entity_id': 'switch.growlights'})

if not status and (light < threshold - hysteresis) and permissive:
    turn_on()

if status and light > threshold + hysteresis:
    turn_off()

#logger.info("cycles: %s", cycles)
if status or light > threshold:
    cycles = cycles + 1
    hass.states.set('input_number.growlight_cycles', cycles)

percent = round((cycles * period * 100) / (setpoint * 3600), 2)
hass.states.set('input_number.growlight_percent', percent)

if percent >= 100:
    permissive = False
    hass.states.set('input_boolean.can_enable_growlights', 'off')
    turn_off()
