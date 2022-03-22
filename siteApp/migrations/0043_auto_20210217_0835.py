# Generated by Django 3.1.5 on 2021-02-17 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteApp', '0042_auto_20210217_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributorrolepermission',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 360821), null=True),
        ),
        migrations.AlterField(
            model_name='contributorrolepermission',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 360855), null=True),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 341824), null=True),
        ),
        migrations.AlterField(
            model_name='custmaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 341881), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 351023), null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 351085), null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 350385), null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 350416), null=True),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 349699), null=True),
        ),
        migrations.AlterField(
            model_name='ordermaster',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 349730), null=True),
        ),
        migrations.AlterField(
            model_name='ssfaqs',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 361463), null=True),
        ),
        migrations.AlterField(
            model_name='ssfaqs',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 361500), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 358039), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='endDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 358002), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='startDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 357972), null=True),
        ),
        migrations.AlterField(
            model_name='sslatestoffers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 358081), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 358739), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='releaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 358694), null=True),
        ),
        migrations.AlterField(
            model_name='ssroadmapreleases',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 358759), null=True),
        ),
        migrations.AlterField(
            model_name='ssstripecustomers',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 345115), null=True),
        ),
        migrations.AlterField(
            model_name='ssstripecustomers',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 345146), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 344477), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplans',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 344510), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 348308), null=True),
        ),
        migrations.AlterField(
            model_name='sssubscriptionplansdetails',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 348338), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 342973), null=True),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='thumbnail',
            field=models.ImageField(default='default-thumb.jpg', upload_to='template_thumbs'),
        ),
        migrations.AlterField(
            model_name='sstemplates',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 343005), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 343809), null=True),
        ),
        migrations.AlterField(
            model_name='sswebsitetype',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 343842), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 357332), null=True),
        ),
        migrations.AlterField(
            model_name='userbackupsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 357363), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 349030), null=True),
        ),
        migrations.AlterField(
            model_name='userbillingaddress',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 349060), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 352511), null=True),
        ),
        migrations.AlterField(
            model_name='userdomain',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 352545), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 353289), null=True),
        ),
        migrations.AlterField(
            model_name='userdomainhost',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 353328), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 359545), null=True),
        ),
        migrations.AlterField(
            model_name='userexports',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 359578), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 356603), null=True),
        ),
        migrations.AlterField(
            model_name='userfontssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 356632), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 355923), null=True),
        ),
        migrations.AlterField(
            model_name='userformssettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 355957), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 354133), null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 354191), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 351706), null=True),
        ),
        migrations.AlterField(
            model_name='usernotificationsettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 351740), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 345813), null=True),
        ),
        migrations.AlterField(
            model_name='userpaymentmethod',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 345845), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 355115), null=True),
        ),
        migrations.AlterField(
            model_name='userseosettings',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 355162), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 360182), null=True),
        ),
        migrations.AlterField(
            model_name='usersitecontributors',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 360212), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 346580), null=True),
        ),
        migrations.AlterField(
            model_name='usersites',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 346611), null=True),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='createdOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 347554), null=True),
        ),
        migrations.AlterField(
            model_name='usersitesplan',
            name='updatedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 17, 8, 35, 36, 347584), null=True),
        ),
    ]
