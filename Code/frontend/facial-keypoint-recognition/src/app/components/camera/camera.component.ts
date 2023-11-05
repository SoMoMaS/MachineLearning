import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Subject, Observable } from 'rxjs';
import { WebcamImage, WebcamInitError, WebcamUtil } from 'ngx-webcam';
import { FacialKeypointsService } from '../../services/facial-keypoints.service'
import { Picture } from '../../interfaces/picture'
import { NONE_TYPE } from '@angular/compiler';
@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.css']
})
export class CameraComponent implements OnInit {
  constructor(private facialKeyPointsService : FacialKeypointsService){}

  private currentImage: WebcamImage | undefined;

  @Output()
  public pictureTaken = new EventEmitter<WebcamImage>();
  // toggle webcam on/off
  public showWebcam = true;
  public multipleWebcamsAvailable = false;
  public deviceId: string = ""
  public allowCameraSwitch = false;
  public captureImageData = true;
  public videoOptions: MediaTrackConstraints = {
    // width: {ideal: 1024},
    // height: {ideal: 576}
  };
  public errors: WebcamInitError[] = [];
  // webcam snapshot trigger
  private trigger: Subject<void> = new Subject<void>();
  // switch to next / previous / specific webcam; true/false: forward/backwards, string: deviceId
  public ngOnInit(): void {
    WebcamUtil.getAvailableVideoInputs()
      .then((mediaDevices: MediaDeviceInfo[]) => {
        this.multipleWebcamsAvailable = mediaDevices && mediaDevices.length > 1;
      });
  }
  public triggerSnapshot(): void {
    this.trigger.next();
  }

  public sendFacialKeypointRequest(): void {
    if(this.currentImage != undefined){
      let normalizedArray = Array.prototype.slice.call(this.currentImage.imageData.data)
      this.facialKeyPointsService.getFacialKeypointsRawImage({ pixels: normalizedArray, width: this.currentImage.imageData.width, height: this.currentImage.imageData.height})
    }
  }
  public toggleWebcam(): void {
    this.showWebcam = !this.showWebcam;
  }
  public handleInitError(error: WebcamInitError): void {
    this.errors.push(error);
  }

  public handleImage(webcamImage: WebcamImage): void {
    console.info('received webcam image', webcamImage);
    webcamImage.imageAsBase64
    this.currentImage = webcamImage
    console.log(webcamImage.imageData.data);
    this.pictureTaken.emit(webcamImage);
    
  }

  public get triggerObservable(): Observable<void> {
    return this.trigger.asObservable();
  }
}