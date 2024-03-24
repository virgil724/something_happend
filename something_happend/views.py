from collections import OrderedDict
from django.urls import NoReverseMatch, get_resolver, URLResolver, URLPattern
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.routers import SimpleRouter


class ApiRootView(APIView):
    router_list = []

    def add_router(self, router: SimpleRouter):
        self.router_list.append(router)

    def get(self, request, *args, **kwargs):
        # print(reverse("api_v1:comment_report-detail"))
        api_dict = OrderedDict()
        api_urls = OrderedDict()
        # print(reverse("api_v1:comment-list"))
        namespace = request.resolver_match.namespace
        for router in self.router_list:
            list_name = router.routes[0].name
            for prefix, viewset, basename in router.registry:
                api_dict[prefix] = list_name.format(basename=basename)
            for key, url_name in api_dict.items():
                if namespace:
                    url_name = namespace + ":" + url_name
                    
                try:    
                    api_urls[key] = reverse(
                        url_name,
                        args=args,
                        kwargs=kwargs,
                        request=request,
                        format=kwargs.get("format"),
                    )
                    print(url_name)
                except NoReverseMatch:
                    pass
        return Response(api_urls)
