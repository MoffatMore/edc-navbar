from django.apps import apps as django_apps

from .navbar import Navbar
from .navbar_item import NavbarItem
from .site_navbars import site_navbars

app_config = django_apps.get_app_config('edc_navbar')

if app_config.register_default_navbar:

    default_navbar = Navbar(name=app_config.default_navbar_name)

    default_navbar.append_item(
        NavbarItem(name='dashboard',
                   title='Home',
                   fa_icon='fa-home',
                   url_name='home_url',
                   template_name='edc_navbar/navbar_default_item.html'))

    default_navbar.append_item(
        NavbarItem(name='administration',
                   title='Administration',
                   fa_icon='fa-cog',
                   url_name='administration_url',
                   template_name='edc_navbar/navbar_default_item.html'))

    default_navbar.append_item(
        NavbarItem(name='logout',
                   title='Logout',
                   fa_icon='fa-sign-out-alt',
                   url_name='logout_url',
                   template_name='edc_navbar/navbar_default_item.html'))

    site_navbars.register(default_navbar)
