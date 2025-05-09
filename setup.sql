CREATE DATABASE IF NOT EXISTS monitoramento;

USE monitoramento;

DROP TABLE IF EXISTS dados_rede;
DROP TABLE IF EXISTS aps;

CREATE TABLE IF NOT EXISTS dados_rede (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Data e hora da coleta
  ip_local VARCHAR(50),  -- IP local do Raspberry Pi
  ip_externo VARCHAR(50),  -- IP externo do Raspberry Pi
  latencia_ms FLOAT,  -- Latência em milissegundos
  perda_pacotes FLOAT,  -- Perda de pacotes em porcentagem
  download_mbps FLOAT,  -- Velocidade de download em Mbps
  upload_mbps FLOAT,  -- Velocidade de upload em Mbps
  rtt_min FLOAT,  -- RTT mínimo em milissegundos
  rtt_avg FLOAT,  -- RTT médio em milissegundos
  rtt_max FLOAT,  -- RTT máximo em milissegundos
  rtt_mdev FLOAT  -- Desvio padrão do RTT
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
