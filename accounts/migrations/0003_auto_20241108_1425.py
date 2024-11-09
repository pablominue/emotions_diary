from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', 'xxxx_previous_migration'),  # Reemplaza con la migración anterior
    ]

    operations = [
        migrations.AddField(
            model_name='emotion',
            name='intensity',
            field=models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=5),
        ),
    ]