# Vulnerable-Bottle-App

**Intentionally vulnerable web application built with the Bottle framework,
Bottle is a lightweight micro web-framework for Python**

### files Structure
```bash
vuln-bottle-app/
├── app.py                     # Main application entry point
├── requirements.txt           # List of dependencies
├── README.md                  # Project description and usage instructions
├── config/
│   ├── settings.py            # App configuration settings
│   ├── routes.py              # Route registration logic
│   └── api.py                 # api end points
│── triggers/
│   └── trigger.py             # vulnerability triggers
├── views/                     # HTML templates
│   └── base.tpl               # Base template for common layout
├── static/                    # Static assets
│   ├── css/
│   │   └── styles.css         # CSS styles
│   ├── js/
│   │   └── scripts.js         # JavaScript files
│   └── img/                   # Images
├── logs/                      # Log files
│   └── logs.log               # Access logs
├── utils/                     # helper files
│   └── main.py                # helper functions
├── tests/                     # Test cases for vulnerabilities and routes
│   └── unittest.py
└── Dockerfile                 # Docker          
```