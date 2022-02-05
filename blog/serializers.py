from rest_framework import serializers
from blog.models import AllCategory
from blog.models import EachCategory




class AllCategorySerializer(serializers.HyperlinkedModelSerializer):
	Course = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='eachcategory-detail')
	
	class Meta:
		model = AllCategory
		fields = [
		'url',
		'pk',
		'name',
		'Course']
class EachCategorySerializer(serializers.HyperlinkedModelSerializer):
	category = serializers.SlugRelatedField(queryset=AllCategory.objects.all(),slug_field='name')
	
	
	class Meta:
		model = EachCategory
		fields = ['url',
		'pk',
		'Course',
		'Title',
		'Blogdetails',
		'Image',
		'category',
		'start_date',]
		
		

