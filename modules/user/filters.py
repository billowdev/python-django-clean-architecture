from django_filters import FilterSet, CharFilter, DateTimeFilter
from datetime import datetime
from modules.user.models import User

# class BaseDatetimeFilter:
# 	def filter_created_at_iso(self, queryset, name, value):
# 		from datetime import datetime
# 		iso_datetime = datetime.fromisoformat(value)
# 		return queryset.filter(created_at__date=iso_datetime.date())

# 	def filter_updated_at_iso(self, queryset, name, value):
# 		from datetime import datetime
# 		iso_datetime = datetime.fromisoformat(value)
# 		return queryset.filter(updated_at__date=iso_datetime.date())
	
class UserFilter(FilterSet):
	username = CharFilter(field_name="username", lookup_expr='iexact')
	email = CharFilter(field_name="email", lookup_expr='email')
	first_name = CharFilter(field_name="first_name", lookup_expr='icontains')
	last_name = CharFilter(field_name="last_name", lookup_expr='icontains')
	created_at = CharFilter(method='filter_created_at_iso')
	updated_at = CharFilter(method='filter_updated_at_iso')

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
			'created_at',
			'updated_at',
		]

	def filter_created_at_iso(self, queryset, name, value):
		from datetime import datetime
		iso_datetime = datetime.fromisoformat(value)
		return queryset.filter(created_at__date=iso_datetime.date())

	def filter_updated_at_iso(self, queryset, name, value):
		from datetime import datetime
		iso_datetime = datetime.fromisoformat(value)
		return queryset.filter(updated_at__date=iso_datetime.date())