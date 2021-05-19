


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/tasatr/chord_master">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Chord Master</h3>

  <p align="center">
    Predict chords for any youtube music video and show them as subtitles
    <br />
    <a href="https://github.com/tasatr/chord_master">View Demo</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#first-approach">The First Approach</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project sprang up from a personal interest in playing along to YouTube music videos. That requires knowing the sequence of chords that best fit the melody. Chords are generally considered to be a collection of 3 or more notes played at the same time, but there are so many exceptions that in the end it seems more correct to say that a chord is any number of notes played at a specific time that fits to the melody.
<br/>
It does not initially seem like too difficult a task: we cut the recording into frames, generate a chromagram for each frame and then match it to a predefined chord model. When reading about chord prediction/chord recognition by Meinard Müller in his wonderful "Fundamentals of Music Processing" he devotes quite a few pages for explaining why this is actually a rather difficult thing to do. One of the most obvious problems are inversions - playing the same chord but starting with different notes. There is no way to determine these from a chromagram, but it makes a really big difference in sound, especially in chord sequences. Secondly, the amount of chords seems almost endless, and only a small subset of them have simple names (that beginners are able to decipher). Most of the chords in real songs have all possible additions to base chords, and getting reliable training data for them is tricky. Thirdly, due to the presence of harmonics the chromagram might show equal energy in different harmonics even if just one note is played.
<br/>
One of the major hurdles in predicting chords is picking the right chord from a set of chords that match the chromagram equally well. It is well known that for any key there are certain chords that sound better than others, and there are certain sequences that sound better than others. Therefore it is common to use Hidden Markov Models in chord predictions, by specifying initial probabilities and the probabilities of transitions to other chords. There are lots of papers written about transition probabilities, they differ between cultures, genres and even between artists. Hence it is near impossible to get chords right. But it is still fun to try.

### Built With

* []()
* []()
* []()



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/tasatr/chord_master.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/tasatr/chord_master/issues) for a list of proposed features (and known issues).



<!-- CONTACT -->
## Contact

Triinu Tasa - triinu.tasa@gmail.com

Project Link: [https://github.com/tasatr/chord_master](https://github.com/tasatr/chord_master)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
