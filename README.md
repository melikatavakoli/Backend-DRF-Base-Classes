# Django Common Base Package

A reusable Django & Django REST Framework (DRF) **base package** that provides common building blocks for modern backend projects.

This package is designed to eliminate boilerplate code and standardize core patterns such as **soft delete**, **audit fields**, **base serializers**, **custom managers**, **pagination**, **middleware**, and **exception handling** across multiple projects.

---

## ✨ Features

- ✅ Soft Delete (Model, QuerySet, Manager)
- ✅ Base Models with audit fields (`created_at`, `updated_at`, `created_by`, `updated_by`)
- ✅ Reusable DRF Base Serializers
- ✅ Custom Managers & QuerySets
- ✅ Standard Pagination for DRF
- ✅ Global Exception Handling
- ✅ Common Middleware (current user, logging, etc.)
- ✅ Shared Filters & Utilities
- ✅ Clean, modular, production-ready structure
- ✅ Installable via `pip` (Git-based dependency)

---

## 📦 Installation

### Using pip (recommended)

```bash
pip install git+https://github.com/your-username/django-common-base.git
```

Or inside `requirements.txt`:

```text
git+https://github.com/your-username/django-common-base.git
```

---

## ⚙️ Django Setup

### 1. Add to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    "common",
]
```

---

### 2. Middleware (optional)

```python
MIDDLEWARE = [
    ...
    "common.middleware.current_user.CurrentUserMiddleware",
]
```

---

### 3. DRF Settings (optional)

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "common.paginations.pagination.StandardPagination",
    "EXCEPTION_HANDLER": "common.exceptions.handlers.custom_exception_handler",
}
```

---

## 🧱 Package Structure

```
common/
├── models/
│   ├── base.py
│   ├── audit.py
│   └── mixins.py
│
├── managers/
│   ├── soft_delete.py
│   └── queryset.py
│
├── serializers/
│   └── base.py
│
├── middleware/
│   └── current_user.py
│
├── paginations/
│   └── pagination.py
│
├── exceptions/
│   └── handlers.py
│
├── filters/
│   └── base.py
│
├── storage/
│   └── s3.py
│
├── utils/
│   ├── format.py
│   └── validators.py
│
└── __init__.py
```

---

## 🧩 Usage Examples

### Soft Delete Model

```python
from common.models.mixins import SoftDeleteModel

class Article(SoftDeleteModel):
    title = models.CharField(max_length=255)
```

```python
Article.objects.all()        # Only alive records
Article.all_objects.all()    # Includes deleted records
```

---

### Base Serializer

```python
from common.serializers.base import GenericModelSerializer
from .models import Article

class ArticleSerializer(GenericModelSerializer):
    class Meta(GenericModelSerializer.Meta):
        model = Article
        fields = GenericModelSerializer.Meta.fields + ("title",)
```

---

### Soft Delete Manager

```python
Article.objects.delete()        # Soft delete
Article.objects.hard_delete()   # Permanent delete
```

---

## 🎯 Design Goals

- DRY (Don't Repeat Yourself)
- Clean architecture
- High reusability across projects
- Minimal coupling with project-specific logic
- Production-grade defaults

---

## 🚀 When Should You Use This Package?

✅ You manage multiple Django/DRF projects  
✅ You want consistent base logic across services  
✅ You are tired of copying `common/` folders  
✅ You want a clean dependency instead of boilerplate  

---

## 🛠️ Compatibility

- Python 3.10+
- Django 4.2+
- Django REST Framework 3.14+

---

## 📄 License

MIT License  
Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Pull requests are welcome.  
For major changes, please open an issue first to discuss what you would like to change.

---

## ⭐ Support

If you find this package useful, please consider giving it a ⭐ on GitHub.
```

---
