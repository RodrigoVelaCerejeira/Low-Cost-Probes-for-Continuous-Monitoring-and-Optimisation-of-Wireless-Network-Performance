CREATE DATABASE IF NOT EXISTS central_monitoramento;

USE central_monitoramento;

DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS dados_rede;
DROP TABLE IF EXISTS all_aps;
DROP TABLE IF EXISTS raspberrypis;

CREATE TABLE IF NOT EXISTS raspberrypis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mac_address VARCHAR(17) UNIQUE NOT NULL, -- Endereço MAC único
    ultimo_registro DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    localizacao VARCHAR(50)
);

-- CREATE TABLE IF NOT EXISTS logs (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     raspberrypi_id INT NOT NULL,  -- ID do Raspberry Pi (referência à tabela raspberrypis)
--     mensagem TEXT,       -- Mensagem do log
--     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Hora de inserção do log
--     FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id) -- Relacionamento com raspberrypis
-- );

CREATE TABLE IF NOT EXISTS dados_rede (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único
    raspberrypi_id INT,  -- Identificador do Raspberry Pi
    timestamp DATETIME NOT NULL,  -- Data e hora da coleta
    latencia_ms FLOAT,  -- Latência em milissegundos
    perda_pacotes INT,  -- Perda de pacotes em porcentagem
    download_mbps FLOAT,  -- Velocidade de download em Mbps
    upload_mbps FLOAT,  -- Velocidade de upload em Mbps
    rtt_min FLOAT,  -- RTT mínimo em milissegundos
    rtt_avg FLOAT,  -- RTT médio em milissegundos
    rtt_max FLOAT,  -- RTT máximo em milissegundos
    rtt_mdev FLOAT,  -- Desvio padrão do RTT
    num_aps INT,
    FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id)  -- Relacionamento com a tabela raspberrypis
);

CREATE TABLE IF NOT EXISTS all_aps (
  id INT AUTO_INCREMENT PRIMARY KEY,
  timestamp DATETIME,
  raspberrypi_id INT,
  ssid VARCHAR(50),
  bssid VARCHAR(50),
  rate INT,
  sig INT,
  FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id)  -- Relacionamento com a tabela raspberrypis
);

CREATE USER IF NOT EXISTS 'monitor'@'%' IDENTIFIED BY 'senha_segura';

GRANT ALL PRIVILEGES ON central_monitoramento.* TO 'monitor'@'%';

FLUSH PRIVILEGES;
