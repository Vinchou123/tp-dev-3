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

