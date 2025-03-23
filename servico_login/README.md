# Dar setup ao script dos logins

Seguem-se os passos para dar setup ao servico de logins para os raspberrypis


## Script login
O script em questao (login.sh) que envia a data e o ip do raspberrypi cada vez que ele se liga a uma rede.

**Devem fazer uma pequena alteracao no script**, para especificar para que ficheiro querem escrever o login. Se nao alterarem nada, estaremos a escrever todos para o mesmo ficehiro, escrevendo por cima uns dos outros.

No ficheiro login.sh, devem alterar a 6a e 7a linha.
- Na 6ª linha deve-se alterar o "CHANGETHIS!" para o nome do ficheiro onde se quer ler os logins da maquina (**certificar que o nome é único**)
- Na 7ª linha deve'se alterar o "CHANGETHIS!" para o caminho absoluto onde está guardada a chave privada para estabelecer comunicação com o servidor.

Finalmente, dar permicoes para executar o ficheiro, e move-lo para o diretório /usr/local/bin/:

```bash
sudo chmod +x login.sh
sudo mv login.sh /usr/local/bin/
```

## Servico e timer

O ficheiro login.service, contem informacao que para o sistema operativo saber quando e correr o login.sh, e o login.timer tem informacao para o sistema saber quando deve voltar a correr o login.sh.

Mover o login.service e o login.timer para o diretorio /etc/systemd/system/:

```bash
sudo mv login.service /etc/systemd/system
sudo mv login.timer /etc/systemd/system
```

Depois de ter os ficheiros no diretorio correto, basta dar o comando para o sistema passar a reconhece-los:

```bash
sudo systemctl enable login.service
sudo systemctl enable login.timer
```

E a seguir para inicia-los:

```bash
sudo systemctl start login.service
sudo systemctl start login.timer
```

Se tudo correr bem, vao poder ver o vosso ficheiro no diretorio /home/ubuntu/
