from django.db import models

CONTRACT_TYPES = (
    ('a', 'A'),
    ('b', 'B'),
    ('c', 'C'),
    ('d', 'D'),
    ('e', 'E'),
    ('f', 'F'),
    ('g', 'G'),
    ('h', 'H'),
    ('i', 'I'),
    ('j', 'J'),
)

CURRENCY_CHOICES = (
    ('usd', 'US Dollars'),
    ('cad', 'Canadian Dollars'),
)


class Contract(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(choices=CONTRACT_TYPES, max_length=10)
    date = models.DateTimeField()
    authors = models.ManyToManyField('Person')
    premium_value = models.DecimalField(
        max_digits=10, decimal_places=2)
    premium_currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES)
    limit_value = models.DecimalField(
        max_digits=10, decimal_places=2)
    limit_currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES)
    franchise_value = models.DecimalField(
        max_digits=10, decimal_places=2)
    franchise_currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES)
    attachment_value = models.DecimalField(
        max_digits=10, decimal_places=2)
    attachment_currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES)

    @property
    def premium(self):
        return {'value': self.premium_value,
                'currency': self.premium_currency}

    @premium.setter
    def premium(self, value):
        self.premium_value = value['value']
        self.premium_currency = value['currency']

    @property
    def limit(self):
        return {'value': self.limit_value,
                'currency': self.limit_currency}

    @limit.setter
    def limit(self, value):
        self.limit_value = value['value']
        self.limit_currency = value['currency']

    @property
    def franchise(self):
        return {'value': self.franchise_value,
                'currency': self.franchise_currency}

    @franchise.setter
    def franchise(self, value):
        self.franchise_value = value['value']
        self.franchise_currency = value['currency']

    @property
    def attachment(self):
        return {'value': self.attachment_value,
                'currency': self.attachment_currency}

    @attachment.setter
    def attachment(self, value):
        self.attachment_value = value['value']
        self.attachment_currency = value['currency']


class Portfolio(models.Model):
    contracts = models.ManyToManyField('Contract')


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
