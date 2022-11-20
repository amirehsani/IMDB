# from django.shortcuts import render
#
# from movies.models import Movie
# # from movies.form import MovieForm
#
#
# # a view should be created each time a URL is made and included in URL file
# # for each page in our template, we should have a view function
# # when each template page is created, the view func should be created too
#
#
# def movies_list(request):
#     if request.method == 'GET':
#
#         movies = Movie.object.filter(is_valid=True)
#         context = {'movies': movies}
#
#         # when 'movies' was mentioned in the template page, pass each movie to be rendered
#         return render(request, 'movies_list.html', context=context)
#         # render has 3 attrs; 1. request, 2. template_name, 3. context
#
#     elif request.method == 'POST':
#         # when POST is used, we must have forms in our template page
#         form = MovieForm(request.POST, request.FILES)
#         # this is the form that movie edit passes to the movies list
#         if form.is_valid():
#             form.save()  # save the form information sent by the user
#             return redirect('movies_list')
#
#         return movie_add(request, form)
#
#
# def movie_detail(request, pk):  # PK stands for Primary Key
#     # movie = get_object_or_404(Movie, pk=pk, is_valid=True)
#     # if requst.method == 'GET':
#     #     return HttpResponse(f'<h1>This is movie {pk}</h1>')
#     #
#     # elif requst.method == 'POST':
#     #     form = MovieForm(request.POST, request.FILES, istance=movie)
#     #     if not form.is_valid():
#     #         return movie_edit(request, pk, movie_form=form)
#     #
#     #     form.save()
#     #     return redirect('movie_detail', pk=pk)
#
from django.shortcuts import render
from movies.models import Movie


# from movies.form import MovieForm

def movies_list(request):
    pass


def movie_detail(request):
    pass


def movie_add(request):
    pass


def movie_edit(request):
    pass


def movie_delete(request):
    pass
