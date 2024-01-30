import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, tap, of, map } from 'rxjs';



type AddressInfo = {
  cep: string;
  logradouro: string;
  complemento: string;
  bairro: string;
  localidade: string;
  uf: string;
  ibge: string;
  gia: string;
  ddd: string;
  siafi: string;
};


@Injectable({
  providedIn: 'root'
})
export class ViaCepService {

  constructor(private http: HttpClient) { }

  getAddressInfo(cep: string) {
    const url = `https://viacep.com.br/ws/${cep}/json/`;
    const cachedData = this.getCachedData(cep);
    if (cachedData) {
      return of(cachedData);
    }
    return this.http.get(url).pipe(
      map((data: any) => {
        this.setCachedData(data)
        return data;
      }),
      catchError((error) => {
        console.error('Error fetching address info:', error);
        throw error;
      })
    );

  }

  private getCachedData(key: string): AddressInfo | null {
    const numbersOnly = key.match(/\d/g)
    const cep = (numbersOnly) ? numbersOnly.join('') : ''
    const cachedDataString = localStorage.getItem(cep);
    return cachedDataString ? JSON.parse(cachedDataString) : null;
  }

  setCachedData(data: AddressInfo): void {
    const numbersOnly = data.cep.match(/\d/g)
    const cep = (numbersOnly) ? numbersOnly.join('') : ''
    localStorage.setItem(cep, JSON.stringify(data));
  }
}
