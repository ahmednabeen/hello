from django.apps import AppConfig


class DoctorprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctorProfile'

    def ready(self):
        import doctorProfile.pending_admin
