Criamos a base de dados monitoramento no servidor central, que será usada para armazenar os dados coletados dos Raspberry Pis.

Criamos a tabela raspberrypis no banco de dados:

Esta tabela armazena informações dos Raspberry Pis, como MAC address, IP local, IP externo, status (ativo/inativo), e último registro.

O objetivo dessa tabela é ter um registro centralizado de todos os Raspberry Pis que estão se conectando e enviando dados para o servidor central.

Criamos a tabela dados_rede:

Esta tabela armazena os dados de rede coletados pelos Raspberry Pis, como latência, velocidade de download/upload, e perda de pacotes.

Ela tem um campo raspberrypi_id que é uma chave estrangeira para a tabela raspberrypis. Isso permite associar os dados de rede a um Raspberry Pi específico.

Funcionamento:
Quando um Raspberry Pi começa a coletar dados de rede (como latência e velocidade de rede), ele os armazena no banco de dados local MariaDB.

O script sincronizar_raspberrypi.py envia esses dados para o banco de dados central no servidor central, e os dados são armazenados na tabela dados_rede.

A tabela raspberrypis é usada para garantir que cada dado esteja associado a um Raspberry Pi específico (usando o campo raspberrypi_id).
