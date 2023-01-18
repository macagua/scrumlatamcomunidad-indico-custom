# scrumlatamcomunidad-indico-custom

This repository holds the Indico customization files used for the "Scrum LATAM Comunidad" event management system deployment

## Installing Indico software

Following the Installation guides for [Production](https://docs.getindico.io/en/stable/installation/production/) environment.


## Installing the Awesome theme plugin

Navigate to your Indico project and clone the theme repository:

```
mkdir ~/src/ ; cd $_
git clone https://github.com/macagua/scrumlatamcomunidad-indico-custom.git src/scrumlatamcomunidad-indico-custom
```

## Set Customization Directory

You need set into the ``indico.conf`` file the customization directory from Indico software read the new debranding, executing the following command:

```
echo -e "\n# Customization\nCUSTOMIZATION_DIR = '/opt/indico/src/scrumlatamcomunidad-indico-custom'" >> ~/etc/indico.conf
```

Then you need restart Indico service, executing the following command:

```
systemctl restart nginx.service indico-celery.service indico-uwsgi.service
```

## About Indico Software

<img src="https://github.com/indico/indico/raw/master/indico/web/static/images/logo_indico.png"
     align="right"
     width="300"
     style="width: 300px; float: right; margin-right: 50px;">

**Indico** is:
 * 🗓 a general-purpose **event management** tool;
 * 🌍 fully **web-based**;
 * 🧩 **feature-rich** but also **extensible** through the use of [plugins](https://docs.getindico.io/en/stable/plugins/);
 * ⚖️ **Open-Source** Software under the MIT License;
 * <img src="https://raw.githubusercontent.com/indico/assets/master/cern_badge.png" width="20"> **made at CERN**, [the place where the web was born](https://home.cern/science/computing/birth-web)!

![A sneak peek of Indico](https://raw.githubusercontent.com/indico/indico/master/sneakpeek.gif)
