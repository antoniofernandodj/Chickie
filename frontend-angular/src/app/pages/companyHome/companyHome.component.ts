import { Component } from '@angular/core';
import { AuthService, AuthData } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './companyHome.component.html',
  styleUrl: './companyHome.component.sass'
})
export class CompanyHomeComponent {
  companyData: BehaviorSubject<AuthData | null>

  constructor (private authService: AuthService) {
    this.companyData = this.authService.companyData
  }

}
