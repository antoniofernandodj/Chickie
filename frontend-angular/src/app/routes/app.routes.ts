import { Routes } from '@angular/router';
import { PageNotFoundComponent } from '../pages/page-not-found/page-not-found.component';
import { RootComponent } from '../pages/root/root.component';
import { lojaRoutes } from './app.loja.routes';
import { publicRoutes } from './app.public.routes';



export const routes: Routes = [

  ...publicRoutes,
  ...lojaRoutes,

  {
    path: '',
    component: RootComponent
  },

  {
    path: '**',
    component: PageNotFoundComponent
  }

];
