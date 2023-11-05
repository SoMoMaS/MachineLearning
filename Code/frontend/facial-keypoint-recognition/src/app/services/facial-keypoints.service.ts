import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Picture } from '../interfaces/picture';
import { FacialKeypoints } from '../interfaces/facial-keypoints';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FacialKeypointsService {


  serverURI = "http://localhost/8000/"
  constructor(private http: HttpClient) { }


  getFacialKeypoints10(picture: Picture): Observable<any>{
      return this.http.get(this.serverURI + "facialkeypoints/epochs_10")
  }

  getFacialKeypoints50(picture: Picture): Observable<any>{
    return this.http.get(this.serverURI + "facialkeypoints/epochs_50")
  }

  getFacialKeypoints100(picture: Picture): Observable<any>{
    return this.http.get(this.serverURI + "facialkeypoints/epochs_100")
  }

  getFacialKeypointsRawImage(picture: Picture){
    console.log(picture.pixels.length)
    this.http.post<any>(this.serverURI + "facialkeypoints/raw", picture).subscribe(result => {
      console.log(result);
    })
  }
}
