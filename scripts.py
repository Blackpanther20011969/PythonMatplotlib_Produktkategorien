"""
# Daten für die Produktkategorien und die Anzahl der verkauften Produkte
"""

import matplotlib.pyplot as plt

# Liste der verfügbaren Stile anzeigen
print(plt.style.available)

# Einen anderen Stil auswählen, z.B. 'ggplot'
plt.style.use('ggplot')

# Daten für die Produktkategorien und die Anzahl der verkauften Produkte
categories = ['Elektronik', 'Kleidung', 'Lebensmittel', 'Bücher', 'Spielzeug']
sales = [150, 200, 300, 250, 100]

# Balkendiagramm erstellen
fig, ax = plt.subplots()
ax.bar(categories, sales, color='skyblue')

# Titel und Achsenbeschriftungen hinzufügen
ax.set_title('Verkäufe nach Produktkategorie')
ax.set_xlabel('Produktkategorie')
ax.set_ylabel('Anzahl der verkauften Produkte')

# Diagramm anzeigen
plt.show()
