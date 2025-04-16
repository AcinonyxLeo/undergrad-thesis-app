from django.contrib import admin
from .models import lora_details, ESP32Mapping
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

# Admin site header customizations
admin.site.site_header = "LoRa Tracking System"  # Admin header
admin.site.site_title = "Admin Portal"          # Browser tab title
admin.site.index_title = "Device Management"    # Welcome text

class LoraDetailsResource(resources.ModelResource):
    # Custom fields
    location_lat = fields.Field(
        attribute='latitude',
        column_name='Latitude (Decimal Degrees)'
    )
    location_lon = fields.Field(
        attribute='longitude',
        column_name='Longitude (Decimal Degrees)'
    )
    vehicle_plate = fields.Field(
        attribute='plate_number',
        column_name='License Plate'
    )
    owner_name = fields.Field(
        attribute='last_name',
        column_name='Registered Owner'
    )
    
    # Add a calculated field
    satellite_status = fields.Field(column_name='Satellite Status')
    
    def dehydrate_satellite_status(self, obj):
        if obj.satellite >= 3:
            return "✅ Strong Signal"
        return "⚠️ Weak Signal"
    
    class Meta:
        model = lora_details
        fields = (
            'id',
            'packet_number',
            'timestamp',
            'owner_name',
            'vehicle_plate',
            'location_lat',
            'location_lon',
            'satellite',
            'satellite_status',
            'rssi',
            'speed',
        )
        export_order = fields

@admin.register(lora_details)
class LoraDetailsAdmin(ImportExportModelAdmin):
    resource_class = LoraDetailsResource
    formats = [base_formats.XLSX, base_formats.CSV]
    
    list_display = (
        'id',
        'packet_number',
        'timestamp',
        'last_name',
        'plate_number',
        'latitude',
        'longitude',
        'satellite',
        'rssi',
        'speed',
    )
    list_filter = ('satellite',)
    search_fields = ('plate_number', 'last_name')

    # Customize admin display name
    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        perms['name'] = "GPS Information"
        return perms

@admin.register(ESP32Mapping)
class ESP32MappingAdmin(admin.ModelAdmin):
    # Customize admin display name
    def get_model_perms(self, request):
        perms = super().get_model_perms(request)
        perms['name'] = "Vehicle Infomation"
        return perms