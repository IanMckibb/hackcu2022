import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

export interface FlickrPhoto {
  farm: string;
  id: string;
  secret: string;
  server: string;
  title: string;
}

export interface FlickrOutput {
  photos: {
    photo: FlickrPhoto[];
  };
}

@Injectable({
  providedIn: 'root'
})


export class FlickrService {

  constructor(private http: HttpClient) { }

  search_keyword(keyword: string) {
    const url = 'https://www.flickr.com/services/rest/?method=flickr.test.echo&name=value' 
    const params = 'api_key=a5f0c1254bcf381da6bb7355bcafaa0b&text=${keyword}&format=json&nojsoncallback=1&per_page=12'

    // return this.http.get(url + params).pipe(map((res: FlickrOutput) => {
    //   const urlArr = [];
    //   resizeBy.photos.photo.forEach((ph: FlickrPhoto)  => {

    //   }
    }
  }
// }
