import { Component } from '@angular/core';
import { AuthService, CompanyAuthData } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './companyHome.component.html',
  styleUrl: './companyHome.component.sass'
})
export class CompanyHomeComponent {
  companyData: BehaviorSubject<CompanyAuthData | null>
  imageBase64String: string

  constructor (private authService: AuthService) {
    this.imageBase64String = '';
    this.companyData = this.authService.companyData
    if (this.companyData.value) {
      this.imageBase64String = this.companyData.value.loja.imagem_cadastro
      console.log({'this.companyData': this.companyData.value})
    }

  }


}
