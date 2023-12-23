import { Component } from '@angular/core';
import { LoginService } from '../../services/login.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.sass'
})
export class LoginComponent {
  loginValue: string;
  passwordValue: string;

  constructor(private service: LoginService) {
    this.loginValue = "";
    this.passwordValue = "";
  }

  ngOnInit(): void { }

  doLogin(): void {
    this.service.doLogin(
      this.loginValue, this.passwordValue
    )
  }
}
