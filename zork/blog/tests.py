from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Blog
from django.contrib.auth.models import User
from .forms import BlogForm
from django.urls import resolve
from .views import home,detail,create


class DetailTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='Tanja')
        self.blog = Blog.objects.create(title="summer",content="test me",author= user)

    def test_detail_view_status_ok(self):
        detail_url = reverse('blog:detail',kwargs={'pk':1})
        response = self.client.get(detail_url)
        self.assertEquals(response.status_code,200)

    def test_detail_view_status_not_found_404(self):
        detail_url = reverse('blog:detail',kwargs={'pk':145})
        response = self.client.get(detail_url)
        self.assertEquals(response.status_code,404)


    def test_detail_url_resolvers_to_detail_view(self):
        view = resolve('/blog/detail/1/')
        self.assertEquals(view.func,detail)

    def test_detail_view_contains_link_to_home_view(self):
        detail_url = reverse('blog:detail',kwargs={'pk':1})
        home_url = reverse('blog:home')
        response = self.client.get(detail_url)
        self.assertContains(response,'href="{0}"'.format(home_url))

class CreateTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='Tanja')
        self.blog = Blog.objects.create(title="summer",content="test me",author=user)


    def test_csrf_token(self):
        create_url = reverse('blog:create')
        response = self.client.get(create_url)
        self.assertContains(response,'csrfmiddlewaretoken')

    def test_create_blog_valid_data(self):
        url = reverse('blog:create')
        data = {'title':'gh','content':"fjfjfj"}
        response = self.client.post(url,data)
        self.assertTrue(Blog.objects.exists())

    def test_create_form_empty_fields_data(self):
            '''
            Invalid post data should not redirect
            The expected behavior is to show the form again with validation
            '''
            url = reverse('blog:create')
            data = {
                'title':"",
                "content":"",
                #"author":"",
            }
            response = self.client.post(url,data)
            self.assertEquals(response.status_code,200)
            # should be an error
            #self.assertFalse(Blog.objects.exists())

    def test_create_blog_invalid_data(self):
        url = reverse('blog:create')
        response = self.client.post(url,{})
        form = response.context.get('form')
        self.assertEquals(response.status_code,200)
        self.assertTrue(form.errors)

    def test_new_topic_contains_form(self):
        url = reverse('blog:create')
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form,BlogForm)
