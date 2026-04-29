<p align="center">
  <h1>🛡️ arch-quantum-security</h1>
  <h3>Runtime Intrusion Detection on Arch Linux</h3>
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

### 1.  Simulation d’attaque

Un script génère un événement simulant une activité malveillante :
