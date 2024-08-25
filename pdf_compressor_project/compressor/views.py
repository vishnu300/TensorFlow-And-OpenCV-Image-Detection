from django.shortcuts import render

# Create your views here.

# compressor/views.py

from django.shortcuts import render
from django.http import HttpResponse
import aspose.pdf as ap
import os

def compress_pdf(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        
        # Define input and output file paths
        input_path = f'temp/{pdf_file.name}'
        output_path = f'temp/compressed_{pdf_file.name}'

        # Save the uploaded file temporarily
        with open(input_path, 'wb+') as destination:
            for chunk in pdf_file.chunks():
                destination.write(chunk)

        # Compress the PDF
        comppdf = ap.Document(input_path)
        pdfopti = ap.optimization.OptimizationOptions()
        pdfopti.image_compression_options.compress_images = True
        comppdf.optimize_resources(pdfopti)
        comppdf.save(output_path)

        # Send the compressed PDF file as a response
        with open(output_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename=compressed_{pdf_file.name}'
            return response
    else:
        return render(request, 'compress_pdf.html')
