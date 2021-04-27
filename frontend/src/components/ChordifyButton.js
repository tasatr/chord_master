import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";


export default class ChordifyButton extends Component {
  constructor(props, handleAnalyzeVideoButton) {
    super(props);
    this.handleAnalyzeVideoButton = handleAnalyzeVideoButton;
  }

  render() {
    return <Grid container spacing={1}>
      <Grid item xs={12} align="center"></Grid>
        <Typography component="h4" variant="h4">
          Analyze this video
        </Typography>
        <Button variant="contained" color="primary" handleAnalyzeVideoButton={this.handleAnalyzeVideoButton}>
          Link
        </Button>
    </Grid>
  }
}
