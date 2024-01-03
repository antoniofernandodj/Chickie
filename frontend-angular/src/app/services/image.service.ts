import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ImageService {


  constructor(private http: HttpClient) { }

  async getImageBytes(file: File): Promise<string> {

    let errorMsg = 'Erro no carregamento da imagem'

    try {
      let base64 = await this.getBase64(file)
      let imageBytesBase64 = ''
      if (base64 instanceof ArrayBuffer) {
        let uint8View = new Uint8Array(base64);
        let binaryArray = Array.from(uint8View);
        let binaryString = String.fromCharCode.apply(null, binaryArray);
        imageBytesBase64 = btoa(binaryString);
      } else {
        imageBytesBase64 = base64;
      }
      return imageBytesBase64
    } catch(error) {
      alert(errorMsg);
      console.log(error);
    }

    throw new Error(errorMsg)
  }

  private getBase64(file: File): Promise<string | ArrayBuffer> {
    return new Promise((resolve, reject) => {
      const reader = new FileReader()
      reader.readAsDataURL(file);
      reader.onload = () => {
        if (reader.result) {
          resolve(reader.result)
        } else {
          reject(reader.result)
        }
      }
      reader.onerror = (error) => {
        reject(error);
      }
    })
  }
}
