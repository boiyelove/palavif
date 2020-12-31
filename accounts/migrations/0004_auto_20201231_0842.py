# Generated by Django 3.1.3 on 2020-12-31 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20201222_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('transgender', 'transgender'), ('gender neutral', 'gender neutral'), ('non-binary', 'non-binary'), ('agender', 'agender'), ('pangender', 'pangender'), ('genderqueer', 'genderqueer'), ('two-spirit', 'two-spirit'), ('third gender', 'third gender')], max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(choices=[('single', 'single'), ('married', 'married'), ('widowed', 'widowed'), ('divorced', 'divorced'), ('separated', 'separated'), ('registred partnership', 'registred partnership')], max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(default='middle_name', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='state_of_origin',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.CreateModel(
            name='ReligionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('religion', models.CharField(blank=True, max_length=60, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=60, null=True)),
                ('department_in_organization', models.CharField(blank=True, max_length=60, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='religionInfo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NextOfKinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('middle_name', models.CharField(max_length=60)),
                ('relationship', models.CharField(max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nexofkinInfo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('home_address', models.CharField(blank=True, max_length=160, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state_region', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=6, null=True)),
                ('office_address', models.CharField(blank=True, max_length=60, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contactInfo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
