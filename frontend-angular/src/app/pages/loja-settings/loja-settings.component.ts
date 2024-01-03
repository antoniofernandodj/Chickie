import { Component } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { FormGroup, FormBuilder } from '@angular/forms';
import { ImageService } from '../../services/image.service';
import { LojaService } from '../../services/loja.service';
import { AuthService, CompanyAuthData } from '../../services/auth.service';
import { HttpErrorResponse } from '@angular/common/http';
import { UploadImageDataResponse } from '../../models/image';
import { atualizarImagemCadastroRequest } from '../../services/loja.service';


@Component({
  selector: 'app-loja-settings',
  standalone: true,
  imports: [ReactiveFormsModule, FormsModule],
  templateUrl: './loja-settings.component.html',
  styleUrl: './loja-settings.component.sass'
})
export class LojaSettingsComponent {

  imageForm: FormGroup
  file: atualizarImagemCadastroRequest
  companyData: CompanyAuthData | null
  atualizandoImagem: boolean

  constructor(
    private formBuilder: FormBuilder,
    private imageService: ImageService,
    private lojaService: LojaService,
    private authService: AuthService
  ) {
    this.imageForm = this.formBuilder.group({ imageFile: [''] });
    this.companyData = authService.currentCompany()
    this.atualizandoImagem = false

    this.file = {
      bytes_base64: '',
      filename: ''
    }
  }

  async onFileSelected(event: any) {
    const eventFile: File = event.target.files[0];
    if (eventFile) {
      this.file = {
        filename: eventFile.name,
        bytes_base64: await this.imageService.getImageBytes(eventFile)

      }
    }
  }

  uploadImage() {
    this.atualizandoImagem = true
    this.lojaService.atualizarImagemCadastro(this.file, this.companyData).subscribe({
      next: (response: any) => {
        let result: UploadImageDataResponse = {...response.result}

        if (!this.companyData) {
          let msg = 'Dados de autenticação não encontrados!';
          alert(msg); throw new Error(msg);
        }

        this.companyData.loja.imagem_cadastro = result.data.secure_url
        this.authService.setCompanyData(this.companyData)
        alert('Imagem atualizada com sucesso!')
        this.atualizandoImagem = false

      },
      error: (result: HttpErrorResponse) => {
        console.log({result: result.error})
        alert('Erro no upload da imagem!')
        this.atualizandoImagem = false
      }
    })
  }
}
