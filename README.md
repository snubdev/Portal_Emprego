# Portal_Emprego

### Instalando as dependências
```
pip install -r requirements.txt
```
### Configurações

```
'NAME': 'NAME',
'USER': 'USER',
'PASSWORD': 'PASSWORD',
'HOST': 'HOST',
'PORT': 'PORT'
```

```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = # Segredo do Consumidor do Google
```

### Execução
Criando Migração

```
python manage.py makemigrations
```
Sincronizando com banco de dados
```
python manage.py migrate
```
Inicia o servidor
```
python manage.py runserver
```
