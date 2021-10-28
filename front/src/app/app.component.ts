import { Component } from '@angular/core';
import { PublicService } from './services/public.service'; 
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Welcome to Flashcards Web app';
  msg: any ;


  constructor (private service:PublicService){

  }
  ngOnInit(): void {

    this.showMessage();


  }

  showMessage(){
    this.service.getMessage().subscribe(data => {

      this.msg = data,
        console.log(this.msg);



    })

    
  }




}
