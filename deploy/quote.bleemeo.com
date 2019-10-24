# quote.bleemeo.com

upstream django {
    server uwsgi:8181;
}

server {
    listen      80;
    listen      443;
    server_name quote.bleemeo.com;
    charset     utf-8;

    location / {
        include uwsgi_params;
        uwsgi_pass django;
        uwsgi_param HTTPS off;
        uwsgi_param UWSGI_SCHEME http;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Forwarded-Proto http;
    }
}
