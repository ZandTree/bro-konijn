
    # def test_create_form_empty_fields_data(self):
    #         '''
    #         Invalid post data should not redirect
    #         The expected behavior is to show the form again with validation
    #         '''
    #         url = reverse('blog:create')
    #         data = {
    #             'title':"",
    #             "content":"",
    #             #"author":"",
    #         }
    #         response = self.client.post(url,data)
    #         self.assertEquals(response.status_code,200)
    #         #self.assertFalse(Blog.objects.exists())
    #
    # def test_create_blog_valid_data(self):
    #     url = reverse('blog:create')
    #     data = {'title':'gh','content':"fjfjfj"}
    #     response = self.client.post(url,data)
    #     self.assertTrue(Blog.objects.exists())
# <p>blog number is {{blogs.number}}</p>
# <p>then paginator blogs.paginator</p>
# <h5>blogs has previous {{blogs.has_previous}}</h5>
# <p>{{blogs.paginator}}</p>
# <p>{{blogs.paginator.count}}</p>
# <p>{{blogs.paginator.num_page}}</p>
# <p>{{blogs.paginator.page_range}}</p>
# <h5>blogs has next {{blogs.has_next}}</h5>
# <span class="current">
#     Page {{ blogs.number }} of {{ blogs.paginator.num_pages }}.
# </span>
# <div class="pagination">
#
#     <div class="pagination">
#
#         <span class="step-links">
#             <i class="fa fa-angle-double-left" aria-hidden="true"></i>
#             {% if blogs.has_previous %}
#                 <a href="?page={{ blogs.previous_page_number }}">previous</a>
#             {% endif %}
#
#             {% for num in blogs.paginator.page_range %}
#
#                 {% if blogs.number == num %}
#                 <span class="current">{{ num }}</span>
#                 {% elif num > blogs.number|add:'-3' and num < blogs.number|add:'3' %}
#                 <a class="pagination-number" href="?page={{ num }}">{{ num }}</a>
#                 {% endif %}
#
#               {% endfor %}
#
#
#             {% if blogs.has_next %}
#                 <a href="?page={{ blogs.next_page_number }}">next</a>
#                 <i class="fa fa-angle-double-right" aria-hidden="true"></i>
#             {% endif %}
#         </span>
#
#     </div>
# <!-- option 1 ul-based -->
# {% if blogs.has_other_pages %}
#   <ul class="pagination">
#     {% if blogs.has_previous %}
#       <li><a class="pagination-action" href="?page={{ blogs.previous_page_number }}">&laquo;</a></li>
#     {% else %}
#       <li class="disabled"><span>&laquo;</span></li>
#     {% endif %}
#
#      {% for i in blogs.paginator.page_range %}
#       {% if blogs.number == i %}
#         <li class="active " ><span class="pagination-number pagination-current">{{ i }}<span class="sr-only">(current)</span></span></li>
#       {% else %}
#         <li><a href="?page={{ i }}" class="pagination-number">{{ i }}</a></li>
#       {% endif %}
#     {% endfor %}
#
#         {% if page_obj.has_next %}
#           <li><a href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
#         {% else %}
#           <li class="disabled"><a href="#">&raquo;</a></li>
#         {% endif %}
#
#   </ul>
#   {% endif %}
# <!-- end option 1 ul-based   -->
