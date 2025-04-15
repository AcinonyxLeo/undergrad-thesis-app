from django.contrib import admin
from .models import lora_details, ESP32Mapping
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin  # Changed from ExportMixin
from import_export.formats import base_formats  # Required for format handling

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
        export_order = fields  # Maintain column order

@admin.register(lora_details)
class LoraDetailsAdmin(ImportExportModelAdmin):  # Changed to ImportExportModelAdmin
    resource_class = LoraDetailsResource
    formats = [base_formats.XLSX, base_formats.CSV]  # Define supported formats
    
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

    # Removed the problematic get_export_data override
    # The parent class already handles this properly

@admin.register(ESP32Mapping)
class ESP32MappingAdmin(admin.ModelAdmin):
    pass