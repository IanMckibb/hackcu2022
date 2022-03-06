import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ServerService } from '../../server.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  constructor(private httpClient: HttpClient) { }
  public loading: boolean = false;
  public number: any = "";

  ngOnInit(): void {
  }
  public getInputValue(){
      var inputVal = (document.getElementById("searchbar") as HTMLInputElement).value;
      this.loading = true;
      this.httpClient.get<string>(`http://localhost:8000/doIt?search=` + inputVal).subscribe(
        (response: string) => {
          this.loading = false;
          this.number = response;
        },
        (error: HttpErrorResponse) => {
          console.log(error.message);
          alert(error.message);
        }
      );
  }

}
