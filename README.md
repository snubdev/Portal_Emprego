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

### Configuração

Crie um banco de dados postgresql

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
