# TP5 DEV : Coding Encoding Decoding OPTIMIZE

## I. Opti calculatrice

### 1. Optimisation avec headers

🌞 tp5_enc_client_1.py

```bash
[vince@ClientTP4 tp-dev-3]$ python tp5_enc_client_1.py
Calcul à envoyer : 3 + 3
Connexion au serveur établie.
Message envoyé : b'\x00\x00\x00\x053 + 3<clafin>'
Réponse du serveur : Message reçu avec succès
[vince@ClientTP4 tp-dev-3]$
```

🌞 tp5_enc_server_1.py

```bash
[vince@ServeurTP4 tp-dev-3]$ python tp5_enc_server_1.py
Serveur en écoute sur 127.0.0.1:9999
Connexion acceptée depuis ('10.2.2.222', 49956)
Taille du message : 5 octets
Message reçu : 3 + 3
Connexion fermée avec le client
```

### 2. Optimisation avec taille fixe et connue

A. Python et les octets

B. Un autre exemple d'opti

C. Calculatrice opti


## III. Serveur Web HTTP

### 0. Ptite intro HTTP

1. Serveur Web

🌞 tp5_web_serv_1.py

```
[vince@ServeurTP4 tp-dev-3]$ python tp5_web_serv_1.py
Serveur lancé
```

2. Client Web

🌞 tp5_web_client_2.py

```
[vince@ClientTP4 tp-dev-3]$ python tp5_web_client_2.py
HTTP/1.0 200 OK

<h1>Hello je suis un serveur HTTP</h1>
```

3. Délivrer des pages web

🌞 tp5_web_serv_3.py



