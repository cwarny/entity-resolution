# Entity Resolution on Online Social Networks (OSN)

This document describes a basic Python-based implementation of a system to ID people across the main online social networks (Facebook, LinkedIn, Twitter, Google +). The goal is to be able to tell that the same real-life person (“entity”) is behind different profiles on different social networks.

The system gathers candidate profiles from the different OSNs and compares profile attributes. If enough attribute profiles match, the profiles are assumed to represent the same entity. The matching tests conducted between two profiles will depend on what profile attributes overlap.

Finally, a graph is progressively built, linking matching profiles. Candidate entities consist in paths of this graph linking profiles together and are ranked according to the average strength of the links along their path.

## 1. Search

*Casting the initial net by making a web search or directly querying the OSNs*

The first thing is to gather an initial set of candidates for each OSN based on some initial data. At this stage we favor recall over precision, so we want to cast a wide net. This step is basically a search problem: given some initial data, find all possibly matching profiles on each OSN. Let’s say we only have first and last names. Two approaches are possible here:

- OSN-specific: Do a search directly on each OSN through their dedicated API (most of them have a search capability).
- Custom search engine (CSE): Set up a customized web search engine, e.g. Google Custom Search Engine, which uses the power of Google Search while restricting it on a selection of web domains (e.g., facebook.com, linkedin.com, etc.).

It is not clear which approach is the best. The first approach has probably better recall but less precision, and vice-versa for the second one. 

Both approaches entail making an API call with first and last names as query parameters. The CSE approach will return a list of relevant URLs (as in the familiar Google Search experience) while the OSN-specific search will return a list of profiles in a structured data format (JSON or XML), organized by “attribute fields”. An overview of these fields for the different OSNs is detailed in the attached Excel spreadsheet.

The CSE approach requires an additional intermediate step where the URL is parsed with a regular expression engine to extract the profile ID from that URL. This ID is then used to build a “get” query for the relevant OSN (as opposed to a “search” query) to fetch the OSN profile in a familiar structured data format.

The profile data varies according to the platform (different OSNs collect different data from their users and have different default privacy settings) as well as according to the user’s customized privacy settings. In general, LinkedIn and Twitter tend to be more generous platforms than Facebook or Google + in terms of how much data they make available.

The API calls are made either through direct HTTP requests or through a third-party library. The Temboo libraries facilitate the API call process by standardizing the process across more than a hundred platforms (see full list in accompanying Excel spreadsheet). Temboo makes the rather painful process of learning the peculiarities of different APIs appear seamless.

## 2.	Sanity-check

*Comparing search results to initial query and dropping low-information profiles*

The next step aims at increasing precision in two ways:

- First, the search results returned in step 1 might include irrelevant profiles (e.g., a friend of the entity appears in the result because he/she posted a lot of pictures of the entity we are looking for). A simple sanity-check consists therefore in checking whether a profile’s name corresponds to the initial search query.
- Second, some profiles returned exhibit so little information that it might not make sense trying to match to other profiles from other OSNs. They are therefore dropped. This favors precision at the expense of recall.

## 3.	Standardize

*Ensuring consistent attribute field formats across OSNs*

Given that our goal is to compare similar attribute fields across two different OSNs, an important intermediate step is to standardize the data received from different OSNs who might have different ways of designating and/or structuring similar information. For instance:
-	What Facebook calls ‘name’, Google + calls ‘formattedName’.
-	Facebook returns a list of languages for a user while Twitter returns a string for the user’s profile language.
Both attribute field label and structure are then standardized across OSNs.

## 4. Match

*Scoring the similarity of profiles across OSNs*

The matching process consists in gradually adjusting a score according to how well attributes from two profiles from two different OSNs match. Only profiles from different OSNs are matched against each other by comparing their overlapping attributes (which attributes overlap depends on which two OSNs are being considered).

The matching tests and rules vary in function of what attribute is under consideration. Some matching tests will compare the string similarity of two strings, while others will test for exact equality of two strings. Others still, for long strings (e.g., bio information), will compare the lexical similarity of two strings.

The way the similarity score is adjusted depends on the attribute under consideration as well. A matching e-mail is very positively informative and will therefore substantially increase the score. Adjustments to the score can also be negative. A non-matching gender is very informative and will result in a sharp decrease in the matching score, while a non-matching job will have less impact (though still a negative impact).

#### Matching tests and rules

<table>
    <tr>
        <th>Attribute</td>
        <th>Matching test</td>
        <th>Threshold</td>
        <th>Matching</td>
        <th>Non-matching</td>
    </tr>
    <tr>
        <td>Name</td>
        <td>String similarity</td>
        <td>0.8</td>
        <td>+1</td>
        <td>-10</td>
    </tr>
    <tr>
        <td>Username</td>
        <td>String similarity</td>
        <td>0.7</td>
        <td>+1</td>
        <td></td>
    </tr>
    <tr>
        <td>E-mail</td>
        <td>Equality</td>
        <td></td>
        <td>+8</td>
        <td></td>
    </tr>
    <tr>
        <td>Location 1 (free-text location)</td>
        <td>Any common word</td>
        <td></td>
        <td>+2</td>
        <td>-1</td>
    </tr>
    <tr>
        <td>Location 2 (country code)</td>
        <td>Equality</td>
        <td></td>
        <td>+1</td>
        <td>-5</td>
    </tr>
    <tr>
        <td>Education</td>
        <td>String similarity</td>
        <td>0.7</td>
        <td>+2</td>
        <td>-1</td>
    </tr>
    <tr>
        <td>Work</td>
        <td>String similarity</td>
        <td>0.7</td>
        <td>+2</td>
        <td>-1</td>
    </tr>
    <tr>
        <td>Language 1 (language code)</td>
        <td>Equality</td>
        <td></td>
        <td>+1</td>
        <td>-2</td>
    </tr>
    <tr>
        <td>Language 2 (free-text language)</td>
        <td>String similarity</td>
        <td>0.7</td>
        <td>+2</td>
        <td></td>
    </tr>
    <tr>
        <td>Description</td>
        <td>Lexical similarity</td>
        <td>0.5</td>
        <td>+1</td>
        <td></td>
    </tr>
    <tr>
        <td>Birthday-year</td>
        <td>Equality</td>
        <td></td>
        <td>+4</td>
        <td></td>
    </tr>
    <tr>
        <td>Birthday-month</td>
        <td>Equality</td>
        <td></td>
        <td>+2</td>
        <td></td>
    </tr>
    <tr>
        <td>Age</td>
        <td>Equality</td>
        <td></td>
        <td>+1</td>
        <td></td>
    </tr>
    <tr>
        <td>Gender</td>
        <td>Equality</td>
        <td></td>
        <td></td>
        <td>-10</td>
    </tr>
    <tr>
        <td>Timezone</td>
        <td>Equality</td>
        <td></td>
        <td>+1</td>
        <td></td>
    </tr>
    <tr>
        <td>URL</td>
        <td>String similarity</td>
        <td>0.8</td>
        <td>+5</td>
        <td>-0.5</td>
    </tr>
</table>

<small>Note: String similarity is calculated as the normalized “edit distance” (also known as Levenshtein distance) and the lexical similarity is calculated as the number of similar tokens found in two strings, normalized by the average number of tokens in both strings.</small>

If the similarity score of two profiles is above an arbitrary threshold (0), the profiles are “linked”. This information is stored as a graph where nodes represent profiles and edges represent similarity scores. The use of a graph is appropriate to a situation where:

- One does not know how many data points are to be clustered together according to distance.
- The distance metric is different for different platforms (the similarity between a Twitter and a Facebook profile is based on different attribute fields than the distance between a Facebook and a LinkedIn profile).

Following attribute overlap, a LinkedIn profile might be linked to a Twitter and a Facebook profile, while no link was made between that Twitter and that Facebook profile, but this might only be due to a lack of attribute overlap between Twitter and Facebook for that particular entity.

## 5.	Candidate entities definition

*Defining entities and ensuring the graph does not give inconsistent results*

An entity is defined as a path on the graph resulting from step 4. A path is a series of edges linking profiles (nodes) in the graph. The reason an entity is defined by a path and not some other graph structure like a “component” (set of nodes directly or indirectly connected to each other) or a “clique” (set of nodes directly connected to each other) is that any bifurcation in a path actually creates a different candidate entity. While a clique could be a good definition of an entity, it is too demanding a requirement (cliques are difficult to form in our context).

However, this definition faces a technical problem when the same path happens to go through two different nodes of the same OSN. This might either mean that that entity has two different profiles on the same OSN (unlikely) or that some link in the path is wrong. It can be proven that this problem is solved by clipping the “weakest” edge (edge with lowest similarity score) in the subpath connecting the two nodes of the same OSN.

## 6.	Rank

*Ranking entities by the average similarity score along their associated path*

It is important to note that for each path in the graph, every subpath of that path is also a path, and therefore a candidate entity competing with the other candidate entities. This feature of the graph approach is useful because it allows for entities that might actually lack a profile on a certain OSN. If the average likelihood of the subpath of a path is higher than the likelihood of the path itself, this might mean that the entity does not actually possess a profile on one of the OSN. Here, likelihood is to be understood as the average similarity score of the edges of a path. Entities are thus ranked by this likelihood.
