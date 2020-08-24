# Generated by Django 2.2.15 on 2020-08-07 09:17

from django.db import migrations
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_simple_cms', '0015_rename_visible_available_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageopengraphtranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup_simple_cms.PageOpenGraph'),
        ),
        migrations.AlterField(
            model_name='pagetranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup_simple_cms.Page'),
        ),
    ]