## Project Abstract

Recently, people have started using online forums frequently for discussions. Along with the discussions on online forums,
trolls and spammers have become more common. It is a timeconsuming and tedious job to moderate the comments and posts on these forums, so the organizations have to rely on external people to handle them. We are trying to differentiate between negative and positive comments and tweets on Twitter, Reddit, and YouTube. To achieve this, we would get real-world data from the above mentioned platforms. We also intend to visualize Twitter, Reddit, and YouTube’s data.

## Team - Systematic_Squad

* Nagalakshmi Prasanna Pujita Bodapati, nbodapa1@binghamton.edu
* Saisuraj Aitha, saitha2@binghamton.edu
* kshamitha Gandu, kgandu1@binghamton.edu
* Mohith kumar Sopparam, msoppar1@binghamton.edu
* Anshul Upadhyay, aupadhy5@binghamton.edu

## Tech-stack

* `Java/Springboot` - This project for Twitter/Youtube is created and developed using Java/Spring boot. [Springboot - website](https://spring.io/projects/spring-boot)
* `Python` - For Reddit Data extraction we used python to create and develop this project. [Python Website](https://www.python.org/)
* `pymongo` - For storing comments that are collected from Reddit/Subreddits we used pymongo to conenct to Mongodb client [pymongo - Documentation](https://pymongo.readthedocs.io/en/stable/)
* `reddit` - Reddit API documentation for extracting and authenticating HTTP requests. [Reddit website](https://www.reddit.com/dev/api/)
* `GoogleAPIClient and services` - Used for authentication and extracting youtube comments [Google API Client](https://developers.google.com/android/reference/com/google/android/gms/common/api/GoogleApiClient)
* `BufferedReader/InputStreamReader ` - An InputStreamReader is a bridge from byte streams to character streams: It reads bytes and decodes them into characters using a specified charset. The charset that it uses may be specified by name or may be given explicitly, or the platform's default charset may be accepted. [Website](https://docs.oracle.com/javase/7/docs/api/java/io/InputStreamReader.html)
* `org.apache.http` - Apache HttpComponents - The Apache HttpComponents project is responsible for creating and maintaining a toolset of low level Java components focused on HTTP and associated protocols (https://hc.apache.org/)
* `com.mongodb` - Tool used to develop applications and store data in NoSql db  (https://www.mongodb.com/docs/)

## Three data-source documentation
* `Twitter`:
    * [Sample Stream API](https://api.twitter.com/2/tweets/sample/stream#lang=en) <Streams about 1% of all Tweets in real-time>.
* `Reddit`:
    * [Sample Stream API](https://oauth.reddit.com/api/v1/me) <In order to make requests to reddit's API via OAuth, you must acquire an Authorization token, either on behalf of a user or for your client (see Application Only OAuth, below)>
                         (https://oauth.reddit.com/r/ + sub_reddit + /comments) <extracting comments and posts for subreddits>
                         (https://oauth.reddit.com/search) <We can search for specific comment on subreddits>
* `Youtube`:
    * [Google Client API](request.setKey(SECRET_KEY)
                    .setVideoId("Jo0D_u-QSXs")
                    .execute()) <Using the services provided by Google client API requesting the comments for the video `Jo0D_u-QSXs` and storing in Mongodb>

## System Architecture

https://drive.google.com/file/d/10vfyd0rwn-WWS43LMJZPxOk2QSQYB__4/view?usp=sharing

## How to run the project?

Install Python
Install Mongodb / Mongoshell
Run server for Mongodb and run mongoshell
Create databases
    * `Twitter` - 'twitterdatabase'
    * `Youtube` - 'youtubedatabase'
    * `Reddit` -  'redditdatabase'
Create Collections
    * `Twitter` - 'twitter'
    * `Youtube` - 'youtube'
    * `Reddit` -  'redditcomments'
Go to project-1-implementation
For Reddit extractions run - 'python trigger.py'
For Twitter and Youtube - Run application in eclipse

## Database schema - NoSQL (Also included sample data collection in a separate folder - Sample-Data)
* `Twitter`:
   {
        _id: ObjectId("635feaab64c3b753cedb037e"),
        data: {
            edit_history_tweet_ids: ['1587105335612956673'],
            id: '1587105335612956673',
            text: 'did you see this? @knowmadicc @Ryleeprattdafoe @aspekt_ai @RomeDan20 @EcuaHomes @CANDRACENDANA1 @KarenKei5 @BizNifty @kevinmhj_eth @HectorH07077743 @akhmedovco @Montesi1Armanni @EtherCurryHouse https://t.co/EkaHdIVp06'
        }
    }
* `Reddit`:
    {
    _id: ObjectId("635fde94a35ed38c2d80fac0"),
    subReddits: 'Games',
    comments: 'No need for the passive aggressive comment sir/madam. I think game pass is a great deal and have it on PC myself. I didn’t say anything negative about it? Just pointing out some stuff. Sorry I ruffled your feathers, have a good one.',
    created_utc: '2022-10-31 10:39:25',
    time: ISODate("2022-10-31T10:41:24.981Z"),
    comm_id: 'iui415e'
    }
* `Youtube`:
    {
        _id: ObjectId("635fec0e67862114b5a6a83f"),
        authorChannelId: { value: 'UCDQAbfhCpN5LfAvIjXXQaGA' },
        authorChannelUrl: 'http://www.youtube.com/channel/UCDQAbfhCpN5LfAvIjXXQaGA',
        authorDisplayName: 'Bontha kumari Kumari',
        authorProfileImageUrl: 'https://yt3.ggpht.com/ytc/AMLnZu9nWPfrPK6iu_t5x0yNOCslkUSm49BjB8kacXy-I1Va0Ww1T_I4e6ZevLxdtv-N=s48-c-k-c0x00ffffff-no-rj',
        canRate: true,
        likeCount: 0,
        publishedAt: '2022-10-26T08:18:26.000Z',
        textDisplay: 'One of my favourite song 😔😔',
        textOriginal: 'One of my favourite song 😔😔',
        updatedAt: '2022-10-26T08:18:26.000Z',
        videoId: 'Jo0D_u-QSXs',
        viewerRating: 'none'
    },

## Special instructions for us???
The mongodb server should be running with corresponding databases and collections created.
To run the java application we have used Eclipse and created the project iin Springboot.



