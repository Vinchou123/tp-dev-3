# I. Simple bs program

## 1. First steps

🌞 bs_server_I1.py`

```
[vince@ClientTP4 tp-dev-3]$ python bs_client.py
Le serveur à répondu b'Hi mate ! '
```

🌞 bs_client_I1.py

```
[vince@ServeurTP4 tp-dev-3]$ python bs_server.py
Connecting by ('10.2.2.222', 33142)
Données reçu du client: b'Meooooo !'
 ```


🌞 Commandes...
```
[vince@ServeurTP4 tp-dev-3]$ ss -lnpt | grep ':13337'
LISTEN 0      1            0.0.0.0:13337      0.0.0.0:*    users:(("python",pid=1356,fd=3))
```

## 2. User friendly

🌞 bs_client_I2.py


```
[vince@ClientTP4 tp-dev-3]$ python bs_client.py
Connecté avec succès au serveur 10.2.2.2 sur le port 13337
Que souhaites-tu écrire au serveur ? meo
Le serveur a répondu : 'Meo à toi confrère.'
[vince@ClientTP4 tp-dev-3]$ python bs_client.py
Connecté avec succès au serveur 10.2.2.2 sur le port 13337
Que souhaites-tu écrire au serveur ? waf
Le serveur a répondu : 'ptdr t ki'
[vince@ClientTP4 tp-dev-3]$ python bs_client.py
Connecté avec succès au serveur 10.2.2.2 sur le port 13337
Que souhaites-tu écrire au serveur ? salut daz waf
Le serveur a répondu : 'ptdr t ki'
[vince@ClientTP4 tp-dev-3]$ python bs_client.py
Connecté avec succès au serveur 10.2.2.2 sur le port 13337
Que souhaites-tu écrire au serveur ? salut !
Le serveur a répondu : 'Mes respects humble humain.'
```


🌞 bs_server_I2.py

```
[vince@ServeurTP4 tp-dev-3]$ python bs_server.py
Serveur en attente de connexions sur le port 13337...
Un client vient de se connecter, son IP c'est 10.2.2.222.
Données reçues du client : meo
[vince@ServeurTP4 tp-dev-3]$ python bs_server.py
Serveur en attente de connexions sur le port 13337...
Un client vient de se connecter, son IP c'est 10.2.2.222.
Données reçues du client : waf
[vince@ServeurTP4 tp-dev-3]$ python bs_server.py
Serveur en attente de connexions sur le port 13337...
Un client vient de se connecter, son IP c'est 10.2.2.222.
Données reçues du client : salut daz waf
[vince@ServeurTP4 tp-dev-3]$ python bs_server.py
Serveur en attente de connexions sur le port 13337...
Un client vient de se connecter, son IP c'est 10.2.2.222.
Données reçues du client : salut !
```

## 3. You say client I hear control

🌞 bs_client_I3.py

```
[vince@ClientTP4 tp-dev-3]$ python bs_client_I3.py
Connecté avec succès au serveur 10.2.2.2 sur le port 13337
Que souhaites-tu écrire au serveur ? salut
Erreur : La chaîne doit contenir soit 'waf' soit 'meo'.
[vince@ClientTP4 tp-dev-3]$ python bs_client_I3.py
Connecté avec succès au serveur 10.2.2.2 sur le port 13337
Que souhaites-tu écrire au serveur ? salut meo
Le serveur a répondu : 'Meo à toi confrère.'
```

```
[vince@ServeurTP4 tp-dev-3]$ python bs_server_I2.py
Serveur en attente de connexions sur le port 13337...
Un client vient de se connecter, son IP c'est 10.2.2.222.
[vince@ServeurTP4 tp-dev-3]$ python bs_server_I2.py
Serveur en attente de connexions sur le port 13337...
Un client vient de se connecter, son IP c'est 10.2.2.222.
Données reçues du client : salut meo
```


# II. You say dev I say good practices

## 1. Args

🌞 bs_server_II1.py

```
[vince@ServeurTP4 tp-dev-3]$ python bs_server_II1.py --port 13337 --listen 10.2.2.2
Serveur en attente de connexions sur 10.2.2.2:13337...
Un client vient de se connecter, son IP c'est 10.2.2.222.
Données reçues du client : Salut meo !
```


## 2. Logs

### A. Logs serveur

```
[vince@ServeurTP4 ~]$ cd /var/log
[vince@ServeurTP4 log]$ ls
anaconda       cron             dnf.rpm.log          kdump.log         messages           secure            spooler-20241023
audit          cron-20241003    firewalld            lastlog           messages-20241003  secure-20241003   sssd
btmp           cron-20241023    hawkey.log           maillog           messages-20241023  secure-20241023   tallylog
btmp-20241003  dnf.librepo.log  hawkey.log-20241003  maillog-20241003  private            spooler           wtmp
chrony         dnf.log          hawkey.log-20241023  maillog-20241023  README             spooler-20241003
```

Pour créer le dossier :
```
[vince@ServeurTP4 log]$ sudo mkdir -p /var/log/bs_server
[sudo] password for vince:
```

Pour créer le fichier dans le dossier : 

```
[vince@ServeurTP4 log]$ sudo touch /var/log/bs_server/bs_server.log
```

Modofier les permissions pour pouvoir écrire dedans : 

```
[vince@ServeurTP4 log]$ sudo chmod 666 /var/log/bs_server/bs_server.log
```

Pour vérifier qu'il a bien était créer :
```
[vince@ServeurTP4 log]$ ls -l /var/log/bs_server/
total 0
-rw-rw-rw- 1 root root 0 Oct 23 20:42 bs_server.log
```

```
[vince@ServeurTP4 tp-dev-3]$ python bs_server_II2A.py
2024-10-23 21:56:38 INFO Le serveur tourne sur 10.2.2.2:13337
Le serveur tourne sur 10.2.2.2:13337
2024-10-23 21:57:40 WARNING Aucun client depuis plus de une minute.
Aucun client depuis plus de une minute.
2024-10-23 21:58:27 INFO Un client (10.2.2.222) s'est connecté.
Un client (10.2.2.222) s'est connecté.
2024-10-23 21:58:34 INFO Le client 10.2.2.222 a envoyé "coucou".
Le client 10.2.2.222 a envoyé "coucou".
2024-10-23 21:58:34 INFO Réponse envoyée au client 10.2.2.222 : "Mes respects humble humain."
Réponse envoyée au client 10.2.2.222 : "Mes respects humble humain."
2024-10-23 21:59:27 WARNING Aucun client depuis plus de une minute.
Aucun client depuis plus de une minute.
```
Dans le fichier des logs :
```
[vince@ServeurTP4 /]$ cd /var/log/bs_server/
[vince@ServeurTP4 bs_server]$ cat bs_server.log

2024-10-23 21:45:34 INFO Le serveur tourne sur 10.2.2.2:13337
2024-10-23 21:51:02 INFO Un client (10.2.2.222) s'est connecté.
2024-10-23 21:51:18 INFO Le client 10.2.2.222 a envoyé "Salut !".
2024-10-23 21:51:18 INFO Réponse envoyée au client 10.2.2.222 : "Mes respects humble humain."
2024-10-23 21:56:38 INFO Le serveur tourne sur 10.2.2.2:13337
2024-10-23 21:57:40 WARNING Aucun client depuis plus de une minute.
2024-10-23 21:58:27 INFO Un client (10.2.2.222) s'est connecté.
2024-10-23 21:58:34 INFO Le client 10.2.2.222 a envoyé "coucou".
2024-10-23 21:58:34 INFO Réponse envoyée au client 10.2.2.222 : "Mes respects humble humain."
2024-10-23 21:59:27 WARNING Aucun client depuis plus de une minute.
2024-10-23 22:00:27 WARNING Aucun client depuis plus de une minute.
2024-10-23 22:01:28 WARNING Aucun client depuis plus de une minute.
2024-10-23 22:02:28 WARNING Aucun client depuis plus de une minute.
2024-10-23 22:03:28 WARNING Aucun client depuis plus de une minute.
```
🌞 bs_client_II2B.py





