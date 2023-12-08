import uuid
from django.db import models

from modules.user.models import User

class Order(models.Model):
	class Meta:
		db_table = "orders"
  
	ORDER_STATUS = [
		("processing", "processing"),
		("on_hold", "on hold"),
		("cancelled", "cancelled"),
		("completed", "completed"),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	order_no = models.CharField(max_length=35, null=False, blank=False)
	port_of_loading = models.CharField(max_length=50, null=True, blank=True)
	port_of_discharge = models.CharField(max_length=50, null=True, blank=True)
	status = models.CharField(
		max_length=35, null=False, blank=False,
		choices=ORDER_STATUS,
		default="processing"
  	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	@staticmethod
	def generate_unique_code(self, prefix="A"):
		last_entry = self.objects.order_by('-order_no').first()

		if last_entry:
			last_number = int(last_entry.your_running_number[len(prefix):])
		else:
			last_number = 0

		new_number = last_number + 1

		# Format the new running number
		unique_message_reference = f"{prefix}{new_number:04d}"
		return unique_message_reference

	@staticmethod
	def save(self, *args, **kwargs):
		self.order_no = self.generate_unique_code(prefix="A")
		super().save(*args, **kwargs)
  
	def __str__(self):
		return f"{self.order_no}"

class OrderAssignee(models.Model):
	class Meta:
		db_table = "order_assignees"
  
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	order = models.ForeignKey(
		Order, on_delete=models.CASCADE, 
		null=False, 
		blank=False,
		unique=False,
		db_column="order"
		)
 
	user = models.ForeignKey(
		User, on_delete=models.CASCADE, 
		null=False, 
		blank=False,
		unique=False,
		db_column="user"
		)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
 
 
