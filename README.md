
<p align="center">
  <h1 align="center"> arch-quantum-security</h1>
</p>

<p align="center">
  <b>Runtime Intrusion Detection on Arch Linux</b>
</p>


##  Description du projet

Ce projet implémente un mini moteur de détection d’intrusion (IDS) capable d’analyser des logs système afin d’identifier des comportements suspects.

L’objectif est de simuler une activité malveillante, de générer des logs, puis de les analyser automatiquement afin de détecter des événements critiques.

---

##  Objectifs

- Simuler une attaque système  
- Générer des logs exploitables  
- Analyser automatiquement les événements  
- Détecter des comportements suspects  
- Structurer les résultats en format JSON  

---

## ⚙️ Architecture du projet

Le projet repose sur un pipeline simple et efficace :

Attack Script → Log File → Detection Engine → Alert

---


## 1. Simulation d’attaque

Un script génère un événement simulant une activité malveillante :


ATTACK|bash|940|0|/etc/passwd

📄 2. Stockage des logs

Les événements sont enregistrés dans :

logs/events.log

Ce fichier constitue la source principale pour l’analyse.

🔍 3. Moteur de détection

Le script principal analyse les logs :

python detection/engine.py logs/events.log

⚙️ Fonctionnement interne

📥 Lecture des logs

Le moteur lit le fichier ligne par ligne :

with open(sys.argv[1]) as f:

🎯 Filtrage

Seules les lignes contenant "ATTACK|" sont analysées :

if "ATTACK|" in line:

🧩 Parsing

Chaque ligne est transformée en objet structuré :

{
  "type": "ATTACK",
  "process": "bash",
  "pid": 940,
  "uid": 0,
  "file": "/etc/passwd",
  "timestamp": "..."
}

🚨 Détection

Le moteur applique des règles simples mais efficaces :

* 🔴 UID = 0 → activité avec privilèges root
* 🔴 Accès à /etc/passwd → fichier sensible
