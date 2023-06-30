title: HTTPS: Moving on from EC2 Instance's HTTP
slug: https-moving-on-from-ec2-http
date: 2023-06-27 23:34 
author: Emmanuel Okwudike 
category: DevOps 
tags: ssl, https, aws, flask, api, ubuntu, nginx, web development, devOps, backend
summary: _I move on from HTTP to HTTPS; for security and other benefits_


For the past year I've been building and improving VoIP services - at first it was a hobby then it turned into a professional skill for a SaaS firm. This article reflects on the hobby phase and the cross-origin issue I had.<sup>[1](#footnote1)</sup>

[enter [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS "cors - bane of my web development existence")]

It's February, 2022 and I'm watching a Twilio Conference on YouTube; the next couple of days I'll put to use the Twilio documentation.

I have two projects on AWS in regards to this hobby: a rest API utilizing the powers of Twilio — from buying a local number (from a few supported countries) to handling voice calls, running on an [EC2 instance.](https://aws.amazon.com/ec2/) And other project — a web service that hits the API's endpoints. As a fun project, just for me and a colleague to play around with, NGROK was sufficient for local hosting; running a _temporary_ HTTPS It eliminated cross-origin issues, but the con with this 'hack' was its fragility in terms of custom domain availability and short-term use. Also, worthy of note that I could not serve this API on render, vercel or even Heroku as it is quite dense, and it affected performance and latency.

For the purpose of having my Web service to conveniently hit my API, I had to set both up as HTTPS — moving on from HTTP.

> Hypertext Transfer Protocol Secure (HTTPS) is an extension of the Hypertext Transfer Protocol (HTTP). It uses encryption for secure communication over a computer network, and is widely used on the Internet. In HTTPS, the communication protocol is encrypted using Transport Layer Security (TLS) or, formerly, Secure Sockets Layer (SSL). The protocol is therefore also referred to as HTTP over TLS, or HTTP over SSL. 


<span style="font-size: smaller">My Web service had to be HTTPS as well as it uses audio connectivity on browsers and this is disabled on HTTP by browsers. And to allow HTTPS-HTTPS cmmunication</span>

Moving on, I assume these things:
- you have an EC2 instance running a live project (and preferably running on Ubuntu)
- you have nginx properly configured (hence technically sound in reverse proxy?)
- you have Security Groups on this instance properly configured (**80 on HTTP; 443 on HTTPS; and additional PORTS you may need**)
- your elastic IP points to your ec2 instance that has an active service (in my case gunicorn for my flask application)

To cut cost, we are not using Route 53, Certificate Manager and a Load Balancer to achieve running your instance on HTTPS — in a production, I strongly advise making use of these services. Even more so, if you have just a single instance for your application then this article suits you, <span style="font-size: smaller">but it's not an excuse to not use the aforementioned services.</span>


### Getting a Domain

As at June 2023, Freenom Domain registrations and services are down, so I had to opt for buying a domain.  Yikes! 

<div style="text-align: center">
    <img class="force-display" src="https://media.tenor.com/POm7fis_GHQAAAAd/ptdr.gif" alt="yikes!" width="400" height="300">
</div>

This step is entirely down to your preferences; from cost, depending on the domain, to domain provider. I purchased a .com.ng on WhogoHost, a domain provider based in Nigeria.

Depending on the domain provider most of the DNS informations will be automatically filled while allowing edit where necessary, under **DNS manager**. This step is ideally initiated once **Add New Zone** is triggered.


![whogohost - manage DNS](/images/manage_dns.png "whogohost - manage DNS")
<p style="text-align: center; font-size: smaller">screenshot of whogohost dashboard</p>

![whogohost - add new zone](/images/add_new_zone.png "whogohost - add new zone")
<p style="text-align: center; font-size: smaller">screenshot of whogohost dashboard - add new zone</p>

*Zone name points to your domain name. IP Address points to your Elastic IP address.<sup>[2](#footnote2)</sup>*

&nbsp;

![AWS EC2 connect - active nginx](/images/nginx_active.png "AWS EC2 connect - active nginx")
<p style="text-align: center; font-size: smaller">EC2 instance terminal showing active nginx</p>

Ensure your NGINX is running and try visiting your domain (http) - you are likely to hit a server issue here as it takes time for DNS changes to reflect, especially after registering one.

Good? proceed to.....


### Configuring Instance for HTTPS


In order to use Certbot, you need a live HTTP website (domain) with an open PORT 80 (EC2's Security Group) which is hosted on a server; in our case Ubuntu server.

In your machine's terminal (EC2 connect/SSH):

Installing snapd...

> A snap is a bundle of one or more applications ("apps") and their dependencies that  works without modification across many different Linux distributions. Snaps are discoverable and installable from the Snap Store, an app store with an audience of millions.

While the below is finetuned for Nginx on Ubuntu, visit [certbox instructions](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal "certbox instructions for all") to use commands based on your web server.

```
$ sudo snap install core; sudo snap refresh core
```
```
$ sudo snap install --classic certbot
```
```
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
```
$ sudo certbot --nginx -v
```

<span style="font-size: smaller">Before running the last command make sure your domain has been properly configured and you get "All ok!" on [Let's Debug](https://letsdebug.net/). Upon succession, your nginx file is automatically modified to reflect the SSL changes (SSL port, SSL certification, SSL certification key)</span>

A typical success output, generated by certbot:

```
Performing the following challenges:
http-01 challenge for www.yourdomain
Waiting for verification...
Cleaning up challenges

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/yourdomain/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/yourdomain/privkey.pem
This certificate expires on 20xx-xx-xx.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.

Deploying certificate
Deploying Certificate to VirtualHost /your/nginx/path
Successfully deployed certificate for yourdomain to /your/nginx/path
Deploying Certificate to VirtualHost /your/nginx/path
Successfully deployed certificate for yourdomain to /your/nginx/path
Redirecting all traffic on port 80 to ssl in /your/nginx/path
Redirecting all traffic on port 80 to ssl in /your/nginx/path
Congratulations! You have successfully enabled HTTPS on https://yourdomain and https://www.yourdomain
```

Visit your domain on https: https://yourdomain

![https enabled](/images/emvoip.png "HTTPS enabled")

&nbsp;
### Challanges

- subsequent to purchasing and adding a new zone in my DNS manager dashboard I could not access my site nor check its DNS information on Let's Debug showed me this:

> NoRecords FATAL\
No valid A or AAAA records could be ultimately resolved for emvoip.com.ng.\
This means that Let's Encrypt would not be able to connect to your domain to perform HTTP validation, since it would not know where to connect to.\
No A or AAAA records found.

Incidentally, trying to reach your domain on a browser would result to this:

> This site can’t be reached\
Check if there is a typo in emvoip.com.ng.\
If spelling is correct, try running Windows Network Diagnostics.\
DNS_PROBE_FINISHED_NXDOMAIN

On any DNS Check tool you are likely to see the same as below for your domain, at this point.

![dns fail](/images/dnspropatefail.png "DNS yet to propagate")

Fix: It can take a while for DNS changes to reflect on all nodes. Making sure my A record points to my Elastic IP and having to wait for about 110 minutes, I was able to have my API running on my domain (HTTP) before moving on to establish SSL. You can check your DNS propagation here: [DNS Checker](https://dnschecker.org/ "CHECK DNS PROPAGATION").

![DNS propagating fairly](/images/dns_propagate_fair.png "DNS propagating fairly")
<p style="text-align: center; font-size: smaller">After a long, long time DNS is propagating fairly</p>

&nbsp;
- **Connect using EC2 Instance Connect** failed multiple times with the error message as seen below.

> Failed to connect to your instance\
Error establishing SSH connection to your instance. Try again later.

"Fix": I had to check my Security Group to enable PORT 22<sup>[3](#footnote3)</sup> for incoming connections, but saw it enabled already. Culprit ended up being IP related (running, at the time, a new network connection). I think. Anyhow I had to SSH instead, as a quick fix using ```ssh -i "KEYNAME.pem" ubuntu@ec2-ela-stic-ip.compute-1.amazonaws.com ``` on my local machine.

&nbsp;
- DNS taking darn too long to propagate

Fix: ***sleep***<sup>[4](#footnote4)</sup>


<div style="text-align: center">
    <img class="force-display" src="https://media3.giphy.com/media/RMMNGb1KGmIX9LFei6/giphy.gif?cid=ecf05e47h9yx982kwvqc1u054g3zw1h3fbgqtg4dl8hn0tfc&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="close curtain!" width="400" height="300">
</div>


<p></p>
&nbsp;

### References

Official certbox website [certbox homepage](https://certbot.eff.org/).

Oficial snapcraft website [linux snap](https://snapcraft.io/).

Domain provider used [whogohost](https://www.whogohost.ng/).

Amazon Web Services [AWS](https://aws.amazon.com/).

SSL: [what is SSL (Secure Sockets Layer)?](https://www.cloudflare.com/learning/ssl/what-is-ssl/) 

TTL: [What is TTL?](https://www.cloudns.net/wiki/article/188/ "TTL")
&nbsp;
<p></p>
&nbsp;
<p></p>

<a name="footnote1">1</a> On production level, this API is modeled as a microservice with AWS Load Balancer, CodePipeline, CloudWatch, CloudFront, Route 53, S3, and a couple more Amazon Web Services to ensure better performance, robustness and general security. [check out Amazon Web Services here](https://aws.amazon.com/ "AWS")

<a name="footnote2">2</a> [What is A record](https://support.dnsimple.com/articles/a-record/#:~:text=An%20A%20record%20uses%20a,A%20record%20stands%20for%20Address "What's an A record")

<a name="footnote3">3</a> Myth or Legend? [Port 22 - EC2](https://stackoverflow.com/questions/44802363/cannot-connect-to-ec2-ssh-connect-to-host-port-22-connection-refused "port 22 and the prisoner of IPban")

<a name="footnote4">4</a> Seriously, sleep! [see this](https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/how-to-fall-asleep-faster-and-sleep-better/ "sleep faster...")
