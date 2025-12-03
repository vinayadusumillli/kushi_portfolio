#!/bin/bash

# Create images directory if it doesn't exist
mkdir -p static/images/brands

# Download Gujarat Titans Logo
curl -o static/images/brands/gujarat_titans.svg https://upload.wikimedia.org/wikipedia/en/0/09/Gujarat_Titans_Logo.svg

# Download Decathlon Logo
curl -o static/images/brands/decathlon.svg https://upload.wikimedia.org/wikipedia/commons/a/aa/Decathlon_Logo.svg

# Download LCR Honda Logo (using a likely URL, if fails we'll generate)
curl -o static/images/brands/lcr_honda.svg https://upload.wikimedia.org/wikipedia/commons/1/16/LCR_Honda_Castrol_Logo.svg

echo "Downloads complete."
