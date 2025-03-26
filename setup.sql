-- Criar a base de dados caso não exista 
CREATE DATABASE IF NOT EXISTS monitoramento;

-- Usar a base de dados
USE monitoramento;

-- Criar a tabela para armazenar as informações dos Raspberry Pis
CREATE TABLE IF NOT EXISTS raspberrypis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mac_address VARCHAR(17) UNIQUE NOT NULL,  -- Endereço MAC único
    ip_local VARCHAR(50),
    ip_externo VARCHAR(50),
    ultimo_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo'  -- Status do Raspberry Pi (ativo/inativo)
);

-- Criar a tabela para armazenar os dados de rede
CREATE TABLE IF NOT EXISTS dados_rede (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_local VARCHAR(50) NOT NULL,
    ip_externo VARCHAR(50),
    latencia_ms FLOAT,
    perda_pacotes FLOAT,
    download_mbps FLOAT,
    upload_mbps FLOAT,
    raspberrypi_id INT,  -- Chave estrangeira para o Raspberry Pi
    FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id)  -- Relaciona com a tabela raspberrypis
);

-- Criar o utilizador 'monitor' com uma senha segura
CREATE USER IF NOT EXISTS 'monitor'@'localhost' IDENTIFIED BY 'senha_segura';

-- Criar o utilizador rodrigo com uma senha segura na base central
CREATE USER IF NOT EXISTS rodrigo@'localhost' IDENTIFIED BY 'senha_segura';

-- Conceder permissões para o utilizador acessar a base de dados
GRANT ALL PRIVILEGES ON monitoramento.* TO 'monitor'@'localhost';

-- Atualizar privilégios
FLUSH PRIVILEGES;
