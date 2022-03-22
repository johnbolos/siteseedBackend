# Generated by Django 3.1.5 on 2021-05-06 03:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0068_auto_20210430_0401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersites',
            old_name='path',
            new_name='json_path',
        ),
        migrations.AddField(
            model_name='usersites',
            name='folder_path',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='contributorrolepermission',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 637196), null=True),
        ),
        migrations.AlterField(
            model_name='contributorrolepermission',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 637225), null=True),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 618433), null=True),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 618471), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 626850), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 626880), null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 626205), null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 626232), null=True),
        ),
        migrations.AlterField(
            model_name='ssfaqs',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 637868), null=True),
        ),
        migrations.AlterField(
            model_name='ssfaqs',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 637989), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 634721), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='endDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 634686), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 634654), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 634740), null=True),
        ),
        migrations.AlterField(
            model_name='sspromocodes',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 639243), null=True),
        ),
        migrations.AlterField(
            model_name='sspromocodes',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 639271), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 635376), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='releaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 635331), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 635426), null=True),
        ),
        migrations.AlterField(
            model_name='ssstripecustomers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 621545), null=True),
        ),
        migrations.AlterField(
            model_name='ssstripecustomers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 621574), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 620926), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 620955), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 624700), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 624729), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 619537), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 619566), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 620283), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 620313), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 633959), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 633989), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 625431), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 625462), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 628413), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 628441), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 629092), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 629120), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 636010), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 636039), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 633253), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 633306), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 631221), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 631249), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 629741), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 629770), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 627728), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 627762), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 622206), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 622235), null=True),
        ),
        migrations.AlterField(
            model_name='userpurchasedtemplates',
            name='purchased_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 639957), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 630548), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 630577), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 636596), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 636625), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 622944), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 622972), null=True),
        ),
        migrations.AlterField(
            model_name='usersubscriptionplan',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 623942), null=True),
        ),
        migrations.AlterField(
            model_name='usersubscriptionplan',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 623972), null=True),
        ),
        migrations.AlterField(
            model_name='zohoauthtoken',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 638585), null=True),
        ),
        migrations.AlterField(
            model_name='zohoauthtoken',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 3, 4, 27, 638613), null=True),
        ),
    ]