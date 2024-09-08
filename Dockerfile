FROM odoo:17.0

COPY ./conf/odoo.conf /etc/odoo/odoo.conf

WORKDIR /var/lib/odoo

EXPOSE 8069

CMD ["odoo"]
