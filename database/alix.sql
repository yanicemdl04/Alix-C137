-- SQLite
CREATE TABLE acces(
   Id COUNTER PRIMARY KEY,
   email VARCHAR(50),
   mdp VARCHAR(50) NOT NULL
);

CREATE TABLE creer(
   Id COUNTER PRIMARY KEY,
   email VARCHAR(50),
   nom VARCHAR(50),
   prenom VARCHAR(50),
   mdp VARCHAR(50) NOT NULL
);