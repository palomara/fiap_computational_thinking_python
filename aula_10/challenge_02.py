extra_hours = int(input("Insert colaborator's hours: "))
missing_hours = int(input("Insert colaborator's missing hours: "))

h = extra_hours - (2 / 3 * (extra_hours - missing_hours))

if h > 2.400:
    premio = 1500
elif 1800 < h < 2.399:
    premio = 1.000
elif 1200 < h < 1799:
    premio = 890
else:
    premio = 500

print("R$", float(premio))