import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, tap, of } from 'rxjs';



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

  private readonly localStorageKey = 'addressInfo';

  getAddressInfo(cep: string) {
    const url = `https://viacep.com.br/ws/${cep}/json/`;
    const cachedData = this.getCachedData(cep);
    if (cachedData) {
      console.log({msg: 'Got from cache!', value: cachedData})
      return of(cachedData);
    }
    console.log({msg: 'Getting from api...', value: cachedData})
    return this.http.get(url)

  }

  private getCachedData(key: string): AddressInfo | null {
    console.log({'this.localStorageKey': this.localStorageKey})
    const cachedDataString = localStorage.getItem(key);
    return cachedDataString ? JSON.parse(cachedDataString) : null;
  }

  setCachedData(data: AddressInfo): void {
    localStorage.setItem(this.localStorageKey, JSON.stringify(data));
  }
}
