import pyautogui
import time

def get_position(message):
    print(message)
    time.sleep(3)
    return pyautogui.position()

print("Place ta souris")
coin_lecture_haut_gauche = get_position("5 secondes...")

print("Place ta souris")
coin_lecture_bas_droit = get_position("5 secondes...")


print("\nMerci ! Voici les positions :")
print("Grille du bas (lecture) :")
print(coin_lecture_haut_gauche)
print(coin_lecture_bas_droit)

