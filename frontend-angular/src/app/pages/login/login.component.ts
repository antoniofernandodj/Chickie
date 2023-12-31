import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, RouterModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.sass'
})
export class LoginComponent {

  loginCompanyValue: string;
  passwordCompanyValue: string;

  loginUserValue: string;
  passwordUserValue: string;

  constructor(private authService: AuthService, private router: Router) {
    this.loginCompanyValue = "";
    this.passwordCompanyValue = "";

    this.loginUserValue= "";
    this.passwordUserValue = "";

  }

  ngOnInit(): void { }

  doCompanyLogin(): void {
    this.authService.doCompanyLogin(this.loginCompanyValue, this.passwordCompanyValue)
  }

  doUserLogin(): void {
    this.authService.doUserLogin(this.loginUserValue, this.passwordUserValue)
  }
}
