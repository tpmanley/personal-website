Title: npm install TheEnemy
Date: 2015-1-6
Tags: IoT, cloud, M2M

OK, TheEnemy is a bit harsh, but I did check out a competitor's device cloud
solution recently. It is called [Octoblu](http://octoblu.com) and was founded
in early 2014 and acquired by [Citrix](http://www.citrix.com) in December
2014. There are a couple of things that intrigued me about this solution. The
first is that their cloud platform called Meshblu is open sourced on GitHub
so anyone can run their own private instance. The other is they support both
CoAP and MQTT. These two protocols work well on resource and bandwidth 
contrained devices like many IoT devices are bound to be and so I've been
looking for an opportunity to get more experience with them. It looks like
Octoblu will give me that chance.

Installing Meshblu on my MacBook Pro was almost as simple as following the
README in the [GitHub repo](https://github.com/octoblu/meshblu). First I
cloned the repo:

    git clone https://github.com/octoblu/meshblu.git
    cd meshblu

Then I installed it:

    npm install

According to the README I was then supposed to copy the `config.fs.sample` file
over the `config.js` file, but when I did that the next step didn't work so
I just left `config.fs` as is.

Meshblu optionally supports Mongo, Redis, ElasticSearch and Splunk for
scalability and performance but I wasn't interested in any of that right now
so I left the configuration with the default settings. I did change the
HTTP and HTTPS port so I didn't need to run the server as root:

    diff --git a/config.js b/config.js
    index db7b6c3..36b6a59 100644
    --- a/config.js
    +++ b/config.js
    @@ -16,9 +16,9 @@ module.exports = {
       mongo: {
         databaseUrl: process.env.MONGODB_URI
       },
    -  port: parseInt(process.env.PORT) || 80,
    +  port: parseInt(process.env.PORT) || 8080,
       tls: {
    -    sslPort: parseInt(process.env.SSL_PORT) || 443,
    +    sslPort: parseInt(process.env.SSL_PORT) || 8443,

Next I ran the server:

    node server.js --http

    MM    MM              hh      bb      lll         
    MMM  MMM   eee   sss  hh      bb      lll uu   uu 
    MM MM MM ee   e s     hhhhhh  bbbbbb  lll uu   uu 
    MM    MM eeeee   sss  hh   hh bb   bb lll uu   uu 
    MM    MM  eeeee     s hh   hh bbbbbb  lll  uuuu u 
                     sss                              
    Meshblu (formerly skynet.im) development environment loaded... 

    Starting HTTP/HTTPS... done.
    HTTP listening at http://0.0.0.0:8080

And finally a basic test:

    curl -X GET http://localhost:8080/status
    {"meshblu":"online"}

I got little stuck at this point because the I didn't read the documenation
carefully and just tried commands pseudo-randomly. It didn't take too long 
before I figured out I needed to add a device and then use the authentication
credentials (a UUID and secret token) to use most of the HTTP API. That was pretty
straightforward:

    curl -X POST -d "type=example" http://localhost:8080/devices
    {"type":"example","ipAddress":"127.0.0.1","uuid":"7c348710-955a-11e4-820b-0f6c4a76a790","timestamp":"2015-01-06T04:14:18.972Z","token":"0086jbhffmc5zh0k9bckcr90lkvjkyb9","channel":"main","online":false,"geo":null}

The `uuid` and `token` fields are the important ones. To access say the 
`/devices` endpoint you pass those fields in with the HTTP headers like this:

    curl -X GET http://localhost:8080/devices --header "meshblu_auth_uuid: 7c348710-955a-11e4-820b-0f6c4a76a790" --header "meshblu_auth_token: 0086jbhffmc5zh0k9bckcr90lkvjkyb9"
    {"devices":[{"type":"example","ipAddress":"127.0.0.1","uuid":"7c348710-955a-11e4-820b-0f6c4a76a790","timestamp":"2015-01-06T04:14:18.972Z","token":"0086jbhffmc5zh0k9bckcr90lkvjkyb9","channel":"main","online":false,"geo":null,"_id":"L5tEWjAITwhp5n8H"}]}

That's about as far as I've got so far, but I look forward to trying out the
CoAP and MQTT APIs in the near future.

