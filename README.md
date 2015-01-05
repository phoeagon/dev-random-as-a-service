/dev/random As a Service
==============================
phoeagon

`/dev/random` as a service. 

<a name="getstart"></a>
## Getting Started

Go [here](http://dev-random-as-a-service.appspot.com/dev/urandom) or go CLI-ish:

        curl "http://dev-random-as-a-service.appspot.com/dev/urandom?count=34&io=binary"

Enjoy an *aesthetical feast* by seeing those bytes in garbage codes!

        curl "http://dev-random-as-a-service.appspot.com/dev/urandom?io=ascii"

Use non-blocking `/dev/urandom`, or check for
[*entropy* level](http://dev-random-as-a-service.appspot.com/proc/sys/kernel/random/entropy_avail)
 before using `/dev/random`.

        curl "http://dev-random-as-a-service.appspot.com/proc/sys/kernel/random/entropy_avail"

**New**: For our experimental `/dev/full`, `/dev/null` and `/dev/zero`,
see the [API](#api) section.

<a id="accordion_pre"><!-- ABC --></a>

<a name="home"></a>

## Home

Cloud computing era has come and now virtually everything is a service. You
create [documents](https://docs.google.com),
[upload files](https://drive.google.com), 
[deploy websites](https://cloud.google.com). You can 
get [movies](http://youtube.com), [software](http://github.com), etc.
But **what if you want some random garbage**?

[IaaS](https://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_service_.28IaaS.29),
[SaaS](https://en.wikipedia.org/wiki/Cloud_computing#Software_as_a_service_.28SaaS.29),
[PaaS](https://en.wikipedia.org/wiki/Cloud_computing#Platform_as_a_service_.28PaaS.29),
[DaaS](http://devnull-as-a-service.com), we *proudly present* **DRaaS**.

Start to use our `/dev/random`-as-a-service` to get random garbage today!
No need to worry if your random generator on your computer is good enough.
Switch to our DRaaS, a distributed service available in and optimized for
countries worldwide.

### Who we are

`/dev/random`-as-a-service is maintained by a team of software engineers
who have failed at finding their girlfriends in real life. Our first-hand
experiences in generating non-sense garbage at datings is more than *awesome*!
Over the years we have creating *tons of* random garbage orally and electronically. So we start this business out of our strengths.

![I'm so random. XKCD](http://imgs.xkcd.com/comics/im_so_random.png "I'm so random. XKCD")

[XKCD-1210: I'm so random!](http://www.xkcd.com/1210/)

<a name="features"></a>
## Features

### What is `/dev/random`

Quote wikipedia:

  > In Unix-like operating systems, `/dev/random` is a special file
  > that serves as a blocking pseudorandom number generator.
  > It allows access to environmental noise collected from device
  > drivers and other sources.

### Features

+ Cryptographically secure randomness from `/dev/random`, blocks if
    entropy exhausted.
+ Unified API access for randomness, on all major platforms.

        Android
        Windows
        Linux
        Unix
        MacOS
        iOS

+ We support **Big Data**!
+ 67.77% uptime guaranteed! (Overtime pay may apply.)
+ Provide both `/dev/random` and a `/dev/urandom` that generates
    tons of garbage.
+ Provide both blocking and non-blocking mode for both, *something you
    don't find on your local computer*!
+ Provide both binary and hex-text I/O.
+ Contribute randomness by writing to `/dev/random` as well! Feel at home
    and build your identity with our community!
+ Professional equipment to generate *high quality* randomness![1]

[1] ![High Quality Randomness](http://imgs.xkcd.com/comics/random_number.png "XKCD")

[Random Number Generator](http://xkcd.com/221/)

### Upcoming

+ An Android library for ease of development! (Considering Cloud Endpoints).
+ **Premium only**: Issue `ioctl` to increase entropy count!
+ [Character Generation protocol](http://en.wikipedia.org/wiki/Character_Generator_Protocol)
as described in [RFC864](http://tools.ietf.org/html/rfc864) to provide you with
random data.

### Confidentiality, Privacy & Privileges

+ If you are an lawyer representing `/dev/random`-as-a-service, the communication
    between the server and you is protected by
    [Attorney Client Privilege](http://en.wikipedia.org/wiki/Attorney–client_privilege) .
+ We promise we give you real randomness! (Unconditional refund for 3-sec).
+ We promise we don't implement any logs on what you submit to our entropy pool. [1]

[1] Because we never have the resources to do so. This may change to ensure
compliance with *authority* regulations[2], and we may be compelled to do
so without prior notifications.

[2] *Authority* includes but not limited to Google, Github, NSA, CIA, KGB,
CCP, our romantic partners (should they appear in the future). 

<a name="pricing"></a>
## Pricing

      Plan          Basic   Premium   BusinessPremium
      ----------------------------------------------
      MaxCount      4096    65536     [Customize]

      Read           Yes     Yes        Yes

      Write          Yes     Yes        Yes

      Refund         3-sec   4-sec     10-sec

      IOCTL           No      Yes        Yes

      Check
      Entropy         Yes     Yes        Yes
      Level

      Routine free
      Entropy Pool     Yes    Yes        Yes
      Refill

      Dedicated       No      Avail 4   Included
      Entropy                Purchase

      Price           Free    $20/Month*   $100/Month*

        * A limited offer is available currently, at 50% discount.

<a name="api"></a>
## API

### Getting Random Garbage

An HTTP-based API is provided for access to `/dev/random` and `/dev/urandom`.

The API is simple and elegant. Do an HTTP GET to get the random garbage you
want, and we take care of the rest! Our powerful servers across the globe
provide you with high-quality random garbage for *free*!

        $ curl "http://dev-random-as-a-service.appspot.com/dev/urandom"
        c977187c45a5d4b5f495364be3fcccfd442b6d1400a872acadbb2067bac0749a4a6
        <...truncated>
        240e045420e8eaeedba32d5ee3860265d8a888dfa957faf7fa3451d00c46b3e3cb4

We support the following parameters to be sent in the URL.

        non-block: Include this parameter, regardless of its value,
            ensures that the request doesn't block due to lack of
            entropy. This is useful for `/dev/random`, which by default
            blocks if entropy level is not enough for your request.
        count: The number of random bytes to acquire. The limitation depends
            on the quota of your subscription plan. For free users, it's
            limited to 4096.
        io: either 'binary', 'ascii' or 'text'. Default is 'text', which converts
            random data to its corresponding hexidecimal representation
            for human-readability. 'binary' serves raw binary streams and
            'ascii' the same raw-binary stream but pretending to be HTML
            by manipulating its `Content-Type` header.

For example, to get 1234 bytes of random data as binary stream from
`/dev/random`, and force server to return a status code of `503 Service Unavailable`
when entropy is not enough, use:

        curl "http://dev-random-as-a-service.appspot.com/dev/random?io=binary&count=1234&non-block=a"

### Contributing to entropy pool

Issue a POST request to `/dev/random`.

        curl -v -d @my_password_list.txt -X POST http://dev-random-as-a-service.appspot.com/dev/random

On success, a status code of `202 Accepted` is returned.

### (Premium only) IOCTL for `/dev/random`

This API is premium only.

Issue GET/POST request to `/ioctl/<fd>/<OPERATION>/<param>/`.

According to `man 4 random`, `<OPERATION>` may be:

        RNDGETENTCNT
        RNDADDTOENTCNT
        RNDADDENTROPY
        RNDZAPENTCNT
        ...

`<fd>` indicates the file descriptor and may be any integer. `<param>`
depends on `<OPERATIONS>` and you should consult the manual for detailed
usage.

For example, to check the entropy level, use:

        $ curl http://dev-random-as-a-service.appspot.com/ioctl/4/RNDGETENTCNT/4/
        8192
        <Your result may differ>

To increase the entropy level by 30, use:

        $ curl http://dev-random-as-a-service.appspot.com/ioctl/4/RNDADDTOENTCNT/30/

(We have a fancy nuclear based randomness generator that refills the entropy pool
every some interval.)

### `/proc/sys/kernel/random/entropy_avail` API

This is an HTTP-GET API to get the entropy level.

        $ curl http://dev-random-as-a-service.appspot.com/proc/sys/kernel/random/entropy_avail
        8192
        <Your result may differ>

This differs from the IOCTL version for it's not restricted to *permium* users.
        

### Use python as a client!

For ease of illustration we use [requests](http://docs.python-requests.org/en/latest/).

        import requests
        req = requests.get('http://dev-random-as-a-service.appospot.com/dev/urandom')
        if req.status_code != 200:
            print "ERR"
        else:
            print req.text

### (Experimental) `/dev/full`, `/dev/zero` & `/dev/null`

This API is *experimental* and in early stage.

`/dev/full`, `/dev/zero` & [`/dev/null`](http://devnull-as-a-service.com)
API is the same
as that of `/dev/random` and `/dev/urandom`, both GET and POST supported.

      curl "http://dev-random-as-a-service.appspot.com/dev/null"
      <You get a response of 0-length in content.>
      curl "http://dev-random-as-a-service.appspot.com/dev/zero?count=10&io=binary" | md5sum
      a63c90cc3684ad8b0a2176a6a8fe9005  -
      <MD5 of 10-bytes, all of which are 0x0>

Posting to `/dev/full` always yields `413 Entity too large` and reading is
equivalent to from `/dev/zero`.

### Implementations & Hosting Your Own

We implemented our service using the device of
[Schrodinger's Cat](http://en.wikipedia.org/wiki/Schr%C3%B6dinger's_cat).

![Schrodinger's Cat](misc/schrodinger.png)

To start your own, firstly you need a cat farm.

![Kitten](misc/kitten.jpg)
![Kitten](misc/kitten.jpg)
![Kitten](misc/kitten.jpg)
![Kitten](misc/kitten.jpg)
![Kitten](misc/kitten.jpg)
![Kitten](misc/kitten.jpg)
![Kitten](misc/kitten.jpg)
![Kitten](misc/kitten.jpg)



<a name="contact"></a>
## Contact

phoeagon

+ [Github](http://github.com/phoeagon/)
+ [About.me](http://about.me/phoeagon/)
+ [Blog](http://phoeagon.appspot.com/)
+ [Twitter](http://twitter.com/phoeagon/)

Other projects:

+ [GFW-Router](http://gfwrouter.info/)
+ [Google Reader Dump](https://github.com/phoeagon/GReaderDump)

<a name="_epilog"></a>
<div id="accordion_post"></div>
