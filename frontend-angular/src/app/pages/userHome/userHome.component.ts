import { Component } from '@angular/core';
import { AuthService, AuthData } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-user-home',
  standalone: true,
  imports: [],
  templateUrl: './userHome.component.html',
  styleUrl: './userHome.component.sass'
})
export class UserHomeComponent {
  userData: BehaviorSubject<AuthData | null>

  constructor (private authService: AuthService) {
    this.userData = authService.userData
  }
}
