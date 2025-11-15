from django.db import models
from django.contrib.auth.models import AbstractUser
from academics.models import *
from django.utils import timezone



class User(AbstractUser):

    USER_TYPE_CHOICE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]

    user_type = models.CharField(choices=USER_TYPE_CHOICE, max_length=10, default='Admin')

    user_id = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        db_index=True,
        blank=True,
        null=True
    )

    # login user_id set
    USERNAME_FIELD = 'user_id'

    # for superuser create
    REQUIRED_FIELDS = ['username', 'email'] 


    # Student class (Must contain code field)
    student_class = models.ForeignKey(
        StudentClass,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    #
    # Generate Prefix (YYMM + type-digit)
    #
    def _generate_prefix(self) -> str:
        now = timezone.now()
        year = now.strftime("%y")     # 25
        month = now.strftime("%m")    # 01..12

        base = f"{year}{month}"

        if self.user_type == "Admin":
            return base + "1"

        elif self.user_type == "Teacher":
            return base + "2"

        elif self.user_type == "Student":
            if self.student_class and hasattr(self.student_class, "code"):
                return base + str(self.student_class.code).zfill(2)

        return base

    #
    # Generate Final User ID
    #
    def generate_user_id(self):
        prefix = self._generate_prefix()

        # Count existing users with same prefix
        count = User.objects.filter(user_id__startswith=prefix).count()

        # 4-digit sequence
        sequence = str(count + 1).zfill(4)

        return prefix + sequence

    #
    # Override save
    #
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.generate_user_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
