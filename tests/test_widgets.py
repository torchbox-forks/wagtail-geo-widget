import pytest
from django.test import TestCase
from wagtail import VERSION as WAGTAIL_VERSION

from wagtailgeowidget import app_settings, geocoders
from wagtailgeowidget.widgets import GeocoderField, GoogleMapsField, LeafletField


class GoogleMapsFieldTestCase(TestCase):
    def test_google_maps_field_contains_constuct_regular(self):
        widget = GoogleMapsField()
        html = widget.render(
            "field",
            "",
            {
                "id": "X",
            },
        )

        if WAGTAIL_VERSION >= (6, 0):
            self.assertIn(
                '<input type="hidden" name="field" id="X" data-controller="google-maps-field"',
                html,
            )
        else:
            self.assertIn("new GoogleMapsField", html)

    def test_google_maps_field_js_init_contains_construct(self):
        if WAGTAIL_VERSION >= (6, 0):
            pytest.skip("Test only runs on Wagtail versions lower than 6.0")

        widget = GoogleMapsField()
        html = widget.render_js_init("id", "field", "")

        self.assertIn("new GoogleMapsField", html)


class LeafletFieldTestCase(TestCase):
    def test_leaflet_field_contains_constuct_regular(self):
        widget = LeafletField()
        html = widget.render(
            "field",
            "",
            {
                "id": "X",
            },
        )

        if WAGTAIL_VERSION >= (6, 0):
            self.assertIn(
                '<input type="hidden" name="field" id="X" data-controller="leaflet-field"',
                html,
            )
        else:
            self.assertIn("new LeafletField", html)

    def test_leaflet_field_js_init_contains_construct(self):
        widget = LeafletField()

        if WAGTAIL_VERSION >= (6, 0):
            html = widget.render(
                "field",
                "",
                {
                    "id": "X",
                },
            )
            self.assertIn(
                '<input type="hidden" name="field" id="X" data-controller="leaflet-field"',
                html,
            )
        else:
            html = widget.render_js_init("id", "field", "")
            self.assertIn("new LeafletField", html)

    def test_value_are_parsed_properly(self):
        widget = LeafletField()

        if WAGTAIL_VERSION >= (6, 0):
            from html import escape

            html = widget.render(
                "field",
                "SRID=5432;POINT(12.0 13.0)",
                {
                    "id": "X",
                },
            )
            self.assertIn(escape('"lat": "13.0"'), html)
            self.assertIn(escape('"lng": "12.0"'), html)
        else:
            html = widget.render_js_init("id", "field", "SRID=5432;POINT(12.0 13.0)")
            self.assertIn('"lat": "13.0"', html)
            self.assertIn('"lng": "12.0"', html)


class GeocoderFieldTestCase(TestCase):
    def setUp(self):
        app_settings.MAPBOX_ACCESS_TOKEN = None
        app_settings.MAPBOX_LANGUAGE = "en"

    def test_geocoder_field_contains_constuct_regular(self):
        widget = GeocoderField()
        html = widget.render(
            "field",
            "",
            {
                "id": "X",
            },
        )

        if WAGTAIL_VERSION >= (6, 0):
            self.assertIn(
                '<input type="text" name="field" id="X" data-controller="geocoder-field" data-geocoder-field-geocoder-value="nominatim"',
                html,
            )
        else:
            self.assertIn("new NominatimGeocoderField", html)

    def test_geocoder_field_js_init_contains_construct(self):
        if WAGTAIL_VERSION >= (6, 0):
            pytest.skip("Test only runs on Wagtail versions lower than 6.0")

        widget = GeocoderField()
        html = widget.render_js_init("id", "field", "")

        self.assertIn("new NominatimGeocoderField", html)

    def test_googlemaps_geocoder_returns_googlemaps_field(self):
        widget = GeocoderField(geocoder=geocoders.GOOGLE_MAPS)

        if WAGTAIL_VERSION >= (6, 0):
            html = widget.render(
                "field",
                "",
                {
                    "id": "X",
                },
            )
            self.assertIn(
                '<input type="text" name="field" id="X" data-controller="geocoder-field" data-geocoder-field-geocoder-value="google_maps"',
                html,
            )
        else:
            html = widget.render_js_init("id", "field", "")
            self.assertIn("new GoogleMapsGeocoderField", html)

    def test_mapbox_geocoder_returns_googlemaps_field(self):
        widget = GeocoderField(geocoder=geocoders.MAPBOX)

        if WAGTAIL_VERSION >= (6, 0):
            from html import escape

            html = widget.render(
                "field",
                "",
                {
                    "id": "X",
                },
            )
            self.assertIn(
                '<input type="text" name="field" id="X" data-controller="geocoder-field" data-geocoder-field-geocoder-value="mapbox"',
                html,
            )
            self.assertIn(escape('accessToken": null'), html)
        else:
            html = widget.render_js_init("id", "field", "")
            self.assertIn("new MapboxGeocoderField", html)
            self.assertIn('accessToken": null', html)

    def test_mapbox_access_token_gets_outputted(self):
        app_settings.MAPBOX_ACCESS_TOKEN = "<MAPBOX ACCESS TOKEN>"

        widget = GeocoderField(geocoder=geocoders.MAPBOX)

        if WAGTAIL_VERSION >= (6, 0):
            from html import escape

            html = widget.render(
                "field",
                "",
                {
                    "id": "X",
                },
            )
            self.assertIn(
                '<input type="text" name="field" id="X" data-controller="geocoder-field" data-geocoder-field-geocoder-value="mapbox"',
                html,
            )
            self.assertIn(escape('accessToken": "<MAPBOX ACCESS TOKEN>'), html)
        else:
            html = widget.render_js_init("id", "field", "")
            self.assertIn("new MapboxGeocoderField", html)
            self.assertIn('accessToken": "<MAPBOX ACCESS TOKEN>', html)

        app_settings.MAPBOX_ACCESS_TOKEN = None

    def test_mapbox_language_parameter_gets_outputted(self):
        widget = GeocoderField(geocoder=geocoders.MAPBOX)

        if WAGTAIL_VERSION >= (6, 0):
            from html import escape

            html = widget.render(
                "field",
                "",
                {
                    "id": "X",
                },
            )
            self.assertIn(
                '<input type="text" name="field" id="X" data-controller="geocoder-field" data-geocoder-field-geocoder-value="mapbox"',
                html,
            )
            self.assertIn(escape('language": "en'), html)
        else:
            html = widget.render_js_init("id", "field", "")

            self.assertIn("new MapboxGeocoderField", html)
            self.assertIn('language": "en', html)
