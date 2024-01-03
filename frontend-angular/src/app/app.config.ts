import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { provideEnvironmentNgxMask } from 'ngx-mask';
import { routes } from './routes/app.routes';


export const appConfig: ApplicationConfig = {
  providers: [
    provideEnvironmentNgxMask(),
    provideRouter(routes),
    provideHttpClient()
  ]
};
