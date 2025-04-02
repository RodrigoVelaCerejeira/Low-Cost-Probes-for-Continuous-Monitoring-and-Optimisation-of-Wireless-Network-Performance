-- Criação do banco de dados (caso não exista)
CREATE DATABASE IF NOT EXISTS monitoramento;

-- Selecionar o banco de dados
USE monitoramento;

-- Criação da tabela 'raspberrypis' para armazenar informações dos Raspberry Pis
CREATE TABLE IF NOT EXISTS raspberrypis (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único (chave primária)
    mac_address VARCHAR(17) UNIQUE NOT NULL,  -- Endereço MAC único
    ip_local VARCHAR(50) DEFAULT 'Desconhecido',  -- IP local do Raspberry Pi
    ip_externo VARCHAR(50) DEFAULT 'Desconhecido',  -- IP externo do Raspberry Pi
    ultimo_registro DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Data do último registro
    status ENUM('ativo', 'inativo') DEFAULT 'ativo',  -- Status do Raspberry Pi (ativo/inativo)
    raspberrypi_id INT  -- Este campo será preenchido com o mesmo valor do 'id' gerado automaticamente
);

-- Criação da tabela 'dados_rede' para armazenar dados de rede coletados
CREATE TABLE IF NOT EXISTS dados_rede (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Data e hora da coleta
    ip_local VARCHAR(50),  -- IP local do Raspberry Pi
    ip_externo VARCHAR(50),  -- IP externo do Raspberry Pi
    latencia_ms FLOAT,  -- Latência em milissegundos
    perda_pacotes FLOAT,  -- Perda de pacotes em porcentagem
    download_mbps FLOAT,  -- Velocidade de download em Mbps
    upload_mbps FLOAT,  -- Velocidade de upload em Mbps
    raspberrypi_id INT,  -- Identificador do Raspberry Pi
    rtt_min FLOAT,  -- RTT mínimo em milissegundos
    rtt_avg FLOAT,  -- RTT médio em milissegundos
    rtt_max FLOAT,  -- RTT máximo em milissegundos
    rtt_mdev FLOAT,  -- Desvio padrão do RTT
    FOREIGN KEY (raspberrypi_id) REFERENCES raspberrypis(id)  -- Relacionamento com a tabela raspberrypis
);

-- Criação do índice para acelerar as consultas no campo raspberrypi_id da tabela dados_rede
CREATE INDEX idx_raspberrypi_id ON dados_rede (raspberrypi_id);

-- Exemplo de inserção de dados na tabela raspberrypis (caso deseje adicionar manualmente os 3 Raspberry Pis)
-- Não é necessário atribuir raspberrypi_id manualmente, pois ele será igual ao 'id'
INSERT INTO raspberrypis (mac_address, ip_local, ip_externo, status)
VALUES
('2c:cf:67:5e:92:66', '127.0.0.1', '2001:6900:2100:1016:1615:878c:6e1d:873c', 'ativo'),
('2c:cf:67:5e:90:63', 'Desconhecido', 'Desconhecido', 'ativo'),
('2c:cf:67:53:2a:74', 'Desconhecido', 'Desconhecido', 'ativo');

-- Limpeza das tabelas caso necessário (opcional)
-- DELETE FROM dados_rede;
-- DELETE FROM raspberrypis;

-- Limpeza das tabelas e reinício do contador de AUTO_INCREMENT (opcional)
-- TRUNCATE TABLE dados_rede;
-- TRUNCATE TABLE raspberrypis;

-- Criar o utilizador 'monitor' com uma senha segura
CREATE USER IF NOT EXISTS 'monitor'@'localhost' IDENTIFIED BY 'senha_segura';

-- Criar o utilizador rodrigo com uma senha segura na base central
CREATE USER IF NOT EXISTS rodrigo@'localhost' IDENTIFIED BY 'senha_segura';

-- Conceder permissões para o utilizador acessar a base de dados
GRANT ALL PRIVILEGES ON monitoramento.* TO 'monitor'@'localhost';

-- Atualizar privilégios
FLUSH PRIVILEGES;
