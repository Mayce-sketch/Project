///////////////////////////////////////////////////// //<>//
//07/12/2025
// Jeu de Nim
//
/////////////////////////////////////////////////////
//
// Les constantes
// ==============
int nbMatches = 20; // nb d alumette
//
// Les variables globales
// ======================
float player_x, player_y;
float ia_x, ia_y;

float panel_width, panel_height; // dimensions des panels
// postion des panels
float pl_panel_x, pl_panel_y;
float ia_panel_x, ia_panel_y;
float match_x, match_y;     // position de la première allumette
float cup_x, cup_y;         // position du premier gobelet
float cup_w, cup_h;         // dimensions des gobelets
// Positions des boutons du joueur
float b1_x, b1_y;
float b2_x, b2_y;
float b3_x, b3_y;
// Bouton 1 ,2 ,3
boolean inside1, inside2, inside3; // si la souris survole les boutons

int lastPlayTime; // temps

boolean iaTurn = false;
boolean gameOver = false;

int nbCups = 20;            // nombre de gobelets
boolean[][] tokens;          // tokens[cup][token]
int[] coups;                 // jeton choisi par IA

int scorePlayer = 0;
int scoreIA = 0;

//=================================================================
//
// Initialisation de la fenêtre graphique
//
//=================================================================
void settings() {
  size(900, 600);
}

//=================================================================
//
// Initialisation du programme
//
//=================================================================
void setup() {
  rectMode(CORNER);
  ellipseMode(CORNER);
  noStroke();
  player_x = 800;
  player_y = 475;

  ia_x = 775;
  ia_y = 25;

  // dimensions des panneaux
  panel_width  = 870;
  panel_height = 150;

  //postion des panels
  pl_panel_x = 15;
  pl_panel_y = 435;

  ia_panel_x = 15;
  ia_panel_y = 15;

  // position de la premiere allumettes
  match_x = 50;
  match_y = 215;
  // postion et taille du goblet
  cup_x = 37.5 + 15;
  cup_y = 37.5;

  cup_w = 25;
  cup_h = 100;

  // postion des bouton du joueur
  b1_x = 175;
  b1_y = 460;

  b2_x = 350;
  b2_y = 460;

  b3_x = 525;
  b3_y = 460;
  initIA(); // on crée la mémoire de l'IA
  initGame(); // initialise le jeu et l'IA au démarrage
}

//=================================================================
//
// Boucle de rendu
//
//=================================================================
void draw() {
  background(0);
  display(); // affiche l état actuel du jeu

  // affichage du chargement de reflexion de l ia
  if (iaTurn && !gameOver) {
    fill(255);
    textSize(30);
    textAlign(CENTER);
    text("L'IA réfléchit...", width/2, 100+90);

    noStroke();
    fill(0, 200, 255);
    rect(width/2 - 75, 110+90, (millis()/10) % 142.5, 5);
  }

  if (iaTurn && !gameOver) {
    // index du gobelet (0-19)
    int cupIndex = min(nbMatches - 1, nbCups - 1);

    // l ia  doit jouer mais le gobelet est vide
    if (cupIndex >= 0 && losingCup(cupIndex)) {
      gameOver = true;
      learn(); // l ia a perdu
      scorePlayer++;
    }
    // l ia peux jouer
    else if (millis() - lastPlayTime > 2000) {
      play();
    }
  }

  // Condition de fin de partie ,plus d'allumettes
  if (nbMatches <= 0 && !gameOver) {
    nbMatches = 0;
    gameOver = true;

    // si l ia perd
    if (iaTurn) {
      learn();
      scorePlayer++;
    } else {
      scoreIA++;
    }
  }
}

//=================================================================
//
// Initialisation du jeu
//
//=================================================================
void initGame() {
  nbMatches = 20;
  iaTurn = false;
  gameOver = false;
  lastPlayTime = millis();
  initCoups();
}

//=================================================================
//
// Création des structures nécessaires à l'IA
//
//=================================================================
void initIA() {
  // création du tableau tokens : nbCups x 3 jetons
  tokens = new boolean[nbCups][3];
  for (int i = 0; i < nbCups; i++) {
    for (int j = 0; j < 3; j++) {
      tokens[i][j] = true;   // tous les jetons sont présents
    }
  }

  // jetons spéciaux pour les deux premiers gobelets
  tokens[0][1] = false;     // 2ème jeton du premier gobelet absent
  tokens[0][2] = false;     // 3ème jeton du premier gobelet absent
  tokens[1][2] = false;     // 3ème jeton du deuxième gobelet absent

  // initialisation du tableau coups
  coups = new int[nbCups];
  for (int i = 0; i < nbCups; i++) {
    coups[i] = 0;
  }
}

//=================================================================
//
// Initialisation des coups joués par l'IA
// remet la table des coups à 0
//
//=================================================================
void initCoups() {
  coups = new int[nbCups];
  for (int i = 0; i < nbCups; i++) {
    coups[i] = 0;
  }
}

//=================================================================
//
// Au tour de l'IA de jouer...
//
//=================================================================
void play() {
  // si parti fini ou memoire ia null
  if (nbMatches <= 0 || tokens == null) {
    iaTurn = false;
    return;
  }
  // gobelet correspondant au nb d allumettes restantes
  int cupIndex = nbMatches - 1;
  int choix = 0;
  // si l index calculer et superrieur a la taille du tableau de goblet
  if (cupIndex >= tokens.length) {
    iaTurn = false;
    return;
  }

  // liste des coups possibles
  int[] possibles = new int[3];
  int nbPossibles = 0;
  for (int i = 0; i < 3; i++) {
    if (i < nbMatches && tokens[cupIndex][i]) {
      possibles[nbPossibles++] = i + 1;
    }
  }

  if (nbPossibles > 0) {
    int r = (int) random(nbPossibles);
    choix = possibles[r];
    nbMatches -= choix;
    coups[cupIndex] = choix;
  }

  iaTurn = false;
}

//=================================================================
//
// Mécanisme d'apprentissage
//
//=================================================================
void learn() {
  // l'IA a perdu, on  retire le premier jeton choisi dans les coups
  for (int i = 0; i < nbCups; i++) {
    if (coups[i] != 0) { // si l IA a jouer diferent de 0
      tokens[i][coups[i] - 1] = false; // rejeter le  jeton choisi
      break; // on rejette que le  mauvais coup
    }
  }
}
//=================================================================
//
// Affichage du jeu
//
//=================================================================
void display() {
  // affichage panels pour le joueur ou l ai selon le tour
  if (iaTurn) {
    // panel IA actif
    fill(122);
    rect(ia_panel_x, ia_panel_y, panel_width, panel_height, 5);
  } else {
    // panel joueur actif
    fill(214, 190, 81);
    rect(pl_panel_x, pl_panel_y, panel_width, panel_height, 5);
  }

  // elements du jeu
  displayCups();
  displayTokens();
  displayMatches();
  displayButtons();

  // avatars
  if (!iaTurn) displayAvatar(player_x, player_y);
  if (iaTurn) displayIA(ia_x, ia_y);

  // panneau de fin de partie
  if (gameOver) {
    fill(0, 150);
    rect(150, 200, 600, 200, 10);

    fill(255);
    textSize(40);
    textAlign(CENTER, CENTER);
    if (iaTurn) {
      text("Le joueur a gagné !", 450, 300);
    } else {
      text("L'IA a gagné !", 450, 300);
    }
    textSize(20);
    text( "(appuier sur espace pour relencer la partie)", 450, 350);
  }
  fill(255);
  textSize(16);
  textAlign(CENTER);
  text("Joueur : " + scorePlayer, 835, 580);
  text("IA : " + scoreIA, 835, 35);
}



//=================================================================
//
// Renvoie vrai si plus aucun coup possible (le gobelet est vide)
// cup = le numéro du gobelet
//
//=================================================================
boolean losingCup(int cup) {
  for (int i = 0; i < 3; i++) {
    if (tokens[cup][i]) return false; // au moins un jeton disponible
  }
  return true; // aucun jeton disponible
}

//=================================================================
//
// Affiche les gobelets
//
//=================================================================
void displayCups() {
  // nombre de goblet corespondant au nb d allumette restente
  int activeCup = nbMatches - 1;
  for (int i = 0; i < nbCups - 1; i++) {
    if (i == activeCup && !gameOver) { // ou joue le joueur
      noFill();
      //if (!iaTurn) {
      //  stroke(255);
      //}
      if (iaTurn) {
        stroke(0, 200, 255);
      }

      strokeWeight(3);
      // Un cadre blanc autour du gobelet actf
      rect(cup_x + (i * 37.5) - 2, cup_y - 2, cup_w + 3, cup_h + 4, 5);
      noStroke();
    }
    // si le gobelet contient encore au moins un jeton
    if (!losingCup(i)) {

      float xPos = cup_x + (i * 37.5);
      fill(214, 190, 81);
      rect(xPos, cup_y, cup_w, cup_h, 1000);
    }
    if (losingCup(i)) {
      float xPos = cup_x + (i * 37.5);
      fill(255, 0, 0);
      rect(xPos, cup_y, cup_w, cup_h, 1000);
    }
  }

  if (iaTurn) {
    strokeWeight(1);
    displayIA(ia_x, ia_y);
  }
}

//=================================================================
//
// Affiche les jetons dans les gobelets
//
//=================================================================
void displayTokens() {
  textSize(20);
  textAlign(CENTER, CENTER);

  // boucle sur chaque gobelet
  for (int cup = 0; cup < nbCups - 1; cup++) {

    // calcul de la position X pour ce gobelet
    float tokenX = 55 + (cup * 37.5);

    // Coordonnées Y fixes
    float y1 = 45;
    float y2 = 77.5;
    float y3 = 110;

    displayToken(cup, tokenX, y1, 0); // jeton 1
    displayToken(cup, tokenX, y2, 1); // jeton 2
    displayToken(cup, tokenX, y3, 2); // jeton 3
  }
}

//=================================================================
//
// Affiche un jeton dans un gobelet
// cup = le gobelet
// token = le numéro du jeton
// s = le texte à afficher sur le jeton
//
//=================================================================
void displayToken(int cup, float x, float y, int id) {
  // si le jeton existe
  if (!tokens[cup][id]) return;

  // coups[cup] stocke 1, 2 ou 3 , id stocke 0, 1 ou 2, on compare id+1.
  if (coups[cup] == id + 1) {
    fill(0, 200, 255); // Couleur IA
  } else {
    fill(81, 105, 214); // Couleur normale
  }

  ellipse(x, y, 20, 20);
  fill(0);
  text(id + 1, x + 10, y + 10);
}

//=================================================================
//
// Affiche les allumettes
//
//=================================================================
void displayMatches() {
  for (float i = match_x; i < match_x + 40 * nbMatches; i += 40) {
    displayMatch(i, match_y);
  }
}

//=================================================================
//
// Dessine une allumette
// x, y = les coordonnées de l'allumette
//
//=================================================================
void displayMatch(float x, float y) {
  fill(200, 140, 80);
  rect(x + 0, y + 20, 10, 140, 3);

  fill(220, 80, 40);
  ellipse(x - 3, y + 15, 15, 25);

  fill(82, 58, 33);
  fill(91, 33, 16);
}

//=================================================================
//
// Affiche les boutons du joueur humain
//
//=================================================================
void displayButtons() {

  if (!iaTurn) {
    displayAvatar(-100, -100);
  }

  // boucle pour les boutons 1, 2, 3
  for (int i = 1; i <= 3; i++) {
    // position des boutons
    int x = i * 175;
    int y = int(b1_y);

    // si survol du bouton
    boolean isInside = insideButton(x, y, 100);

    if (i == 1) inside1 = isInside;
    else if (i == 2) inside2 = isInside;
    else if (i == 3) inside3 = isInside;

    if (iaTurn || i > nbMatches) {
      // tour ia ou pas assez d'allumettes
      fill(255, 0, 0);
    } else if (isInside) {
      // Cas 2 : souris dessus
      fill(150, 200, 255);
    } else {
      // Cas 3 : normal
      fill(81, 105, 214);
    }

    displayButton(x, y, 100, isInside, char('0' + i));
  }
}

//=================================================================
//
// Renvoie vrai quand la souris est dans le bouton
// x, y = les coordonnées du bouton
// radius = le rayon du bouton
//
//=================================================================
boolean insideButton(int x, int y, int d) {
  float cx = x + d/2.0;   // centre X
  float cy = y + d/2.0;   // centre Y
  float r  = d/2.0;       // rayon

  return dist(mouseX, mouseY, cx, cy) <= r;
}

//=================================================================
//
// Affiche un bouton
// x, y = les coordonnées du bouton
// d = le diamètre du bouton
// inside = est-ce que la souris est à l'intérieur du bouton
// t = le texte à afficher dans le bouton
//
//=================================================================
void displayButton(int x, int y, int d, boolean inside, char t) {
  // si sur le bouton
  if (inside) {
    stroke(255);
    strokeWeight(4);
  } else {
    noStroke();
  }
  ellipse(x, y, d, d);
  noStroke();
  fill(0);
  textSize(100);
  text(t, x + 50, y + 47);
}

//=================================================================
// Affiche l'avatar du joueur
// x, y = les coordonnées de l'avatar
//=================================================================
void displayAvatar(float x, float y) {

  //  Corps
  fill(150, 210, 240);
  ellipse(x +  5, y + 30, 50, 45); // corps
  ellipse(x + 10, y + 10, 40, 40); // tête

  //  Pattes
  fill(255, 180, 180);
  ellipse(x + 10, y + 65, 12, 12); // patte gauche
  ellipse(x + 35, y + 65, 12, 12); // patte droite
  ellipse(x +  0, y + 35, 10, 12); // main gauche
  ellipse(x + 47, y + 35, 10, 12); // main droite

  //  Nez
  fill(255, 160, 160);
  ellipse(x + 25, y + 24, 10, 8);

  //  Dent
  fill(255);
  rect(x + 23, y + 32, 8, 4, 2);

  //  Yeux
  fill(255);
  ellipse(x + 15, y + 15, 10, 10); // gauche
  ellipse(x + 30, y + 15, 10, 10); // droite
  fill(0);
  ellipse(x + 18, y + 18, 4, 4); // gauche
  ellipse(x + 33, y + 18, 4, 4); // droite

  //  Oreilles
  fill(255, 180, 180);
  ellipse(x + 2, y + 10, 14, 14); // gauche
  ellipse(x + 42, y + 10, 14, 14); // droite

  // Toque
  fill(255);
  rect(x + 20, y + 5, 20, 8, 3);
  ellipse(x + 20, y - 7, 30, 18);
  // Mini allumette dans la main

  rotate(radians(30));

  fill(200, 140, 80);
  rect(x + 194.5, y - 473, 4, 35, 2);
  fill(220, 80, 40);
  ellipse(x + 193, y - 476, 6, 10);

  rotate(radians(-30));
}

//=================================================================
// Affiche l'IA
// x, y = les coordonnées de l'avatar
//=================================================================
void displayIA(float x, float y) {
  
  strokeWeight(1);
  stroke(0);
  //  Corps
  fill(240);
  ellipse(x + 40, y + 50, 35, 45);

  //  Bras
  fill(230);
  ellipse(x + 30, y + 60, 5, 27); // gauche
  ellipse(x + 63, y + 60, 5, 27); // droit


  // tete
  fill(255);
  ellipse(x + 40, y + 25, 35, 23);
  fill(0);
  ellipse(x + 37, y + 30, 25, 15);
  noStroke();
  //  Yeux
  fill(0, 150, 255);
  ellipse(x + 36, y + 38, 6, 4); // gauche
  ellipse(x + 48, y + 39, 6, 4); // droit

  fill(150, 220, 255);
  ellipse(x + 38, y + 40, 2.2, 1.2); // gauche
  ellipse(x + 50, y + 41, 2.2, 1.2); // droit
}

//=================================================================
//
// Interactivité pour le joueur
//
//=================================================================
void mousePressed() {
  if (iaTurn || gameOver) return;

  if (inside1 && nbMatches >= 1) {
    nbMatches -= 1;
    iaTurn = true;
  } else if (inside2 && nbMatches >= 2) {
    nbMatches -= 2;
    iaTurn = true;
  } else if (inside3 && nbMatches >= 3) {
    nbMatches -= 3;
    iaTurn = true;
  }
  lastPlayTime = millis();
}

//=================================================================
//
// Relance une nouvelle partie quand on appuie sur la touche espace
//
//=================================================================
void keyPressed() {
  if (key == ' ') {  // touche espace
    initGame();
  }
}
