# Generated by Django 3.1.5 on 2021-03-31 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0065_auto_20210323_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributorrolepermission',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 27702), null=True),
        ),
        migrations.AlterField(
            model_name='contributorrolepermission',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 27732), null=True),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 9219), null=True),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 9257), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 18128), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 18159), null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 17428), null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 17461), null=True),
        ),
        migrations.AlterField(
            model_name='ssfaqs',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 28394), null=True),
        ),
        migrations.AlterField(
            model_name='ssfaqs',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 28425), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 25070), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='endDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 25030), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 24997), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 25092), null=True),
        ),
        migrations.AlterField(
            model_name='sspromocodes',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 29793), null=True),
        ),
        migrations.AlterField(
            model_name='sspromocodes',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 29821), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 25775), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='releaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 25726), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 25799), null=True),
        ),
        migrations.AlterField(
            model_name='ssstripecustomers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 12509), null=True),
        ),
        migrations.AlterField(
            model_name='ssstripecustomers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 12540), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 11855), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 11886), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 15846), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 15881), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 10342), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 10373), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 11141), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 11174), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 24380), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 24411), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 16627), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 16657), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 19768), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 19797), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 20498), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 20528), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 26419), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 26451), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 23560), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 23593), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 22783), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 22814), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 21193), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 21222), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 18719), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 18749), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 13256), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 13290), null=True),
        ),
        migrations.AlterField(
            model_name='userpurchasedtemplates',
            name='purchased_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 30467), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 22072), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 22104), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 27047), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 27077), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 13992), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='path',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 14021), null=True),
        ),
        migrations.AlterField(
            model_name='usersubscriptionplan',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 14951), null=True),
        ),
        migrations.AlterField(
            model_name='usersubscriptionplan',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 14979), null=True),
        ),
        migrations.AlterField(
            model_name='zohoauthtoken',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 29130), null=True),
        ),
        migrations.AlterField(
            model_name='zohoauthtoken',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 31, 10, 43, 14, 29160), null=True),
        ),
    ]
