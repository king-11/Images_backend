# Generated by Django 3.0.8 on 2020-08-06 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifiedAccount',
            fields=[
                ('uid', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('provider', models.CharField(choices=[('facebook.com', 'Facebook'), ('google.com', 'Google'), ('github.com', 'Github'), ('password', 'Email')], max_length=15)),
                ('provider_uid', models.CharField(blank=True, max_length=64, null=True)),
                ('is_verified', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verified_account', related_query_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('provider', 'provider_uid')},
            },
        ),
    ]
