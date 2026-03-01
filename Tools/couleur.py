import pyautogui
import time

# Fonction pour récupérer la couleur du pixel où tu as cliqué
def obtenir_couleur_souris():
    # Récupère la position actuelle de la souris
    x, y = pyautogui.position()
    # Capture la couleur du pixel à la position de la souris
    couleur = pyautogui.screenshot(region=(x, y, 1, 1)).getpixel((0, 0))
    return couleur, x, y

print("Appuie sur Entrée pour commencer à détecter la couleur du pixel que tu cliques.")

# Boucle qui attend l'entrée pour détecter un clic
while True:
    input("Clique n'importe où sur l'écran, puis appuie sur Entrée...")
    couleur, x, y = obtenir_couleur_souris()
    print(f"Couleur à ({x}, {y}) : {couleur}")
    time.sleep(1)  # Petite pause pour éviter un trop grand nombre de récupérations rapides
