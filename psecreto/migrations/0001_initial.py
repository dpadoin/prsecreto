# Generated by Django 5.1.3 on 2024-12-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AmigoSecreto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chave", models.CharField(max_length=25)),
                ("descricao", models.CharField(max_length=256)),
                ("nome", models.CharField(max_length=100)),
                ("autor", models.CharField(max_length=100)),
                ("amigo", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="AmigoSecretoTeste2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chave", models.CharField(max_length=25)),
                ("descricao", models.CharField(max_length=256)),
                ("nome", models.CharField(max_length=100)),
                ("autor", models.CharField(max_length=100)),
                ("amigo", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("enviou_desc", models.CharField(max_length=10)),
                ("enviou_amigo", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Descrever",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quem", models.CharField(max_length=100)),
                ("descricao", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Entrada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chave", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("idade", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Teste",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chave", models.CharField(max_length=25)),
                ("nome", models.CharField(max_length=25)),
                ("amigo", models.CharField(max_length=25)),
            ],
        ),
    ]
