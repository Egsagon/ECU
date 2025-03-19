import ecu

r = ecu.select('text', list(range(0, 100)), max = 0)

print(f'{r = }')