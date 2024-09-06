<<<<<<< HEAD
# sort_fixtures
=======
# Sort Fixtures

This repository contains the sorted fixtures for Frappe/ERPNext, including important fixtures and customizations.

## Prerequisites

`jq` is needed to reorder JSON fixtures. Install it using the following command:

```bash
sudo apt-get update
sudo apt-get install jq
```

Reordering fixtures helps organize JSON files for the app. Use the following command to reorder the fixtures:

```bash
bench reorder-fixtures --app your_custom_app
```
>>>>>>> develop
