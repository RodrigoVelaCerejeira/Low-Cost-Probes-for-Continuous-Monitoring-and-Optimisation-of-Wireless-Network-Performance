-- Criação do banco de dados central_monitoramento
CREATE DATABASE IF NOT EXISTS central_monitoramento;

-- Seleção do banco de dados central_monitoramento
USE central_monitoramento;

-- Criação da tabela raspberrypis
CREATE TABLE IF NOT EXISTS raspberrypis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mac_address VARCHAR(17) UNIQUE NOT NULL, -- Endereço MAC único
    ip_local VARCHAR(50),
    ip_externo VARCHAR(50),
    ultimo_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo',
    raspberrypi_id INT -- Pode ser usado se precisar de relacionamento com outra tabela
);

-- Criação da tabela logs
CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raspberrypi_id INT,  -- ID do Raspberry Pi (referência à tabela raspberrypis)
    mensagem TEXT,       -- Mensagem do log
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Hora de inserção do log
    FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id) -- Relacionamento com raspberrypis
);

-- Criação da tabela dados_rede
CREATE TABLE IF NOT EXISTS dados_rede (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_local VARCHAR(50),
    ip_externo VARCHAR(50),
    latencia_ms FLOAT,
    perda_pacotes FLOAT,
    download_mbps FLOAT,
    upload_mbps FLOAT,
    raspberrypi_id INT,
    FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id) -- Relacionamento com raspberrypis
);
