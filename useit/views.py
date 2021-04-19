from django.shortcuts import render
from .models import Tool
# Create your views here.

"""def Tool_list(request): 
    tools = Tool.objects.all().order_by('_date')

    context = {
        'tools': tools
    }

    return render(request,'tools.html',context)

def tool_detail(request,user_slug, tool_name):
    tool = Tool.objects.get(user__slug=user_slug,name= tool_name )

    context = {
        'tool': tool
    }

    return render(request, 'tool.html', context)"""