import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({ providedIn: 'root' })
export class LojaService {

  baseUrl: string

  constructor(private http: HttpClient) {
    this.baseUrl = 'http://localhost:8000/loja'
  }

  getOne(uuid: string): Observable<Object> {
    let observable = this.http.get(this.baseUrl.concat(`/${uuid}`))
    return observable
  }

  getAll():Observable<Object> {
    let observable = this.http.get(this.baseUrl)
    return observable
  }
}
