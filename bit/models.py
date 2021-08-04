from django.db import models
import requests
# Create your models here.
class Bitcoin(models.Model):
    amount = models.FloatField(blank=True)
    price = models.FloatField(blank=True)
    test = models.CharField(max_length=1000)
    def __str__(self):
        return self.amount

    def save(self, *args, **kwargs): 
        # get currenct rate
        url = "https://api.bitbay.net/rest/trading/ticker"
        headers = {'content-type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        data_j = response.json()
        self.price = self.amount * float(data_j["items"]["BTC-USD"]["rate"])
        super(Bitcoin, self).save(*args, **kwargs) 

