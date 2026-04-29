
<p align="center">
  <h1 align="center"> arch-quantum-security</h1>
</p>

<p align="center">
  <b>Runtime Intrusion Detection on Arch Linux</b>
</p>



## 🔵 Description du projet

Ce projet implémente un mini moteur de détection d’intrusion (IDS) capable d’analyser des logs système afin d’identifier des comportements suspects.

L’objectif est de simuler une activité malveillante, de générer des logs, puis de les analyser automatiquement afin de détecter des événements critiques.

---

- **ebpf/**  
  Détection au niveau kernel  

- **detection/**  
  Moteur d’analyse  

- **attacks/**  
  Simulation d’attaques  

- **tests/**  
  Validation du pipeline  

- **logs/**  
  Stockage des événements  

- **run.sh**  
  Exécution globale  

- **README.md**  
  Documentation  

---

## 🟢 Objectifs

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

## Pipeline de détection   

### 🔺 1. Simulation d’attaque   

Un script génère un événement simulant une activité malveillante :   
 → ATTACK|bash|940|0|/etc/passwd  

---

### 🔷 2. Stockage des logs

Les événements sont enregistrés dans :
 → logs/events.log   

---

### 🔷 3. Moteur de détection

Le script principal analyse les logs :

Ce fichier constitue la source principale pour l’analyse.   
 → python detection/engine.py logs/events.log   

---

## Fonctionnement interne

### 🔷 Lecture des logs

Le moteur lit le fichier ligne par ligne :
⚙️ Fonctionnement interne   
 → with open(sys.argv[1]) as f:   

### 🔷 Filtrage

Seules les lignes contenant `"ATTACK|"` sont analysées :



 Filtrage  

Seules les lignes contenant "ATTACK|" sont analysées :   

 → if "ATTACK|" in line:   

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

 Détection   

Le moteur applique des règles simples mais efficaces :   

* 🔴 UID = 0 → activité avec privilèges root   
* 🔴 Accès à /etc/passwd → fichier sensible   

Exemple de sortie :  

 → [ALERT] Root activity detected    
 → [CRITICAL] Sensitive file access   

Sauvegarde   

Les événements sont enregistrés au format JSON dans :   

 → logs/events.log

🔵 Pourquoi “Quantum Security” ?   

Dans ce projet, le terme “Quantum” ne fait pas référence à l’informatique quantique.   

Il représente une approche multi-critères et multi-états de la détection :   

* analyse simultanée de plusieurs attributs (processus, utilisateur, fichier)  
* corrélation de différents indicateurs  
* évaluation du niveau de risque selon plusieurs règles     

Cette approche permet une détection plus intelligente et contextuelle.

⸻

  → Concepts abordés

* Analyse de logs
* Détection d’intrusion (IDS)
* Parsing de données
* Corrélation d’événements
* Structuration JSON

⸻

👥 Cas d’usage

Ce type de système est utilisé par :

* Analystes SOC (Security Operations Center)
* Administrateurs systèmes
* Équipes cybersécurité
* Entreprises pour la surveillance des systèmes

⸻

 → Points forts

* Pipeline complet (attaque → détection)
* Code clair et structuré
* Détection basée sur des règles
* Format JSON exploitable
* Simulation réaliste

⸻

⚠️ Limites

* Règles de détection simples
* Pas de traitement en temps réel
* Pas d’interface graphique

⸻

🔵 Conclusion

Ce projet démontre la mise en place d’un système de détection d’intrusion simplifié capable d’analyser des logs, d’identifier des comportements suspects et de générer des alertes.

Il constitue une base concrète et réaliste des outils utilisés en cybersécurité.

⸻

⚠️ Disclaimer

This project is for educational purposes only.
All outputs have been sanitized.

⸻

Lexique des outils et concepts utilisés

🐍 Python

* python : exécution du moteur de détection
* sys.argv : récupération du fichier en argument
* json.dumps() : conversion en JSON
* datetime.now(UTC) : génération d’un timestamp
* open() : lecture/écriture de fichier
* split() : parsing des logs
* if : règles de détection

⸻

🟢 Bash / Linux

* Scripts .sh : simulation d’attaques
* echo : écriture dans les logs
* >> : append dans un fichier
* chmod +x : rendre un script exécutable
