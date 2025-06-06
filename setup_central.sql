CREATE DATABASE IF NOT EXISTS central_monitoramento;

USE central_monitoramento;

DROP TABLE IF EXISTS dados_rede;
DROP TABLE IF EXISTS erros_dados_rede;
DROP TABLE IF EXISTS all_aps;
DROP TABLE IF EXISTS raspberrypis;

CREATE TABLE IF NOT EXISTS raspberrypis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mac_address VARCHAR(17) UNIQUE NOT NULL, -- Endereço MAC único
    ultimo_registro DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    localizacao VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dados_rede (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raspberrypi_id INT,
    timestamp DATETIME NOT NULL,
    latencia_ms FLOAT,
    perda_pacotes INT,
    download_mbps FLOAT,
    upload_mbps FLOAT,
    rtt_min FLOAT,
    rtt_avg FLOAT,
    rtt_max FLOAT,
    rtt_mdev FLOAT,
    num_aps INT,
    FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id)
);

CREATE TABLE IF NOT EXISTS erros_dados_rede (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raspberrypi_id INT,
    timestamp DATETIME NOT NULL,
    latencia_ms FLOAT,
    perda_pacotes INT,
    download_mbps FLOAT,
    upload_mbps FLOAT,
    rtt_min FLOAT,
    rtt_avg FLOAT,
    rtt_max FLOAT,
    rtt_mdev FLOAT,
    num_aps INT,
    FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id)
);

CREATE TABLE IF NOT EXISTS all_aps (
  id INT AUTO_INCREMENT PRIMARY KEY,
  timestamp DATETIME,
  raspberrypi_id INT,
  ssid VARCHAR(50),
  bssid VARCHAR(50),
  rate INT,
  sig INT,
  FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id)
);

CREATE USER IF NOT EXISTS 'monitor'@'%' IDENTIFIED BY 'senha_segura';

GRANT ALL PRIVILEGES ON central_monitoramento.* TO 'monitor'@'%';

FLUSH PRIVILEGES;

DELIMITER //

CREATE TRIGGER trg_erros_na_rede
AFTER INSERT ON dados_rede
FOR EACH ROW
BEGIN
  IF NEW.latencia_ms > 50.0
  OR NEW.perda_pacotes > 2
  OR NEW.download_mbps < 10.0
  OR NEW.upload_mbps < 10.0
  OR NEW.rtt_avg > 200.0 THEN
    INSERT INTO erros_dados_rede (
    raspberrypi_id,
    timestamp,
    latencia_ms,
    perda_pacotes,
    download_mbps,
    upload_mbps,
    rtt_min,
    rtt_avg,
    rtt_max,
    rtt_mdev,
    num_aps
    )
    VALUES (
    NEW.raspberrypi_id,
    NEW.timestamp,
    NEW.latencia_ms,
    NEW.perda_pacotes,
    NEW.download_mbps,
    NEW.upload_mbps,
    NEW.rtt_min,
    NEW.rtt_avg,
    NEW.rtt_max,
    NEW.rtt_mdev,
    NEW.num_aps
    );
  END IF;
END;//

DELIMITER ;
