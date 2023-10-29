import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Picture } from '../interfaces/picture';
import { FacialKeypoints } from '../interfaces/facial-keypoints';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FacialKeypointsServiceService {

  serverURI = "http://127.0.0.1/8000/"
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
}
