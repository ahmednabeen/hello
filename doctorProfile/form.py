from django import forms
from .models import Doctor, Hospital


class DoctorRegistrationForm(forms.ModelForm):
    specialties_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition',
            'placeholder': 'Cardiology, Neurology, Dermatology',
        }),
        help_text='Enter specialties separated by commas',
    )
    location_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition',
            'placeholder': 'Write your district',
        }),
    )
    hospital_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition',
            'placeholder': 'Write the hospital name in where you practice',
        }),
    )

    about = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition',
            'rows': 4,
            'placeholder': 'About yourself...',
        }),
    )

    class Meta:
        model = Doctor
        fields = [
            'name', 'designation', 'qualifications', 'experience_years',
            'profile_picture',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'placeholder': 'Dr. John Doe'}),
            'designation': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'placeholder': 'Cardiologist'}),
            'qualifications': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'placeholder': 'MBBS, FCPS (Cardiology)'}),
            'experience_years': forms.NumberInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'placeholder': '10'}),
            'profile_picture': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition'}),
        }


class HospitalRegistrationForm(forms.ModelForm):
    location_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition',
            'placeholder': 'Write your district',
        }),
    )

    class Meta:
        model = Hospital
        fields = [
            'name', 'address', 'contact_numbers',
            'facilities', 'about', 'image',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'placeholder': 'Hospital Name'}),
            'address': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'rows': 3, 'placeholder': 'Full address...'}),
            'contact_numbers': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'placeholder': '01790-000000, 01900-000000'}),
            'facilities': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'rows': 3, 'placeholder': '24/7 Emergency, ICU, CCU, Pharmacy...'}),
            'about': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition', 'rows': 4, 'placeholder': 'About the hospital...'}),
            'image': forms.FileInput(attrs={'class': 'w-full px-4 py-3 rounded-xl bg-white border border-slate-300 focus:ring-2 focus:ring-accent focus:border-accent transition'}),
        }
