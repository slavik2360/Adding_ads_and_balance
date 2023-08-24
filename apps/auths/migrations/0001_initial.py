# Generated by Django 4.2.4 on 2023-08-23 10:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='почта/логин')),
                ('nickname', models.CharField(max_length=120, verbose_name='ник')),
                ('currency', models.CharField(choices=[('KZT', 'Tenge'), ('RUB', 'Rubli'), ('EUR', 'Euro'), ('USD', 'Dollar')], default='KZT', max_length=4, verbose_name='валюта')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='ads/', verbose_name='Изображение')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Рекламное объявление',
                'verbose_name_plural': 'Рекламные объявления',
                'ordering': ('-start_date',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='сумма')),
                ('datetime_created', models.DateField(auto_now_add=True, verbose_name='дата транкзации')),
                ('is_filled', models.BooleanField(default=False, verbose_name='пополнение?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='BankCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\d{16}$')], verbose_name='номер')),
                ('cvv', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(regex='^\\d{3}$')], verbose_name='номер')),
                ('experation_time', models.DateField(verbose_name='срок действия')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': ('Банкоская карта',),
                'verbose_name_plural': 'Банкоская карты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ActivationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_created=True, verbose_name='дата создания')),
                ('code', models.CharField(max_length=200, unique=True, verbose_name='код')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный?')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='code', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': ('Код',),
                'verbose_name_plural': 'Коды активации',
                'ordering': ('-id',),
            },
        ),
    ]
