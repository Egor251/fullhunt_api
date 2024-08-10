# FullHunt API library #

## What is this? ##
The module allows you to use fullhunt.io api easy (api key is required).

## Quick Guide ##

### Methods list:</br> ###
domain</br>
subdomains</br>
host</br>
intelligence</br>
search_tag</br>
web_tech</br>
product</br>
intel_subdomains</br>
ip_to_hosts</br>
asn</br>
virt_asn</br>
hosts_in_range</br>
dns_mx</br>
dns_ns</br>
search  (check docs for more details https://fullhunt.io/docs/global-search/filters)

Some of these methods require Enterprise status. 


----------


### Usage ###


Usafe is very simple, you need to create Session object.

    sess = fullhunt.Session(api_key)


after you can use all provided methods, for example:

    result = sess.domain('google.com')





----------


## Developer ##
My site: [github](https://github.com/egor251/) 