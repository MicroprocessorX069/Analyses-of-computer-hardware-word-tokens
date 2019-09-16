library(httr)
library(twitteR)
consumer_api="1bvQOzOZ8qG9qygEWPJF6Vk8t"
consumer_secret="wlirqGOkbnlaZe0v6tm2bxOTsZaY5eQxBWojzXXan4mDVw3jGQ"
access_token="1076337411263729666-idPWq8FNUNkCDESFrM2KnDJBkBwAaM"
access_secret="uPcWVwL3TIIYuwXAQZbbJDUPtxBvmIGgcUq54thafPFrN"
setup_twitter_oauth(consumer_api, consumer_secret,
                    access_token,access_secret)

tweets <- searchTwitter("CPU",n=4000 ,lang="en",  since="2019-01-01")
tw <- twListToDF(tweets)
tx <- tw$text
write.table(tx, file = "sample1.txt", append = TRUE)

tweets <- searchTwitter("GPU",n=4000,lang = "en", since="2019-01-01")
tw <- twListToDF(tweets)
tx <- tw$text
write.table(tx, file = "sample2.txt", append = TRUE)

tweets <- searchTwitter("RAM",n=4000,lang = "en", since="2019-01-01")
tw <- twListToDF(tweets)
tx <- tw$text
write.table(tx, file = "sample3.txt", append = TRUE)

tweets <- searchTwitter("motherboard",n=4000,lang = "en", since="2019-01-01")
tw <- twListToDF(tweets)
tx <- tw$text
write.table(tx, file = "sample4.txt", append = TRUE)

tweets <- searchTwitter("storage",n=4000,lang = "en", since="2019-01-01")
tw <- twListToDF(tweets)
tx <- tw$text
write.table(tx, file = "sample5.txt", append = TRUE)

tweets <- searchTwitter("server",n=4000,lang = "en", since="2019-01-01")
tw <- twListToDF(tweets)
tx <- tw$text
write.table(tx, file = "sample6.txt", append = TRUE)

