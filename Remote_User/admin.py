from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    ClientRegister_Model,
    Spam_Prediction,
    detection_ratio,
    detection_accuracy
)

admin.site.register(ClientRegister_Model)
admin.site.register(Spam_Prediction)
admin.site.register(detection_ratio)
admin.site.register(detection_accuracy)