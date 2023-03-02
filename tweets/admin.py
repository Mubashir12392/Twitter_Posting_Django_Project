from django.contrib import admin
from tweets.models import Tweet

# Register your models here.

@admin.register(Tweet)
class Tweet_Class(admin.ModelAdmin):
    list_display= ['author', 'created_at', 'updated_at']
    date_hierarchy= 'created_at'
    actions_on_top= True 
    
    list_filter= ['author', 'created_at', 'updated_at']
