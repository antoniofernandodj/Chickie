import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-logout',
  standalone: true,
  imports: [],
  template: '',
  styles: []
})
export class LogoutComponent {
  constructor (
    private router: Router,
    private authService: AuthService
  ) {
    this.authService.doLogout()
    this.authService.isLoginPage.next(true)
    this.router.navigate(['/login'])
  }
}
