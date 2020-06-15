from django.test import SimpleTestCase
from django.urls import reverse,resolve
from budget.views import project_detail,project_list,ProjectCreateView
class TestUrls(SimpleTestCase):
	def test_list_url_resolves(self):
		url = reverse('list')
		self.assertEquals(resolve(url).func, project_list)

	# def test_add_url_resolves(self):
	# 	url = reverse('add')
	# 	self.assertEquals(resolve(url).func, ProjectCreateView)

	# def test_detail_url_resolves(self):
	# 	url = reverse('detail',args=['some.slug'])
	# 	self.assertEquals(resolve(url).func, project_detail)
