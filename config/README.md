# Configuration Guide

This directory contains environment-specific configuration files for the Cyber Incident Monitoring System.

## Files in This Directory

### `development.yaml`
Configuration for local development environment. Used when running the application on your local machine.

**Key Features**:
- Debug mode enabled
- Verbose logging for troubleshooting
- SQLite database option for quick setup
- CORS enabled for frontend development
- Lower performance requirements

### `production.yaml`
Configuration for production deployment. Used when the application is deployed to a live server.

**Key Features**:
- Debug mode disabled
- Minimal logging (warnings and errors only)
- PostgreSQL with connection pooling
- Security hardening
- Performance optimizations
- Resource monitoring

## How These Files Work

### Relationship with `.env` File

These YAML files and the `.env` file serve **different but complementary** purposes:

```
┌─────────────────────────────────────────────────┐
│  .env (Sensitive Credentials)                   │
│  - Database passwords                           │
│  - API keys                                     │
│  - Secret keys                                  │
│  ❌ Never committed to Git                      │
└─────────────────────────────────────────────────┘
              ↓ (referenced by)
┌─────────────────────────────────────────────────┐
│  config/*.yaml (Application Settings)           │
│  - Debug mode, logging levels                   │
│  - Performance tuning                           │
│  - Feature flags                                │
│  - References: ${DATABASE_URI}, ${SECRET_KEY}   │
│  ✅ Safe to commit to Git                       │
└─────────────────────────────────────────────────┘
```

### Configuration Loading Priority

1. **Environment Variables** (`.env`) - Highest priority
2. **YAML Config Files** (`config/*.yaml`) - Medium priority
3. **Application Defaults** (in code) - Lowest priority

### Environment Variable References in YAML

YAML files can reference environment variables using the `${VARIABLE_NAME}` syntax:

```yaml
database:
  uri: "${DATABASE_URI}"  # Reads from .env file

security:
  secret_key: "${SECRET_KEY}"  # Reads from .env file
```

## Usage Scenarios

### Scenario 1: Simple Local Development
**What you need**: Just the `.env` file

```bash
# 1. Copy the example file
cp .env.example .env

# 2. Edit .env with your database credentials
nano .env

# 3. Run the application
python backend/app.py
```

You don't need to modify the YAML files for basic local development.

### Scenario 2: Team Development with Different Environments
**What you need**: Both `.env` and appropriate YAML file

```bash
# Developer 1 uses development config
export APP_ENV=development
python backend/app.py

# Developer 2 uses custom config
export APP_ENV=staging
python backend/app.py
```

### Scenario 3: Docker Deployment
**What you need**: YAML files + environment variables passed to container

```bash
docker run -e DATABASE_URI=postgresql://... \
           -e SECRET_KEY=xyz123 \
           -e APP_ENV=production \
           cyber-monitoring-app
```

### Scenario 4: Kubernetes Deployment
**What you need**: YAML files + ConfigMaps/Secrets

```yaml
# Secrets stored in Kubernetes
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
data:
  DATABASE_URI: <base64-encoded>
  SECRET_KEY: <base64-encoded>
```

## Best Practices

### ✅ DO:
- Store all sensitive data in `.env` or environment variables
- Commit YAML files to version control
- Use different YAML files for different environments
- Document all configuration options
- Use environment variable references in YAML files

### ❌ DON'T:
- Put passwords or API keys in YAML files
- Commit `.env` file to Git
- Hardcode credentials in application code
- Use production credentials in development
- Share your `.env` file with others

## Adding New Configuration Options

### For Non-Sensitive Settings:
Add to the appropriate YAML file:

```yaml
# config/development.yaml
new_feature:
  enabled: true
  option: "value"
```

### For Sensitive Settings:
1. Add to `.env.example` as documentation:
```bash
# .env.example
NEW_API_KEY=your_api_key_here
```

2. Reference in YAML:
```yaml
# config/production.yaml
new_service:
  api_key: "${NEW_API_KEY}"
```

3. Users set actual value in their `.env` file:
```bash
# .env (user's personal file)
NEW_API_KEY=abc123xyz789
```

## Troubleshooting

### Issue: "Configuration not found"
**Solution**: Ensure the YAML file exists and is properly formatted. Check YAML syntax.

### Issue: "Environment variable not set"
**Solution**: Check that the variable exists in your `.env` file and the application has loaded it.

### Issue: "Database connection failed"
**Solution**: Verify `DATABASE_URI` in your `.env` file matches your actual database setup.

### Issue: "Which config file is being used?"
**Solution**: Check the `APP_ENV` or `FLASK_ENV` environment variable. Default is usually `development`.

## Further Reading

- [Flask Configuration Documentation](https://flask.palletsprojects.com/en/latest/config/)
- [12-Factor App Configuration](https://12factor.net/config)
- [Environment Variables Best Practices](https://12factor.net/config)

## Questions?

If you have questions about configuration, please:
1. Check this README first
2. Review `.env.example` for available options
3. Look at the YAML file comments
4. Open an issue on GitHub
