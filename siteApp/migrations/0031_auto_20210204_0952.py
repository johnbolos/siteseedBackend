# Generated by Django 3.1.5 on 2021-02-04 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0030_auto_20210204_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersites',
            name='is_domain_connected',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='usersites',
            name='is_published',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='usersites',
            name='site_name',
            field=models.CharField(default='null', max_length=250),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 533033), null=True),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 533073), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 541046), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 541076), null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 540418), null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 540447), null=True),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 539792), null=True),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 539822), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 547666), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='endDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 547608), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 547568), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 547692), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 548504), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='releaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 548446), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 548536), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 535565), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 535595), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 538332), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 538360), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 534276), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 534308), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 534880), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 534910), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 546863), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 546893), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 539103), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 539132), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 542228), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 542257), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 542946), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 542976), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 549136), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 549165), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 546128), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 546166), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 545437), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 545468), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 543803), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 543847), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 541576), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 541605), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 536267), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 536294), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 544723), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 544752), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 549786), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 549815), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 536960), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='is_active',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 537006), null=True),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 537655), null=True),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 4, 9, 52, 45, 537681), null=True),
        ),
    ]