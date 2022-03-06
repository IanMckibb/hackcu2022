import { Component, OnInit } from '@angular/core';
import { ServerService } from '../../server.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  constructor() { }
  public phrase = "";

  ngOnInit(): void {
  }
  public getInputValue(){
      // Selecting the input element and get its value 
      var inputVal = (document.getElementById("searchbar") as HTMLInputElement).value;
      
      // Displaying the value
      alert(inputVal);
  }
  // public getResult() {
  //   //console.log((document.getElementById("searchbar") as HTMLElement).value);
    
  // }

}
