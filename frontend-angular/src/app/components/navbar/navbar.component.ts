import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterModule, Router } from '@angular/router';
import { AuthService, AuthData } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.sass'
})
export class NavbarComponent {
  companyData: BehaviorSubject<AuthData | null>
  userData: BehaviorSubject<AuthData | null>
  userIsLoggedIn: BehaviorSubject<boolean>;
  companyIsLoggedIn: BehaviorSubject<boolean>;
  isLoginPage: BehaviorSubject<boolean>;

  constructor(private authService: AuthService, private router: Router) {
    this.isLoginPage = this.authService.isLoginPage
    this.companyData = this.authService.companyData
    this.userData = this.authService.userData
    this.userIsLoggedIn = this.authService.userIsLoggedIn
    this.companyIsLoggedIn = this.authService.companyIsLoggedIn
  }

}

