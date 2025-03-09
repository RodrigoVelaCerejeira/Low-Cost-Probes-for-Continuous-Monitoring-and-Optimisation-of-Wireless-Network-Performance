-- Criar o banco de dados caso não exista
CREATE DATABASE IF NOT EXISTS monitoramento;

-- Usar o banco de dados
USE monitoramento;

-- Criar a tabela para armazenar os dados de rede
CREATE TABLE IF NOT EXISTS dados_rede (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_local VARCHAR(50) NOT NULL,
    ip_externo VARCHAR(50),
    latencia_ms FLOAT,
    perda_pacotes FLOAT,
    download_mbps FLOAT,
    upload_mbps FLOAT
);

-- Criar o usuário 'monitor' com uma senha segura
CREATE USER IF NOT EXISTS 'monitor'@'localhost' IDENTIFIED BY 'senha_segura';

-- Conceder permissões para o usuário acessar o banco
GRANT ALL PRIVILEGES ON monitoramento.* TO 'monitor'@'localhost';

-- Atualizar privilégios
FLUSH PRIVILEGES;
