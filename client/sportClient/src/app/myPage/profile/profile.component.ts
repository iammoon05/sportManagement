import {Component} from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';

@Component({
  selector: 'profile-card',
  templateUrl: 'profile.component.html',
  standalone: true,
  imports: [MatCardModule, MatDividerModule, MatIconModule, MatButtonModule]
})
export class ProfileCard {

}
