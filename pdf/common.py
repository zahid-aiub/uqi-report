# from django.template.loader import get_template
# from django.http import HttpResponse
#
# from weasyprint import HTML
#
#
# def render_pdf(template, data):
#     html_template = get_template(template)
#     rendered_html = html_template.render(data).encode(encoding="UTF-8")
#     pdf_file = HTML(string=rendered_html).write_pdf()
#
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     return response
