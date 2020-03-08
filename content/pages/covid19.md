Title: COVID19
Slug: covid19
Date: 2020-03-05 17:52
Status: published
Tags: covid19
image: {photo}plot_covid_most.png

This page is about COVID19, i.e. the disease caused by the new Coronavirus SARS-CoV-2. I am
not an expert in the field, but have been following developments closely since January
and feel the need to collect some information. No guarantees about being correct and no need
to trust me on anything, I link the sources. What I found enlightening myself might work
for you, or not.

For other posts with more day-to-day updates and news see [/tag/covid19]({tag}covid19).

Last update: 2020-03-07

Current assessment, moody, personal, and in very broad terms: This disease will not blow over
quickly, it will impact everbody over the current months or years, until a vaccine becomes
available. Overwhelmed health care systems will be the biggest primary problem.

The graph of deceased in the ten countries or regions with the highest numbers looks like this:

[![COVID19 deaths]({photo}plot_covid_most.png "COVID19 deaths")]({static}/pic/plot_covid_most.png)  
Data Source: [WHO](https://github.com/CSSEGISandData/2019-nCoV), Code: [github](https://github.com/ivh/covid19), 
License: [CC-BY](https://creativecommons.org/licenses/by/4.0/)  
Note that this is a logarithmic plot. Currently it looks like the increase in China has slowed down,
while Italy and Iran are the most worrying.

[Dashboard](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
with statistics on a map.
[Another one with more plots](https://covid19info.live/)

There are several scientists and journalists that do an outstanding job communicating on Twitter.
Among them: [@HelenBraswell](https://twitter.com/HelenBranswell), [@cmyeaton](https://twitter.com/cmyeaton)
[@MackayIM](https://twitter.com/MackayIM), [@kakape](https://twitter.com/kakape), 
[@clairlemon](https://twitter.com/clairlemon), [@primalpoly](https://twitter.com/primalpoly).  
[More here](https://twitter.com/i/lists/1235865725962604548), or just [follow me](https://twitter.com/ivh).

Current best estimates on the basic parameter of the disease:

* Estimates for how many people wih COVID19 die range from 0.5% to 3% ([1](https://twitter.com/AdamJKucharski/status/1235700941422198787)
[2](https://www.scmp.com/week-asia/health-environment/article/3065187/coronavirus-south-koreas-aggressive-testing-gives),
[3](https://www.statnews.com/2020/03/06/were-learning-a-lot-about-the-coronavirus-it-will-help-us-assess-risk/))
and the high estimates are from China and are more disputed. 
* Being infected without symptoms seems to be the exception, so I will not distinguish IFR from CFR.
* Once people recover from COVID19, they are [immune](https://twitter.com/MackayIM/status/1236449541047504896), as is common with
virus infections.
* The _doubling time_ seems to be roughly one week. This is related to R0, i.e. on average how many new cases are caused per existing case.
The [estimtes by country](https://cmmid.github.io/topics/covid19/current-patterns-transmission/global-time-varying-transmission.html)
vary, S.Korea for example seems to be well on its way to R0=1, meaning the disease no longer grows.
* 10% of cases in Italy need hospitalization ([1](https://medium.com/@cisba/hospitalization-a-clear-and-reliable-crisis-index-438fc6e9805e)).
This is a very worrying number, because it means that health care systems can get overwhelmed by even a moderate outbreak.
* incubation 4-5 days, 2 weeks possible but rare
* The age distribution of the disease CFR, together with the age distribution of populations can
[strongly influence the mortality](https://twitter.com/CJEMetcalf/status/1229792572513669121). Whether this gets compensated
by better health care in richer countries with older populations remains to be seen.

CFR of ~1% means that per death there are on average 100 cases, yet discovered or not.
Since people do not die immediately, but after 2-4 weeks, this means a
death today corresponds to around 500 current cases. With the uncertainties in CFR, incubation and
doubling times, this number is very uncertain and might as well be 150 or over 1000.

But sticking to 500 cases per death for now, the 100 deaths each in S.Korea and Italy
would mean 50000 infected. Even if this is an overestimate,
the order of magnitude seems right, and that means many undetected cases, especially in Italy.

The point above about ICU care makes apparent why spreading out the outbreak over time helps
([historic example](https://twitter.com/florian_krammer/status/1235761684431724550)) and should be highest
priority once local containment is no longer possible. Figure 1 from [here](https://virologydownunder.com/so-you-think-youve-about-to-be-in-a-pandemic/)
illustrates this point. We do not want everybody to get sick at once.

[That same article](https://virologydownunder.com/so-you-think-youve-about-to-be-in-a-pandemic/) also
serves as a good primer on what you can and should do now, before your life becomes seriously affected.

But I will come back to that in more detail shortly...
