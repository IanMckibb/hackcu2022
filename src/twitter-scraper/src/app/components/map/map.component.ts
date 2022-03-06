import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ServerService } from '../../server.service';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  constructor(private httpClient: HttpClient) { }
  public loading: boolean = false;
  public number: any = "";
  public faSearch = faSearch;
  public likes = 0;

  ngOnInit(): void {
  }
  public getInputValue(){
      var inputVal = (document.getElementById("searchbar") as HTMLInputElement).value;
      if (inputVal.length <= 0) {
        alert("Please enter a word to search.");
        return;
      }
      this.number = "";
      this.loading = true;
      this.httpClient.get<string>(`http://localhost:8000/doIt?search=` + inputVal).subscribe(
        (response: string) => {
          this.loading = false;
          this.number = (parseInt(response).toFixed(2)).toString();
          if (this.number >= 60) this.likes = 0;
          else if (this.number >= 40) this.likes = 1;
          else this.likes = 2;
        },
        (error: HttpErrorResponse) => {
          console.log(error.message);
          alert(error.message);
        }
      );
  }

}
