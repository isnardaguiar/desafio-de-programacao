from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class UploadFileViewTest(TestCase):
    def test_upload_file_view_get(self):
        url = reverse('sales:upload')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/pages/upload.html')

    def test_upload_file_view_post(self):
        url = reverse('sales:upload')
        file_content = "purchaser name\titem description\titem price\tpurchase count\tmerchant address\tmerchant name\nJohn\tItem ABC\t10.0\t2\tAddress XYZ\tMerchant XYZ"
        file = SimpleUploadedFile("file.tab", file_content.encode('utf-8'))

        response = self.client.post(url, {'file': file})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sales/pages/result.html')

    def test_upload_file_with_error_view_post(self):
        url = reverse('sales:upload')
        # String onde era para ser números
        file_content = "purchaser name\titem description\titem price\tpurchase count\tmerchant address\tmerchant name\nJohn\tItem ABC\tabc\tabc\tAddress XYZ\tMerchant XYZ"
        file = SimpleUploadedFile("file.tab", file_content.encode('utf-8'))

        response = self.client.post(url, {'file': file})

        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'sales/pages/upload.html')


