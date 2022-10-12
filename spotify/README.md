<H1>Spotify to Youtube MP3</H1>
<p>This project will alow you to download your liked songs playlist in spotify with the help of OAuth to get the authorization to access. </p>

<H2> What is OAuth ? </H2>
<p>is an open standard for access delegation, commonly used as a way for internet users to grant websites or applications access to their information on other websites but without giving them the passwords. This mechanism is used by companies such as Amazon, Spotify, Google, Facebook, Microsoft, and Twitter to permit the users to share information about their accounts with third-party applications or websites.</p>

<H2> How the application works ? </H2>
<p> This schema shows in details the relationship beetwen OAuth and the App to access to information needed </p>



![ff](https://user-images.githubusercontent.com/58567636/195393125-40e18191-ae4c-4be4-add7-b1249d93b41e.png)

<p> Ater getting the data in the form of cookies, the application transform it to a .csv file with the help of Pandas library </p>
<H2> What is Pandas ? </H2>
<p> is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. </p>

<H2> How the application downloads the songs ? </H2>
<p> The app Web scape the links of the songs from the .csv with the help of the urlib.request.</p>
<p> urlib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more. </p>
<p>After the application gets all the links, it uses youtube_dl library to download the songs from youtube and send it to the folder wanted by the user .</p>

