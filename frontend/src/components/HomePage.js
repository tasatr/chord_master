import React, { Component } from "react";
import SearchBar from './Searchbar';
import youtube from '../youtube';
import VideoList from './VideoList';
import VideoDetail from './VideoDetail';
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";


export default class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      videos: [],
      selectedVideo: null
    };
    this.handleAnalyzeVideoButton = this.handleAnalyzeVideoButton.bind(this);
  };
    handleSubmit = async (termFromSearchBar) => {
        const response = await youtube.get('/search', {
            params: {
                q: termFromSearchBar
            }
        })

        this.setState({
            videos: response.data.items
        })
        console.log("this is resp",response);
    };
    handleVideoSelect = (video) => {
      console.log("this is selected video ",video);
        this.setState({selectedVideo: video})
    };

    handleAnalyzeVideoButton() {
      console.log('###### state is : ', this.state);
      if (this.state.selectedVideo) {
        console.log('video_id is: ', this.state.selectedVideo.id.videoId);
        console.log('title is: ', this.state.selectedVideo.snippet.title);

        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            video_id: this.state.selectedVideo.id.videoId,
            title: this.state.selectedVideo.snippet.title
          }),
        };
        fetch('/api/create-video', requestOptions).then((response) => response.json());
      }
    };

    render() {
        return (
          <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <SearchBar handleFormSubmit={this.handleSubmit}/>
            </Grid>
            <Grid item xs={6} align="center">
              <VideoDetail video={this.state.selectedVideo}/>
              <Button variant="contained" color="primary" onClick={this.handleAnalyzeVideoButton}>
                Analyze this video
              </Button>
            </Grid>
            <Grid item xs={6} align="right">
              <VideoList handleVideoSelect={this.handleVideoSelect} videos={this.state.videos}/>
            </Grid>
          </Grid>
        )
    }
}
