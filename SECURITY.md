# 🔒 Security Policy

## Supported Versions

We actively maintain and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of WhisperFrame seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

### How to Report

1. **Email us directly** at [security@cocode.dk](mailto:security@cocode.dk)
2. **Use GitHub Security Advisories** (if you have access)
3. **Contact the maintainers** through private channels

### What to Include

When reporting a vulnerability, please include:

- **Description** of the vulnerability
- **Steps to reproduce** the issue
- **Potential impact** of the vulnerability
- **Suggested fix** (if you have one)
- **Your contact information** for follow-up

### Response Timeline

- **Initial Response**: Within 24 hours
- **Assessment**: Within 3 business days
- **Fix Development**: Depends on complexity
- **Public Disclosure**: Coordinated with fix release

## Security Best Practices

### For Users

1. **Keep dependencies updated**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Use virtual environments**
   ```bash
   python -m venv env
   source env/bin/activate  # or source activate_env.fish
   ```

3. **Verify file integrity**
   - Download from official sources
   - Check checksums when available
   - Verify GPG signatures

4. **Monitor for updates**
   - Watch the repository for security releases
   - Subscribe to security notifications
   - Follow our security announcements

### For Developers

1. **Security-focused development**
   - Follow secure coding practices
   - Use dependency scanning tools
   - Implement proper input validation

2. **Regular security audits**
   - Run `bandit` for security analysis
   - Use `safety` for dependency checking
   - Perform code reviews with security focus

3. **Testing security measures**
   - Test with malicious inputs
   - Validate file handling security
   - Check permission handling

## Security Features

### Built-in Protections

- **Input Validation**: All user inputs are validated and sanitized
- **File Path Security**: Prevents directory traversal attacks
- **Process Isolation**: FFmpeg processes run with limited permissions
- **Error Handling**: Secure error messages that don't leak sensitive information

### Dependencies

We regularly audit our dependencies for security issues:

- **PyTorch**: Latest stable versions with security patches
- **FFmpeg**: System-provided versions with security updates
- **Whisper**: Latest from OpenAI with security improvements

## Vulnerability Disclosure

### Public Disclosure Process

1. **Security Issue Identified**
2. **Fix Developed and Tested**
3. **Security Advisory Created**
4. **Fix Released**
5. **Public Disclosure** (within 30 days)

### CVE Assignment

We work with the Python Security Response Team and other security organizations to:
- Assign CVE identifiers when appropriate
- Coordinate disclosure with affected parties
- Provide guidance on mitigation strategies

## Security Updates

### Update Channels

- **GitHub Releases**: Official releases with security fixes
- **Security Advisories**: GitHub Security Advisories for critical issues
- **Email Notifications**: Direct notifications for critical vulnerabilities

### Update Process

1. **Security fix** is developed and tested
2. **Patch release** is created
3. **Security advisory** is published
4. **Users are notified** through multiple channels
5. **Documentation** is updated with security information

## Responsible Disclosure

We believe in responsible disclosure and will:

- **Acknowledge** security researchers who report vulnerabilities
- **Credit** contributors in security advisories
- **Coordinate** disclosure with affected parties
- **Provide** clear guidance on mitigation

### Hall of Fame

We maintain a security researchers hall of fame for those who responsibly disclose vulnerabilities:

- [Your Name] - [Vulnerability Description] - [Date]

## Contact Information

### Security Team

- **Email**: [security@cocode.dk](mailto:security@cocode.dk)
- **PGP Key**: [Available on request]
- **Emergency**: [Emergency contact information]

### Maintainers

- **COCODE.DK**: [info@cocode.dk](mailto:info@cocode.dk)
- **GitHub Issues**: [Security Issues](https://github.com/cocode-dk/whisperframe/issues?q=label%3Asecurity)

## Security Resources

### Tools and Services

- **Dependency Scanning**: `safety check`
- **Code Analysis**: `bandit -r .`
- **Vulnerability Database**: [PyPI Safety DB](https://github.com/pyupio/safety-db)

### Documentation

- [OWASP Security Guidelines](https://owasp.org/)
- [Python Security Best Practices](https://python-security.readthedocs.io/)
- [GitHub Security Features](https://docs.github.com/en/github/managing-security-vulnerabilities)

---

**Thank you for helping keep WhisperFrame secure!**

*Last updated: December 2024*
