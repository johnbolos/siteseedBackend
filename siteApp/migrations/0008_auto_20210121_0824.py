# Generated by Django 2.1 on 2021-01-21 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0007_auto_20210121_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custmaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 949324)),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='display_name',
            field=models.CharField(default='null', max_length=250),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='email',
            field=models.CharField(default='null', max_length=250),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='forgot_pswd_status',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='phone',
            field=models.CharField(default='null', max_length=250),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 949363)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 958402)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 958435)),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 957725)),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 957755)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 956868)),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 956898)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 966846)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='endDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 966812)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 966777)),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 966954)),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 967804)),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='releaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 967752)),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 967825)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 951921)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 951951)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 955407)),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 955458)),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 950410)),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 950441)),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 951171)),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 951211)),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 966097)),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 966128)),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 956222)),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 956252)),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 959871)),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 959901)),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 960622)),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 960652)),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 968484)),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 968518)),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 965329)),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 965359)),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 964623)),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 964653)),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 963020)),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 963084)),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 959069)),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 959100)),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 952959)),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 952989)),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 963875)),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 963907)),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 953735)),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 953766)),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 954506)),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 21, 8, 23, 59, 954534)),
        ),
    ]
