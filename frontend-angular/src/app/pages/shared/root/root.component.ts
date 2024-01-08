import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../../services/services';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [],
  template: '',
  styleUrls: []
})
export class RootComponent {

  companyData: any
  userData: any

  constructor(private authService: AuthService, private router: Router) {

    let companyData = authService.currentCompany()
    let userData = authService.currentUser()

    if (companyData) {
      this.router.navigate(['loja/home'])
    }

    else if (userData) {
      this.router.navigate(['user/home'])
    }

    else {
      this.router.navigate(['login'])
    }


  }

}
