from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()

    subject = forms.CharField(
        max_length=200
    )

    message = forms.CharField(
        widget=forms.Textarea
    )

    attachment = forms.FileField(
        required=False
    )

    def clean_attachment(self):

        file = self.cleaned_data.get("attachment")

        if not file:
            return file

        # Maximum 5 MB
        max_size = 5 * 1024 * 1024

        if file.size > max_size:
            raise forms.ValidationError(
                "File size must not exceed 5 MB."
            )

        allowed_extensions = {
            ".pdf",
            ".jpg",
            ".jpeg",
            ".png",
        }

        filename = file.name.lower()

        if not any(
            filename.endswith(extension)
            for extension in allowed_extensions
        ):
            raise forms.ValidationError(
                "Only PDF, JPG, JPEG, and PNG files are allowed."
            )

        return file