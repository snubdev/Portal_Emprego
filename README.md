# Portal_Emprego

### Instalando as dependências
```
pip install django
```
```
pip install Pillow==7.0.0
```
```
pip install psycopg2-binary==2.8.4
```
```
pip install social-auth-app-django==3.1.0
```
```
pip install django-extensions==2.2.5
```
```
pip install werkzeug==0.16.0
```
```
pip install pyOpenSSL==21.0.0
```

### Configuração

```
Crie um banco de dados postgresql
```
```
Altere o DATABASES no arquivo settings.py
```
```
Aponte o nome do host myjob.com para sua propia maquina
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
