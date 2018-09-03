from django.shortcuts import render
from django.views import generic
from catalog.models import Memory, RAM, Processor, Category, Product, ProductInstance, Brand
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView


class ProductListView(ListView):
    model = Product
    paginate_by = 2
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context



class ProductDetailView(generic.DetailView):
    model = Product

    def product_detail_view(request, primary_key):
        product = get_object_or_404(Product, pk=primary_key)
        return render(request, 'catalog/product_detail.html', context={'product': product})


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_products = Product.objects.all().count()
    num_instances = ProductInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = ProductInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_brands = Brand.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_products': num_products,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_brands': num_brands,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)  # Specify your own template name/location

class BrandListView(generic.ListView):
    """
    Generic class-based list view for a list of authors.
    """
    model = Brand
    paginate_by = 2

    template_name = 'brand_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BrandListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BrandDetailView(generic.DetailView):
    """
    Generic class-based detail view for an author.
    """
    model = Brand


    def brand_detail_view(request, primary_key):
        brand = get_object_or_404(Product, pk=primary_key)
        return render(request, 'catalog/brand_detail.html', context={'brand': brand})