from django.contrib import admin
from .models import Category, Book, BookCopy

class BookCopyInline(admin.TabularInline):
    model = BookCopy
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'department', 'category', 'is_new_arrival', 'is_donated', 'total_copies', 'available_copies')
    list_filter = ('department', 'category', 'is_new_arrival', 'is_donated', 'language')
    search_fields = ('title', 'author', 'isbn', 'classification_number')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BookCopyInline]

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('accession_number', 'book', 'shelf_location', 'status', 'acquisition_date')
    list_filter = ('status', 'shelf_location')
    search_fields = ('accession_number', 'book__title', 'barcode')

