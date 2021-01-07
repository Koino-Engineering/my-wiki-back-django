# my-wiki-back-django

## 起動
    docker-compose up

## 初期データ投入
    docker-compose exec back bash -c "python manage.py loaddata ./dump/data.json"

## 画面
- 管理画面
    - `localhost:5000/admin`
- apiルート
    - `localhost:5000/`
- swagger
    - `localhost:5000/swagger`
