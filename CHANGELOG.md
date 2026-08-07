# Changelog

All notable changes to this project will be documented in this file.

## [v1.2.0 Bloom Update] - 2026-08-07

### Added

- Standalone executable support.
- PowerShell build script for creating releases.
- Executable icon.
- New file system management system for handling development and packaged environments.

### Changed

- Reworked file loading to support both source execution and executable versions.
- Assets and data are now stored outside the executable for easier customization.
- Improved internal project organization.

### Fixed

- Fixed issues caused by missing or incorrect file paths when running outside the development environment.
- Improved stability when launching MikuPet as an executable.

## [v1.1.0 Rebirth Update] - 2026-08-05

### Added

- Logger system
- Event system
- Engine system
- Configurable FPS system

### Changed

- Rebuilt most of the application's internal architecture. (Thank you for wait!!)
- Internal render system
- How walk works internally
- How gravity works internally
- How animation works internally

### Fixed

- Fixed a critical error that cause MikuPet didn't work

### Removed

- Temporary console commands from the legacy implementation.

---

## [v1.0.0] - 2025-07-26

### Added

- Follows the active window around your desktop.
- Drag her around with your mouse.
- Respond to simple text commands.
- Super lightweight and made with love.
