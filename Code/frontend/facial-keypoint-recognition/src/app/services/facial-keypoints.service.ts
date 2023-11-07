import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Picture } from '../interfaces/picture';
import { FacialKeypoints } from '../interfaces/facial-keypoints';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FacialKeypointsService {


  serverURI = "http://localhost:8000/"
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

  getFacialKeypointsRawImage(picture: Picture): Observable<string>{
    const headers = new HttpHeaders();
    headers.append('Content-Type', 'application/json');
    console.log(this.serverURI + "facialkeypoints/raw")
    return this.http.post<string>(this.serverURI + "facialkeypoints/raw", picture, {headers: headers})
  }
}
