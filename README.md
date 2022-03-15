# rym_genre_decade_links
Documentation of the important links that help music enthusiasts or newcomers navigate rateyourmusic.com seamlessly.

This upload is the culmination of a long winded project I've been working on for a while.

The purpose of this project has been to use rateyourmusic.com to make it (more) easy for people to discover new music.

My original idea was to create playlists with a song per album from certain charts. This proved to be very useful, but ultimately extremely time consuming. So, I tried something else.

Next I tried cataloguing the charts into word documents. The purpose of this in my mind was to have rateyourmusic without accessing the internet. Ultimately I realized the work I put into it was pointless. Accessing rateyourmusic is infinitely better than using word documents that mirror rateyourmusic.

Both the playlists and the word documents have the problem of being morally draining, time consuming, and easily outdated. The creation is morally draining because with how many albums there are, I cannot include everything and have to draw the line somewhere with rating caps for every genre playlist. I don't want to exclude any albums. With all the work I put into them, the data I use to produce them becomes outdated very quickly. Charts are constantly changing, and ideally I wanted my playlists to update with the changes to charts. This proved to be an impossible quandary because the automation I wrote for playlists still required human help due to the structure.

What I mean by that is the playlists I made (using one song per album of albums in the charts) took the most popular song from that album according to Spotify. The only way to access this information is to look at the plays in Spotify's desktop application. You cannot access this information from their public API.

One way I could solve this problem is by using rateyourmusic's song rating system available when subscribing to rateyourmusic. However, if I wanted it to be seamless and generate playlists instantaneously, the Spotify song titles would need to match what is on rateyourmusic exactly for every single album included on the playlist for there to be no issues. That proves to be even more of a challenge when albums may not even have the same number of songs for albums (for a number of reasons). Selecting the correct album can also be a challenge. Many albums are not even on Spotify. How would I automate knowing if the album is on Spotify? Perhaps the link system of rateyourmusic. etc. Things get very messy when trying to accomplish this task. The results would be amazing, but it is simply not worth it knowing the effort it would take.

Even if I did fully automate the playlist creation, the idea might not even be worth it. rateyourmusic displays a lot more useful information than Spotify when listening to new music. Going into new music without context can be an unpleasant experience. Building interest through research gives you the motivation to give new music a chance.

This brings me to what I created that attempts to better avoid these problems and still helps to find new music despite being a compromise.

I have created a directory view of (almost) every genre on rateyourmusic, and some useful links to help in the discovery process.

rateyourmusic's GUI is good, but in my view needs some improvements. I mean no disrespect to the creators and workers of rateyourmusic, take my criticism with a grain of salt. I don't know how difficult these would be to fix, but fixing them would improve the website surely imo.

1. There are many genres that not many people care about because they have so few albums. The way I solved this is by introducing a rule. That rule is I will not create a .txt file for a sub-genre that doesn't have 50 albums each with 50 ratings or more.

2. There is no way to tell how popular certain genres are when looking straight at the genre hierarchy (and not individual genre pages or charts). Why can you not see how many albums are above 50 ratings for each genre when looking through the genre hierarchy?

3. The hierarchy of genres is bloated and forces loading multiple pages to get to the charts you want.

4. Pages could offer more features instead of hiding editing behind another page. Why can users not rate albums right in the charts? Why can't users change album ratings, track ratings, or reviews from their profile page?

There are improvements to be made. Using this link tree will hopefully limit the number of pages you load on the website.

# FAQ (that nobody asked for):

***What is the number in front of every .txt file?***

That is how many albums are supposedly contained in that genre (according to the genre page for that genre in rateyourmusic). Sort by the name of the .txt file, you get a general idea of which genres are more popular than others.

***Why do I care about genres? Why do I care about decade charts?***

Because telling someone to check out rateyoumusic leads to them just looking at Best Albums in EVERY GENRE of ALL TIME. That's a shit ton of albums, and won't give enough options. Genre and Age filters help new and experienced users narrow in on what they like, and what they don't like. Giving new users one chart of albums they should like because they're the best of everything combined ultimately leads to disappointment. Or, a user searching their favorite artist and realizing their favorite album is terribly rated turns them off as well. Those situations are very important to avoid, and that is what I've attempted to do.

***Why are there folders?***

Each folder represents a genre that contains sub-genres.

***Why do folders contain a .txt file with the keyword "General" at the end of the file name?***

"General" .txt files have the same name as the folder they are contained in because they are the charts for the genre that contains every sub-genre in that folder and the albums classified as part of the folder genre but not any of the sub-genres.

***What are "Exclusive" charts contained in "General" keyword text documents?***

Exclusive charts are charts that exclude every sub-genre that is big enough and has been made into it's own .txt file within that folder. Now remember that I said I did not make .txt files for sub-genres that were too small. Those sub-genres now show up in the "Exclusive" charts I have created along with the folder genre.

***How do I open the links?

If you open a .txt file and cannot open the links by clicking on them, that is a fault of your .txt application. For windows, I recommend Notepad++. I don't know what Mac or Linux .txt editors allow this functionality.
