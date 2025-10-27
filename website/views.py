from django.shortcuts import render

from django.http import HttpResponse

def index_view(request):
    html_code = """
    <!DOCTYPE html>
    <html lang="fa">
    <head>
        <meta charset="UTF-8">
        <title>صفحه تست</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .card {
                background: white;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #0078D7;
            }
            p {
                color: #555;
            }
            button {
                background: #0078D7;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
            }
            button:hover {
                background: #005a9e;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>سلام جنگو 👋</h1>
            <p>این یک صفحه تست ساده است.</p>
            <button onclick="alert('کلیک شد!')">کلیک کن</button>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_code)

def contact_view(request):
    return HttpResponse('This is contact')

def about_view(request):
    return HttpResponse('This is about')