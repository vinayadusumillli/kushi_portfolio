import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Service

def populate_services():
    """Populate initial services"""
    
    services_data = [
        {
            'name': 'Sport Communications',
            'icon': 'fa-solid fa-comments',
            'order': 1,
            'description': 'Strategic communication planning and execution for sports organizations'
        },
        {
            'name': 'Market Research',
            'icon': 'fa-solid fa-chart-line',
            'order': 2,
            'description': 'Data-driven insights and competitive analysis'
        },
        {
            'name': 'Sponsorship & Brand Activation',
            'icon': 'fa-solid fa-handshake',
            'order': 3,
            'description': 'Partnership development and brand activation strategies'
        },
        {
            'name': 'Merchandise & Asset Tracking',
            'icon': 'fa-solid fa-box',
            'order': 4,
            'description': 'Efficient inventory management and asset coordination'
        },
        {
            'name': 'Event Operations',
            'icon': 'fa-solid fa-calendar-check',
            'order': 5,
            'description': 'Seamless event planning and execution'
        },
        {
            'name': 'Stakeholder Coordination',
            'icon': 'fa-solid fa-users',
            'order': 6,
            'description': 'Managing relationships across teams and partners'
        },
        {
            'name': 'Digital Marketing',
            'icon': 'fa-solid fa-bullhorn',
            'order': 7,
            'description': 'Social media strategy and digital campaign management'
        },
        {
            'name': 'Reporting & Data Tracking',
            'icon': 'fa-solid fa-chart-pie',
            'order': 8,
            'description': 'Performance analytics and detailed reporting'
        },
        {
            'name': 'MS Excel & PowerPoint',
            'icon': 'fa-solid fa-file-excel',
            'order': 9,
            'description': 'Professional presentations and data analysis'
        },
    ]
    
    print("Starting services population...")
    
    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            name=service_data['name'],
            defaults=service_data
        )
        
        if created:
            print(f"✓ Created service: {service.name}")
        else:
            # Update existing service
            service.icon = service_data['icon']
            service.order = service_data['order']
            service.description = service_data['description']
            service.save()
            print(f"✓ Updated service: {service.name}")
    
    print(f"\n🎉 Successfully populated {len(services_data)} services!")
    print("\nYou can now:")
    print("1. Run migrations: python manage.py makemigrations && python manage.py migrate")
    print("2. View services on your homepage")
    print("3. Manage services via admin panel at /admin/")

if __name__ == '__main__':
    populate_services()
