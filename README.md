# docker-django-vue

- docker上におけるdjango-vueのテンプレート

# 作成

```
docker-compose build
```

# 本番相当環境

- fargate等にデプロイすることを想定(dockerで閉じている)

```
docker-compose -f docker-compose-product.yml up
```

- http://localhost:8001/ にてアクセス


# 開発環境

- ターミナル上で下記にて起動

```
docker-compose up
```

- 別ターミナルにて 書きを実行し vueを起動する

```
cd front && npm install && npm run serve
```

- http://localhost:8001/ にてアクセス
- 編集時動的に反映される


# ソースツリー

- project: djangoの設定ファイル群
- static: （clone時にはない) distに webpackより書き込まれる
- templates: index.htmlが起点
- front: vue.js関係
