from django.contrib import admin
from .models import Test, Question, Choice

 
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4
    
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 4
    
class TestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Test Name',        {'fields': ['test_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [QuestionInline]
 
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Name',        {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    
admin.site.register(Test,TestAdmin)
admin.site.register(Question,QuestionAdmin)