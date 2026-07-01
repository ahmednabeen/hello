from django.contrib import admin, messages
from django.utils import timezone
from .pending_models import PendingDoctor, PendingHospital
from .models import Doctor, Hospital, Location, Specialty


def approve_single_doctor(pending):
    location = None
    if pending.location_text:
        location, _ = Location.objects.get_or_create(name=pending.location_text.strip())

    hospital = None
    if pending.hospital_text:
        hospital, _ = Hospital.objects.get_or_create(name=pending.hospital_text.strip())

    doctor = Doctor(
        name=pending.name,
        designation=pending.designation,
        qualifications=pending.qualifications,
        experience_years=pending.experience_years,
        location=location,
        hospital=hospital,
        about=pending.about,
    )
    if pending.profile_picture:
        doctor.profile_picture = pending.profile_picture
    doctor.save()

    if pending.specialties_text:
        names = [s.strip() for s in pending.specialties_text.split(',') if s.strip()]
        for name in names:
            specialty, _ = Specialty.objects.get_or_create(name=name)
            doctor.specialties.add(specialty)

    pending.status = 'approved'
    pending.reviewed_at = timezone.now()
    pending.save()


def approve_single_hospital(pending):
    location = None
    if pending.location_text:
        location, _ = Location.objects.get_or_create(name=pending.location_text.strip())

    hospital = Hospital(
        name=pending.name,
        address=pending.address,
        contact_numbers=pending.contact_numbers,
        facilities=pending.facilities,
        about=pending.about,
        location=location,
    )
    if pending.image:
        hospital.image = pending.image
    hospital.save()

    pending.status = 'approved'
    pending.reviewed_at = timezone.now()
    pending.save()


def reject_single(instance):
    if instance.status == 'approved':
        return
    instance.status = 'rejected'
    instance.reviewed_at = timezone.now()
    instance.save()


@admin.action(description='Approve selected doctors')
def approve_doctors(modeladmin, request, queryset):
    for pending in queryset.filter(status='pending'):
        try:
            approve_single_doctor(pending)
            modeladmin.message_user(
                request, f'Approved doctor: {pending.name}', messages.SUCCESS
            )
        except Exception as e:
            modeladmin.message_user(
                request, f'Error approving {pending.name}: {e}', messages.ERROR
            )


@admin.action(description='Reject selected doctors')
def reject_doctors(modeladmin, request, queryset):
    updated = queryset.filter(status='pending').update(
        status='rejected', reviewed_at=timezone.now()
    )
    modeladmin.message_user(
        request, f'Rejected {updated} doctor registration(s).', messages.WARNING
    )


@admin.action(description='Approve selected hospitals')
def approve_hospitals(modeladmin, request, queryset):
    for pending in queryset.filter(status='pending'):
        try:
            approve_single_hospital(pending)
            modeladmin.message_user(
                request, f'Approved hospital: {pending.name}', messages.SUCCESS
            )
        except Exception as e:
            modeladmin.message_user(
                request, f'Error approving {pending.name}: {e}', messages.ERROR
            )


@admin.action(description='Reject selected hospitals')
def reject_hospitals(modeladmin, request, queryset):
    updated = queryset.filter(status='pending').update(
        status='rejected', reviewed_at=timezone.now()
    )
    modeladmin.message_user(
        request, f'Rejected {updated} hospital registration(s).', messages.WARNING
    )


@admin.register(PendingDoctor)
class PendingDoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'location_text', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('name', 'designation', 'location_text')
    readonly_fields = ('submitted_at', 'reviewed_at')
    actions = [approve_doctors, reject_doctors]
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'designation', 'qualifications', 'experience_years', 'profile_picture')
        }),
        ('Details', {
            'fields': ('about',)
        }),
        ('Registration Info', {
            'fields': ('location_text', 'hospital_text', 'specialties_text')
        }),
        ('Status', {
            'fields': ('status', 'admin_notes', 'submitted_at', 'reviewed_at')
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.status == 'approved' and not Doctor.objects.filter(name=obj.name).exists():
            approve_single_doctor(obj)
            messages.success(request, f'Approved doctor: {obj.name}')
        else:
            super().save_model(request, obj, form, change)


@admin.register(PendingHospital)
class PendingHospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_text', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('name', 'location_text')
    readonly_fields = ('submitted_at', 'reviewed_at')
    actions = [approve_hospitals, reject_hospitals]
    fieldsets = (
        ('Hospital Information', {
            'fields': ('name', 'address', 'contact_numbers', 'facilities', 'about', 'image')
        }),
        ('Registration Info', {
            'fields': ('location_text',)
        }),
        ('Status', {
            'fields': ('status', 'admin_notes', 'submitted_at', 'reviewed_at')
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.status == 'approved' and not Hospital.objects.filter(name=obj.name).exists():
            approve_single_hospital(obj)
            messages.success(request, f'Approved hospital: {obj.name}')
        else:
            super().save_model(request, obj, form, change)
