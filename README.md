
coletor.py - Coleta de Dados no Raspberry Pi
O script coletor.py é responsável por coletar dados da rede no Raspberry Pi


sincronizar_raspberrypi.py - Sincronização dos Dados com o Servidor Central
O script sincronizar_raspberrypi.py é responsável por sincronizar os dados coletados no Raspberry Pi com o servidor central. Ele realiza as seguintes funções:

Conexão ao Banco de Dados Central:

Estabelece uma conexão com o banco de dados MariaDB no servidor central.

Envio dos Dados:

Recupera os dados coletados e armazenados no banco de dados MariaDB local no Raspberry Pi e os envia para a base de dados do servidor central.

Armazenamento Remoto:

Os dados são armazenados na tabela dados_rede do banco de dados central, garantindo que as informações de desempenho da rede do Raspberry Pi estejam centralizadas para análise.

Nota: A sincronização ainda não foi testada com sucesso, pois o Raspberry Pi ainda não está conectado à rede Eduroam (necessária para comunicação com o servidor central). Assim, não foi possível verificar se a sincronização está funcionando corretamente.



sincronizar_logs.py - Sincronização dos Logs
O script sincronizar_logs.py tem a função de sincronizar os logs de desempenho do Raspberry Pi com o servidor central



setup.sql - Criação e Atualização do Banco de Dados
Atualizações no setup.sql:
Criação da Tabela raspberrypis:
Foi criada uma tabela raspberrypis para armazenar informações sobre cada Raspberry Pi, como MAC Address, IP local, IP externo, último registro e status (ativo/inativo).
Alteração da Tabela dados_rede:
A tabela dados_rede foi modificada para incluir uma chave estrangeira raspberrypi_id que faz referência à tabela raspberrypis.
Isso cria uma relação entre os dados coletados e o Raspberry Pi que os enviou.



