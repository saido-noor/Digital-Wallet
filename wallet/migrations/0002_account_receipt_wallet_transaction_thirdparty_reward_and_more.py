# Generated by Django 4.0.6 on 2022-07-31 09:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_name', models.CharField(max_length=20)),
                ('balance', models.BigIntegerField()),
                ('pin', models.PositiveIntegerField()),
                ('currency', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=20)),
                ('receipt_date', models.DateTimeField()),
                ('receipt_number', models.BigIntegerField()),
                ('total_amount', models.IntegerField()),
                ('receipt_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.BigIntegerField()),
                ('currency', models.CharField(max_length=20)),
                ('amount', models.BigIntegerField()),
                ('account_pin', models.PositiveIntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.IntegerField()),
                ('transaction_amount', models.BigIntegerField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('Wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountb', to='wallet.account')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_a', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.BigIntegerField()),
                ('transaction_cost', models.BigIntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_c', to='wallet.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_d', to='wallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('date_reward', models.DateTimeField(default=datetime.datetime.now)),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.receipt')),
                ('transacation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=30)),
                ('tittle', models.CharField(max_length=20)),
                ('date_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('a', 'active'), ('in', 'inactive')], max_length=10, null=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.receipt')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('loan_type', models.CharField(max_length=20)),
                ('interest_rate', models.PositiveIntegerField()),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('loan_id', models.SmallIntegerField()),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('card_holder_name', models.CharField(max_length=39)),
                ('expiry_date', models.DateTimeField(default=datetime.datetime.now)),
                ('date_issued', models.DateTimeField(default=datetime.datetime.now)),
                ('card_type', models.CharField(max_length=20)),
                ('card_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_e', to='wallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_f', to='wallet.account')),
            ],
        ),
    ]
