from django.db import models


class Story(models.Model):
	story = models.TextField()
	name = models.TextField()
	letter = models.ForeignKey(Letter)

	class Meta:
		verbose_name_plural = "stories"

class Player(models.Model):
	title = models.CharField(max_length=255, default='Pilgrim')
	avatar = models.CharField(max_length=255)
	banner = models.CharField(max_length=255)
	trouble_technique = models.CharField(max_length=500)
	helping_technique = models.CharField(max_length=500)
	trouble_state = models.BooleanField(default=False)
	num_white_tokens = models.PositiveIntegerField(default=0)
	num_black_tokens = models.PositiveIntegerField(default=0)
	num_tokens_kept_in_current_turn = models.PositiveIntegerField(default=0)
	story = models.ForeignKey(Story)

	def in_trouble():
		return self.trouble_state

class Letter(models.Model):
	content = models.TextField()
	goal_words = models.TextField() #JSON serialized list of goal words
