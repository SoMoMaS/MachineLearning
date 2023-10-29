import { Component } from '@angular/core';
import { Subject, Observable } from 'rxjs';
import { WebcamImage } from 'ngx-webcam';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'facial-keypoint-recognition';

  // latest snapshot
  public webcamImage: WebcamImage = null!;
  handleImage(webcamImage: WebcamImage) {
    this.webcamImage = webcamImage;
  }
}
