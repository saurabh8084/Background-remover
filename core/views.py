from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views import View
from .forms import ImageForm
from . import utils

import base64
import mimetypes
import os


class HomeView(View):
    def get(self, requset):
        form = ImageForm()
        context = {'form': form}
        return render(requset, 'index.html', context=context)

    def post(self, request):
        files = request.FILES
        image = files.get("img", None)
        if image:
            output = utils.remove_bg(image)

            # print(type(output))
            # print(output)
            # output = base64.b64encode(output).decode("utf-8")

            # response = FileResponse(output)
            response = HttpResponse(
                content_type=mimetypes.guess_type("bgremove.png"))
            response.write(output)
            response["content-Disposition"] = "attachment; filename={0}".format(
                os.path.splitext(image.name)[0]+".png")
        else:
            response = HttpResponse("Successfull")

        # form = ImageForm(data=request.POST, files=request.FILES)
        # if form.is_valid():
        #     form.save()
        # else:
        #     image_form = ImageForm()

        #     context = {'image_form':image_form}
        #     return render(context=context)

        # return HttpResponse("Successfull")
        #    return render(request,'index.html',context=context)
        return response


class RemoveBGView(View):
    def post(self, request):
        try:
            files = request.FILES
            image = files.get("img", None)
            output = utils.remove_bg(image)

            response = HttpResponse(
                content_type=mimetypes.guess_type("bgremove.png"))
            response.write(output)
            response["content-Disposition"] = "attachment; filename={0}".format(
                os.path.splitext(image.name)[0]+".png")
            return response
        except Exception as ex:
            print(ex)
            response = HttpResponse("Unknown data!")
            response.status_code = 500
            return response
