#02/03/2025
import sqlite3

def creer_base():
    conn = sqlite3.connect('MesMusiques.db')
    cursor = conn.cursor()
    # Table Auteur
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Auteurs (
            id_auteur INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            nationalite TEXT
        )
    ''')
    # Table Morceaux
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Morceaux (
            id_morceau INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT,
            genre TEXT,
            duree TEXT,
            id_auteur INTEGER,
            FOREIGN KEY (id_auteur) REFERENCES Auteurs(id_auteur)
        )
    ''')
    # Table Playlists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Playlists (
            id_playlist INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_playlist TEXT
        )
    ''')
    # Table Playlist_Morceaux
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Playlist_Morceaux (
            id_playlist INTEGER,
            id_morceau INTEGER,
            PRIMARY KEY (id_playlist, id_morceau),
            FOREIGN KEY (id_playlist) REFERENCES Playlists(id_playlist),
            FOREIGN KEY (id_morceau) REFERENCES Morceaux(id_morceau)
        )
    ''')

    # Insertion de données (2 auteur avec 2 musique par auteur touts dans un meme playlist)
    # Auteurs
    cursor.execute("INSERT INTO Auteurs (nom, prenom, nationalite) VALUES ('Aznavour', 'Charles', 'Française')")
    cursor.execute("INSERT INTO Auteurs (nom, prenom, nationalite) VALUES ('Piaf', 'Edith', 'Française')")

    # Morceaux pour Charles Aznavour (id_auteur = 1)
    cursor.execute("INSERT INTO Morceaux (titre, genre, duree, id_auteur) VALUES ('La Bohème', 'Chanson', '04:05', 1)")
    cursor.execute(
        "INSERT INTO Morceaux (titre, genre, duree, id_auteur) VALUES ('Emmenez-moi', 'Chanson', '03:40', 1)")

    # Morceaux pour Edith Piaf (id_auteur = 2)
    cursor.execute(
        "INSERT INTO Morceaux (titre, genre, duree, id_auteur) VALUES ('La Vie en Rose', 'Chanson', '03:22', 2)")
    cursor.execute(
        "INSERT INTO Morceaux (titre, genre, duree, id_auteur) VALUES ('Non, je ne regrette rien', 'Chanson', '02:25', 2)")

    # Playlist
    cursor.execute("INSERT INTO Playlists (nom_playlist) VALUES ('Chansons Françaises')")

    # Ajouter les morceaux à la playlist (id_playlist = 1)
    cursor.execute("INSERT INTO Playlist_Morceaux (id_playlist, id_morceau) VALUES (1, 1)")  # La Bohème
    cursor.execute("INSERT INTO Playlist_Morceaux (id_playlist, id_morceau) VALUES (1, 2)")  # Emmenez-moi
    cursor.execute("INSERT INTO Playlist_Morceaux (id_playlist, id_morceau) VALUES (1, 3)")  # La Vie en Rose
    cursor.execute("INSERT INTO Playlist_Morceaux (id_playlist, id_morceau) VALUES (1, 4)")  # Non, je ne regrette rien

    conn.commit()
    conn.close()
    print("Base créée avec succès !")


creer_base()
