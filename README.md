<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** asperduti, repo, arielsperduti, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/asperduti/automatic-time-tracking-desktop-client">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Automatic Time Tracking Software</h3>

  <p align="center">
    It is an <strong>automatic time tracking software</strong>. You will be able to know where and how you spend your time. It runs in the background on your computer, and phone to track in real-time the time that you spent in each application or website.
    <br />
    <a href="https://github.com/asperduti/automatic-time-tracking-desktop-client"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/asperduti/automatic-time-tracking-desktop-client">View Demo</a>
    ·
    <a href="https://github.com/asperduti/automatic-time-tracking-desktop-client/issues">Report Bug</a>
    ·
    <a href="https://github.com/asperduti/automatic-time-tracking-desktop-client/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
  - [Linux](#linux)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is the client app for desktops. It's runs on Linux, Windows and MacOs.
There will be two more parts, a backend, and a client app for smartphones.

### Built With

* [Python 3.6]()



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/asperduti/automatic-time-tracking-desktop-client.git
```


<!-- USAGE EXAMPLES -->
## Usage

To start to track the time that you spend at your computer just run the app:
```sh
python3 run.py
```

And when you finish the program, you will get a resume like this one:
```sh
Resume:

Activity        Time Spent
________        __________
time_tracking : bash    0:00:01.026519
time_tracking : python3 0:00:08.180052
time_tracking   0:00:11.213815
```

The best idea is start the tracker at login time, the steps to achive this depend of the platform.

### Linux

This is as simple as create a new [Desktop Entry](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)(a file with extension .desktop) inside of *~/.config/autostart* with the following conten:
```
[Desktop Entry]
Name=TimeTracking
GenericName=Time Tracking Desktop App
Comment=Run the Time Tracking app in background
Exec=/path/to/my/script.sh
Terminal=false
Type=Application
X-GNOME-Autostart-enabled=true
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/asperduti/automatic-time-tracking-desktop-client/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@arielsperduti](https://twitter.com/arielsperduti)

Project Link: [https://github.com/asperduti/automatic-time-tracking-desktop-client](https://github.com/asperduti/automatic-time-tracking-desktop-client)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/asperduti/automatic-time-tracking-desktop-client.svg?style=flat-square
[contributors-url]: https://github.com/asperduti/automatic-time-tracking-desktop-client/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/asperduti/automatic-time-tracking-desktop-client.svg?style=flat-square
[forks-url]: https://github.com/asperduti/automatic-time-tracking-desktop-client/network/members
[stars-shield]: https://img.shields.io/github/stars/asperduti/automatic-time-tracking-desktop-client.svg?style=flat-square
[stars-url]: https://github.com/asperduti/automatic-time-tracking-desktop-client/stargazers
[issues-shield]: https://img.shields.io/github/issues/asperduti/automatic-time-tracking-desktop-client.svg?style=flat-square
[issues-url]: https://github.com/asperduti/automatic-time-tracking-desktop-client/issues
[license-shield]: https://img.shields.io/github/license/asperduti/automatic-time-tracking-desktop-client.svg?style=flat-square
[license-url]: https://github.com/asperduti/automatic-time-tracking-desktop-client/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/arielsperduti
[product-screenshot]: images/screenshot.png
