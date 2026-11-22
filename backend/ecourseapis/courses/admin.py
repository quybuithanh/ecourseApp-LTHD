from django.contrib import admin
from django.utils.safestring import mark_safe
from courses.models import Category, Course, Lesson, Tag

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

class Meta:
    model = Lesson
    fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'active', 'created_date', 'updated_date']
    search_fields = ['subject', 'content']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['image_view']
    form = LessonForm

    def image_view(self, lesson):
        return mark_safe(f'<img src="/static/{lesson.image.name}" width="200" />')

    class Media:
        css = {
            'all': ('/static/css/styles.css',)
        }

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
