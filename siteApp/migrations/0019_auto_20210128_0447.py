# Generated by Django 2.1 on 2021-01-28 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0018_auto_20210128_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custmaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 510217)),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 510253)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 518329)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 518366)),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 517649)),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 517680)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 516884)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 516914)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 526173)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='endDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 526139)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 526105)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 526278)),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 526997)),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='releaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 526946)),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 527018)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 512536)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 512565)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 515527)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 515561)),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 511217)),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 511250)),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 511895)),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 511926)),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 525452)),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 525481)),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 516226)),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 516255)),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 519631)),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 519660)),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 520354)),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 520383)),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 527759)),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 527789)),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 524773)),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 524802)),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 524103)),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 524132)),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 522564)),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 522594)),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 518899)),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 518927)),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 513407)),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 513437)),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 523358)),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 523420)),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 514113)),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 514144)),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 514781)),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 28, 4, 47, 19, 514808)),
        ),
    ]
