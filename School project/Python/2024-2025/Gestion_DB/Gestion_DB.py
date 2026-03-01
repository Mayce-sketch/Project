#02/03/2025

import sqlite3
from tkinter import *

DB = 'MesMusiques.db'
def rechercher_morceau():
    titre = entree_titre.get()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    # Requête SQL pour récupérer toutes les informations du morceau et de son auteur correspondant au titre saisi
    cursor.execute('''
        SELECT titre, genre, duree, nom, prenom
        FROM Morceaux
        JOIN Auteurs ON Morceaux.id_auteur = Auteurs.id_auteur
        WHERE titre = ?
    ''', (titre,))

    result = cursor.fetchone()
    conn.close()

    # Affiche les informations du morceau ou un message si le morceau n'existe pas
    if result:
        label_resultat.config(text="Titre: " + result[0] + "\nGenre: " + result[1] + "\nDurée: " + result[2] + "\nAuteur: " + result[3] + " " + result[4])
    else:
        label_resultat.config(text="Aucun morceau trouvé.")


def rechercher_auteur():
    nom = entree_auteur.get()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Cherche l’auteur dans la table Auteurs
    cursor.execute("SELECT * FROM Auteurs WHERE nom = ?", (nom,))
    auteur = cursor.fetchone()

    # Si l’auteur existe, cherche tous les morceaux associés
    if auteur:
        texte = "Auteur: " + auteur[1] + " " + auteur[2] + "\nNationalité: " + auteur[3] + "\nMorceaux:\n"
        cursor.execute("SELECT titre FROM Morceaux WHERE id_auteur = ?", (auteur[0],))
        morceaux = cursor.fetchall()

        # Ajoute chaque morceau à la variable texte
        for morceau in morceaux:
            texte = texte + "- " + morceau[0] + "\n"

        # Affiche les informations de l’auteur et ses morceaux
        label_resultat.config(text=texte)
    else:
        # Si l’auteur n’existe pas, affiche un message
        label_resultat.config(text="Auteur introuvable.")

    conn.close()


def afficher_playlists():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Récupérer toutes les playlists
    cursor.execute('SELECT id_playlist, nom_playlist FROM Playlists')
    playlists = cursor.fetchall()

    texte = ""
    total_morceaux = 0
    nombre_playlists = len(playlists)

    for id_playlist, nom_playlist in playlists:
        texte = texte + "Playlist: " + nom_playlist + "\nContenu:\n"

        cursor.execute('''
            SELECT titre FROM Morceaux
            JOIN Playlist_Morceaux ON Morceaux.id_morceau = Playlist_Morceaux.id_morceau
            WHERE id_playlist = ?
        ''', (id_playlist,))

        morceaux = cursor.fetchall()
        total_morceaux = total_morceaux + len(morceaux)

        for morceau in morceaux:
            texte = texte + "- " + morceau[0] + "\n"
        texte = texte + "\n"

    # Afficher le texte dans le label résultat
    label_resultat.config(text=texte)

    # Calcul de la hauteur de la fenetre en fonction du nombre playlist
    hauteur_base = 500
    hauteur_par_morceau = 10  # Espace supplémentaire par morceau
    hauteur_par_playlist = 35  # Espace supplémentaire par playlist

    nouvelle_hauteur = hauteur_base + (total_morceaux * hauteur_par_morceau) + (nombre_playlists * hauteur_par_playlist)
    print(nouvelle_hauteur)
    # Mise à jour de la taille de la fenêtre
    fenetre.config(width=550, height=nouvelle_hauteur)

    conn.close()




def ajouter_auteur():
    nom = entree_nom_auteur.get()
    prenom = entree_prenom_auteur.get()
    nationalite = entree_nationalite.get()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Insère l’auteur dans la table Auteurs
    cursor.execute("INSERT INTO Auteurs (nom, prenom, nationalite) VALUES (?, ?, ?)", (nom, prenom, nationalite))

    conn.commit()
    conn.close()
    label_resultat.config(text="Auteur ajouté.")


def ajouter_morceau():
    titre = entree_titre_morceau.get()
    genre = entree_genre.get()
    duree = entree_duree.get()
    nom_auteur = entree_nom_morceau.get()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Vérifie si l’auteur existe
    cursor.execute("SELECT id_auteur FROM Auteurs WHERE nom = ?", (nom_auteur,))
    auteur = cursor.fetchone()

    # Si l’auteur existe, ajoute le morceau
    if auteur:
        cursor.execute("INSERT INTO Morceaux (titre, genre, duree, id_auteur) VALUES (?, ?, ?, ?)",
                       (titre, genre, duree, auteur[0]))
        conn.commit()
        label_resultat.config(text="Morceau ajouté.")
    else:
        # Si l’auteur n’existe pas, affiche un message
        label_resultat.config(text="Auteur introuvable, ajoutez-le d'abord.")

    conn.close()


def creer_playlist():
    nom_playlist = entree_nom_playlist.get()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Insère la nouvelle playlist
    cursor.execute("INSERT INTO Playlists (nom_playlist) VALUES (?)", (nom_playlist,))

    conn.commit()
    conn.close()
    label_resultat.config(text="Playlist créée.")


def modifier_playlist():
    nom_playlist = entree_nom_playlist_modif.get()
    action = entree_action_playlist.get()
    titre_morceau = entree_titre_playlist.get()

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # Récupère l’ID de la playlist et de la chanson
    cursor.execute("SELECT id_playlist FROM Playlists WHERE nom_playlist = ?", (nom_playlist,))
    playlist = cursor.fetchone()

    cursor.execute("SELECT id_morceau FROM Morceaux WHERE titre = ?", (titre_morceau,))
    morceau = cursor.fetchone()

    # Si la playlist et le morceau existent, ajoute ou supprime le morceau de la playlist
    if playlist and morceau:
        if action == "ajouter":
            cursor.execute("INSERT INTO Playlist_Morceaux (id_playlist, id_morceau) VALUES (?, ?)", (playlist[0], morceau[0]))
            label_resultat.config(text="Morceau ajouté à la playlist.")
        elif action == "supprimer":
            cursor.execute("DELETE FROM Playlist_Morceaux WHERE id_playlist = ? AND id_morceau = ?", (playlist[0], morceau[0]))
            label_resultat.config(text="Morceau supprimé de la playlist.")
        conn.commit()
    else:
        # Si la playlist ou le morceau n’existe pas
        label_resultat.config(text="Playlist ou morceau introuvable.")

    conn.close()


# Interface
fenetre = Tk()
fenetre.title("Gestion BD Musique")
fenetre.config(width=550, height=550,bg="#FAE3C6")

Label(fenetre, text="Titre du morceau",bg="#FAE3C6").place(x=20, y=20)
entree_titre = Entry(fenetre)
entree_titre.place(x=200, y=20)
Button(fenetre, text="Rechercher morceau", command=rechercher_morceau).place(x=400, y=18)

Label(fenetre, text="Nom de l'auteur",bg="#FAE3C6").place(x=20, y=60)
entree_auteur = Entry(fenetre)
entree_auteur.place(x=200, y=60)
Button(fenetre, text="Rechercher auteur", command=rechercher_auteur).place(x=400, y=58)

Button(fenetre, text="Afficher playlists", command=afficher_playlists).place(x=20, y=100)

Label(fenetre, text="Ajouter auteur (nom, prénom, nationalité)",bg="#FAE3C6").place(x=20, y=140)
entree_nom_auteur = Entry(fenetre)
entree_prenom_auteur = Entry(fenetre)
entree_nationalite = Entry(fenetre)
entree_nom_auteur.place(x=20, y=160)
entree_prenom_auteur.place(x=200, y=160)
entree_nationalite.place(x=400, y=160)
Button(fenetre, text="Ajouter auteur", command=ajouter_auteur).place(x=20, y=190)

Label(fenetre, text="Ajouter morceau (titre, genre, durée(mm:ss), auteur)",bg="#FAE3C6").place(x=20, y=230)
entree_titre_morceau = Entry(fenetre)
entree_genre = Entry(fenetre)
entree_duree = Entry(fenetre)
entree_nom_morceau = Entry(fenetre)
entree_titre_morceau.place(x=20, y=250)
entree_genre.place(x=150, y=250)
entree_duree.place(x=280, y=250)
entree_nom_morceau.place(x=400, y=250)
Button(fenetre, text="Ajouter morceau", command=ajouter_morceau).place(x=20, y=280)

Label(fenetre, text="Créer playlist",bg="#FAE3C6").place(x=20, y=320)
entree_nom_playlist = Entry(fenetre)
entree_nom_playlist.place(x=200, y=320)
Button(fenetre, text="Créer playlist", command=creer_playlist).place(x=400, y=318)

Label(fenetre, text="Modifier playlist (nom, action('ajouter'/'supprimer'), titre)",bg="#FAE3C6").place(x=20, y=360)
entree_nom_playlist_modif = Entry(fenetre)
entree_action_playlist = Entry(fenetre)
entree_titre_playlist = Entry(fenetre)
entree_nom_playlist_modif.place(x=20, y=380)
entree_action_playlist.place(x=200, y=380)
entree_titre_playlist.place(x=400, y=380)
Button(fenetre, text="Modifier playlist", command=modifier_playlist).place(x=20, y=410)

label_resultat = Label(fenetre, text="",bg="#FAE3C6")
label_resultat.place(x=20, y=450)

fenetre.mainloop()
