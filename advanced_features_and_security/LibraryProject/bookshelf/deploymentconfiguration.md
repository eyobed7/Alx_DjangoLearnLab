Install Certbot and Obtain SSL/TLS Certificate:


sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
Nginx Configuration:

nginx
Copy code
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Redirect all HTTP traffic to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    # SSL/TLS certificates
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    # Security configurations
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:50m;
    ssl_session_tickets off;

    # HSTS (optional: include_subdomains and preload)
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # Other security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";

    # Django project setup
    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/gunicorn.sock;
    }

    # Static and media files
    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/mediafiles/;
    }
}
Enable Automatic Certificate Renewal:


sudo certbot renew --dry-run