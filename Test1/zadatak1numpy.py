import numpy as np

plate=[700,850,950,1000,1050,1150, 1200, 1250, 5000]

sredina=np.mean(plate)

medijan=np.median(plate)

print(f"Aritmetička sredina: {sredina:.2f} KM")
print(f"Medijan: {medijan:.2f} KM")
