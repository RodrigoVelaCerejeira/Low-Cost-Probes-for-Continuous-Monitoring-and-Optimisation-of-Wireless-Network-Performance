CREATE DATABASE IF NOT EXISTS monitoramento;

USE monitoramento;

DROP TABLE IF EXISTS dados_rede;
DROP TABLE IF EXISTS aps;

CREATE TABLE IF NOT EXISTS dados_rede (
  id INT AUTO_INCREMENT PRIMARY KEY,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  ip_local VARCHAR(50),
  ip_externo VARCHAR(50),
  latencia_ms FLOAT,
  perda_pacotes FLOAT,
  download_mbps FLOAT,
  upload_mbps FLOAT,
  rtt_min FLOAT,
  rtt_avg FLOAT,
  rtt_max FLOAT,
  rtt_mdev FLOAT,
  num_aps INT,
  synch BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS aps (
  id INT AUTO_INCREMENT PRIMARY KEY,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  ssid VARCHAR(50),
  bssid VARCHAR(50),
  rate INT,
  sig INT
);

CREATE USER IF NOT EXISTS 'monitor'@'localhost' IDENTIFIED BY 'senha_segura';

GRANT ALL PRIVILEGES ON monitoramento.* TO 'monitor'@'localhost';

FLUSH PRIVILEGES;
