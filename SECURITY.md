# Security and publication policy

## Public repository boundary

The public repository must not contain credentials, API keys, OAuth tokens, service-account files, private keys, raw voice recordings, production audio masters, or downloaded source media.

Production media is stored privately in Google Drive and excluded by `.gitignore`. Before each public release, inspect staged files with `git diff --cached --name-only` and run a secret scanner if one is available.

## Reporting

If a secret is committed, revoke or rotate it immediately, then remove it from Git history. Deleting it in a later commit is not sufficient because earlier commits remain public.

## Local configuration

Store machine-specific values in ignored `.env` files. Commit only a redacted `.env.example` when configuration documentation is needed.
