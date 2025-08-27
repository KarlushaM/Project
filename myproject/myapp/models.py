from django.db import models

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

	fio = models.CharField("ФИО", max_length=20)
	description = models.TextField("Onиcaниe", null=True, blank=True)
	price = models.TextField("Цена", null=True, blank=True)
	subjects = models.ManyToManyField(Subjects, verbose_name="Учебный предмет")
	author = models.ManyToManyField(Klass, verbose_name= "Класс")

	def __str__(self):
		return f"{self.fio}, {self.subjects}"
	
	class Meta:
		verbose_name_plural = "Учителя"
		verbose_name = "Учитель"
