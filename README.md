


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://github.com/tasatr/chord_master/blob/master/images/chordmaster.jpg" alt="Logo" width="300" height="80">

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
        <li>[The First Approach](first-approach)</li>
        <li><a href="#The Second Approach">The Second Approach</a></li>
        <li><a href="#The Third Approach">The Third Approach</a></li>
        <li><a href="#The Fourth Approach">The Fourth Approach</a></li>
        <li><a href="#The Next Steps">The Next Steps</a></li>
      </ul>
    </li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project sprang up from a personal interest in playing along to YouTube music videos. That requires knowing the sequence of chords that best fit the melody. Chords are generally considered to be a collection of 3 or more notes played at the same time, but there are so many exceptions that in the end it seems more correct to say that a chord is any number of notes played at a specific time that fits to the melody.
<br/>
It does not initially seem like too difficult a task: we cut the recording into frames, generate a chromagram for each frame and then match it to a predefined chord model. When reading about chord prediction/chord recognition by Meinard Müller in his wonderful "Fundamentals of Music Processing" he devotes quite a few pages for explaining why this is actually a rather difficult thing to do. One of the most obvious problems are inversions - playing the same chord but starting with different notes. There is no way to determine these from a chromagram, but it makes a really big difference in sound, especially in chord sequences. Secondly, the amount of chords seems almost endless, and only a small subset of them have simple names (that beginners are able to decipher). Most of the chords in real songs have all possible additions to base chords, and getting reliable training data for them is tricky. Thirdly, due to the presence of harmonics the chromagram might show equal energy in different harmonics even if just one note is played.
<br/>
One of the major hurdles in predicting chords is picking the right chord from a set of chords that match the chromagram equally well. It is well known that for any key there are certain chords that sound better than others, and there are certain sequences that sound better than others. Therefore it is common to use Hidden Markov Models in chord predictions, by specifying initial probabilities and the probabilities of transitions to other chords. There are lots of papers written about transition probabilities, they differ between cultures, genres and even between artists. Hence it is near impossible to get chords right. But it is still fun to try.

### <a name="first-approach"></a>The First Approach

When first researching chord prediction I stumbled upon this superb tutorial:
https://github.com/caiomiyashiro/music_and_science/blob/master/Chord%20Recognition/complete_pydata_hidden_markov_models_for_chord_recognition.ipynb

This approach takes the annotated Beatles tracks generated by Harte (<a href="https://code.soundsoftware.ac.uk/attachments/download/330/chris_harte_phd_thesis.pdf">Link to PhD thesis</a>) and determines the probabilities for initial chords and chord transitions from these. These are plugged into a HMM and a chord sequence is generated accordingly. The code is visible in
[Chord Prediction using Beatles and HMM.ipynb](https://github.com/tasatr/chord_master/blob/master/Chord%20Prediction%20using%20Beatles%20and%20HMM.ipynb)

It didn't work out very well, for example the chords changed when ever the melody note changed, and the chords were not often correct.
Also, there's one major issue with this. Almost every song has some noise in the beginning and hence the first chord is usually not correct. Which also means that the following chords are not correct. So for this approach I would first need to write some clever method to figure out exactly when the song really begins. I will leave this task for the future.


### <a name="second-approach"></a>The Second Approach

As I didn't like the fact that the first approach had so many chords so frequently that it would be rather impossible to follow, I wondered how to narrow down the amount of chords for any song. I decided to go with the naughty approach of scraping ultimate-guitar for the list of all possible chords for the specific song, and then selecting only among these.

First, I had to get the training data to match chromagrams to chords. I took it from the Beatles collection again as previously.
Second, I trained a KNN classifier with the subset of training data (only the chords that appear in the song).
Third, I got the predictions from the KNN classifier

This didn't work terribly well either, as the training data is terribly uneven. There are tens of thousands of examples of C chord, but not so many about Cadd2 for example. And then I decided to make things even simpler.

### <a name="third-approach"></a>The Third Approach

I decided to take average values for each chord in my training data. That left the training data very small, training became instant, and for prediction I used only 1 neighbour. So far this approach seemed to work the best. But again, the vocal part completely confused the classifier, so it was obvious I had to do source separation. After searching the web and trying out 3 different source separators, I found <a href="https://github.com/deezer/spleeter">Spleeter</a>. That tool is fantastic for separating vocals from accompaniment and far exceeds in quality all others I tried. So I added source separation and the result became almost tolerable for me.

### <a name="fourth-approach"></a>The Fourth Approach
A friend of mine suggested trying out FCN for chord prediction, so this was my fourth approach (the code is here: [FCN.ipynb](https://github.com/tasatr/chord_master/blob/master/FCN.ipynb)
). However, while training my FCN network, I never got accuracy above 16%, and basically stopped my fourth approach there. I am certainly not experienced in deep learning, and don't know if the network that I designed corresponds well with the underlying data and the task at hand. Also, as I mentioned before, the training data is terribly skewed.

### <a name="final-project"></a>The Final Project
The project is built on django framework, the backend is written in python and the frontend in React. I use multiple libraries including youtube-dl for downloading audio and video files, Spleeter for source separation and ffmpeg for adding the chords to the final video as subtitles.

### <a name="next-steps"></a>The Next steps
1. Remove the noisy beginnings
2. Start with a small subset of chords that would still sound OK when replacing the more difficult chords (That's more of music theory)
3. Use the HMM model for predicting chord sequences
4. Use a full chromagram, not a 12-note chromagram for predicting more difficult chords


<!-- CONTACT -->
## Contact

Triinu Tasa - triinu.tasa@gmail.com

Project Link: [https://github.com/tasatr/chord_master](https://github.com/tasatr/chord_master)




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
