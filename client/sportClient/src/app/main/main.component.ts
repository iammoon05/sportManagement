import {Component} from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import { MyOptionsCarousel } from '../myPage/topTab/myOptionsCarousel.component';
import { ProfileCard } from '../myPage/profile/profile.component';

@Component({
  selector: 'main',
  templateUrl: 'main.component.html',
  standalone: true,
  imports: [MatIconModule, MatButtonModule, MyOptionsCarousel, ProfileCard]
})
export class Main {

}
