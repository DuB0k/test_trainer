from django.contrib import admin
from .models import Test, Question, Choice

    
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 20
    
class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['test_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]
    list_display = ('test_name', 'pub_date','was_published_recently')
    
admin.site.register(Test, TestAdmin)