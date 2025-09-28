from django.db import models
from django.contrib.auth.models import User


class Subjects(models.Model):
	name = models.CharField("Учебный предмет", max_length = 50)
	
	def __str__(self):
		return f"{self.name}"
	class Meta:
		verbose_name_plural = "Учебные предметы"
		verbose_name = "Учебный предмет"
		
class Klass(models.Model):
	name = models.CharField("Класс", max_length = 2)
	
	def __str__(self):
		return f"{self.name}"
	class Meta:
		verbose_name_plural = "Классы"
		verbose_name = "Класс"
		

class Teacher(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
	photo = models.ImageField(upload_to='teachers_photos/', blank=True, null=True, verbose_name="Фото")
	fio = models.CharField("ФИО", max_length=50)
	description = models.TextField("Onиcaниe", null=True, blank=True)
	price = models.TextField("Цена", null=True, blank=True)
	subjects = models.ManyToManyField(Subjects, verbose_name="Учебный предмет")
	klass = models.ManyToManyField(Klass, verbose_name= "Класс")
	phone = models.CharField("Телефон", max_length=20, blank=True, null=True)

	def average_rating(self):
		reviews = self.reviews.all()  # предполагается, что related_name='reviews'
		if not reviews:
			return 0
		avg = sum(review.rating for review in reviews) / len(reviews)
		return round(avg, 1)

	def __str__(self):
		return f"{self.fio}, {self.subjects_list}"
	
	class Meta:
		verbose_name_plural = "Учителя"
		verbose_name = "Учитель"

	@property
	def subjects_list(self):
		return ", ".join(map(str, self.subjects.all()))
	
	@property
	def klass_list(self):
		return ", ".join(map(str, self.klass.all()))


class Review(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Отзыв")
    rating = models.IntegerField(verbose_name="Оценка", choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.teacher.fio}"