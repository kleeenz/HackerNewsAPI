from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
import requests
from .filters import UserFilter
from .models import Job
from rest_framework import mixins, generics
from . serializers import modelSerial
from rest_framework import filters



def sync_items():

    '''
    connects to the API
    pulls the first 100 stories from the API
    syncs new data to the database if data does not exist in the databse

    '''
    recent_stories_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    get_recent_url = requests.get(recent_stories_url).json()
    for j in get_recent_url[:100]:
        recent_item_url = 'https://hacker-news.firebaseio.com/v0/item/'+ str(j) + '.json?print=pretty'
        convert_recent_item_to_json = requests.get(recent_item_url).json()
        added_field = {
            "By": convert_recent_item_to_json["by"],
            "identifier": convert_recent_item_to_json["id"],
            "type": convert_recent_item_to_json["type"],
            "title": convert_recent_item_to_json["title"]
        }

        Job.objects.get_or_create(id = added_field["identifier"], By = added_field["By"],
                                                  type = added_field["type"],
                                                  title = added_field["title"])


def display_all_items(request):

    '''
    pulls all data from the database
    create a paginator object to paginate the records pull
    encapsulate the db object into the paginator object
    renders the paginator object
    '''

    All_jobs = Job.objects.all()
    paginator = Paginator(All_jobs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'job_page': page_obj}
    return render(request, "Hacknews/indexApp.html", context)


def detailView(request, id):

    '''
    this function displays the details page based on the ID provided in the url
    it raises a 404 error if no item of that ID is found.
    '''

    items_needed = get_object_or_404(Job, id = id)
    context = {"items": items_needed}
    return render(request, "Hacknews/detail.html", context)


def search_result(request):
    '''
    create a view function to search by the title column
    the function gets values from the input field
    checks the value entered satisifies a search condition specified in line 64.
    renders the result
    '''

    if "input_text" in request.GET:
        query_data = request.GET['input_text']
        new_query = Job.objects.filter(title__icontains=query_data)
    else:
        new_query = Job.objects.all()
    return render(request, "Hacknews/search.html", {'new_q': new_query})


def filter_job(request):
    '''
    
    A filter query view, to filter through the type column in the db
    '''
    if "user_input" in request.GET:
        model_to_filter = Job.objects.filter(type__icontains = "user_input")
        queries = UserFilter(request.GET, queryset=model_to_filter)
    return render(request, "Hacknews/filter.html", {"queries": queries})
    

#API: model mixin to set up the API that allows for the get and post actions
class mymodelView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Job.objects.all()
    search_fields = ["title"]
    filter_backends = (filters.SearchFilter,)
    serializer_class = modelSerial

#get action
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

#post action
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class mymodelViewDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                    generics.GenericAPIView):

    queryset = Job.objects.all()
    serializer_class = modelSerial

#retrienve action
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

#update action
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#delete action
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

