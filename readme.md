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
