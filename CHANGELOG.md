# Changelog

## [Unreleased]
### Added
### Changed
### Fixed
### Removed

## [8.2.1] - 2025.02.09
### Fixed
- Add support for Wagtail 6.4 (@marteinn)
- Hide WidgetWithScript deprecation warning on Wagtail < 6 (@jorenham)

### Removed
- Drop support for Wagtail 6.2 (@marteinn)

## [8.2.0] - 2025.02.01
### Added
- Add support for Wagtail 6.0/6.1 (@katdom13)
- Add support for Wagtail 6.2 (@engineervix)
- Add error handling to geocoding fields (@marteinn)

### Fixed
- Fix rendering of MapsField when Point is a NoneType (@nickmoreton)
- Update CI testing matrix to test against python 3.9 to 3.13 (@nickmoreton)
- Update CI testing matrix to test against wagtail 5.2 to 6.3 (@nickmoreton)
- Update CI testing matrix to test against Django 4.2 to 5.1 (@nickmoreton)
- Update classifiers to include Django 5.1 and Python 3.13 (@nickmoreton)
- Update leaflet to 1.9.4 (@marteinn)
- Upgrade mapbox geocoding API to v6 (@marteinn)
- App test page descriptions to improve testing (@marteinn)

### Changed
- Implement stimulus approach to GoogleMapsField, GeocoderField, and LeafletField (@katdom13)

### Removed
- Drop support for Django 4.1 (@katdom13)
- Drop support for Wagtail < 5.2 (@katdom13)
- Drop testing around python 3.8 (@nickmoreton)

## [8.1.1] - 2023.12.29
### Fixed
- Fix invalid regex escape character causing a `SyntaxWarning` on Python 3.12 (@jorenham)
- Upgrade example docker image python version to 3.12 (@marteinn)

## [8.1.0] - 2023.12.22
### Added
- Add tests for Wagtail 5.1 (@katdom13)
- Add support for Wagtail 5.2 (@marteinn)
- Add support for Python 3.12 (@marteinn)

### Fixed
- Fix broken readme link (@wimfeijen)
- Include contribution guidelones in README (@marteinn)
- Throw Exception if geo string is invalid in GoogleMapsBlock to_python (@marteinn)

### Removed
- Drop support for Python 3.7 (@katdom13)
- Drop support for Wagtail 5.0 (@marteinn)
- Drop support for Wagtail 4.2 (@marteinn)

## [8.0.0] - 2023.05.21
### Fixed
- Add Wagtail 5.0 compability (@marteinn)
- Add MAPBOX_LANGUAGE setting to handle mobox language (@Pytsh)

### Removed
- Drop support for Wagtail < 4.1 (@marteinn)

## [7.0.0] - 2022.12.03
### Added
- Add Wagtail 4 compability (@katdom13)
- Add contribution documentation (@marteinn)

### Changed
- Update StreamFieldPanel to just FieldPanel in tests (@katdom13)
- Update StreamFields to have additional argument use_json_field in test (@katdom13)
- Rename wagtailgeowidget.edit_handlers to wagtailgeowidget.panels (@katdom13)
- Update imports in docs (@katdom13)

### Fixed
- Ensure setup() is only called after user focus if showEmptyLocation is true (@kleingeist)
- Add support for permissions on field panels (@unicode-it)

### Breaking changes
- `wagtailgeowidget.edit_handlers` has been renamed to `wagtailgeowidget.panels`


## [6.2.0] - 2022.07.03
### Added
- Add Wagtail 3 compability (@marteinn)
- Add French translations (@ThbtSprt)

### Changed
- Make GEO_WIDGET_EMPTY_LOCATION False by default (@marteinn)

### Removed
- Drop support for Wagtail 2.14 (@marteinn)

### Fixed
- Add support for running outside of docker with custom .env file in development (@marteinn)


## [6.1.0] - 2022.02.20
### Added
- Add geocoding support for Mapbox (Martin Sandström)
- Add Wagtail 2.16 support

### Fixed
- Fix: Replace ugettext with gettext (@mariusboe)
- Fix: Add documentation on leaflet settings (Martin Sandström)
- Fix: Replace test runniner with pytest
- Fix: Drop duplicated tests from wagtailgeowidget/tests


## [6.0.0] - 2022.02.06

### Added
- Add support for Leaflet with LeafletPanel/LeafletBlock (Martin Sandström)
- Add standalone block and panel for GoogleMaps (Martin Sandström)
- Add panel for address field (Martin Sandström)
- Add geocoding support for Nominatim (Martin Sandström)
- Add telepath to widgets (Martin Sandström)

### Changed
- Deprecate GeoPanel, GeoBlock and GeoWidget in favour of GoogleMapsPanel, GoogleMapsBlock and GoogleMapsWidget (Martin Sandström)
- Add Swedish translations (Martin Sandströms)

### Fixed
- Fix: Disable form submit on latlang field enter (Martin Sandström)
- Fix: Apply prettier formatting to all js (Martin Sandström)

### Removed
- Drop support for Wagtail < 2.14 (Martin Sandström)

### Note: Upgrading from 5 to 6

- Replace `GeoPanel` with `GoogleMapsPanel`
- Replace `GeoBlock` with `GoogleMapsBlock`
- Replace `FieldPanel('address')` with `GeoAddressPanel("address", geocoder=geocoders.GOOGLE_MAPS)`


## [5.3.0] - 2022.01.05

### Added
- Add persistant and user editable zoom for map widget (Martin Sandström)
- Enable loading Google Maps API key dynamically (Martin Sandström)
- Make it possible to hide latlng field for GeoBlock (@vladox)

### Fixed
- Fix: Solve issue with address not working streamfield in Wagtail 1.13+ (@vladox)
- Fix: Drop six dependency (Martin Sandström)


## [5.2.0] - 2022.01.04

### Removed
- Drop support for Python 3.6
- Drop support for EOL Wagtail


## [5.1.0] - 2020.11.21

### Added
- Implement setting for leaving location field empty (Andreas Bernacca)

### Fixed
- Update docs for services that needs to be activated (Timothy Allen)
- Fix: Move CI from Travis to Github Actions (Martin Sandström)

