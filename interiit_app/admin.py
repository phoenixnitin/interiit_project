from django.contrib import admin
from .models import Sport_Aquatics_Men, Sport_Aquatics_Women, Sport_Aquatics_Staff

# Register your models here.

admin.site.register(Sport_Aquatics_Men)
admin.site.register(Sport_Aquatics_Women)
admin.site.register(Sport_Aquatics_Staff)

